from datetime import datetime
from functools import partial
import math
from typing import Any, List, Optional
from pathlib import Path
import json
import queue

from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QThreadPool, Qt, QUrl, QTimer
from PyQt6.QtGui import QIcon, QCloseEvent, QPixmap, QStandardItem, QStandardItemModel, QAction
from PyQt6.QtWidgets import (QComboBox, QCompleter, QFrame, QLineEdit, QListWidget,
                             QHBoxLayout, QPushButton, QSizePolicy, QToolBar, QVBoxLayout)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings

from simsapa import SEARCH_TIMER_SPEED, SIMSAPA_PACKAGE_DIR, logger, ApiAction, ApiMessage
from simsapa import APP_QUEUES, GRAPHS_DIR, TIMER_SPEED
from simsapa.layouts.dictionary_queries import DictionaryQueries
from simsapa.layouts.find_panel import FindPanel
from simsapa.layouts.reader_web import ReaderWebEnginePage
from ..app.db import appdata_models as Am
from ..app.db import userdata_models as Um
from ..app.db.search import SearchIndexed, SearchResult, dict_word_hit_to_search_result
from ..app.types import AppData, DictionarySearchWindowInterface, USutta, UDictWord
from ..assets.ui.dictionary_search_window_ui import Ui_DictionarySearchWindow
from .memo_dialog import HasMemoDialog
from .memos_sidebar import HasMemosSidebar
from .links_sidebar import HasLinksSidebar
from .fulltext_list import HasFulltextList
from .import_stardict_dialog import HasImportStarDictDialog
from .help_info import show_search_info, setup_info_button
from .search_query_worker import SearchQueryWorker, SearchRet


