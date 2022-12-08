# Form implementation generated from reading ui file 'simsapa/assets/ui/sutta_search_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SuttaSearchWindow(object):
    def setupUi(self, SuttaSearchWindow):
        SuttaSearchWindow.setObjectName("SuttaSearchWindow")
        SuttaSearchWindow.resize(1068, 625)
        SuttaSearchWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(SuttaSearchWindow)
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
        self.sutta_tabs_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.sutta_tabs_layout.setContentsMargins(0, 0, 0, 0)
        self.sutta_tabs_layout.setObjectName("sutta_tabs_layout")
        spacerItem = QtWidgets.QSpacerItem(500, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.sutta_tabs_layout.addItem(spacerItem)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fulltext_tab.sizePolicy().hasHeightForWidth())
        self.fulltext_tab.setSizePolicy(sizePolicy)
        self.fulltext_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.fulltext_tab.setObjectName("fulltext_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fulltext_tab)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.fulltext_list.setLineWidth(1)
        self.fulltext_list.setObjectName("fulltext_list")
        self.fulltext_layout.addWidget(self.fulltext_list)
        self.verticalLayout.addLayout(self.fulltext_layout)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/search"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightside_tabs.addTab(self.fulltext_tab, icon4, "")
        self.links_tab = QtWidgets.QWidget()
        self.links_tab.setObjectName("links_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.links_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.verticalLayout_2.addLayout(self.links_controls_layout)
        self.links_layout = QtWidgets.QVBoxLayout()
        self.links_layout.setObjectName("links_layout")
        self.verticalLayout_2.addLayout(self.links_layout)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/diagram"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightside_tabs.addTab(self.links_tab, icon7, "")
        self.memos_tab = QtWidgets.QWidget()
        self.memos_tab.setObjectName("memos_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.memos_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
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
        self.verticalLayout_5.addLayout(self.memos_layout)
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
        SuttaSearchWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(SuttaSearchWindow)
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
        self.menu_Suttas = QtWidgets.QMenu(self.menubar)
        self.menu_Suttas.setObjectName("menu_Suttas")
        self.menu_Go = QtWidgets.QMenu(self.menubar)
        self.menu_Go.setObjectName("menu_Go")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        SuttaSearchWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(SuttaSearchWindow)
        self.toolBar.setObjectName("toolBar")
        SuttaSearchWindow.addToolBar(QtCore.Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.action_Copy = QtGui.QAction(SuttaSearchWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtGui.QAction(SuttaSearchWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtGui.QAction(SuttaSearchWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Quit.setIcon(icon10)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtGui.QAction(SuttaSearchWindow)
        self.action_Sutta_Search.setIcon(icon6)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtGui.QAction(SuttaSearchWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Dictionary_Search.setIcon(icon11)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtGui.QAction(SuttaSearchWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtGui.QAction(SuttaSearchWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtGui.QAction(SuttaSearchWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtGui.QAction(SuttaSearchWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtGui.QAction(SuttaSearchWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Library = QtGui.QAction(SuttaSearchWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Memos = QtGui.QAction(SuttaSearchWindow)
        self.action_Memos.setIcon(icon8)
        self.action_Memos.setObjectName("action_Memos")
        self.action_Dictionaries_Manager = QtGui.QAction(SuttaSearchWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.action_Links = QtGui.QAction(SuttaSearchWindow)
        self.action_Links.setIcon(icon7)
        self.action_Links.setObjectName("action_Links")
        self.action_Search_Query_Terms = QtGui.QAction(SuttaSearchWindow)
        self.action_Search_Query_Terms.setObjectName("action_Search_Query_Terms")
        self.action_Lookup_Clipboard_in_Suttas = QtGui.QAction(SuttaSearchWindow)
        self.action_Lookup_Clipboard_in_Suttas.setShortcutContext(QtCore.Qt.ShortcutContext.ApplicationShortcut)
        self.action_Lookup_Clipboard_in_Suttas.setObjectName("action_Lookup_Clipboard_in_Suttas")
        self.action_Select_Sutta_Authors = QtGui.QAction(SuttaSearchWindow)
        self.action_Select_Sutta_Authors.setObjectName("action_Select_Sutta_Authors")
        self.action_Re_index_database = QtGui.QAction(SuttaSearchWindow)
        self.action_Re_index_database.setObjectName("action_Re_index_database")
        self.action_Re_download_database = QtGui.QAction(SuttaSearchWindow)
        self.action_Re_download_database.setObjectName("action_Re_download_database")
        self.action_Notify_About_Updates = QtGui.QAction(SuttaSearchWindow)
        self.action_Notify_About_Updates.setCheckable(True)
        self.action_Notify_About_Updates.setChecked(True)
        self.action_Notify_About_Updates.setObjectName("action_Notify_About_Updates")
        self.action_Lookup_Clipboard_in_Dictionary = QtGui.QAction(SuttaSearchWindow)
        self.action_Lookup_Clipboard_in_Dictionary.setShortcutContext(QtCore.Qt.ShortcutContext.ApplicationShortcut)
        self.action_Lookup_Clipboard_in_Dictionary.setObjectName("action_Lookup_Clipboard_in_Dictionary")
        self.action_Show_Toolbar = QtGui.QAction(SuttaSearchWindow)
        self.action_Show_Toolbar.setCheckable(True)
        self.action_Show_Toolbar.setObjectName("action_Show_Toolbar")
        self.action_First_Window_on_Startup = QtGui.QAction(SuttaSearchWindow)
        self.action_First_Window_on_Startup.setObjectName("action_First_Window_on_Startup")
        self.action_Focus_Search_Input = QtGui.QAction(SuttaSearchWindow)
        self.action_Focus_Search_Input.setObjectName("action_Focus_Search_Input")
        self.action_Find_in_Page = QtGui.QAction(SuttaSearchWindow)
        self.action_Find_in_Page.setObjectName("action_Find_in_Page")
        self.action_Show_Word_Scan_Popup = QtGui.QAction(SuttaSearchWindow)
        self.action_Show_Word_Scan_Popup.setCheckable(True)
        self.action_Show_Word_Scan_Popup.setObjectName("action_Show_Word_Scan_Popup")
        self.action_Show_Related_Suttas = QtGui.QAction(SuttaSearchWindow)
        self.action_Show_Related_Suttas.setCheckable(True)
        self.action_Show_Related_Suttas.setObjectName("action_Show_Related_Suttas")
        self.action_Next_Result = QtGui.QAction(SuttaSearchWindow)
        self.action_Next_Result.setObjectName("action_Next_Result")
        self.action_Previous_Result = QtGui.QAction(SuttaSearchWindow)
        self.action_Previous_Result.setObjectName("action_Previous_Result")
        self.action_Previous_Tab = QtGui.QAction(SuttaSearchWindow)
        self.action_Previous_Tab.setObjectName("action_Previous_Tab")
        self.action_Next_Tab = QtGui.QAction(SuttaSearchWindow)
        self.action_Next_Tab.setObjectName("action_Next_Tab")
        self.action_Sutta_Study = QtGui.QAction(SuttaSearchWindow)
        self.action_Sutta_Study.setIcon(icon6)
        self.action_Sutta_Study.setObjectName("action_Sutta_Study")
        self.action_Lookup_Selection_in_Dictionary = QtGui.QAction(SuttaSearchWindow)
        self.action_Lookup_Selection_in_Dictionary.setObjectName("action_Lookup_Selection_in_Dictionary")
        self.action_Increase_Text_Size = QtGui.QAction(SuttaSearchWindow)
        self.action_Increase_Text_Size.setObjectName("action_Increase_Text_Size")
        self.action_Decrease_Text_Size = QtGui.QAction(SuttaSearchWindow)
        self.action_Decrease_Text_Size.setObjectName("action_Decrease_Text_Size")
        self.action_Increase_Text_Margins = QtGui.QAction(SuttaSearchWindow)
        self.action_Increase_Text_Margins.setObjectName("action_Increase_Text_Margins")
        self.action_Decrease_Text_Margins = QtGui.QAction(SuttaSearchWindow)
        self.action_Decrease_Text_Margins.setObjectName("action_Decrease_Text_Margins")
        self.action_Import_Suttas_with_Spreadsheet = QtGui.QAction(SuttaSearchWindow)
        self.action_Import_Suttas_with_Spreadsheet.setObjectName("action_Import_Suttas_with_Spreadsheet")
        self.action_Remove_Imported_Suttas = QtGui.QAction(SuttaSearchWindow)
        self.action_Remove_Imported_Suttas.setObjectName("action_Remove_Imported_Suttas")
        self.action_Search_Result_Sizes = QtGui.QAction(SuttaSearchWindow)
        self.action_Search_Result_Sizes.setObjectName("action_Search_Result_Sizes")
        self.action_Search_As_You_Type = QtGui.QAction(SuttaSearchWindow)
        self.action_Search_As_You_Type.setCheckable(True)
        self.action_Search_As_You_Type.setChecked(True)
        self.action_Search_As_You_Type.setStatusTip("")
        self.action_Search_As_You_Type.setObjectName("action_Search_As_You_Type")
        self.action_Search_Completion = QtGui.QAction(SuttaSearchWindow)
        self.action_Search_Completion.setCheckable(True)
        self.action_Search_Completion.setChecked(True)
        self.action_Search_Completion.setObjectName("action_Search_Completion")
        self.action_Bookmarks = QtGui.QAction(SuttaSearchWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/bookmark"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Bookmarks.setIcon(icon12)
        self.action_Bookmarks.setObjectName("action_Bookmarks")
        self.action_Show_All_Variant_Readings = QtGui.QAction(SuttaSearchWindow)
        self.action_Show_All_Variant_Readings.setCheckable(True)
        self.action_Show_All_Variant_Readings.setChecked(False)
        self.action_Show_All_Variant_Readings.setObjectName("action_Show_All_Variant_Readings")
        self.action_Show_Translation_and_Pali_Line_by_Line = QtGui.QAction(SuttaSearchWindow)
        self.action_Show_Translation_and_Pali_Line_by_Line.setCheckable(True)
        self.action_Show_Translation_and_Pali_Line_by_Line.setObjectName("action_Show_Translation_and_Pali_Line_by_Line")
        self.action_Pali_Courses = QtGui.QAction(SuttaSearchWindow)
        self.action_Pali_Courses.setIcon(icon6)
        self.action_Pali_Courses.setObjectName("action_Pali_Courses")
        self.action_Show_Sidebar = QtGui.QAction(SuttaSearchWindow)
        self.action_Show_Sidebar.setCheckable(True)
        self.action_Show_Sidebar.setChecked(True)
        self.action_Show_Sidebar.setObjectName("action_Show_Sidebar")
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
        self.menu_Windows.addAction(self.action_Pali_Courses)
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
        self.menu_Suttas.addAction(self.action_Show_Sidebar)
        self.menu_Suttas.addAction(self.action_Show_Related_Suttas)
        self.menu_Suttas.addAction(self.action_Show_Translation_and_Pali_Line_by_Line)
        self.menu_Suttas.addAction(self.action_Show_All_Variant_Readings)
        self.menu_Suttas.addAction(self.action_Select_Sutta_Authors)
        self.menu_Suttas.addAction(self.action_Import_Suttas_with_Spreadsheet)
        self.menu_Suttas.addAction(self.action_Remove_Imported_Suttas)
        self.menu_Go.addAction(self.action_Search_As_You_Type)
        self.menu_Go.addAction(self.action_Search_Completion)
        self.menu_Go.addAction(self.action_Previous_Result)
        self.menu_Go.addAction(self.action_Next_Result)
        self.menu_Go.addAction(self.action_Previous_Tab)
        self.menu_Go.addAction(self.action_Next_Tab)
        self.menu_View.addAction(self.action_Increase_Text_Size)
        self.menu_View.addAction(self.action_Decrease_Text_Size)
        self.menu_View.addAction(self.action_Increase_Text_Margins)
        self.menu_View.addAction(self.action_Decrease_Text_Margins)
        self.menu_View.addAction(self.action_Search_Result_Sizes)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Go.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Suttas.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Sutta_Search)
        self.toolBar.addAction(self.action_Dictionary_Search)
        self.toolBar.addAction(self.action_Memos)
        self.toolBar.addAction(self.action_Links)

        self.retranslateUi(SuttaSearchWindow)
        self.rightside_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SuttaSearchWindow)

    def retranslateUi(self, SuttaSearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SuttaSearchWindow.setWindowTitle(_translate("SuttaSearchWindow", "Sutta Search - Simsapa"))
        self.fulltext_prev_btn.setToolTip(_translate("SuttaSearchWindow", "Previous page of results"))
        self.fulltext_next_btn.setToolTip(_translate("SuttaSearchWindow", "Next page of results"))
        self.fulltext_label.setText(_translate("SuttaSearchWindow", "Showing a-b out of x"))
        self.fulltext_first_page_btn.setToolTip(_translate("SuttaSearchWindow", "First page of results"))
        self.fulltext_last_page_btn.setToolTip(_translate("SuttaSearchWindow", "Last page of results"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.fulltext_tab), _translate("SuttaSearchWindow", "Results"))
        self.label_6.setText(_translate("SuttaSearchWindow", "Labels:"))
        self.label_select.setItemText(0, _translate("SuttaSearchWindow", "Sutta Ref."))
        self.label_select.setItemText(1, _translate("SuttaSearchWindow", "Ref. + Title"))
        self.label_select.setItemText(2, _translate("SuttaSearchWindow", "No Labels"))
        self.label.setText(_translate("SuttaSearchWindow", "Distance:"))
        self.label_4.setText(_translate("SuttaSearchWindow", "Min. links:"))
        self.links_regenerate_button.setToolTip(_translate("SuttaSearchWindow", "Regenerate Links Graph"))
        self.open_selected_link_button.setToolTip(_translate("SuttaSearchWindow", "Open Selected Link"))
        self.open_selected_link_button.setText(_translate("SuttaSearchWindow", "Open Selected"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.links_tab), _translate("SuttaSearchWindow", "Links"))
        self.add_memo_button.setText(_translate("SuttaSearchWindow", "Add"))
        self.clear_memo_button.setText(_translate("SuttaSearchWindow", "Clear"))
        self.remove_memo_button.setText(_translate("SuttaSearchWindow", "Remove"))
        self.label_2.setText(_translate("SuttaSearchWindow", "Front"))
        self.label_5.setText(_translate("SuttaSearchWindow", "Back"))
        self.label_3.setText(_translate("SuttaSearchWindow", "Memos for this page"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.memos_tab), _translate("SuttaSearchWindow", "Memos"))
        self.rightside_tabs.setTabText(self.rightside_tabs.indexOf(self.recent_tab), _translate("SuttaSearchWindow", "History"))
        self.menu_File.setTitle(_translate("SuttaSearchWindow", "&File"))
        self.menu_Edit.setTitle(_translate("SuttaSearchWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("SuttaSearchWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("SuttaSearchWindow", "&Help"))
        self.menu_Suttas.setTitle(_translate("SuttaSearchWindow", "&Suttas"))
        self.menu_Go.setTitle(_translate("SuttaSearchWindow", "&Go"))
        self.menu_View.setTitle(_translate("SuttaSearchWindow", "&View"))
        self.toolBar.setWindowTitle(_translate("SuttaSearchWindow", "toolBar"))
        self.action_Copy.setText(_translate("SuttaSearchWindow", "&Copy"))
        self.action_Copy.setShortcut(_translate("SuttaSearchWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("SuttaSearchWindow", "&Paste"))
        self.action_Paste.setShortcut(_translate("SuttaSearchWindow", "Ctrl+V"))
        self.action_Quit.setText(_translate("SuttaSearchWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("SuttaSearchWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("SuttaSearchWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("SuttaSearchWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("SuttaSearchWindow", "F6"))
        self.action_About.setText(_translate("SuttaSearchWindow", "&About"))
        self.action_Website.setText(_translate("SuttaSearchWindow", "&Website"))
        self.action_Close_Window.setText(_translate("SuttaSearchWindow", "&Close Window"))
        self.action_Open.setText(_translate("SuttaSearchWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("SuttaSearchWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("SuttaSearchWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("SuttaSearchWindow", "Document Reader"))
        self.action_Library.setText(_translate("SuttaSearchWindow", "&Library"))
        self.action_Memos.setText(_translate("SuttaSearchWindow", "&Memos"))
        self.action_Memos.setToolTip(_translate("SuttaSearchWindow", "Memos"))
        self.action_Memos.setShortcut(_translate("SuttaSearchWindow", "F9"))
        self.action_Dictionaries_Manager.setText(_translate("SuttaSearchWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("SuttaSearchWindow", "F10"))
        self.action_Links.setText(_translate("SuttaSearchWindow", "&Links"))
        self.action_Links.setShortcut(_translate("SuttaSearchWindow", "F11"))
        self.action_Search_Query_Terms.setText(_translate("SuttaSearchWindow", "Search Query Terms"))
        self.action_Lookup_Clipboard_in_Suttas.setText(_translate("SuttaSearchWindow", "&Lookup Clipboard in Suttas"))
        self.action_Lookup_Clipboard_in_Suttas.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Shift+S"))
        self.action_Select_Sutta_Authors.setText(_translate("SuttaSearchWindow", "&Select Sutta Authors..."))
        self.action_Re_index_database.setText(_translate("SuttaSearchWindow", "Re-index database..."))
        self.action_Re_download_database.setText(_translate("SuttaSearchWindow", "Re-download database..."))
        self.action_Notify_About_Updates.setText(_translate("SuttaSearchWindow", "Notify About Updates"))
        self.action_Lookup_Clipboard_in_Dictionary.setText(_translate("SuttaSearchWindow", "&Lookup Clipboard in Dictionary"))
        self.action_Lookup_Clipboard_in_Dictionary.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Shift+G"))
        self.action_Show_Toolbar.setText(_translate("SuttaSearchWindow", "Show Toolbar"))
        self.action_First_Window_on_Startup.setText(_translate("SuttaSearchWindow", "First Window on Startup..."))
        self.action_Focus_Search_Input.setText(_translate("SuttaSearchWindow", "Focus Search Input"))
        self.action_Focus_Search_Input.setShortcut(_translate("SuttaSearchWindow", "Ctrl+L"))
        self.action_Find_in_Page.setText(_translate("SuttaSearchWindow", "Find in Page..."))
        self.action_Find_in_Page.setShortcut(_translate("SuttaSearchWindow", "Ctrl+F"))
        self.action_Show_Word_Scan_Popup.setText(_translate("SuttaSearchWindow", "Show Word Scan Popup"))
        self.action_Show_Word_Scan_Popup.setShortcut(_translate("SuttaSearchWindow", "Ctrl+F6"))
        self.action_Show_Related_Suttas.setText(_translate("SuttaSearchWindow", "Show Related Suttas"))
        self.action_Next_Result.setText(_translate("SuttaSearchWindow", "Next Result"))
        self.action_Next_Result.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Down"))
        self.action_Previous_Result.setText(_translate("SuttaSearchWindow", "Previous Result"))
        self.action_Previous_Result.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Up"))
        self.action_Previous_Tab.setText(_translate("SuttaSearchWindow", "Previous Tab"))
        self.action_Previous_Tab.setShortcut(_translate("SuttaSearchWindow", "Ctrl+PgUp"))
        self.action_Next_Tab.setText(_translate("SuttaSearchWindow", "Next Tab"))
        self.action_Next_Tab.setShortcut(_translate("SuttaSearchWindow", "Ctrl+PgDown"))
        self.action_Sutta_Study.setText(_translate("SuttaSearchWindow", "Sutta Study"))
        self.action_Sutta_Study.setShortcut(_translate("SuttaSearchWindow", "Ctrl+F5"))
        self.action_Lookup_Selection_in_Dictionary.setText(_translate("SuttaSearchWindow", "Lookup Selection in Dictionary"))
        self.action_Lookup_Selection_in_Dictionary.setShortcut(_translate("SuttaSearchWindow", "Ctrl+G"))
        self.action_Increase_Text_Size.setText(_translate("SuttaSearchWindow", "&Increase Text Size"))
        self.action_Increase_Text_Size.setShortcut(_translate("SuttaSearchWindow", "Ctrl++"))
        self.action_Decrease_Text_Size.setText(_translate("SuttaSearchWindow", "&Decrease Text Size"))
        self.action_Decrease_Text_Size.setShortcut(_translate("SuttaSearchWindow", "Ctrl+-"))
        self.action_Increase_Text_Margins.setText(_translate("SuttaSearchWindow", "Increase Text Margins"))
        self.action_Increase_Text_Margins.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Shift++"))
        self.action_Decrease_Text_Margins.setText(_translate("SuttaSearchWindow", "Decrease Text Margins"))
        self.action_Decrease_Text_Margins.setShortcut(_translate("SuttaSearchWindow", "Ctrl+Shift+-"))
        self.action_Import_Suttas_with_Spreadsheet.setText(_translate("SuttaSearchWindow", "Import Suttas with Spreadsheet..."))
        self.action_Remove_Imported_Suttas.setText(_translate("SuttaSearchWindow", "Remove Imported Suttas..."))
        self.action_Search_Result_Sizes.setText(_translate("SuttaSearchWindow", "&Search Result Sizes..."))
        self.action_Search_As_You_Type.setText(_translate("SuttaSearchWindow", "Search As You &Type"))
        self.action_Search_As_You_Type.setToolTip(_translate("SuttaSearchWindow", "Run search query when you stop typing"))
        self.action_Search_Completion.setText(_translate("SuttaSearchWindow", "Search &Completion"))
        self.action_Bookmarks.setText(_translate("SuttaSearchWindow", "&Bookmarks"))
        self.action_Bookmarks.setShortcut(_translate("SuttaSearchWindow", "F7"))
        self.action_Show_All_Variant_Readings.setText(_translate("SuttaSearchWindow", "Show All &Variant Readings"))
        self.action_Show_Translation_and_Pali_Line_by_Line.setText(_translate("SuttaSearchWindow", "Show Translation and Pali &Line by Line"))
        self.action_Pali_Courses.setText(_translate("SuttaSearchWindow", "&Pali Courses"))
        self.action_Pali_Courses.setShortcut(_translate("SuttaSearchWindow", "F8"))
        self.action_Show_Sidebar.setText(_translate("SuttaSearchWindow", "Show &Sidebar"))
        self.action_Show_Sidebar.setShortcut(_translate("SuttaSearchWindow", "Ctrl+F9"))
