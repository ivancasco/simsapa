from functools import partial
from typing import Optional

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

from simsapa import IS_WINDOWS, SIMSAPA_PACKAGE_DIR, logger
from ..app.types import AppData, USutta
from .html_content import html_page

class SuttaTabWidget(QWidget):
    def __init__(self,
                 app_data: AppData,
                 title: str,
                 tab_index: int,
                 qwe: QWebEngineView,
                 sutta: Optional[USutta] = None) -> None:

        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.setProperty('style_class', 'sutta_tab')

        self._app_data = app_data
        self.title = title
        self.tab_index = tab_index
        self.qwe = qwe
        self.sutta = sutta
        self.api_url = self._app_data.api_url

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)
        self._layout.addWidget(self.qwe, 100)

        if not IS_WINDOWS:
            # FIXME app not responding
            icon = QIcon()
            icon.addPixmap(QPixmap(":/new-window"))

            open_new_action = QAction("Open in New Window", qwe)
            open_new_action.setIcon(icon)
            open_new_action.triggered.connect(partial(self._handle_open_content_new))

            self.qwe.addAction(open_new_action)

        self.devToolsAction = QAction("Show Inspector", qwe)
        self.devToolsAction.setCheckable(True)
        self.devToolsAction.triggered.connect(partial(self._toggle_dev_tools_inspector))

        self.qwe.addAction(self.devToolsAction)

    def set_content_html(self, html: str):
        self.qwe.setHtml(html, baseUrl=QUrl(str(SIMSAPA_PACKAGE_DIR)))

    def render_sutta_content(self):
        if self.sutta is None:
            return

        if self.sutta.content_html is not None and self.sutta.content_html != '':
            content = str(self.sutta.content_html)
        elif self.sutta.content_plain is not None and self.sutta.content_plain != '':
            content = '<pre>' + str(self.sutta.content_plain) + '</pre>'
        else:
            content = 'No content.'

        html = html_page(content, self.api_url)

        self.set_content_html(html)

    def _toggle_dev_tools_inspector(self):
        if self.devToolsAction.isChecked():
            self.dev_view = QWebEngineView()
            self._layout.addWidget(self.dev_view, 100)
            self.qwe.page().setDevToolsPage(self.dev_view.page())
        else:
            self.qwe.page().devToolsPage().deleteLater()
            self.dev_view.deleteLater()

    def _handle_open_content_new(self):
        if self._app_data.actions_manager is not None \
           and self.sutta is not None:
            self._app_data.actions_manager.open_sutta_new(str(self.sutta.uid))
        else:
            logger.warn("Sutta is not set")