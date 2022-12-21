#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import json
import tomlkit
from typing import Dict, List, Optional
from dotenv import load_dotenv
from collections import namedtuple

from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func
# from sqlalchemy.dialects.sqlite import insert

from pyArango.connection import Connection
from pyArango.database import DBHandle

from simsapa import DbSchemaName, logger
from simsapa.app.db import appdata_models as Am
from simsapa.app.helpers import bilara_html_post_process, bilara_text_to_html, consistent_nasal_m, create_app_dirs, html_get_sutta_page_body, compact_rich_text

from simsapa.app.stardict import parse_stardict_zip
from simsapa.app.db.stardict import import_stardict_as_new

import helpers
import cst4
import dhammatalks_org
import dhammapada_munindo
import dhammapada_tipitaka_net
import create_links

load_dotenv()

s = os.getenv('BOOTSTRAP_ASSETS_DIR')
if s is None or s == "":
    logger.error("Missing env variable: BOOTSTRAP_ASSETS_DIR")
    sys.exit(1)

BOOTSTRAP_ASSETS_DIR = Path(s)
SC_DATA_DIR = BOOTSTRAP_ASSETS_DIR.joinpath("sc-data")

for p in [BOOTSTRAP_ASSETS_DIR, SC_DATA_DIR]:
    if not p.exists():
        logger.error(f"Missing folder: {p}")
        sys.exit(1)

s = os.getenv('BOOTSTRAP_LIMIT')
if s is None or s == "":
    BOOTSTRAP_LIMIT = None
else:
    BOOTSTRAP_LIMIT = int(s)


def get_suttacentral_db() -> DBHandle:
    conn = Connection(
        arangoURL="http://localhost:8529",
        username="root",
        password="test",
    )

    # db = conn.createDatabase(name="suttacentral")
    db: DBHandle = conn["suttacentral"]

    return db


def html_text_uid(x) -> str:
    '''dn1/en/bodhi'''
    return f"{x['uid']}/{x['lang']}/{x['author_uid']}"


def bilara_text_uid(x) -> str:
    '''dn1/pli/ms'''

    a = x['muids'].copy()
    for k in ['translation', 'root', 'reference', 'variant', 'comment', 'html', x['lang']]:
        if k in a:
            a.pop(a.index(k))

    if len(a) == 1:
        author = a[0]
    elif len(a) == 0 and '/pli/ms/' in x['file_path']:
        author = 'ms'
    elif len(a) == 0 and '/pli/vri/' in x['file_path']:
        author = 'vri'
    else:
        logger.warn(f"bilara_text_uid() Unknown author for bilara text, _id: {x['_id']}, muids: {x['muids']}, {x['file_path']}")
        author = 'unknown'

    return f"{x['uid']}/{x['lang']}/{author}"


def html_text_to_sutta(x, title: str, _: Optional[str]) -> Am.Sutta:
    # html pages can be complete docs, <!DOCTYPE html><html>...
    page = x['text']

    body = html_get_sutta_page_body(page)
    body = bilara_html_post_process(body)
    content_html = '<div class="suttacentral html-text">' + consistent_nasal_m(body) + '</div>'
    content_plain = compact_rich_text(content_html)

    uid = html_text_uid(x)
    source_uid = uid.split('/')[-1]

    return Am.Sutta(
        source_uid = source_uid,
        source_info = x['_id'],
        # The All-embracing Net of Views
        title = consistent_nasal_m(title),
        # dn1/en/bodhi
        uid = uid,
        # SN 12.23
        sutta_ref = helpers.uid_to_ref(x['uid']),
        # en
        language = x['lang'],
        content_html = content_html,
        content_plain = content_plain,
        created_at = func.now(),
    )


