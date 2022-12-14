import re
from typing import List, Optional, TypedDict
from binascii import crc32
from urllib.parse import urlencode
from PyQt6.QtCore import QObject, QRunnable, QUrl, pyqtSignal, pyqtSlot
import bleach
from bs4 import BeautifulSoup

from sqlalchemy import or_

from simsapa import DICTIONARY_JS, SIMSAPA_PACKAGE_DIR, DbSchemaName, logger
from simsapa.app.db.search import RE_SUTTA_REF, SearchResult, dict_word_to_search_result
from simsapa.app.db_helpers import get_db_engine_connection_session
from ..app.types import AppData, Labels, QueryType, UDictWord
from ..app.db import appdata_models as Am
from ..app.db import userdata_models as Um
from .html_content import page_tmpl

class ResultHtml(TypedDict):
    body: str
    css: str
    js: str

class DictionaryQueries:
    def __init__(self, app_data: AppData):
        self._app_data = app_data

    def get_words_by_uid(self, uid: str) -> List[UDictWord]:
        results: List[UDictWord] = []

        res = self._app_data.db_session \
            .query(Am.DictWord) \
            .filter(Am.DictWord.uid == uid) \
            .all()
        results.extend(res)

        res = self._app_data.db_session \
            .query(Um.DictWord) \
            .filter(Um.DictWord.uid == uid) \
            .all()
        results.extend(res)

        return results

    def dict_word_from_result(self, x: SearchResult) -> Optional[UDictWord]:
        if x['schema_name'] == DbSchemaName.AppData.value:
            word = self._app_data.db_session \
                                 .query(Am.DictWord) \
                                 .filter(Am.DictWord.id == x['db_id']) \
                                 .first()
        else:
            word = self._app_data.db_session \
                                 .query(Um.DictWord) \
                                 .filter(Um.DictWord.id == x['db_id']) \
                                 .first()
        return word

    def words_to_html_page(self, words: List[UDictWord], css_extra: Optional[str] = None) -> str:
        # avoid multiple copies of the same content with a crc32 checksum
        page_body: dict[int, str] = {}
        page_css: dict[int, str] = {}
        page_js: dict[int, str] = {}

        for w in words:
            word_html = self.get_word_html(w)

            body_sum = crc32(bytes(word_html['body'], 'utf-8'))
            if body_sum not in page_body.keys():
                page_body[body_sum] = word_html['body']

            css_sum = crc32(bytes(word_html['css'], 'utf-8'))
            if css_sum not in page_css.keys():
                page_css[css_sum] = word_html['css']

            js_sum = crc32(bytes(word_html['js'], 'utf-8'))
            if js_sum not in page_js.keys():
                page_js[js_sum] = word_html['js']

        font_size = self._app_data.app_settings.get('dictionary_font_size', 18)
        css = f"html {{ font-size: {font_size}px; }}"
        if css_extra:
            css_extra += css
        else:
            css_extra = css

        page_html = self.render_html_page(
            body = "\n\n".join(page_body.values()),
            css_head = "\n\n".join(page_css.values()),
            css_extra = css_extra,
            js_head = "\n\n".join(page_js.values()))

        return page_html

    def _add_grammar_links(self, html_page: str) -> str:
        """
        <tr>
        <td><b>noun</b></td>
        <td>nt loc sg</td>
        <td>of</td>
        <td>dhammacakkhu</td>
        </tr>
        """

        grammar_rows = re.findall(r'(<td>([^>]+)</td>\s*</tr>)', html_page)

        for m in grammar_rows:
            dict_word = m[1].lower().strip()
            url = QUrl(f"ssp://{QueryType.words.value}/{dict_word}")
            link = f'<a href="{url.toString()}">{m[1]}</a>'

            html_page = html_page.replace(m[0], f'<td>{link}</td></tr>')

        return html_page

    def _add_example_links(self, html_page: str) -> str:
        example_ids: List[str] = re.findall(r'id="(example__[^"]+)"', html_page)
        if len(example_ids) == 0:
            return html_page

        soup = BeautifulSoup(html_page, 'html.parser')
        for idx, div_id in enumerate(example_ids):
            h = soup.find(id = div_id)
            if h is None:
                logger.error(f"Can't find #{div_id}")
            else:
                example_content = h.decode_contents() # type: ignore

                # FIXME: DPD dict. exmple text <p> tags are not closed before the sutta <p>.
                # FIXME: DPD dict. sutta refs format doesn't match.
                """
                <p>atthi nu kho bhante kiñci rūpaṃ yaṃ rūpaṃ niccaṃ dhuvaṃ sassataṃ avipariṇāma<b>dhammaṃ</b> sassatisamaṃ tath'eva ṭhassati<p class="sutta">SN 22.97 nakhasikhāsuttaṃ</p><p>gāth'ābhigītaṃ me abhojaneyyaṃ,<br/>sampassataṃ brāhmaṇa n'esa dhammo,<br/>gāth'ābhigītaṃ panudanti buddhā,<br/><b>dhamme</b> satī brāhmaṇa vutti'r'esā.<p class="sutta">SNP 4 kasibhāradvājasuttaṃ<br/>uragavaggo 4</p><p>Can you think of a better example? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSf9boBe7k5tCwq7LdWgBHHGIPVc4ROO5yjVDo1X5LDAxkmGWQ/viewform?usp=pp_url&amp;entry.438735500=dhamma 01&amp;entry.326955045=Example1&amp;entry.1433863141=GoldenDict 2022-11-08" target="_blank">Add it here.</a></p></p></p>
                """

                linked_content = example_content

                for m in re.findall(r'<p>(.*?)\s*(<p class="sutta">([^>]+)</p>)', example_content, flags = re.DOTALL | re.MULTILINE):
                    quote = bleach.clean(m[0], tags=[], strip=True)
                    n = 50 if len(quote) > 50 else len(quote)
                    quote = quote[0:n]

                    text = m[2].strip()
                    ref = re.search(RE_SUTTA_REF, text)
                    if not ref:
                        continue

                    sutta_uid = f"{ref.group(1)}{ref.group(2)}/pli/cst4".lower()

                    url = QUrl(f"ssp://{QueryType.suttas.value}/{sutta_uid}")
                    url.setQuery(urlencode({'q': quote}))

                    link = f'<a href="{url.toString()}">{m[2]}</a>'

                    linked_content = re.sub(m[1], f'<p class="sutta">{link}</p>', linked_content)

                html_page = html_page.replace(example_content, linked_content)

        return html_page

    def render_html_page(self,
                          body: str,
                          css_head: str = '',
                          css_extra: Optional[str] = None,
                          js_head: str = '',
                          js_body: str = '') -> str:
        try:
            with open(SIMSAPA_PACKAGE_DIR.joinpath('assets/css/dictionary.css'), 'r') as f:
                css = f.read()
                if self._app_data.api_url is not None:
                    css = css.replace("http://localhost:8000", self._app_data.api_url)
        except Exception as e:
            logger.error("Can't read dictionary.css")
            css = ""

        css_head = re.sub(r'font-family[^;]+;', '', css_head)
        css_head += css

        if css_extra is not None:
            css_head += css_extra

        js_head += DICTIONARY_JS

        if 'id="example__' in body:
            body = self._add_example_links(body)

        # body = self._add_grammar_links(body)

        html = str(page_tmpl.render(content=body,
                                    css_head=css_head,
                                    js_head=js_head,
                                    js_body=js_body,
                                    api_url=self._app_data.api_url))

        return html

    def word_heading(self, w: UDictWord) -> str:
        return f"""
        <div class="word-heading">
            <h1>{w.word}</h1>
            <div class="uid">{w.uid}</div>
        </div>
        <div class="clear"></div>
        """

    def get_word_html(self, word: UDictWord) -> ResultHtml:
        if word.definition_html is not None and word.definition_html != '':
            definition = str(word.definition_html)

        elif word.definition_plain is not None and word.definition_plain != '':
            style = '<style>pre { font-family: serif; }</style>'
            text = str(word.definition_plain)

            # Wordnet uses curly braces syntax for links: {Lions' beard}
            matches = re.findall(r'(\{(.+?)\})', text, flags = re.DOTALL)
            for m in matches:
                name = m[0].replace('{', '').replace('}', '')
                name = re.sub(r'[\n ]+', ' ', name)
                url = f"ssp://{QueryType.words.value}/{name.replace(' ', '%20')}"
                text = text.replace(m[0], f'<a href="{url}">{name}</a>')

            definition = style + '<pre>' + text + '</pre>'

        else:
            definition = '<p>No definition.</p>'

        # We'll remove CSS and JS from 'definition' before assigning it to 'body'
        body = ""
        css = ""
        js = ""

        soup = BeautifulSoup(str(definition), 'html.parser')

        if '<style' in definition:
            h = soup.find_all(name = 'style')
            for i in h:
                css += i.decode_contents()
                definition = definition.replace(css, '')

        if '<script' in definition:
            h = soup.find_all(name = 'script')
            for i in h:
                js += i.decode_contents()
                definition = definition.replace(js, '')

        if '<html' in definition or '<HTML' in definition:
            # Definition is a complete HTML page with a <body> block
            h = soup.find(name = 'body')
            if h is not None:
                body = h.decode_contents() # type: ignore
            else:
                logger.warn("Missing <body> from html page in %s" % word.uid)
                body = definition
        else:
            # Definition is a HTML fragment block, CSS and JS already removed
            body = definition

        def example_format(example):
            return "<div>" + example.text_html + "</div><div>" + example.translation_html + "</div>"

        examples = "".join(list(map(example_format, word.examples))) # type: ignore

        # Wrap definition body in a class
        body = "<div class=\"word-definition\">%s</div>" % body

        # Add examples to body
        if len(examples) > 0:
            body += "<div class=\"word-examples\">%s</div>" % examples

        body = self.word_heading(word) + body

        return ResultHtml(
            body = body,
            css = css,
            js = js,
        )

    def autocomplete_hits(self, query: str) -> set[str]:
        a = set(filter(lambda x: x.lower().startswith(query.lower()), self._app_data.completion_cache['dict_words']))
        return a