class DictionarySearchWindow(DictionarySearchWindowInterface, Ui_DictionarySearchWindow, HasMemoDialog,
                             HasLinksSidebar, HasMemosSidebar,
                             HasFulltextList, HasImportStarDictDialog):

    searchbar_layout: QHBoxLayout
    search_extras: QHBoxLayout
    palibuttons_frame: QFrame
    search_input: QLineEdit
    toggle_pali_btn: QPushButton
    content_layout: QVBoxLayout
    qwe: QWebEngineView
    _app_data: AppData
    _results: List[SearchResult]
    _autocomplete_model: QStandardItemModel
    _current_words: List[UDictWord]
    selected_info: Any
    _search_timer = QTimer()
    _last_query_time = datetime.now()
    search_query_worker: Optional[SearchQueryWorker] = None

    def __init__(self, app_data: AppData, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        logger.info("DictionarySearchWindow()")

        self.fulltext_list: QListWidget
        self.recent_list: QListWidget

        self.features: List[str] = []
        self._app_data: AppData = app_data
        self._results: List[SearchResult] = []
        self._recent: List[UDictWord] = []
        self._current_words: List[UDictWord] = []

        self.page_len = 20

        self.thread_pool = QThreadPool()

        self.queries = DictionaryQueries(self._app_data)
        self._autocomplete_model = QStandardItemModel()

        self.queue_id = 'window_' + str(len(APP_QUEUES))
        APP_QUEUES[self.queue_id] = queue.Queue()
        self.messages_url = f'{self._app_data.api_url}/queues/{self.queue_id}'

        self.selected_info = {}

        self.graph_path: Path = GRAPHS_DIR.joinpath(f"{self.queue_id}.html")

        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_messages)
        self.timer.start(TIMER_SPEED)

        self._ui_setup()
        self._connect_signals()

        self.init_fulltext_list()
        self.init_memo_dialog()
        self.init_memos_sidebar()
        self.init_links_sidebar()
        self.init_stardict_import_dialog()

        self._setup_qwe_context_menu()

    def _init_search_query_worker(self, query: str = ""):
        idx = self.dict_filter_dropdown.currentIndex()
        source = self.dict_filter_dropdown.itemText(idx)
        if source == "Dictionaries":
            only_source = None
        else:
            only_source = source

        disabled_labels = self._app_data.app_settings.get('disabled_dict_labels', None)
        self._last_query_time = datetime.now()

        self.search_query_worker = SearchQueryWorker(
            self._app_data.search_indexed.dict_words_index,
            self.page_len,
            dict_word_hit_to_search_result)

        self.search_query_worker.set_query(query,
                                           self._last_query_time,
                                           disabled_labels,
                                           only_source)

        self.search_query_worker.signals.finished.connect(partial(self._search_query_finished))

    def _lookup_clipboard_in_suttas(self):
        text = self._app_data.clipboard_getText()
        if text is not None and self._app_data.actions_manager is not None:
            self._app_data.actions_manager.lookup_in_suttas(text)

    def _lookup_clipboard_in_dictionary(self):
        self.activateWindow()
        s = self._app_data.clipboard_getText()
        if s is not None:
            self._set_query(s)
            self._handle_query()
            self._handle_exact_query()

    def _lookup_selection_in_suttas(self):
        text = self._get_selection()
        if text is not None and self._app_data.actions_manager is not None:
            self._app_data.actions_manager.lookup_in_suttas(text)

    def _lookup_selection_in_dictionary(self):
        self.activateWindow()
        text = self._get_selection()
        if text is not None:
            self._set_query(text)
            self._handle_query()
            self._handle_exact_query()

    def _get_selection(self) -> Optional[str]:
        text = self.qwe.selectedText()
        # U+2029 Paragraph Separator to blank line
        text = text.replace('\u2029', "\n\n")
        text = text.strip()
        if len(text) > 0:
            return text
        else:
            return None

    def highlight_results_page(self, page_num: int) -> List[SearchResult]:
        if self.search_query_worker is None:
            return []
        else:
            return self.search_query_worker.search_query.highlight_results_page(page_num)

    def query_hits(self) -> int:
        if self.search_query_worker is None:
            return 0
        else:
            return self.search_query_worker.search_query.hits

    def closeEvent(self, event: QCloseEvent):
        if self.queue_id in APP_QUEUES.keys():
            del APP_QUEUES[self.queue_id]

        if self.graph_path.exists():
            self.graph_path.unlink()

        event.accept()

    def reinit_index(self):
        self._app_data.search_indexed = SearchIndexed()
        self._init_search_query_worker()

    def handle_messages(self):
        if self.queue_id in APP_QUEUES.keys():
            try:
                s = APP_QUEUES[self.queue_id].get_nowait()
                msg: ApiMessage = json.loads(s)
                if msg['action'] == ApiAction.show_sutta:
                    info = json.loads(msg['data'])
                    self._show_sutta_from_message(info)

                elif msg['action'] == ApiAction.show_sutta_by_uid:
                    info = json.loads(msg['data'])
                    if 'uid' in info.keys():
                        self._show_sutta_by_uid(info['uid'])

                elif msg['action'] == ApiAction.show_word_by_uid:
                    info = json.loads(msg['data'])
                    if 'uid' in info.keys():
                        self._show_word_by_uid(info['uid'])

                elif msg['action'] == ApiAction.lookup_clipboard_in_dictionary:
                    self._lookup_clipboard_in_dictionary()

                elif msg['action'] == ApiAction.lookup_in_dictionary:
                    text = msg['data']
                    self._set_query(text)
                    self._handle_query()
                    self._handle_exact_query()

                elif msg['action'] == ApiAction.set_selected:
                    info = json.loads(msg['data'])
                    self.selected_info = info

                APP_QUEUES[self.queue_id].task_done()
            except queue.Empty:
                pass

    def _ui_setup(self):
        self.links_tab_idx = 1
        self.memos_tab_idx = 2

        style = """
QWidget { border: 1px solid #272727; }
QWidget:focus { border: 1px solid #1092C3; }
        """

        self.search_input.setStyleSheet(style)

        completer = QCompleter(self._autocomplete_model, self)
        completer.setMaxVisibleItems(20)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setModelSorting(QCompleter.ModelSorting.CaseInsensitivelySortedModel)

        self.search_input.setCompleter(completer)

        self._setup_dict_filter_dropdown()
        self._setup_dict_select_button()
        self._setup_toggle_pali_button()
        setup_info_button(self.search_extras, self)

        self._setup_pali_buttons()
        self._setup_qwe()

        self.search_input.setFocus()

        self._find_panel = FindPanel()

        self.find_toolbar = QToolBar()
        self.find_toolbar.addWidget(self._find_panel)

        self.addToolBar(QtCore.Qt.ToolBarArea.BottomToolBarArea, self.find_toolbar)
        self.find_toolbar.hide()

    def _setup_qwe(self):
        self.qwe = QWebEngineView()
        self.qwe.setPage(ReaderWebEnginePage(self))

        self.qwe.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.qwe.setHtml(self.queries.render_html_page(body=''))
        self.qwe.show()
        self.content_layout.addWidget(self.qwe, 100)

        # Enable dev tools
        self.qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        self.qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.ErrorPageEnabled, True)
        self.qwe.settings().setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)

    def _toggle_pali_buttons(self):
        show = self.toggle_pali_btn.isChecked()
        self.palibuttons_frame.setVisible(show)

        self._app_data.app_settings['dictionary_show_pali_buttons'] = show
        self._app_data._save_app_settings()

    def _setup_toggle_pali_button(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(":/keyboard"))

        btn = QPushButton()
        btn.setFixedSize(40, 40)
        btn.setToolTip("Toggle Pali Buttons")
        btn.clicked.connect(partial(self._toggle_pali_buttons))
        btn.setIcon(icon)

        show = self._app_data.app_settings.get('dictionary_show_pali_buttons', False)
        btn.setCheckable(True)
        btn.setChecked(show)

        self.toggle_pali_btn = btn
        self.search_extras.addWidget(self.toggle_pali_btn)

    def _setup_pali_buttons(self):
        palibuttons_layout = QHBoxLayout()
        self.palibuttons_frame.setLayout(palibuttons_layout)

        s = '√'
        btn = QPushButton(s)
        btn.setFixedSize(35, 35)
        btn.clicked.connect(partial(self._append_to_query, s))
        palibuttons_layout.addWidget(btn)

        lowercase = 'ā ī ū ṃ ṁ ṅ ñ ṭ ḍ ṇ ḷ ṛ ṣ ś'.split(' ')

        for i in lowercase:
            btn = QPushButton(i)
            btn.setFixedSize(35, 35)
            btn.clicked.connect(partial(self._append_to_query, i))
            palibuttons_layout.addWidget(btn)

        show = self._app_data.app_settings.get('dictionary_show_pali_buttons', False)
        self.palibuttons_frame.setVisible(show)

    def _get_filter_labels(self):
        res = []

        r = self._app_data.db_session.query(Am.Dictionary.label.distinct()).all()
        res.extend(r)

        r = self._app_data.db_session.query(Um.Dictionary.label.distinct()).all()
        res.extend(r)

        labels = sorted(set(map(lambda x: str(x[0]).lower(), res)))

        return labels

    def _setup_dict_filter_dropdown(self):
        cmb = QComboBox()
        items = ["Dictionaries",]
        items.extend(self._get_filter_labels())

        cmb.addItems(items)
        cmb.setFixedHeight(40)
        self.dict_filter_dropdown = cmb
        self.search_extras.addWidget(self.dict_filter_dropdown)

    def _setup_dict_select_button(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(":/dictionary"))

        btn = QPushButton()
        btn.setFixedSize(40, 40)
        btn.setToolTip("Select Dictionaries")
        btn.clicked.connect(partial(self._show_dict_select_dialog))
        btn.setIcon(icon)

        self.dict_select_btn = btn
        self.search_extras.addWidget(self.dict_select_btn)

    def _show_dict_select_dialog(self):
        from .dictionary_select_dialog import DictionarySelectDialog
        d = DictionarySelectDialog(self._app_data, self)

        if d.exec():
            self._handle_query()

    def _set_query(self, s: str):
        self.search_input.setText(s)

    def _append_to_query(self, s: str):
        a = self.search_input.text()
        n = self.search_input.cursorPosition()
        pre = a[:n]
        post = a[n:]
        self.search_input.setText(pre + s + post)
        self.search_input.setCursorPosition(n + len(s))
        self.search_input.setFocus()

    def _search_query_finished(self, ret: SearchRet):
        if self.search_query_worker is None:
            return

        if self._last_query_time != ret['query_started']:
            return

        self._results = ret['results']

        # Restore the search icon, processing finished
        icon_search = QtGui.QIcon()
        icon_search.addPixmap(QtGui.QPixmap(":/search"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.search_button.setIcon(icon_search)

        if self.search_query_worker.search_query.hits > 0:
            self.rightside_tabs.setTabText(0, f"Fulltext ({self.search_query_worker.search_query.hits})")
        else:
            self.rightside_tabs.setTabText(0, "Fulltext")

        self.render_fulltext_page()

        if self.search_query_worker.search_query.hits == 1 and self._results[0]['uid'] is not None:
            self._show_word_by_uid(self._results[0]['uid'])

        self._update_fulltext_page_btn(self.search_query_worker.search_query.hits)

    def _start_query_worker(self, query: str):
        self._init_search_query_worker(query)
        if self.search_query_worker is not None:
            self.thread_pool.start(self.search_query_worker)

    def _handle_query(self, min_length: int = 4):
        query = self.search_input.text()

        if len(query) < min_length:
            return

        # Not aborting, show the user that the app started processsing
        icon_processing = QtGui.QIcon()
        icon_processing.addPixmap(QtGui.QPixmap(":/stopwatch"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_button.setIcon(icon_processing)

        self._handle_autocomplete_query(min_length)

        self._start_query_worker(query)

    def _handle_autocomplete_query(self, min_length: int = 4):
        query = self.search_input.text()

        if len(query) < min_length:
            return

        self._autocomplete_model.clear()

        a = self.queries.autocomplete_hits(query)

        for i in a:
            self._autocomplete_model.appendRow(QStandardItem(i))

        self._autocomplete_model.sort(0)

    def _handle_exact_query(self, add_recent: bool = False, min_length: int = 4):
        query = self.search_input.text()

        if len(query) < min_length:
            return

        res = self.queries.word_exact_matches(query)

        if len(res) > 0 and add_recent:
            self._add_recent(res[0])

        self._render_words(res)

    def _set_qwe_html(self, html: str):
        self.qwe.setHtml(html, baseUrl=QUrl(str(SIMSAPA_PACKAGE_DIR)))

    def _add_recent(self, word: UDictWord):
        # de-duplicate: if item already exists, remove it
        if word in self._recent:
            self._recent.remove(word)
        # insert new item on top
        self._recent.insert(0, word)

        # Rebuild Qt recents list
        self.recent_list.clear()

        def _to_title(x: UDictWord):
            return " - ".join([str(x.uid), str(x.word)])

        titles = list(map(lambda x: _to_title(x), self._recent))

        self.recent_list.insertItems(0, titles)

    @QtCore.pyqtSlot(str, QWebEnginePage.FindFlag)
    def on_searched(self, text: str, flag: QWebEnginePage.FindFlag):
        def callback(found):
            if text and not found:
                logger.info('Not found')

        self.qwe.findText(text, flag, callback)

    def _handle_result_select(self):
        selected_idx = self.fulltext_list.currentRow()
        if selected_idx < len(self._results):
            word = self.queries.dict_word_from_result(self._results[selected_idx])
            if word is not None:
                self._add_recent(word)
                self._show_word(word)

    def _handle_recent_select(self):
        selected_idx = self.recent_list.currentRow()
        word: UDictWord = self._recent[selected_idx]
        self._show_word(word)

    def _select_prev_recent(self):
        selected_idx = self.recent_list.currentRow()
        if selected_idx == -1:
            self.recent_list.setCurrentRow(0)
        elif selected_idx == 0:
            return
        else:
            self.recent_list.setCurrentRow(selected_idx - 1)

    def _select_next_recent(self):
        selected_idx = self.recent_list.currentRow()
        # List is empty or lost focus (no selected item)
        if selected_idx == -1:
            if len(self.recent_list) == 1:
                # Only one viewed item, which is presently being shown, and no
                # next item
                return
            else:
                # The 0 index is already the presently show item
                self.recent_list.setCurrentRow(1)

        elif selected_idx + 1 < len(self.recent_list):
            self.recent_list.setCurrentRow(selected_idx + 1)

    def _select_prev_result(self):
        selected_idx = self.fulltext_list.currentRow()
        if selected_idx == -1:
            self.fulltext_list.setCurrentRow(0)
        elif selected_idx == 0:
            return
        else:
            self.fulltext_list.setCurrentRow(selected_idx - 1)

    def _select_next_result(self):
        selected_idx = self.fulltext_list.currentRow()
        if selected_idx == -1:
            self.fulltext_list.setCurrentRow(0)
        elif selected_idx + 1 < len(self.fulltext_list):
            self.fulltext_list.setCurrentRow(selected_idx + 1)

    def _render_words(self, words: List[UDictWord]):
        self._current_words = words
        if len(self._current_words) == 0:
            return

        self.update_memos_list_for_dict_word(self._current_words[0])
        self.show_network_graph(self._current_words[0])

        page_html = self.queries.words_to_html_page(words)

        self._set_qwe_html(page_html)

    def _show_word(self, word: UDictWord):
        self._current_words = [word]

        self.update_memos_list_for_dict_word(self._current_words[0])
        self.show_network_graph(self._current_words[0])

        word_html = self.queries.get_word_html(word)

        font_size = self._app_data.app_settings.get('dictionary_font_size', 18)
        css_extra = f"html {{ font-size: {font_size}px; }}"

        page_html = self.queries.render_html_page(
            body = word_html['body'],
            css_head = word_html['css'],
            css_extra = css_extra,
            js_head = word_html['js'])

        self._set_qwe_html(page_html)

    def show_network_graph(self, word: Optional[UDictWord] = None):
        if word is None:
            if len(self._current_words) == 0:
                return
            else:
                word = self._current_words[0]

        self.generate_and_show_graph(None, word, self.queue_id, self.graph_path, self.messages_url)

    def _update_fulltext_page_btn(self, hits: int):
        if hits == 0:
            self.fulltext_page_input.setMinimum(0)
            self.fulltext_page_input.setMaximum(0)
            self.fulltext_first_page_btn.setEnabled(False)
            self.fulltext_last_page_btn.setEnabled(False)

        elif hits <= self.page_len:
            self.fulltext_page_input.setMinimum(1)
            self.fulltext_page_input.setMaximum(1)
            self.fulltext_first_page_btn.setEnabled(False)
            self.fulltext_last_page_btn.setEnabled(False)

        else:
            pages = math.floor(hits / self.page_len) + 1
            self.fulltext_page_input.setMinimum(1)
            self.fulltext_page_input.setMaximum(pages)
            self.fulltext_first_page_btn.setEnabled(True)
            self.fulltext_last_page_btn.setEnabled(True)

    def _show_selected(self):
        self._show_sutta_from_message(self.selected_info)

    def _show_sutta_from_message(self, info):
        sutta: Optional[USutta] = None

        if not 'table' in info.keys() or not 'id' in info.keys():
            return

        if info['table'] == 'appdata.suttas':
            sutta = self._app_data.db_session \
                .query(Am.Sutta) \
                .filter(Am.Sutta.id == info['id']) \
                .first()

        elif info['table'] == 'userdata.suttas':
            sutta = self._app_data.db_session \
                .query(Um.Sutta) \
                .filter(Um.Sutta.id == info['id']) \
                .first()

        self._app_data.sutta_to_open = sutta
        self.action_Sutta_Search.activate(QAction.ActionEvent.Trigger)

    def _show_sutta_by_uid(self, uid: str):
        results: List[USutta] = []

        res = self._app_data.db_session \
            .query(Am.Sutta) \
            .filter(Am.Sutta.uid == uid) \
            .all()
        results.extend(res)

        res = self._app_data.db_session \
            .query(Um.Sutta) \
            .filter(Um.Sutta.uid == uid) \
            .all()
        results.extend(res)

        if len(results) > 0:
            self._app_data.sutta_to_open = results[0]
            self.action_Sutta_Search.activate(QAction.ActionEvent.Trigger)

    def _show_word_by_bword_url(self, url: QUrl):
        # bword://localhost/American%20pasqueflower
        # path: /American pasqueflower
        query = url.path().replace('/', '')
        logger.info(f"Show Word: {query}")
        self._set_query(query)
        self._handle_query()
        self._handle_exact_query(add_recent=True)

    def _show_word_by_uid(self, uid: str):
        results = self.queries.get_words_by_uid(uid)
        if len(results) > 0:
            self._show_word(results[0])

    def _handle_copy(self):
        text = self._get_selection()
        if text is not None:
            self._app_data.clipboard_setText(text)

    def _handle_paste(self):
        s = self._app_data.clipboard_getText()
        if s is not None:
            self._append_to_query(s)
            self._handle_query()

    def _toggle_dev_tools_inspector(self):
        if self.devToolsAction.isChecked():
            self.dev_view = QWebEngineView()
            self.content_layout.addWidget(self.dev_view, 100)
            self.qwe.page().setDevToolsPage(self.dev_view.page())
        else:
            self.qwe.page().devToolsPage().deleteLater()
            self.dev_view.deleteLater()

    def _handle_open_content_new(self):
        if self._app_data.actions_manager is not None \
           and len(self._current_words) > 0:

            def _f(x: UDictWord):
                return (str(x.metadata.schema), int(str(x.id)))

            schemas_ids = list(map(_f, self._current_words))

            self._app_data.actions_manager.open_words_new(schemas_ids)
        else:
            logger.warn("Sutta is not set")

    def _setup_qwe_context_menu(self):
        self.qwe.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)

        copyAction = QAction("Copy", self.qwe)
        # NOTE: don't bind Ctrl-C, will be ambiguous to the window menu action
        copyAction.triggered.connect(partial(self._handle_copy))

        self.qwe.addAction(copyAction)

        memoAction = QAction("Create Memo", self.qwe)
        memoAction.triggered.connect(partial(self.handle_create_memo_for_dict_word))

        self.qwe.addAction(memoAction)

        lookupSelectionInSuttas = QAction("Lookup Selection in Suttas", self.qwe)
        lookupSelectionInSuttas.triggered.connect(partial(self._lookup_selection_in_suttas))

        self.qwe.addAction(lookupSelectionInSuttas)

        lookupSelectionInDictionary = QAction("Lookup Selection in Dictionary", self.qwe)
        lookupSelectionInDictionary.triggered.connect(partial(self._lookup_selection_in_dictionary))

        self.qwe.addAction(lookupSelectionInDictionary)

        icon = QIcon()
        icon.addPixmap(QPixmap(":/new-window"))

        open_new_action = QAction("Open in New Window", self.qwe)
        open_new_action.setIcon(icon)
        open_new_action.triggered.connect(partial(self._handle_open_content_new))

        self.qwe.addAction(open_new_action)

        self.devToolsAction = QAction("Show Inspector", self.qwe)
        self.devToolsAction.setCheckable(True)
        self.devToolsAction.triggered.connect(partial(self._toggle_dev_tools_inspector))

        self.qwe.addAction(self.devToolsAction)

    def _handle_show_find_panel(self):
        self.find_toolbar.show()
        self._find_panel.search_input.setFocus()

    def _increase_text_size(self):
        font_size = self._app_data.app_settings.get('dictionary_font_size', 18)
        self._app_data.app_settings['dictionary_font_size'] = font_size + 2
        self._app_data._save_app_settings()
        self._render_words(self._current_words)

    def _decrease_text_size(self):
        font_size = self._app_data.app_settings.get('dictionary_font_size', 18)
        if font_size < 5:
            return
        self._app_data.app_settings['dictionary_font_size'] = font_size - 2
        self._app_data._save_app_settings()
        self._render_words(self._current_words)

    def _show_search_result_sizes_dialog(self):
        from simsapa.layouts.search_result_sizes_dialog import SearchResultSizesDialog
        d = SearchResultSizesDialog(self._app_data, self)
        if d.exec():
            self.render_fulltext_page()

    def _user_typed(self):
        if not self._search_timer.isActive():
            self._search_timer = QTimer()
            self._search_timer.timeout.connect(partial(self._handle_query, min_length=4))
            self._search_timer.setSingleShot(True)

        self._search_timer.start(SEARCH_TIMER_SPEED)

    def _connect_signals(self):
        self.action_Close_Window \
            .triggered.connect(partial(self.close))

        self.search_button.clicked.connect(partial(self._handle_query, min_length=1))
        self.search_input.textEdited.connect(partial(self._user_typed))

        # FIXME is this useful? completion appears regardless.
        # self.search_input.completer().activated.connect(partial(self._handle_query, min_length=1))

        self.search_input.textEdited.connect(partial(self._handle_autocomplete_query, min_length=4))

        self.search_button.clicked.connect(partial(self._handle_exact_query, min_length=1))
        self.search_input.returnPressed.connect(partial(self._handle_exact_query, min_length=1))
        self.search_input.completer().activated.connect(partial(self._handle_exact_query, min_length=1))

        self.dict_filter_dropdown.currentIndexChanged.connect(partial(self._handle_query, min_length=4))

        self.recent_list.itemSelectionChanged.connect(partial(self._handle_recent_select))

        self._find_panel.searched.connect(self.on_searched) # type: ignore
        self._find_panel.closed.connect(self.find_toolbar.hide)

        self.add_memo_button \
            .clicked.connect(partial(self.add_memo_for_dict_word))

        self.action_Copy \
            .triggered.connect(partial(self._handle_copy))

        self.action_Paste \
            .triggered.connect(partial(self._handle_paste))

        self.action_Find_in_Page \
            .triggered.connect(self._handle_show_find_panel)

        self.action_Import_from_StarDict \
            .triggered.connect(partial(self.show_import_from_stardict_dialog))

        self.action_Search_Query_Terms \
            .triggered.connect(partial(show_search_info, self))

        self.action_Select_Dictionaries \
            .triggered.connect(partial(self._show_dict_select_dialog))

        self.action_Lookup_Clipboard_in_Suttas \
            .triggered.connect(partial(self._lookup_clipboard_in_suttas))

        self.action_Lookup_Clipboard_in_Dictionary \
            .triggered.connect(partial(self._lookup_clipboard_in_dictionary))

        self.action_Previous_Result \
            .triggered.connect(partial(self._select_prev_result))

        self.action_Next_Result \
            .triggered.connect(partial(self._select_next_result))

        self.back_recent_button.clicked.connect(partial(self._select_next_recent))

        self.forward_recent_button.clicked.connect(partial(self._select_prev_recent))

        self.action_Increase_Text_Size \
            .triggered.connect(partial(self._increase_text_size))

        self.action_Decrease_Text_Size \
            .triggered.connect(partial(self._decrease_text_size))

        self.action_Search_Result_Sizes \
            .triggered.connect(partial(self._show_search_result_sizes_dialog))
