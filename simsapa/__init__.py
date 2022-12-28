import os
from pathlib import Path
from typing import Dict, TypedDict
from enum import Enum
import queue
import multiprocessing as mp
from dotenv import find_dotenv, load_dotenv
import appdirs
import platform
import importlib.resources
import pkgutil

p = find_dotenv() or find_dotenv('.env.txt')
if p != '':
    load_dotenv(p)

SIMSAPA_PACKAGE_DIR = importlib.resources.files('simsapa')

PACKAGE_ASSETS_RSC_DIR = Path('assets')
PACKAGE_ASSETS_DIR = SIMSAPA_PACKAGE_DIR.joinpath(str(PACKAGE_ASSETS_RSC_DIR))

ALEMBIC_INI = SIMSAPA_PACKAGE_DIR.joinpath('alembic.ini')
ALEMBIC_DIR = SIMSAPA_PACKAGE_DIR.joinpath('alembic')

ICONS_DIR = SIMSAPA_PACKAGE_DIR.joinpath('assets/icons/')

s = os.getenv('SIMSAPA_DIR')
if s is not None and s != '':
    SIMSAPA_DIR = Path(s)
else:
    SIMSAPA_DIR = Path(appdirs.user_data_dir('simsapa'))

SIMSAPA_LOG_PATH = SIMSAPA_DIR.joinpath('log.txt')

TEST_ASSETS_DIR = SIMSAPA_PACKAGE_DIR.joinpath('../tests/data/assets')

TIMER_SPEED = 30

SEARCH_TIMER_SPEED = 500

#s = os.getenv('USE_TEST_DATA')
#if s is not None and s.lower() == 'true':
#    ASSETS_DIR = TEST_ASSETS_DIR
#else:
#    ASSETS_DIR = SIMSAPA_DIR.joinpath('assets')

ASSETS_DIR = SIMSAPA_DIR.joinpath('assets')

INDEX_DIR = ASSETS_DIR.joinpath('index')

GRAPHS_DIR = ASSETS_DIR.joinpath('graphs')

APP_DB_PATH = ASSETS_DIR.joinpath('appdata.sqlite3')
USER_DB_PATH = ASSETS_DIR.joinpath('userdata.sqlite3')

COURSES_DIR = ASSETS_DIR.joinpath('courses')

STARTUP_MESSAGE_PATH = SIMSAPA_DIR.joinpath("startup_message.json")

APP_QUEUES: Dict[str, queue.Queue] = {}
SERVER_QUEUE = mp.Queue()

IS_LINUX = (platform.system() == 'Linux')
IS_WINDOWS = (platform.system() == 'Windows')
IS_MAC = (platform.system() == 'Darwin')

READING_TEXT_COLOR = "#1a1a1a" # 90% black
READING_BACKGROUND_COLOR = "#FAE6B2"
DARK_READING_BACKGROUND_COLOR = "#F0B211"
BUTTON_BG_COLOR = "#007564"

b = pkgutil.get_data(__name__, str(PACKAGE_ASSETS_RSC_DIR.joinpath("templates/loading.html")))
if b is None:
    LOADING_HTML = "<b>Loading...</b>"
else:
    LOADING_HTML = b.decode("utf-8")

b =  pkgutil.get_data(__name__, str(PACKAGE_ASSETS_RSC_DIR.joinpath("templates/click_generate.html")))
if b is None:
    CLICK_GENERATE_HTML = "<b>Missing click_generate.html</b>"
else:
    CLICK_GENERATE_HTML = b.decode("utf-8")


b = pkgutil.get_data(__name__, str(PACKAGE_ASSETS_RSC_DIR.joinpath('css/suttas.css')))
if b is None:
    SUTTAS_CSS = ""
else:
    SUTTAS_CSS = b.decode("utf-8")

b = pkgutil.get_data(__name__, str(PACKAGE_ASSETS_RSC_DIR.joinpath('js/suttas.js')))
if b is None:
    SUTTAS_JS = ""
else:
    SUTTAS_JS = b.decode("utf-8")

b = pkgutil.get_data(__name__, str(PACKAGE_ASSETS_RSC_DIR.joinpath('js/dictionary.js')))
if b is None:
    DICTIONARY_JS = ""
else:
    DICTIONARY_JS = b.decode("utf-8")

class DbSchemaName(str, Enum):
    AppData = 'appdata'
    UserData = 'userdata'

class ApiAction(str, Enum):
    lookup_clipboard_in_dictionary = 'lookup_clipboard_in_dictionary'
    lookup_clipboard_in_suttas = 'lookup_clipboard_in_suttas'
    lookup_in_dictionary = 'lookup_in_dictionary'
    lookup_in_suttas = 'lookup_in_suttas'
    open_in_study_window = 'open_in_study_window'
    open_sutta_new = 'open_sutta_new'
    open_words_new = 'open_words_new'
    show_sutta_by_uid = 'show_sutta_by_uid'
    show_sutta = 'show_sutta'
    show_word_by_uid = 'show_word_by_uid'
    show_word_scan_popup = 'show_word_scan_popup'
    set_selected = "set_selected"

# Messages sent via the localhost web API
class ApiMessage(TypedDict):
    queue_id: str
    action: ApiAction
    data: str

class ShowLabels(str, Enum):
    SuttaRef = "Sutta Ref."
    RefAndTitle = "Ref. + Title"
    NoLabels = "No Labels"