def bilara_text_to_sutta(x, title: str, tmpl_json: Optional[str]) -> Am.Sutta:
    content = x['text']

    if tmpl_json is None:
        logger.warn(f"No template: {x['uid']} {title} {x['file_path']}")

        a = json.loads(content)
        page = "\n\n".join(a.values())

        content_html = null()
        content_plain = page

    else:
        content_html = bilara_text_to_html(content, tmpl_json)
        content_plain = compact_rich_text(content_html)

    uid = bilara_text_uid(x)
    source_uid = uid.split('/')[-1]

    return Am.Sutta(
        source_uid = source_uid,
        source_info = x['_id'],
        title = consistent_nasal_m(title),
        # mn123/pli/ms
        uid = uid,
        # SN 12.23
        sutta_ref = helpers.uid_to_ref(x['uid']),
        # pli
        language = x['lang'],
        content_plain = content_plain,
        # Not saving the html to reduce DB size. content_plain is used for
        # indexing and search. Re-generate HTML from JSON is needed.
        content_html = null(),
        content_json = consistent_nasal_m(content),
        content_json_tmpl = tmpl_json,
        created_at = func.now(),
    )


def get_titles(db: DBHandle, language = 'en') -> dict[str, str]:
    if language == 'pli':
        get_names_aql = "LET docs = (FOR x IN names FILTER x.is_root == true RETURN x) RETURN docs"
        q = db.AQLQuery(get_names_aql)

    else:
        get_names_aql = "LET docs = (FOR x IN names FILTER x.lang == @language RETURN x) RETURN docs"
        q = db.AQLQuery(
            get_names_aql,
            bindVars={'language': language}
        )

    titles: dict[str, str] = {}
    for x in q.result[0]:
        uid = x['uid']
        if uid in titles.keys():
            logger.warn(f"title for {uid} exists")
        else:
            titles[uid] = x['name']

    return titles


def _res_is_ignored(r: Dict[str, str]) -> bool:
    # ignore site pages and some collections
    if ('file_path' in r.keys() and '/site/' in r['file_path']) \
        or ('file_path' in r.keys() and '/xplayground/' in r['file_path']) \
        or ('file_path' in r.keys() and '/sutta/sa/' in r['file_path']) \
        or ('file_path' in r.keys() and '/sutta/ma/' in r['file_path']) \
        or ('file_path' in r.keys() and '-blurbs_' in r['file_path']) \
        or ('file_path' in r.keys() and '-name_translation' in r['file_path']):

        return True

    # ignore comments
    if 'muids' in r.keys() and 'comment' in r['muids']:

        return True

    # html bilara wrapper JSON already collected, skip
    if ('file_path' in r.keys() and 'sc_bilara_data/html' in r['file_path']) \
        and ('muids' in r.keys() and 'html' in r['muids']):

        return True

    return False


def _uid_is_ignored(uid: str) -> bool:
    # ignore 'none' author
    if uid.endswith('/none'):
        logger.warn(f"Author (source) is None: {uid}")
        return True

    # ignore blurbs
    if uid.endswith('-blurbs'):
        return True

    # ignore titles list json
    if uid.endswith('-name'):
        return True

    if uid.endswith('/than') or uid.endswith('/thanissaro'):
        # We'll use Aj Thanissaro's translations from dhammatalks.org
        return True

    return False


