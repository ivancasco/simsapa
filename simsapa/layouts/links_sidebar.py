from functools import partial
from pathlib import Path
from typing import Callable, Optional, Tuple

from PyQt5.QtWidgets import QSizePolicy, QTabWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QObject, QRunnable, QThread, QUrl, pyqtSignal, pyqtSlot

from ..app.graph import (generate_graph, sutta_nodes_and_edges,
                         dict_word_nodes_and_edges,
                         document_page_nodes_and_edges, sutta_graph_id)

from ..app.file_doc import FileDoc
from ..app.db import userdata_models as Um

from ..app.types import AppData, USutta, UDictWord

from simsapa import LOADING_HTML
from simsapa.app.helpers import get_db_engine_connection_session

class GraphGenSignals(QObject):
    finished = pyqtSignal()
    # Results is the number of hits (links) and the path of the graph html
    result = pyqtSignal(tuple)

class GraphGenerator(QRunnable):
    def __init__(self,
                 sutta: Optional[USutta],
                 dict_word: Optional[UDictWord],
                 queue_id: str,
                 graph_path: Path,
                 messages_url: str):

        super(GraphGenerator, self).__init__()

        # Allow removing the thread when another graph is started and this is
        # still in the queue.
        self.setAutoDelete(True)

        self.signals = GraphGenSignals()

        self.sutta = sutta
        self.dict_word = dict_word
        self.queue_id = queue_id
        self.graph_path = graph_path
        self.messages_url = messages_url

    @pyqtSlot()
    def run(self):
        try:
            _, _, self._db_session = get_db_engine_connection_session()

            if self.sutta is not None:

                (nodes, edges) = sutta_nodes_and_edges(self._db_session, self.sutta, distance=3)

                selected = []
                for idx, n in enumerate(nodes):
                    if n[0] == sutta_graph_id(self.sutta):
                        selected.append(idx)

            elif self.dict_word is not None:
                (nodes, edges) = dict_word_nodes_and_edges(self._db_session, self.dict_word, distance=3)

                selected = []
                for idx, n in enumerate(nodes):
                    if n[0] == sutta_graph_id(self.dict_word):
                        selected.append(idx)

            else:
                return

            generate_graph(nodes, edges, selected, self.queue_id, self.graph_path, self.messages_url)

            hits = len(nodes) - 1

            result = (hits, self.graph_path)

        except Exception as e:
            print("ERROR: {e}" % e)

        else:
            self.signals.result.emit(result)

        finally:
            self.signals.finished.emit()

class HasLinksSidebar:
    _app_data: AppData
    links_layout: QVBoxLayout
    rightside_tabs: QTabWidget
    links_tab_idx: int
    content_graph: QWebEngineView

    def init_links_sidebar(self):
        self.setup_content_graph()

    def setup_content_graph(self):
        self.content_graph = QWebEngineView()
        self.content_graph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.content_graph.setHtml('')
        self.content_graph.show()
        self.links_layout.addWidget(self.content_graph)

    def _graph_finished(self, result: Tuple[int, Path]):
        hits = result[0]
        graph_path = result[1]

        if hits > 0:
            self.rightside_tabs.setTabText(self.links_tab_idx, f"Links ({hits})")
        else:
            self.rightside_tabs.setTabText(self.links_tab_idx, "Links")

        self.content_graph.load(QUrl(str(graph_path.absolute().as_uri())))

    def generate_and_show_graph(self,
                                sutta: Optional[USutta],
                                dict_word: Optional[UDictWord],
                                queue_id: str,
                                graph_path: Path,
                                messages_url: str):

        # Remove worker thread which are in the queue.
        self._app_data.graph_gen_pool.clear()

        graph_gen = GraphGenerator(sutta, dict_word, queue_id, graph_path, messages_url)

        graph_gen.signals.result.connect(self._graph_finished)

        # Only update text when it already has a links number,
        # so that empty results don't cause jumping layout
        if self.rightside_tabs.tabText(self.links_tab_idx) != "Links":
            self.rightside_tabs.setTabText(self.links_tab_idx, "Links (...)")

        self.content_graph.setHtml(LOADING_HTML)

        self._app_data.graph_gen_pool.start(graph_gen)

    def generate_graph_for_document(self,
                                    file_doc: FileDoc,
                                    db_doc: Um.Document,
                                    queue_id: str,
                                    graph_path: Path,
                                    messages_url: str):

        (nodes, edges) = document_page_nodes_and_edges(
            db_session=self._app_data.db_session,
            db_doc=db_doc,
            page_number=file_doc._current_idx + 1,
            distance=3
        )

        hits = len(nodes) - 1
        if hits > 0:
            self.rightside_tabs.setTabText(self.links_tab_idx, f"Links ({hits})")
        else:
            self.rightside_tabs.setTabText(self.links_tab_idx, "Links")

        # central node was appended last
        selected = [len(nodes) - 1]

        generate_graph(nodes, edges, selected, queue_id, graph_path, messages_url)
