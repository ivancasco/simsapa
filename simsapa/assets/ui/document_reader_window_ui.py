# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simsapa/assets/ui/document_reader_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DocumentReaderWindow(object):
    def setupUi(self, DocumentReaderWindow):
        DocumentReaderWindow.setObjectName("DocumentReaderWindow")
        DocumentReaderWindow.resize(856, 581)
        DocumentReaderWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(DocumentReaderWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.splitter = QtWidgets.QSplitter(self.central_widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.setObjectName("sidebar_layout")
        self.sidebar_tabs = QtWidgets.QTabWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_tabs.sizePolicy().hasHeightForWidth())
        self.sidebar_tabs.setSizePolicy(sizePolicy)
        self.sidebar_tabs.setObjectName("sidebar_tabs")
        self.thumbs_tab = QtWidgets.QWidget()
        self.thumbs_tab.setObjectName("thumbs_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.thumbs_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.thumbs_view = QtWidgets.QWidget(self.thumbs_tab)
        self.thumbs_view.setObjectName("thumbs_view")
        self.verticalLayout_2.addWidget(self.thumbs_view)
        self.sidebar_tabs.addTab(self.thumbs_tab, "")
        self.annotations_tab = QtWidgets.QWidget()
        self.annotations_tab.setObjectName("annotations_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.annotations_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.annotations_view = QtWidgets.QWidget(self.annotations_tab)
        self.annotations_view.setObjectName("annotations_view")
        self.verticalLayout_3.addWidget(self.annotations_view)
        self.sidebar_tabs.addTab(self.annotations_tab, "")
        self.bookmarks_tab = QtWidgets.QWidget()
        self.bookmarks_tab.setObjectName("bookmarks_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.bookmarks_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bookmarks_list = QtWidgets.QListWidget(self.bookmarks_tab)
        self.bookmarks_list.setObjectName("bookmarks_list")
        self.verticalLayout_4.addWidget(self.bookmarks_list)
        self.sidebar_tabs.addTab(self.bookmarks_tab, "")
        self.contents_tab = QtWidgets.QWidget()
        self.contents_tab.setObjectName("contents_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.contents_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contents_list = QtWidgets.QListView(self.contents_tab)
        self.contents_list.setObjectName("contents_list")
        self.verticalLayout_5.addWidget(self.contents_list)
        self.sidebar_tabs.addTab(self.contents_tab, "")
        self.sidebar_layout.addWidget(self.sidebar_tabs)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.content_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")
        self.page_number_layout = QtWidgets.QHBoxLayout()
        self.page_number_layout.setObjectName("page_number_layout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.page_number_layout.addWidget(self.label)
        self.current_page_input = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.current_page_input.setMinimumSize(QtCore.QSize(80, 0))
        self.current_page_input.setMaximumSize(QtCore.QSize(80, 16777215))
        self.current_page_input.setAlignment(QtCore.Qt.AlignCenter)
        self.current_page_input.setMinimum(1)
        self.current_page_input.setMaximum(999999)
        self.current_page_input.setObjectName("current_page_input")
        self.page_number_layout.addWidget(self.current_page_input)
        self.page_current_of_total = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.page_current_of_total.setMinimumSize(QtCore.QSize(80, 0))
        self.page_current_of_total.setAlignment(QtCore.Qt.AlignCenter)
        self.page_current_of_total.setObjectName("page_current_of_total")
        self.page_number_layout.addWidget(self.page_current_of_total)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.page_number_layout.addWidget(self.label_4)
        self.content_layout.addLayout(self.page_number_layout)
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(400, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 444))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content_page = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_page.sizePolicy().hasHeightForWidth())
        self.content_page.setSizePolicy(sizePolicy)
        self.content_page.setText("")
        self.content_page.setObjectName("content_page")
        self.verticalLayout.addWidget(self.content_page)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.content_layout.addWidget(self.scrollArea)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.memos_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.memos_layout.setContentsMargins(0, 0, 0, 0)
        self.memos_layout.setObjectName("memos_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_memo_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_memo_button.setObjectName("add_memo_button")
        self.horizontalLayout.addWidget(self.add_memo_button)
        self.clear_memo_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_memo_button.setObjectName("clear_memo_button")
        self.horizontalLayout.addWidget(self.clear_memo_button)
        self.remove_memo_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove_memo_button.setObjectName("remove_memo_button")
        self.horizontalLayout.addWidget(self.remove_memo_button)
        self.memos_layout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.memos_layout.addWidget(self.label_2)
        self.front_input = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.front_input.sizePolicy().hasHeightForWidth())
        self.front_input.setSizePolicy(sizePolicy)
        self.front_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.front_input.setObjectName("front_input")
        self.memos_layout.addWidget(self.front_input)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.memos_layout.addWidget(self.label_5)
        self.back_input = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_input.sizePolicy().hasHeightForWidth())
        self.back_input.setSizePolicy(sizePolicy)
        self.back_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.back_input.setObjectName("back_input")
        self.memos_layout.addWidget(self.back_input)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.memos_layout.addWidget(self.label_3)
        self.memos_list = QtWidgets.QListView(self.verticalLayoutWidget)
        self.memos_list.setObjectName("memos_list")
        self.memos_layout.addWidget(self.memos_list)
        self.main_layout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.main_layout)
        DocumentReaderWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(DocumentReaderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Windows = QtWidgets.QMenu(self.menubar)
        self.menu_Windows.setObjectName("menu_Windows")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menuGo = QtWidgets.QMenu(self.menubar)
        self.menuGo.setObjectName("menuGo")
        DocumentReaderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DocumentReaderWindow)
        self.statusbar.setObjectName("statusbar")
        DocumentReaderWindow.setStatusBar(self.statusbar)
        self.windows_toolbar = QtWidgets.QToolBar(DocumentReaderWindow)
        self.windows_toolbar.setObjectName("windows_toolbar")
        DocumentReaderWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.windows_toolbar)
        self.doc_toolbar = QtWidgets.QToolBar(DocumentReaderWindow)
        self.doc_toolbar.setObjectName("doc_toolbar")
        DocumentReaderWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.doc_toolbar)
        self.action_Copy = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtWidgets.QAction(DocumentReaderWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtWidgets.QAction(DocumentReaderWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtWidgets.QAction(DocumentReaderWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Dictionary_Search.setIcon(icon2)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtWidgets.QAction(DocumentReaderWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Document_Reader = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Open = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Next_Page = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Next_Page.setObjectName("action_Next_Page")
        self.action_Previous_Page = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Previous_Page.setObjectName("action_Previous_Page")
        self.action_Go_to_Page = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Go_to_Page.setObjectName("action_Go_to_Page")
        self.action_Beginning = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Beginning.setObjectName("action_Beginning")
        self.action_End = QtWidgets.QAction(DocumentReaderWindow)
        self.action_End.setObjectName("action_End")
        self.action_Library = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Memos = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Memos.setObjectName("action_Memos")
        self.action_Dictionaries_Manager = QtWidgets.QAction(DocumentReaderWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close_Window)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Windows.addAction(self.action_Sutta_Search)
        self.menu_Windows.addAction(self.action_Dictionary_Search)
        self.menu_Windows.addAction(self.action_Dictionaries_Manager)
        self.menu_Windows.addAction(self.action_Document_Reader)
        self.menu_Windows.addAction(self.action_Library)
        self.menu_Windows.addAction(self.action_Memos)
        self.menu_Help.addAction(self.action_Website)
        self.menu_Help.addAction(self.action_About)
        self.menuGo.addAction(self.action_Previous_Page)
        self.menuGo.addAction(self.action_Next_Page)
        self.menuGo.addSeparator()
        self.menuGo.addAction(self.action_Beginning)
        self.menuGo.addAction(self.action_End)
        self.menuGo.addSeparator()
        self.menuGo.addAction(self.action_Go_to_Page)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menuGo.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.windows_toolbar.addAction(self.action_Sutta_Search)
        self.windows_toolbar.addAction(self.action_Dictionary_Search)
        self.doc_toolbar.addAction(self.action_Beginning)
        self.doc_toolbar.addAction(self.action_Previous_Page)
        self.doc_toolbar.addAction(self.action_Go_to_Page)
        self.doc_toolbar.addAction(self.action_Next_Page)
        self.doc_toolbar.addAction(self.action_End)

        self.retranslateUi(DocumentReaderWindow)
        self.sidebar_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DocumentReaderWindow)

    def retranslateUi(self, DocumentReaderWindow):
        _translate = QtCore.QCoreApplication.translate
        DocumentReaderWindow.setWindowTitle(_translate("DocumentReaderWindow", "Document Reader - Simsapa"))
        self.sidebar_tabs.setTabText(self.sidebar_tabs.indexOf(self.thumbs_tab), _translate("DocumentReaderWindow", "Thumbnails"))
        self.sidebar_tabs.setTabText(self.sidebar_tabs.indexOf(self.annotations_tab), _translate("DocumentReaderWindow", "Annotations"))
        self.sidebar_tabs.setTabText(self.sidebar_tabs.indexOf(self.bookmarks_tab), _translate("DocumentReaderWindow", "Bookmarks"))
        self.sidebar_tabs.setTabText(self.sidebar_tabs.indexOf(self.contents_tab), _translate("DocumentReaderWindow", "Contents"))
        self.page_current_of_total.setText(_translate("DocumentReaderWindow", "_ of _"))
        self.add_memo_button.setText(_translate("DocumentReaderWindow", "Add"))
        self.clear_memo_button.setText(_translate("DocumentReaderWindow", "Clear"))
        self.remove_memo_button.setText(_translate("DocumentReaderWindow", "Remove"))
        self.label_2.setText(_translate("DocumentReaderWindow", "Front"))
        self.label_5.setText(_translate("DocumentReaderWindow", "Back"))
        self.label_3.setText(_translate("DocumentReaderWindow", "Notes for this page"))
        self.menu_File.setTitle(_translate("DocumentReaderWindow", "&File"))
        self.menu_Edit.setTitle(_translate("DocumentReaderWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("DocumentReaderWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("DocumentReaderWindow", "&Help"))
        self.menuGo.setTitle(_translate("DocumentReaderWindow", "Go"))
        self.windows_toolbar.setWindowTitle(_translate("DocumentReaderWindow", "toolBar"))
        self.doc_toolbar.setWindowTitle(_translate("DocumentReaderWindow", "toolBar"))
        self.action_Copy.setText(_translate("DocumentReaderWindow", "&Copy"))
        self.action_Paste.setText(_translate("DocumentReaderWindow", "&Paste"))
        self.action_Quit.setText(_translate("DocumentReaderWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("DocumentReaderWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("DocumentReaderWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("DocumentReaderWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("DocumentReaderWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("DocumentReaderWindow", "F6"))
        self.action_About.setText(_translate("DocumentReaderWindow", "&About"))
        self.action_Website.setText(_translate("DocumentReaderWindow", "&Website"))
        self.action_Close_Window.setText(_translate("DocumentReaderWindow", "&Close Window"))
        self.action_Document_Reader.setText(_translate("DocumentReaderWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("DocumentReaderWindow", "Document Reader"))
        self.action_Document_Reader.setShortcut(_translate("DocumentReaderWindow", "F7"))
        self.action_Open.setText(_translate("DocumentReaderWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("DocumentReaderWindow", "Ctrl+O"))
        self.action_Next_Page.setText(_translate("DocumentReaderWindow", "&Next Page"))
        self.action_Next_Page.setShortcut(_translate("DocumentReaderWindow", "PgDown"))
        self.action_Previous_Page.setText(_translate("DocumentReaderWindow", "&Previous Page"))
        self.action_Previous_Page.setShortcut(_translate("DocumentReaderWindow", "PgUp"))
        self.action_Go_to_Page.setText(_translate("DocumentReaderWindow", "&Go to Page..."))
        self.action_Go_to_Page.setShortcut(_translate("DocumentReaderWindow", "Ctrl+G"))
        self.action_Beginning.setText(_translate("DocumentReaderWindow", "&Beginning"))
        self.action_Beginning.setShortcut(_translate("DocumentReaderWindow", "Ctrl+Home"))
        self.action_End.setText(_translate("DocumentReaderWindow", "&End"))
        self.action_End.setShortcut(_translate("DocumentReaderWindow", "Ctrl+End"))
        self.action_Library.setText(_translate("DocumentReaderWindow", "&Library"))
        self.action_Library.setShortcut(_translate("DocumentReaderWindow", "F8"))
        self.action_Memos.setText(_translate("DocumentReaderWindow", "&Memos"))
        self.action_Memos.setToolTip(_translate("DocumentReaderWindow", "Memos"))
        self.action_Memos.setShortcut(_translate("DocumentReaderWindow", "F9"))
        self.action_Dictionaries_Manager.setText(_translate("DocumentReaderWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("DocumentReaderWindow", "F10"))
from simsapa.assets import icons_rc