def get_suttas(db: DBHandle, language = 'en', limit: Optional[int] = None) -> dict[str, Am.Sutta]:
    logger.info("=== get_suttas() ===")

    # NOTE: In suttacentral records an uid is not a unique record, it is the
    # sutta reference (dn12, an4.10). Some texts exist in two formats, both in
    # html_text and sc_bilara_texts.
    #
    # A record is unique to uid + language + author + format.
    #
    # Bilara format is newer and edited, we'll prefer that source to html_text.

    suttas: dict[str, Am.Sutta] = {}
    suttas_html_tmpl_json: dict[str, str] = {}

    get_html_text_aql = '''
    LET docs = (
        FOR x IN html_text
            FILTER x.lang == @language
            RETURN x
    )
    RETURN docs
    '''

    get_bilara_text_aql = '''
    LET docs = (
        FOR x IN sc_bilara_texts
            FILTER x.lang == @language
            RETURN x
    )
    RETURN docs
    '''

    get_bilara_text_templates_aql = '''
    LET docs = (
        FOR x IN sc_bilara_texts
            FILTER x.lang == 'pli' && x._key LIKE '%_html'
            RETURN x
    )
    RETURN docs
    '''

    # collect templates
    q = db.AQLQuery(get_bilara_text_templates_aql)

    tmpl_results = q.result[0]

    for r in tmpl_results:
        # html bilara wrapper JSON
        if ('file_path' in r.keys() and 'sc_bilara_data/html' in r['file_path']) \
            and ('muids' in r.keys() and 'html' in r['muids']):

            convert_paths_to_content(r)
            text_uid_ref = r['uid']
            if text_uid_ref not in suttas_html_tmpl_json.keys():
                suttas_html_tmpl_json[text_uid_ref] = r['text']

    titles = get_titles(db, language)

    def _html_title(x, _):
        return x['name']

    def _bilara_title(x, titles):
        uid = x['uid']
        if uid in titles:
            return titles[uid]
        else:
            return ''

    queries = (
        (get_html_text_aql, html_text_uid, html_text_to_sutta, _html_title),
        (get_bilara_text_aql, bilara_text_uid, bilara_text_to_sutta, _bilara_title),
    )

    total_results = 0
    ignored = 0
    known_dup = 0
    unknown_dup = 0

    for query, f_uid, f_to_sutta, f_title in queries:
        q = db.AQLQuery(
            query,
            bindVars={'language': language}
        )

        if limit:
            n = limit if len(q.result[0]) >= limit else len(q.result[0])
            text_results = q.result[0][0:n]
        else:
            text_results = q.result[0]

        total_results += len(text_results)

        for r in text_results:
            if _res_is_ignored(r):
                ignored += 1
                continue

            convert_paths_to_content(r)
            uid = f_uid(r)
            title = f_title(r, titles)
            tmpl_json = suttas_html_tmpl_json.get(r['uid'], None)

            if _uid_is_ignored(uid):
                ignored += 1
                continue

            if uid not in suttas.keys():
                suttas[uid] = f_to_sutta(r, title, tmpl_json)

            elif 'muids' in r.keys() and ('reference' in r['muids'] or 'variant' in r['muids']):
                # keeping only the 'root' version
                known_dup += 1
                continue

            elif 'muids' in r.keys() and 'root' in r['muids']:
                # keeping only the 'root' version
                known_dup += 1
                suttas[uid] = f_to_sutta(r, title, tmpl_json)

            elif r['_id'].startswith('sc_bilara_texts/') and suttas[uid].source_info.startswith('html_text/'):
                # keeping the Bilara version
                known_dup += 1
                suttas[uid] = f_to_sutta(r, title, tmpl_json)

            else:
                unknown_dup += 1
                logger.warn(f"Unknown duplicate uid: {uid}")
                logger.warn(r['_id'])
                logger.warn(r['muids'])
                logger.warn(suttas[uid].source_info)

    n = total_results - ignored - known_dup - unknown_dup
    if len(suttas) != n:
        logger.warn(f"Count is not adding up: {len(suttas)} != {n}, {total_results} - {ignored} - {known_dup} - {unknown_dup}.")

    # clear source_info, where we temp stored x['_id']
    for k, v in suttas.items():
        v.source_info = null() # type: ignore
        suttas[k] = v

    return suttas


def convert_paths_to_content(doc):
    conversions = (
        ('file_path', 'text', lambda f: f.read()),
        ('markup_path', 'markup', lambda f: f.read()),
        ('strings_path', 'strings', json.load),
    )

    for from_prop, to_prop, load_func in conversions:
        if (to_prop not in doc) and (from_prop in doc):
            file_path = doc[from_prop]
            if file_path is None:
                doc[to_prop] = None
            else:
                file_path = file_path.replace('/opt/sc/sc-flask/sc-data', f"{SC_DATA_DIR}")
                p = Path(file_path)

                if not p.exists():
                    logger.error(f"File not found: {p}")
                    doc[to_prop] = None
                else:
                    with open(p) as f:
                        doc[to_prop] = load_func(f)