class ExactQueryResult(TypedDict):
    appdata_ids: List[int]
    userdata_ids: List[int]
    add_recent: bool

class ExactQueryWorkerSignals(QObject):
    finished = pyqtSignal(dict)

class ExactQueryWorker(QRunnable):
    signals: ExactQueryWorkerSignals

    def __init__(self,
                 query: str,
                 only_source: Optional[str] = None,
                 disabled_labels: Optional[Labels] = None,
                 add_recent: bool = True):

        super().__init__()
        self.signals = ExactQueryWorkerSignals()
        self.query = query
        self.only_source = only_source
        self.disabled_labels = disabled_labels
        self.add_recent = add_recent

    @pyqtSlot()
    def run(self):
        logger.info("ExactQueryWorker::run()")
        try:
            _, _, db_session = get_db_engine_connection_session()

            res: List[UDictWord] = []

            r = db_session \
                .query(Am.DictWord) \
                .filter(or_(
                    Am.DictWord.word.like(f"{self.query}%"),
                    Am.DictWord.synonyms.like(f"%{self.query}%"),
                )) \
                .all()
            res.extend(r)

            r = db_session \
                .query(Um.DictWord) \
                .filter(or_(
                    Um.DictWord.word.like(f"{self.query}%"),
                    Um.DictWord.synonyms.like(f"%{self.query}%"),
                )) \
                .all()
            res.extend(r)

            def _only_in_source(x: UDictWord):
                if self.only_source is not None:
                    return str(x.uid).endswith(f'/{self.only_source.lower()}')
                else:
                    return True

            def _not_in_disabled(x: UDictWord):
                if self.disabled_labels is not None:
                    for schema in self.disabled_labels.keys():
                        for label in self.disabled_labels[schema]:
                            if x.metadata.schema == schema and str(x.uid).endswith(f'/{label.lower()}'):
                                return False
                    return True
                else:
                    return True

            if self.only_source is not None:
                res = list(filter(_only_in_source, res))

            elif self.disabled_labels is not None:
                res = list(filter(_not_in_disabled, res))

            ch = "." * len(self.query)
            # for 'dhamma' also match 'dhammā'
            # for 'akata' also match 'akaṭa'
            # for 'kondanna' also match 'koṇḍañña'
            p_query = re.compile(f"^{ch}$")
            # for 'dhamma' also match 'dhamma 1'
            p_num = re.compile(f"^{ch}[ 0-9]+$")

            def _is_match(x: UDictWord):
                if x.word is None:
                    return False
                else:
                    return re.match(p_query, str(x.word)) or re.match(p_num, str(x.word))

            res = list(filter(_is_match, res))

            a = filter(lambda x: x.metadata.schema == DbSchemaName.AppData.value, res)
            appdata_ids = list(map(lambda x: x.id, a))

            a = filter(lambda x: x.metadata.schema == DbSchemaName.UserData.value, res)
            userdata_ids = list(map(lambda x: x.id, a))

            db_session.close()

            ret = ExactQueryResult(
                appdata_ids = appdata_ids,
                userdata_ids = userdata_ids,
                add_recent = self.add_recent,
            )

            self.signals.finished.emit(ret)

        except Exception as e:
            logger.error(e)
