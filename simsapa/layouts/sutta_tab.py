from functools import partial
from typing import Optional

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

from simsapa import GRAPHS_DIR, SIMSAPA_PACKAGE_DIR, logger
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

    def set_qwe_html(self, html: str):
        # Around above this size, QWebEngineView doesn't display the HTML with .setHtml()
        size_limit = 0.8 * 1024 * 1024

        if len(html) < size_limit:
            try:
                self.qwe.setHtml(html, baseUrl=QUrl(str(SIMSAPA_PACKAGE_DIR)))
            except Exception as e:
                logger.error("set_qwe_html() : %s" % e)
        else:
            try:
                if self.sutta is not None:
                    sutta_id = self.sutta.id
                else:
                    sutta_id = 0

                html_path = GRAPHS_DIR.joinpath(f"sutta-{sutta_id}.html")
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(html)

                self.qwe.load(QUrl(str(html_path.absolute().as_uri())))

                # TODO consider browser reload
                # - cache folder? empty on start / exit?
                # html_path.unlink()

            except Exception as e:
                logger.error("set_qwe_html() : %s" % e)

    def render_sutta_content(self):
        if self.sutta is None:
            return

        if self.sutta.content_html is not None and self.sutta.content_html != '':
            content = str(self.sutta.content_html)

        elif self.sutta.content_plain is not None and self.sutta.content_plain != '':
            content = '<pre>' + str(self.sutta.content_plain) + '</pre>'

        else:
            content = 'No content.'

        font_size = self._app_data.app_settings.get('sutta_font_size', 22)
        max_width = self._app_data.app_settings.get('sutta_max_width', 75)

        css_extra = f"html {{ font-size: {font_size}px; }} body {{ max-width: {max_width}ex; }}"

        html = html_page(content, self.api_url, css_extra)

        self.set_qwe_html(html)

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