def get_legacy_db(db_path: Path) -> Session:
    try:
        # Create an in-memory database
        engine = create_engine(f"sqlite+pysqlite:///{db_path}", echo=False)

        # db_conn = engine.connect()

        Session = sessionmaker(engine)
        Session.configure(bind=engine)
        db_session = Session()
    except Exception as e:
        logger.error(f"Can't connect to database: {e}")
        exit(1)

    return db_session


def add_sutta_variants(appdata_db: Session, sc_db: DBHandle, language: str, limit: Optional[int] = None):
    logger.info("=== add_sutta_variants() ===")

    get_bilara_text_variant_aql = '''
    LET docs = (
        FOR x IN sc_bilara_texts
            FILTER x.lang == @language && POSITION(x.muids, 'variant')
            RETURN x
    )
    RETURN docs
    '''

    q = sc_db.AQLQuery(
        get_bilara_text_variant_aql,
        bindVars={'language': language}
    )

    if limit:
        n = limit if len(q.result[0]) >= limit else len(q.result[0])
        text_results = q.result[0][0:n]
    else:
        text_results = q.result[0]

    results = []

    for r in text_results:
        convert_paths_to_content(r)

        if _res_is_ignored(r):
            continue

        sutta_uid = bilara_text_uid(r)
        source_uid = sutta_uid.split('/')[-1]

        if _uid_is_ignored(sutta_uid):
            continue

        res = appdata_db \
            .query(Am.Sutta.id) \
            .filter(Am.Sutta.uid == sutta_uid) \
            .first()

        if res is None:
            logger.error(f"add_sutta_variants() Can't find sutta uid: {sutta_uid}")
            continue

        sutta_id = int(res[0])

        item = Am.SuttaVariant(
            sutta_id = sutta_id,
            sutta_uid = sutta_uid,
            language = language,
            source_uid = source_uid,
            content_json = consistent_nasal_m(r['text']),
        )

        results.append(item)

    logger.info(f"Adding {len(results)} sutta variants ...")

    try:
        for i in results:
            appdata_db.add(i)
        appdata_db.commit()
    except Exception as e:
        logger.error(e)
        sys.exit(1)


def add_sutta_comments(appdata_db: Session, sc_db: DBHandle, language: str, limit: Optional[int] = None):
    logger.info("=== add_sutta_comments() ===")

    get_bilara_text_comment_aql = '''
    LET docs = (
        FOR x IN sc_bilara_texts
            FILTER x.lang == @language && POSITION(x.muids, 'comment')
            RETURN x
    )
    RETURN docs
    '''

    q = sc_db.AQLQuery(
        get_bilara_text_comment_aql,
        bindVars={'language': language}
    )

    if limit:
        n = limit if len(q.result[0]) >= limit else len(q.result[0])
        text_results = q.result[0][0:n]
    else:
        text_results = q.result[0]

    results = []

    for r in text_results:
        convert_paths_to_content(r)

        if _res_is_ignored(r):
            continue

        sutta_uid = bilara_text_uid(r)
        source_uid = sutta_uid.split('/')[-1]

        if _uid_is_ignored(sutta_uid):
            continue

        res = appdata_db \
            .query(Am.Sutta.id) \
            .filter(Am.Sutta.uid == sutta_uid) \
            .first()

        if res is None:
            logger.error(f"add_sutta_comments() Can't find sutta uid: {sutta_uid}")
            continue

        sutta_id = int(res[0])

        item = Am.SuttaComment(
            sutta_id = sutta_id,
            sutta_uid = sutta_uid,
            language = language,
            source_uid = source_uid,
            content_json = consistent_nasal_m(r['text']),
        )

        results.append(item)

    logger.info(f"Adding {len(results)} sutta comments ...")

    try:
        for i in results:
            appdata_db.add(i)
        appdata_db.commit()
    except Exception as e:
        logger.error(e)
        sys.exit(1)


