# Form implementation generated from reading ui file 'simsapa/assets/ui/dictionary_search_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DictionarySearchWindow(object):
    def setupUi(self, DictionarySearchWindow):
        DictionarySearchWindow.setObjectName("DictionarySearchWindow")
        DictionarySearchWindow.resize(1068, 642)
        DictionarySearchWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(DictionarySearchWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.searchbar_layout = QtWidgets.QHBoxLayout()
        self.searchbar_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.searchbar_layout.setObjectName("searchbar_layout")
        self.main_layout.addLayout(self.searchbar_layout)
        self.splitter = QtWidgets.QSplitter(self.central_widget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.content_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.content_layout.addItem(spacerItem)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.tabs_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.tabs_layout.setContentsMargins(0, 0, 0, 0)
        self.tabs_layout.setObjectName("tabs_layout")
        self.palibuttons_frame = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.palibuttons_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.palibuttons_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.palibuttons_frame.setLineWidth(0)
        self.palibuttons_frame.setObjectName("palibuttons_frame")
        self.tabs_layout.addWidget(self.palibuttons_frame)
        self.rightside_tabs = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        self.rightside_tabs.setMinimumSize(QtCore.QSize(500, 500))
        self.rightside_tabs.setObjectName("rightside_tabs")
        self.fulltext_tab = QtWidgets.QWidget()
        self.fulltext_tab.setObjectName("fulltext_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fulltext_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fulltext_layout = QtWidgets.QVBoxLayout()
        self.fulltext_layout.setObjectName("fulltext_layout")
        self.fulltext_pages_layout = QtWidgets.QHBoxLayout()
        self.fulltext_pages_layout.setObjectName("fulltext_pages_layout")
        self.fulltext_page_input = QtWidgets.QSpinBox(self.fulltext_tab)
        self.fulltext_page_input.setMinimum(1)
        self.fulltext_page_input.setMaximum(999)
        self.fulltext_page_input.setObjectName("fulltext_page_input")
        self.fulltext_pages_layout.addWidget(self.fulltext_page_input)
        self.fulltext_prev_btn = QtWidgets.QPushButton(self.fulltext_tab)
        self.fulltext_prev_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/angle-left"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fulltext_prev_btn.setIcon(icon)
        self.fulltext_prev_btn.setObjectName("fulltext_prev_btn")
        self.fulltext_pages_layout.addWidget(self.fulltext_prev_btn)
        self.fulltext_next_btn = QtWidgets.QPushButton(self.fulltext_tab)
        self.fulltext_next_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/angle-right"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fulltext_next_btn.setIcon(icon1)
        self.fulltext_next_btn.setObjectName("fulltext_next_btn")
        self.fulltext_pages_layout.addWidget(self.fulltext_next_btn)
        self.fulltext_label = QtWidgets.QLabel(self.fulltext_tab)
        self.fulltext_label.setObjectName("fulltext_label")
        self.fulltext_pages_layout.addWidget(self.fulltext_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.fulltext_pages_layout.addItem(spacerItem1)
        self.fulltext_first_page_btn = QtWidgets.QPushButton(self.fulltext_tab)
        self.fulltext_first_page_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/angles-left"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fulltext_first_page_btn.setIcon(icon2)
        self.fulltext_first_page_btn.setObjectName("fulltext_first_page_btn")
        self.fulltext_pages_layout.addWidget(self.fulltext_first_page_btn)
        self.fulltext_last_page_btn = QtWidgets.QPushButton(self.fulltext_tab)
        self.fulltext_last_page_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/angles-right"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fulltext_last_page_btn.setIcon(icon3)
        self.fulltext_last_page_btn.setObjectName("fulltext_last_page_btn")
        self.fulltext_pages_layout.addWidget(self.fulltext_last_page_btn)
        self.fulltext_layout.addLayout(self.fulltext_pages_layout)
        self.fulltext_loading_bar = QtWidgets.QLabel(self.fulltext_tab)
        self.fulltext_loading_bar.setMinimumSize(QtCore.QSize(0, 5))
        self.fulltext_loading_bar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.fulltext_loading_bar.setText("")
        self.fulltext_loading_bar.setObjectName("fulltext_loading_bar")
        self.fulltext_layout.addWidget(self.fulltext_loading_bar)
        self.fulltext_list = QtWidgets.QListWidget(self.fulltext_tab)
        self.fulltext_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.fulltext_list.setObjectName("fulltext_list")
        self.fulltext_layout.addWidget(self.fulltext_list)
        self.verticalLayout_4.addLayout(self.fulltext_layout)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/search"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightside_tabs.addTab(self.fulltext_tab, icon4, "")
        self.links_tab = QtWidgets.QWidget()
        self.links_tab.setObjectName("links_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.links_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.links_controls_layout = QtWidgets.QHBoxLayout()
        self.links_controls_layout.setObjectName("links_controls_layout")
        self.label_6 = QtWidgets.QLabel(self.links_tab)
        self.label_6.setObjectName("label_6")
        self.links_controls_layout.addWidget(self.label_6)
        self.label_select = QtWidgets.QComboBox(self.links_tab)
        self.label_select.setObjectName("label_select")
        self.label_select.addItem("")
        self.label_select.addItem("")
        self.label_select.addItem("")
        self.links_controls_layout.addWidget(self.label_select)
        self.label = QtWidgets.QLabel(self.links_tab)
        self.label.setObjectName("label")
        self.links_controls_layout.addWidget(self.label)
        self.distance_input = QtWidgets.QSpinBox(self.links_tab)
        self.distance_input.setMinimum(1)
        self.distance_input.setObjectName("distance_input")
        self.links_controls_layout.addWidget(self.distance_input)
        self.label_4 = QtWidgets.QLabel(self.links_tab)
        self.label_4.setObjectName("label_4")
        self.links_controls_layout.addWidget(self.label_4)
        self.min_links_input = QtWidgets.QSpinBox(self.links_tab)
        self.min_links_input.setMinimum(1)
        self.min_links_input.setObjectName("min_links_input")
        self.links_controls_layout.addWidget(self.min_links_input)
        self.links_regenerate_button = QtWidgets.QPushButton(self.links_tab)
        self.links_regenerate_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/reload"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.links_regenerate_button.setIcon(icon5)
        self.links_regenerate_button.setObjectName("links_regenerate_button")
        self.links_controls_layout.addWidget(self.links_regenerate_button)
        self.open_selected_link_button = QtWidgets.QPushButton(self.links_tab)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.open_selected_link_button.setIcon(icon6)
        self.open_selected_link_button.setObjectName("open_selected_link_button")
        self.links_controls_layout.addWidget(self.open_selected_link_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.links_controls_layout.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.links_controls_layout)
        self.links_layout = QtWidgets.QVBoxLayout()
        self.links_layout.setObjectName("links_layout")
        self.verticalLayout_5.addLayout(self.links_layout)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/diagram"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightside_tabs.addTab(self.links_tab, icon7, "")
        self.memos_tab = QtWidgets.QWidget()
        self.memos_tab.setObjectName("memos_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.memos_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.memos_layout = QtWidgets.QVBoxLayout()
        self.memos_layout.setObjectName("memos_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_memo_button = QtWidgets.QPushButton(self.memos_tab)
        self.add_memo_button.setObjectName("add_memo_button")
        self.horizontalLayout.addWidget(self.add_memo_button)
        self.clear_memo_button = QtWidgets.QPushButton(self.memos_tab)
        self.clear_memo_button.setObjectName("clear_memo_button")
        self.horizontalLayout.addWidget(self.clear_memo_button)
        self.remove_memo_button = QtWidgets.QPushButton(self.memos_tab)
        self.remove_memo_button.setObjectName("remove_memo_button")
        self.horizontalLayout.addWidget(self.remove_memo_button)
        self.memos_layout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.memos_tab)
        self.label_2.setObjectName("label_2")
        self.memos_layout.addWidget(self.label_2)
        self.front_input = QtWidgets.QPlainTextEdit(self.memos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.front_input.sizePolicy().hasHeightForWidth())
        self.front_input.setSizePolicy(sizePolicy)
        self.front_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.front_input.setObjectName("front_input")
        self.memos_layout.addWidget(self.front_input)
        self.label_5 = QtWidgets.QLabel(self.memos_tab)
        self.label_5.setObjectName("label_5")
        self.memos_layout.addWidget(self.label_5)
        self.back_input = QtWidgets.QPlainTextEdit(self.memos_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_input.sizePolicy().hasHeightForWidth())
        self.back_input.setSizePolicy(sizePolicy)
        self.back_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.back_input.setObjectName("back_input")
        self.memos_layout.addWidget(self.back_input)
        self.label_3 = QtWidgets.QLabel(self.memos_tab)
        self.label_3.setObjectName("label_3")
        self.memos_layout.addWidget(self.label_3)
        self.memos_list = QtWidgets.QListView(self.memos_tab)
        self.memos_list.setObjectName("memos_list")
        self.memos_layout.addWidget(self.memos_list)
        self.verticalLayout_6.addLayout(self.memos_layout)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/pen-fancy"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightside_tabs.addTab(self.memos_tab, icon8, "")
        self.recent_tab = QtWidgets.QWidget()
        self.recent_tab.setObjectName("recent_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.recent_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.recent_layout = QtWidgets.QVBoxLayout()
        self.recent_layout.setObjectName("recent_layout")
        self.recent_list = QtWidgets.QListWidget(self.recent_tab)
        self.recent_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.recent_list.setObjectName("recent_list")
        self.recent_layout.addWidget(self.recent_list)
        self.verticalLayout_3.addLayout(self.recent_layout)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/history-icon"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightside_tabs.addTab(self.recent_tab, icon9, "")
        self.tabs_layout.addWidget(self.rightside_tabs)
        self.main_layout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.main_layout)
        DictionarySearchWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(DictionarySearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Windows = QtWidgets.QMenu(self.menubar)
        self.menu_Windows.setObjectName("menu_Windows")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Dictionary = QtWidgets.QMenu(self.menubar)
        self.menu_Dictionary.setObjectName("menu_Dictionary")
        self.menu_Go = QtWidgets.QMenu(self.menubar)
        self.menu_Go.setObjectName("menu_Go")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        DictionarySearchWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(DictionarySearchWindow)
        self.toolBar.setObjectName("toolBar")
        DictionarySearchWindow.addToolBar(QtCore.Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.action_Copy = QtGui.QAction(DictionarySearchWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtGui.QAction(DictionarySearchWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtGui.QAction(DictionarySearchWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Quit.setIcon(icon10)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtGui.QAction(DictionarySearchWindow)
        self.action_Sutta_Search.setIcon(icon6)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtGui.QAction(DictionarySearchWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Dictionary_Search.setIcon(icon11)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtGui.QAction(DictionarySearchWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtGui.QAction(DictionarySearchWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtGui.QAction(DictionarySearchWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtGui.QAction(DictionarySearchWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtGui.QAction(DictionarySearchWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Library = QtGui.QAction(DictionarySearchWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Memos = QtGui.QAction(DictionarySearchWindow)
        self.action_Memos.setIcon(icon8)
        self.action_Memos.setObjectName("action_Memos")
        self.action_Dictionaries_Manager = QtGui.QAction(DictionarySearchWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.action_Links = QtGui.QAction(DictionarySearchWindow)
        self.action_Links.setIcon(icon7)
        self.action_Links.setObjectName("action_Links")
        self.action_Import_from_StarDict = QtGui.QAction(DictionarySearchWindow)
        self.action_Import_from_StarDict.setObjectName("action_Import_from_StarDict")
        self.action_Search_Query_Terms = QtGui.QAction(DictionarySearchWindow)
        self.action_Search_Query_Terms.setObjectName("action_Search_Query_Terms")
        self.action_Select_Dictionaries = QtGui.QAction(DictionarySearchWindow)
        self.action_Select_Dictionaries.setObjectName("action_Select_Dictionaries")
        self.action_Lookup_Clipboard_in_Dictionary = QtGui.QAction(DictionarySearchWindow)
        self.action_Lookup_Clipboard_in_Dictionary.setShortcutContext(QtCore.Qt.ShortcutContext.ApplicationShortcut)
        self.action_Lookup_Clipboard_in_Dictionary.setObjectName("action_Lookup_Clipboard_in_Dictionary")
        self.action_Re_index_database = QtGui.QAction(DictionarySearchWindow)
        self.action_Re_index_database.setObjectName("action_Re_index_database")
        self.action_Re_download_database = QtGui.QAction(DictionarySearchWindow)
        self.action_Re_download_database.setObjectName("action_Re_download_database")
        self.action_Notify_About_Updates = QtGui.QAction(DictionarySearchWindow)
        self.action_Notify_About_Updates.setCheckable(True)
        self.action_Notify_About_Updates.setChecked(True)
        self.action_Notify_About_Updates.setObjectName("action_Notify_About_Updates")
        self.action_Lookup_Clipboard_in_Suttas = QtGui.QAction(DictionarySearchWindow)
        self.action_Lookup_Clipboard_in_Suttas.setShortcutContext(QtCore.Qt.ShortcutContext.ApplicationShortcut)
        self.action_Lookup_Clipboard_in_Suttas.setObjectName("action_Lookup_Clipboard_in_Suttas")
        self.action_Show_Toolbar = QtGui.QAction(DictionarySearchWindow)
        self.action_Show_Toolbar.setCheckable(True)
        self.action_Show_Toolbar.setObjectName("action_Show_Toolbar")
        self.action_First_Window_on_Startup = QtGui.QAction(DictionarySearchWindow)
        self.action_First_Window_on_Startup.setObjectName("action_First_Window_on_Startup")
        self.action_Focus_Search_Input = QtGui.QAction(DictionarySearchWindow)
        self.action_Focus_Search_Input.setObjectName("action_Focus_Search_Input")
        self.action_Find_in_Page = QtGui.QAction(DictionarySearchWindow)
        self.action_Find_in_Page.setObjectName("action_Find_in_Page")
        self.action_Show_Word_Scan_Popup = QtGui.QAction(DictionarySearchWindow)
        self.action_Show_Word_Scan_Popup.setCheckable(True)
        self.action_Show_Word_Scan_Popup.setObjectName("action_Show_Word_Scan_Popup")
        self.action_Next_Result = QtGui.QAction(DictionarySearchWindow)
        self.action_Next_Result.setObjectName("action_Next_Result")
        self.action_Previous_Result = QtGui.QAction(DictionarySearchWindow)
        self.action_Previous_Result.setObjectName("action_Previous_Result")
        self.action_Sutta_Study = QtGui.QAction(DictionarySearchWindow)
        self.action_Sutta_Study.setIcon(icon6)
        self.action_Sutta_Study.setObjectName("action_Sutta_Study")
        self.action_Lookup_Selection_in_Dictionary = QtGui.QAction(DictionarySearchWindow)
        self.action_Lookup_Selection_in_Dictionary.setObjectName("action_Lookup_Selection_in_Dictionary")
        self.action_Increase_Text_Size = QtGui.QAction(DictionarySearchWindow)
        self.action_Increase_Text_Size.setObjectName("action_Increase_Text_Size")
        self.action_Decrease_Text_Size = QtGui.QAction(DictionarySearchWindow)
        self.action_Decrease_Text_Size.setObjectName("action_Decrease_Text_Size")
        self.action_Search_Result_Sizes = QtGui.QAction(DictionarySearchWindow)
        self.action_Search_Result_Sizes.setObjectName("action_Search_Result_Sizes")
        self.action_Search_As_You_Type = QtGui.QAction(DictionarySearchWindow)
        self.action_Search_As_You_Type.setCheckable(True)
        self.action_Search_As_You_Type.setChecked(True)
        self.action_Search_As_You_Type.setStatusTip("")
        self.action_Search_As_You_Type.setObjectName("action_Search_As_You_Type")
        self.action_Search_Completion = QtGui.QAction(DictionarySearchWindow)
        self.action_Search_Completion.setCheckable(True)
        self.action_Search_Completion.setChecked(True)
        self.action_Search_Completion.setObjectName("action_Search_Completion")
        self.action_Bookmarks = QtGui.QAction(DictionarySearchWindow)
        self.action_Bookmarks.setIcon(icon6)
        self.action_Bookmarks.setObjectName("action_Bookmarks")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close_Window)
        self.menu_File.addAction(self.action_Re_index_database)
        self.menu_File.addAction(self.action_Re_download_database)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addAction(self.action_Find_in_Page)
        self.menu_Edit.addAction(self.action_Focus_Search_Input)
        self.menu_Edit.addAction(self.action_Lookup_Selection_in_Dictionary)
        self.menu_Edit.addAction(self.action_Lookup_Clipboard_in_Suttas)
        self.menu_Edit.addAction(self.action_Lookup_Clipboard_in_Dictionary)
        self.menu_Windows.addAction(self.action_Sutta_Search)
        self.menu_Windows.addAction(self.action_Sutta_Study)
        self.menu_Windows.addAction(self.action_Dictionary_Search)
        self.menu_Windows.addAction(self.action_Show_Word_Scan_Popup)
        self.menu_Windows.addAction(self.action_Bookmarks)
        self.menu_Windows.addAction(self.action_Dictionaries_Manager)
        self.menu_Windows.addAction(self.action_Document_Reader)
        self.menu_Windows.addAction(self.action_Library)
        self.menu_Windows.addAction(self.action_Memos)
        self.menu_Windows.addAction(self.action_Links)
        self.menu_Windows.addAction(self.action_First_Window_on_Startup)
        self.menu_Windows.addAction(self.action_Show_Toolbar)
        self.menu_Help.addAction(self.action_Search_Query_Terms)
        self.menu_Help.addAction(self.action_Notify_About_Updates)
        self.menu_Help.addAction(self.action_Website)
        self.menu_Help.addAction(self.action_About)
        self.menu_Dictionary.addAction(self.action_Select_Dictionaries)
        self.menu_Dictionary.addAction(self.action_Import_from_StarDict)
        self.menu_Go.addAction(self.action_Search_As_You_Type)
        self.menu_Go.addAction(self.action_Search_Completion)
        self.menu_Go.addAction(self.action_Previous_Result)
        self.menu_Go.addAction(self.action_Next_Result)
        self.menu_View.addAction(self.action_Increase_Text_Size)
        self.menu_View.addAction(self.action_Decrease_Text_Size)
        self.menu_View.addAction(self.action_Search_Result_Sizes)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Go.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Dictionary.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Sutta_Search)
        self.toolBar.addAction(self.action_Dictionary_Search)
        self.toolBar.addAction(self.action_Memos)
        self.toolBar.addAction(self.action_Links)

        self.retranslateUi(DictionarySearchWindow)
        self.rightside_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DictionarySearchWindow)

    def retranslateUi(self, DictionarySearchWindow):
        _translate = QtCore.QCoreApplication.translate
        DictionarySearchWindow.setWindowTitle(_translate("DictionarySearchWindow", "Dictionary Search - Simsapa"))
        self.fulltext_prev_btn.setToolTip(_translate("DictionarySearchWindow", "Previous page of results"))
        self.fulltext_next_btn.setToolTip(_translate("DictionarySearchWindow", "Next page of results"))
        self.fulltext_label.setText(_translate("DictionarySearchWindow", "Showing a-b out of x"))
        self.fulltext_first_page_btn.setToolTip(_translate("DictionarySearchWindow", "First page of results"))
        self.fulltext_last_page_btn.setToolTip(_translate("DictionarySearchWindow", "Last page of results"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.fulltext_tab), _translate("DictionarySearchWindow", "Results"))
        self.label_6.setText(_translate("DictionarySearchWindow", "Labels:"))
        self.label_select.setItemText(0, _translate("DictionarySearchWindow", "Sutta Ref."))
        self.label_select.setItemText(1, _translate("DictionarySearchWindow", "Ref. + Title"))
        self.label_select.setItemText(2, _translate("DictionarySearchWindow", "No Labels"))
        self.label.setText(_translate("DictionarySearchWindow", "Distance:"))
        self.label_4.setText(_translate("DictionarySearchWindow", "Min. links:"))
        self.links_regenerate_button.setToolTip(_translate("DictionarySearchWindow", "Regenerate Links Graph"))
        self.open_selected_link_button.setToolTip(_translate("DictionarySearchWindow", "Open Selected Link"))
        self.open_selected_link_button.setText(_translate("DictionarySearchWindow", "Open Selected"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.links_tab), _translate("DictionarySearchWindow", "Links"))
        self.add_memo_button.setText(_translate("DictionarySearchWindow", "Add"))
        self.clear_memo_button.setText(_translate("DictionarySearchWindow", "Clear"))
        self.remove_memo_button.setText(_translate("DictionarySearchWindow", "Remove"))
        self.label_2.setText(_translate("DictionarySearchWindow", "Front"))
        self.label_5.setText(_translate("DictionarySearchWindow", "Back"))
        self.label_3.setText(_translate("DictionarySearchWindow", "Memos for this page"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.memos_tab), _translate("DictionarySearchWindow", "Memos"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.recent_tab), _translate("DictionarySearchWindow", "History"))
        self.menu_File.setTitle(_translate("DictionarySearchWindow", "&File"))
        self.menu_Edit.setTitle(_translate("DictionarySearchWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("DictionarySearchWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("DictionarySearchWindow", "&Help"))
        self.menu_Dictionary.setTitle(_translate("DictionarySearchWindow", "&Dictionary"))
        self.menu_Go.setTitle(_translate("DictionarySearchWindow", "&Go"))
        self.menu_View.setTitle(_translate("DictionarySearchWindow", "&View"))
        self.toolBar.setWindowTitle(_translate("DictionarySearchWindow", "toolBar"))
        self.action_Copy.setText(_translate("DictionarySearchWindow", "&Copy"))
        self.action_Copy.setShortcut(_translate("DictionarySearchWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("DictionarySearchWindow", "&Paste"))
        self.action_Paste.setShortcut(_translate("DictionarySearchWindow", "Ctrl+V"))
        self.action_Quit.setText(_translate("DictionarySearchWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("DictionarySearchWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("DictionarySearchWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("DictionarySearchWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("DictionarySearchWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("DictionarySearchWindow", "F6"))
        self.action_About.setText(_translate("DictionarySearchWindow", "&About"))
        self.action_Website.setText(_translate("DictionarySearchWindow", "&Website"))
        self.action_Close_Window.setText(_translate("DictionarySearchWindow", "&Close Window"))
        self.action_Open.setText(_translate("DictionarySearchWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("DictionarySearchWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("DictionarySearchWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("DictionarySearchWindow", "Document Reader"))
        self.action_Library.setText(_translate("DictionarySearchWindow", "&Library"))
        self.action_Memos.setText(_translate("DictionarySearchWindow", "&Memos"))
        self.action_Memos.setToolTip(_translate("DictionarySearchWindow", "Memos"))
        self.action_Memos.setShortcut(_translate("DictionarySearchWindow", "F9"))
        self.action_Dictionaries_Manager.setText(_translate("DictionarySearchWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("DictionarySearchWindow", "F10"))
        self.action_Links.setText(_translate("DictionarySearchWindow", "&Links"))
        self.action_Links.setShortcut(_translate("DictionarySearchWindow", "F11"))
        self.action_Import_from_StarDict.setText(_translate("DictionarySearchWindow", "&Import from StarDict..."))
        self.action_Search_Query_Terms.setText(_translate("DictionarySearchWindow", "Search Query Terms"))
        self.action_Select_Dictionaries.setText(_translate("DictionarySearchWindow", "&Select Dictionaries..."))
        self.action_Lookup_Clipboard_in_Dictionary.setText(_translate("DictionarySearchWindow", "&Lookup Clipboard in Dictionary"))
        self.action_Lookup_Clipboard_in_Dictionary.setShortcut(_translate("DictionarySearchWindow", "Ctrl+Shift+G"))
        self.action_Re_index_database.setText(_translate("DictionarySearchWindow", "Re-index database..."))
        self.action_Re_download_database.setText(_translate("DictionarySearchWindow", "Re-download database..."))
        self.action_Notify_About_Updates.setText(_translate("DictionarySearchWindow", "Notify About Updates"))
        self.action_Lookup_Clipboard_in_Suttas.setText(_translate("DictionarySearchWindow", "&Lookup Clipboard in Suttas"))
        self.action_Lookup_Clipboard_in_Suttas.setShortcut(_translate("DictionarySearchWindow", "Ctrl+Shift+S"))
        self.action_Show_Toolbar.setText(_translate("DictionarySearchWindow", "Show Toolbar"))
        self.action_First_Window_on_Startup.setText(_translate("DictionarySearchWindow", "First Window on Startup..."))
        self.action_Focus_Search_Input.setText(_translate("DictionarySearchWindow", "Focus Search Input"))
        self.action_Focus_Search_Input.setShortcut(_translate("DictionarySearchWindow", "Ctrl+L"))
        self.action_Find_in_Page.setText(_translate("DictionarySearchWindow", "Find in Page..."))
        self.action_Find_in_Page.setShortcut(_translate("DictionarySearchWindow", "Ctrl+F"))
        self.action_Show_Word_Scan_Popup.setText(_translate("DictionarySearchWindow", "Show Word Scan Popup"))
        self.action_Show_Word_Scan_Popup.setShortcut(_translate("DictionarySearchWindow", "Ctrl+F6"))
        self.action_Next_Result.setText(_translate("DictionarySearchWindow", "Next Result"))
        self.action_Next_Result.setShortcut(_translate("DictionarySearchWindow", "Ctrl+Down"))
        self.action_Previous_Result.setText(_translate("DictionarySearchWindow", "Previous Result"))
        self.action_Previous_Result.setShortcut(_translate("DictionarySearchWindow", "Ctrl+Up"))
        self.action_Sutta_Study.setText(_translate("DictionarySearchWindow", "Sutta Study"))
        self.action_Sutta_Study.setShortcut(_translate("DictionarySearchWindow", "Ctrl+F5"))
        self.action_Lookup_Selection_in_Dictionary.setText(_translate("DictionarySearchWindow", "Lookup Selection in Dictionary"))
        self.action_Lookup_Selection_in_Dictionary.setShortcut(_translate("DictionarySearchWindow", "Ctrl+G"))
        self.action_Increase_Text_Size.setText(_translate("DictionarySearchWindow", "&Increase Text Size"))
        self.action_Increase_Text_Size.setShortcut(_translate("DictionarySearchWindow", "Ctrl++"))
        self.action_Decrease_Text_Size.setText(_translate("DictionarySearchWindow", "&Decrease Text Size"))
        self.action_Decrease_Text_Size.setShortcut(_translate("DictionarySearchWindow", "Ctrl+-"))
        self.action_Search_Result_Sizes.setText(_translate("DictionarySearchWindow", "&Search Result Sizes..."))
        self.action_Search_As_You_Type.setText(_translate("DictionarySearchWindow", "Search As You &Type"))
        self.action_Search_As_You_Type.setToolTip(_translate("DictionarySearchWindow", "Run search query when you stop typing"))
        self.action_Search_Completion.setText(_translate("DictionarySearchWindow", "Search &Completion"))
        self.action_Bookmarks.setText(_translate("DictionarySearchWindow", "&Bookmarks"))
        self.action_Bookmarks.setShortcut(_translate("DictionarySearchWindow", "F7"))