def populate_suttas_from_suttacentral(appdata_db: Session, sc_db: DBHandle, limit: Optional[int] = None):
    for lang in ['en', 'pli']:
        suttas = get_suttas(sc_db, lang, limit)

        logger.info(f"Adding {lang}, count {len(suttas)} ...")

        try:
            # TODO: bulk insert errors out
            # NOTE: this is slow but works
            for i in suttas.values():
                appdata_db.add(i)
            appdata_db.commit()
        except Exception as e:
            logger.error(e)
            exit(1)

        add_sutta_variants(appdata_db, sc_db, lang, limit)

        add_sutta_comments(appdata_db, sc_db, lang, limit)

        logger.info(f"DONE: {lang}")

def populate_nyanatiloka_dict_words_from_legacy(appdata_db: Session, legacy_db: Session, limit: Optional[int] = None):
    logger.info("Adding Nyanatiloka DictWords from legacy dict_words")

    label = 'NYANAT'
    # create the dictionary
    dictionary = Am.Dictionary(
        label = label,
        title = "Nyanatiloka's Buddhist Dictionary",
        created_at = func.now(),
    )

    try:
        appdata_db.add(dictionary)
        appdata_db.commit()
    except Exception as e:
        logger.error(e)
        exit(1)

    # get words and commit to appdata db

    # label is stored lowercase in legacy db
    if limit:
        a = legacy_db.execute(f"SELECT * from dict_words WHERE entry_source = '{label.lower()}' LIMIT {limit};") # type: ignore
    else:
        a = legacy_db.execute(f"SELECT * from dict_words WHERE entry_source = '{label.lower()}';") # type: ignore

    LegacyDictWord = namedtuple('LegacyDictWord', a.keys())
    records = [LegacyDictWord(*r) for r in a.fetchall()]

    def _legacy_to_dict_word(x: LegacyDictWord) -> Am.DictWord:
        # all-lowercase uid
        uid = f"{x.word}/{label}".lower()
        return Am.DictWord(
            dictionary_id = dictionary.id,
            word = consistent_nasal_m(x.word),
            uid = uid,
            source_uid = label,
            definition_plain = compact_rich_text(x.definition_plain),
            definition_html = consistent_nasal_m(x.definition_html),
            summary = consistent_nasal_m(x.summary),
            created_at = func.now(),
        )

    dict_words: List[Am.DictWord] = list(map(_legacy_to_dict_word, records))

    try:
        for i in dict_words:
            appdata_db.add(i)
        appdata_db.commit()
    except Exception as e:
        logger.error(e)
        exit(1)

def populate_suttas_from_legacy(new_db_session, legacy_db_session):
    a = new_db_session.query(Am.Sutta).all()

    logger.info("Adding Suttas from root_texts")

    a = legacy_db_session.execute("SELECT * from root_texts;")

    # Convert the results into namedtuple
    # https://stackoverflow.com/a/22084672/195141

    RootText = namedtuple('RootText', a.keys())
    records = [RootText(*r) for r in a.fetchall()]

    def root_text_to_sutta(x: RootText) -> Am.Sutta:
        return Am.Sutta(
            title = x.title,
            uid = x.uid,
            sutta_ref = x.acronym,
            language = x.content_language,
            content_plain = x.content_plain,
            content_html = x.content_html,
            created_at = func.now(),
        )

    suttas: List[Am.Sutta] = list(map(root_text_to_sutta, records))

    try:
        # TODO: bulk insert errors out
        """
        (builtins.TypeError) SQLite DateTime type only accepts Python datetime and date objects as input.
        [SQL: INSERT INTO appdata.suttas (id, uid, group_path, group_index, sutta_ref, sutta_ref_pts, language, order_index, title, title_pali, title_trans, description, content_plain, content_html, source_info, source_language, message, copyright, license, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)]
        [parameters: [{}]]
        """

        # stmt = insert(Am.Sutta).values(suttas)
        # new_db_session.execute(stmt)

        # NOTE: this is slow but works
        for i in suttas:
            new_db_session.add(i)
        new_db_session.commit()
    except Exception as e:
        logger.error(e)
        exit(1)

    logger.info("Adding Suttas from traslated_texts")

    a = legacy_db_session.execute("SELECT * from translated_texts;")

    TranslatedText = namedtuple('TranslatedText', a.keys())
    records = [TranslatedText(*r) for r in a.fetchall()]

    def translated_text_to_sutta(x: TranslatedText) -> Am.Sutta:
        return Am.Sutta(
            title = x.title,
            title_pali = x.root_title,
            uid = x.uid,
            sutta_ref = x.acronym,
            language = x.content_language,
            content_plain = x.content_plain,
            content_html = x.content_html,
            created_at = func.now(),
        )

    suttas: List[Am.Sutta] = list(map(translated_text_to_sutta, records))

    try:
        for i in suttas:
            new_db_session.add(i)
        new_db_session.commit()
    except Exception as e:
        logger.error(e)
        exit(1)


def populate_dict_words_from_stardict(appdata_db: Session,
                                      stardict_base_path: Path,
                                      ignore_synonyms = False,
                                      limit: Optional[int] = None):
    logger.info("=== populate_dict_words_from_stardict() ===")

    for d in stardict_base_path.glob("*.zip"):
        logger.info(d)
        # use label as the ZIP file name without the .zip extension
        label = os.path.basename(d).replace('.zip', '')
        paths = parse_stardict_zip(Path(d))

        import_stardict_as_new(appdata_db,
                               DbSchemaName.AppData.value,
                               None,
                               paths,
                               label,
                               10000,
                               ignore_synonyms,
                               limit)


def insert_db_version(appdata_db: Session):
    p = Path('pyproject.toml')
    if not p.exists():
        logger.error("pyproject.toml not found")
        sys.exit(1)

    with open(p) as f:
        s = f.read()

    try:
        t = tomlkit.parse(s)
        v = t['simsapa']['db_version'] # type: ignore
        ver = f"{v}"
    except Exception as e:
        logger.error(e)
        sys.exit(1)

    item = Am.AppSetting(
        key = "db_version",
        value = ver,
    )

    try:
        appdata_db.add(item)
        appdata_db.commit()
    except Exception as e:
        logger.error(e)
        sys.exit(1)


def main():
    create_app_dirs()

    appdata_db_path = BOOTSTRAP_ASSETS_DIR.joinpath("dist").joinpath("appdata.sqlite3")
    appdata_db = helpers.get_appdata_db(appdata_db_path, remove_if_exists = True)

    legacy_db_path = BOOTSTRAP_ASSETS_DIR.joinpath("db").joinpath("appdata-legacy.sqlite3")
    legacy_db = get_legacy_db(legacy_db_path)

    limit = BOOTSTRAP_LIMIT

    sc_db = get_suttacentral_db()

    stardict_base_path = BOOTSTRAP_ASSETS_DIR.joinpath("dict")

    insert_db_version(appdata_db)

    # NOTE: Deprecated. Use the suttacentral db.
    # populate_suttas_from_legacy(appdata_db, legacy_db)

    populate_nyanatiloka_dict_words_from_legacy(appdata_db, legacy_db, limit)

    populate_suttas_from_suttacentral(appdata_db, sc_db, limit)

    cst4.populate_suttas_from_cst4(appdata_db, limit)

    dhammatalks_org.populate_suttas_from_dhammatalks_org(appdata_db, limit)

    dhammapada_munindo.populate_suttas_from_dhammapada_munindo(appdata_db, limit)

    dhammapada_tipitaka_net.populate_suttas_from_dhammapada_tipitaka_net(appdata_db, limit)

    # FIXME improve synonym parsing
    populate_dict_words_from_stardict(appdata_db, stardict_base_path, ignore_synonyms=True, limit=limit)

    # Create db links from ssp:// links after all suttas have been added.
    create_links.populate_links(appdata_db)

if __name__ == "__main__":
    main()
