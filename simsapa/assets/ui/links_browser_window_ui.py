# Form implementation generated from reading ui file 'simsapa/assets/ui/links_browser_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LinksBrowserWindow(object):
    def setupUi(self, LinksBrowserWindow):
        LinksBrowserWindow.setObjectName("LinksBrowserWindow")
        LinksBrowserWindow.resize(1146, 643)
        self.central_widget = QtWidgets.QWidget(parent=LinksBrowserWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.splitter = QtWidgets.QSplitter(parent=self.central_widget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.links_wrap_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.links_wrap_layout.setContentsMargins(0, 0, 0, 0)
        self.links_wrap_layout.setObjectName("links_wrap_layout")
        self.links_controls_layout = QtWidgets.QHBoxLayout()
        self.links_controls_layout.setObjectName("links_controls_layout")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.links_controls_layout.addWidget(self.label_6)
        self.label_select = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.label_select.setObjectName("label_select")
        self.label_select.addItem("")
        self.label_select.addItem("")
        self.label_select.addItem("")
        self.links_controls_layout.addWidget(self.label_select)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.links_controls_layout.addWidget(self.label_4)
        self.min_links_input = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_2)
        self.min_links_input.setMinimum(1)
        self.min_links_input.setObjectName("min_links_input")
        self.links_controls_layout.addWidget(self.min_links_input)
        self.links_regenerate_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.links_regenerate_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/reload"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.links_regenerate_button.setIcon(icon)
        self.links_regenerate_button.setObjectName("links_regenerate_button")
        self.links_controls_layout.addWidget(self.links_regenerate_button)
        self.open_selected_link_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.open_selected_link_button.setIcon(icon1)
        self.open_selected_link_button.setObjectName("open_selected_link_button")
        self.links_controls_layout.addWidget(self.open_selected_link_button)
        self.toggle_links_panel_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/caret-right"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toggle_links_panel_button.setIcon(icon2)
        self.toggle_links_panel_button.setObjectName("toggle_links_panel_button")
        self.links_controls_layout.addWidget(self.toggle_links_panel_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.links_controls_layout.addItem(spacerItem)
        self.links_wrap_layout.addLayout(self.links_controls_layout)
        self.links_layout = QtWidgets.QVBoxLayout()
        self.links_layout.setObjectName("links_layout")
        self.links_wrap_layout.addLayout(self.links_layout)
        spacerItem1 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.links_wrap_layout.addItem(spacerItem1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.tabs_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.tabs_layout.setContentsMargins(0, 0, 0, 0)
        self.tabs_layout.setObjectName("tabs_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_link_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.create_link_btn.setObjectName("create_link_btn")
        self.horizontalLayout.addWidget(self.create_link_btn)
        self.clear_link_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.clear_link_btn.setObjectName("clear_link_btn")
        self.horizontalLayout.addWidget(self.clear_link_btn)
        self.remove_link_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.remove_link_btn.setObjectName("remove_link_btn")
        self.horizontalLayout.addWidget(self.remove_link_btn)
        self.tabs_layout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.set_from_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.set_from_btn.setObjectName("set_from_btn")
        self.verticalLayout_3.addWidget(self.set_from_btn)
        self.from_view = QtWidgets.QPlainTextEdit(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_view.sizePolicy().hasHeightForWidth())
        self.from_view.setSizePolicy(sizePolicy)
        self.from_view.setMaximumSize(QtCore.QSize(16777215, 80))
        self.from_view.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.from_view.setObjectName("from_view")
        self.verticalLayout_3.addWidget(self.from_view)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.set_to_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.set_to_btn.setObjectName("set_to_btn")
        self.verticalLayout_2.addWidget(self.set_to_btn)
        self.to_view = QtWidgets.QPlainTextEdit(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_view.sizePolicy().hasHeightForWidth())
        self.to_view.setSizePolicy(sizePolicy)
        self.to_view.setMaximumSize(QtCore.QSize(16777215, 80))
        self.to_view.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.to_view.setObjectName("to_view")
        self.verticalLayout_2.addWidget(self.to_view)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.tabs_layout.addLayout(self.horizontalLayout_5)
        self.searchbar_layout = QtWidgets.QVBoxLayout()
        self.searchbar_layout.setObjectName("searchbar_layout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search_input = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_3)
        self.search_input.setMinimumSize(QtCore.QSize(0, 35))
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_4.addWidget(self.search_input)
        self.search_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_4.addWidget(self.search_button)
        self.link_table = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_3)
        self.link_table.setObjectName("link_table")
        self.link_table.addItem("")
        self.link_table.addItem("")
        self.link_table.addItem("")
        self.horizontalLayout_4.addWidget(self.link_table)
        self.searchbar_layout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pali_buttons_layout = QtWidgets.QVBoxLayout()
        self.pali_buttons_layout.setObjectName("pali_buttons_layout")
        self.horizontalLayout_6.addLayout(self.pali_buttons_layout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.searchbar_layout.addLayout(self.horizontalLayout_6)
        self.tabs_layout.addLayout(self.searchbar_layout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.set_page_number = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_3)
        self.set_page_number.setEnabled(False)
        self.set_page_number.setObjectName("set_page_number")
        self.horizontalLayout_3.addWidget(self.set_page_number)
        self.page_number = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_3)
        self.page_number.setEnabled(False)
        self.page_number.setObjectName("page_number")
        self.horizontalLayout_3.addWidget(self.page_number)
        self.tabs_layout.addLayout(self.horizontalLayout_3)
        self.results_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_3)
        self.results_list.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.results_list.setLineWidth(1)
        self.results_list.setObjectName("results_list")
        self.tabs_layout.addWidget(self.results_list)
        self.main_layout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.main_layout)
        LinksBrowserWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(parent=LinksBrowserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Windows = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Windows.setObjectName("menu_Windows")
        self.menu_Help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Go = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Go.setObjectName("menu_Go")
        LinksBrowserWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(parent=LinksBrowserWindow)
        self.toolBar.setObjectName("toolBar")
        LinksBrowserWindow.addToolBar(QtCore.Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.action_Copy = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtGui.QAction(parent=LinksBrowserWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Quit.setIcon(icon3)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtGui.QAction(parent=LinksBrowserWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Dictionary_Search.setIcon(icon4)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Library = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Memos = QtGui.QAction(parent=LinksBrowserWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pen-fancy"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Memos.setIcon(icon5)
        self.action_Memos.setObjectName("action_Memos")
        self.action_Dictionaries_Manager = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.action_Links = QtGui.QAction(parent=LinksBrowserWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/diagram"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Links.setIcon(icon6)
        self.action_Links.setObjectName("action_Links")
        self.action_Re_index_database = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Re_index_database.setObjectName("action_Re_index_database")
        self.action_Re_download_database = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Re_download_database.setObjectName("action_Re_download_database")
        self.action_Notify_About_Updates = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Notify_About_Updates.setCheckable(True)
        self.action_Notify_About_Updates.setChecked(True)
        self.action_Notify_About_Updates.setObjectName("action_Notify_About_Updates")
        self.action_Show_Toolbar = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Show_Toolbar.setCheckable(True)
        self.action_Show_Toolbar.setObjectName("action_Show_Toolbar")
        self.action_First_Window_on_Startup = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_First_Window_on_Startup.setObjectName("action_First_Window_on_Startup")
        self.action_Focus_Search_Input = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Focus_Search_Input.setObjectName("action_Focus_Search_Input")
        self.action_Show_Word_Lookup = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Show_Word_Lookup.setCheckable(True)
        self.action_Show_Word_Lookup.setObjectName("action_Show_Word_Lookup")
        self.action_Next_Result = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Next_Result.setObjectName("action_Next_Result")
        self.action_Previous_Result = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Previous_Result.setObjectName("action_Previous_Result")
        self.action_Sutta_Study = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Sutta_Study.setIcon(icon1)
        self.action_Sutta_Study.setObjectName("action_Sutta_Study")
        self.action_Bookmarks = QtGui.QAction(parent=LinksBrowserWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/bookmark"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Bookmarks.setIcon(icon7)
        self.action_Bookmarks.setObjectName("action_Bookmarks")
        self.action_Pali_Courses = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Pali_Courses.setIcon(icon1)
        self.action_Pali_Courses.setObjectName("action_Pali_Courses")
        self.action_Link_Preview = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Link_Preview.setCheckable(True)
        self.action_Link_Preview.setChecked(True)
        self.action_Link_Preview.setObjectName("action_Link_Preview")
        self.action_Ebook_Reader = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Ebook_Reader.setIcon(icon1)
        self.action_Ebook_Reader.setObjectName("action_Ebook_Reader")
        self.action_Check_for_Updates = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Check_for_Updates.setObjectName("action_Check_for_Updates")
        self.action_Sutta_Index = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Sutta_Index.setIcon(icon1)
        self.action_Sutta_Index.setObjectName("action_Sutta_Index")
        self.action_Keep_Running_in_the_Background = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Keep_Running_in_the_Background.setCheckable(True)
        self.action_Keep_Running_in_the_Background.setChecked(True)
        self.action_Keep_Running_in_the_Background.setObjectName("action_Keep_Running_in_the_Background")
        self.action_Tray_Click_Opens_Window = QtGui.QAction(parent=LinksBrowserWindow)
        self.action_Tray_Click_Opens_Window.setObjectName("action_Tray_Click_Opens_Window")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close_Window)
        self.menu_File.addAction(self.action_Keep_Running_in_the_Background)
        self.menu_File.addAction(self.action_Tray_Click_Opens_Window)
        self.menu_File.addAction(self.action_Re_index_database)
        self.menu_File.addAction(self.action_Re_download_database)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addAction(self.action_Focus_Search_Input)
        self.menu_Windows.addAction(self.action_Sutta_Search)
        self.menu_Windows.addAction(self.action_Sutta_Study)
        self.menu_Windows.addAction(self.action_Sutta_Index)
        self.menu_Windows.addAction(self.action_Dictionary_Search)
        self.menu_Windows.addAction(self.action_Show_Word_Lookup)
        self.menu_Windows.addAction(self.action_Bookmarks)
        self.menu_Windows.addAction(self.action_Pali_Courses)
        self.menu_Windows.addAction(self.action_Dictionaries_Manager)
        self.menu_Windows.addAction(self.action_Document_Reader)
        self.menu_Windows.addAction(self.action_Library)
        self.menu_Windows.addAction(self.action_Ebook_Reader)
        self.menu_Windows.addAction(self.action_Memos)
        self.menu_Windows.addAction(self.action_Links)
        self.menu_Windows.addAction(self.action_First_Window_on_Startup)
        self.menu_Windows.addAction(self.action_Show_Toolbar)
        self.menu_Windows.addAction(self.action_Link_Preview)
        self.menu_Help.addAction(self.action_Check_for_Updates)
        self.menu_Help.addAction(self.action_Notify_About_Updates)
        self.menu_Help.addAction(self.action_Website)
        self.menu_Help.addAction(self.action_About)
        self.menu_Go.addAction(self.action_Previous_Result)
        self.menu_Go.addAction(self.action_Next_Result)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Go.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Sutta_Search)
        self.toolBar.addAction(self.action_Dictionary_Search)
        self.toolBar.addAction(self.action_Memos)
        self.toolBar.addAction(self.action_Links)

        self.retranslateUi(LinksBrowserWindow)
        QtCore.QMetaObject.connectSlotsByName(LinksBrowserWindow)

    def retranslateUi(self, LinksBrowserWindow):
        _translate = QtCore.QCoreApplication.translate
        LinksBrowserWindow.setWindowTitle(_translate("LinksBrowserWindow", "Links - Simsapa"))
        self.label_6.setText(_translate("LinksBrowserWindow", "Labels:"))
        self.label_select.setItemText(0, _translate("LinksBrowserWindow", "Sutta Ref."))
        self.label_select.setItemText(1, _translate("LinksBrowserWindow", "Ref. + Title"))
        self.label_select.setItemText(2, _translate("LinksBrowserWindow", "No Labels"))
        self.label_4.setText(_translate("LinksBrowserWindow", "Min. links:"))
        self.links_regenerate_button.setToolTip(_translate("LinksBrowserWindow", "Regenerate Links Graph"))
        self.open_selected_link_button.setToolTip(_translate("LinksBrowserWindow", "Open Selected Link"))
        self.open_selected_link_button.setText(_translate("LinksBrowserWindow", "Open Selected"))
        self.toggle_links_panel_button.setText(_translate("LinksBrowserWindow", "Toggle Links Panel"))
        self.create_link_btn.setText(_translate("LinksBrowserWindow", "Create Link"))
        self.clear_link_btn.setText(_translate("LinksBrowserWindow", "Clear"))
        self.remove_link_btn.setText(_translate("LinksBrowserWindow", "Remove Link"))
        self.set_from_btn.setText(_translate("LinksBrowserWindow", "Set From"))
        self.set_to_btn.setText(_translate("LinksBrowserWindow", "Set To"))
        self.search_button.setText(_translate("LinksBrowserWindow", "Search"))
        self.link_table.setItemText(0, _translate("LinksBrowserWindow", "Suttas"))
        self.link_table.setItemText(1, _translate("LinksBrowserWindow", "DictWords"))
        self.link_table.setItemText(2, _translate("LinksBrowserWindow", "Documents"))
        self.set_page_number.setText(_translate("LinksBrowserWindow", "Set page number:"))
        self.menu_File.setTitle(_translate("LinksBrowserWindow", "&File"))
        self.menu_Edit.setTitle(_translate("LinksBrowserWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("LinksBrowserWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("LinksBrowserWindow", "&Help"))
        self.menu_Go.setTitle(_translate("LinksBrowserWindow", "&Go"))
        self.toolBar.setWindowTitle(_translate("LinksBrowserWindow", "toolBar"))
        self.action_Copy.setText(_translate("LinksBrowserWindow", "&Copy"))
        self.action_Copy.setShortcut(_translate("LinksBrowserWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("LinksBrowserWindow", "&Paste"))
        self.action_Paste.setShortcut(_translate("LinksBrowserWindow", "Ctrl+V"))
        self.action_Quit.setText(_translate("LinksBrowserWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("LinksBrowserWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("LinksBrowserWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("LinksBrowserWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("LinksBrowserWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("LinksBrowserWindow", "F6"))
        self.action_About.setText(_translate("LinksBrowserWindow", "&About"))
        self.action_Website.setText(_translate("LinksBrowserWindow", "&Website"))
        self.action_Close_Window.setText(_translate("LinksBrowserWindow", "&Close Window"))
        self.action_Open.setText(_translate("LinksBrowserWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("LinksBrowserWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("LinksBrowserWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("LinksBrowserWindow", "Document Reader"))
        self.action_Document_Reader.setShortcut(_translate("LinksBrowserWindow", "F7"))
        self.action_Library.setText(_translate("LinksBrowserWindow", "&Library"))
        self.action_Library.setShortcut(_translate("LinksBrowserWindow", "F8"))
        self.action_Memos.setText(_translate("LinksBrowserWindow", "&Memos"))
        self.action_Memos.setToolTip(_translate("LinksBrowserWindow", "Memos"))
        self.action_Memos.setShortcut(_translate("LinksBrowserWindow", "F9"))
        self.action_Dictionaries_Manager.setText(_translate("LinksBrowserWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("LinksBrowserWindow", "F10"))
        self.action_Links.setText(_translate("LinksBrowserWindow", "&Links"))
        self.action_Links.setShortcut(_translate("LinksBrowserWindow", "F11"))
        self.action_Re_index_database.setText(_translate("LinksBrowserWindow", "Re-index database..."))
        self.action_Re_download_database.setText(_translate("LinksBrowserWindow", "Re-download database..."))
        self.action_Notify_About_Updates.setText(_translate("LinksBrowserWindow", "Notify About Updates"))
        self.action_Show_Toolbar.setText(_translate("LinksBrowserWindow", "Show Toolbar"))
        self.action_First_Window_on_Startup.setText(_translate("LinksBrowserWindow", "First Window on Startup..."))
        self.action_Focus_Search_Input.setText(_translate("LinksBrowserWindow", "Focus Search Input"))
        self.action_Focus_Search_Input.setShortcut(_translate("LinksBrowserWindow", "Ctrl+L"))
        self.action_Show_Word_Lookup.setText(_translate("LinksBrowserWindow", "Show Word Lookup"))
        self.action_Show_Word_Lookup.setShortcut(_translate("LinksBrowserWindow", "Ctrl+F6"))
        self.action_Next_Result.setText(_translate("LinksBrowserWindow", "Next Result"))
        self.action_Next_Result.setShortcut(_translate("LinksBrowserWindow", "Ctrl+Down"))
        self.action_Previous_Result.setText(_translate("LinksBrowserWindow", "Previous Result"))
        self.action_Previous_Result.setShortcut(_translate("LinksBrowserWindow", "Ctrl+Up"))
        self.action_Sutta_Study.setText(_translate("LinksBrowserWindow", "Sutta Study"))
        self.action_Sutta_Study.setShortcut(_translate("LinksBrowserWindow", "Ctrl+F5"))
        self.action_Bookmarks.setText(_translate("LinksBrowserWindow", "&Bookmarks"))
        self.action_Bookmarks.setShortcut(_translate("LinksBrowserWindow", "F7"))
        self.action_Pali_Courses.setText(_translate("LinksBrowserWindow", "&Pali Courses"))
        self.action_Pali_Courses.setShortcut(_translate("LinksBrowserWindow", "F8"))
        self.action_Link_Preview.setText(_translate("LinksBrowserWindow", "Link Preview"))
        self.action_Ebook_Reader.setText(_translate("LinksBrowserWindow", "&Ebook Reader"))
        self.action_Check_for_Updates.setText(_translate("LinksBrowserWindow", "Check for Updates..."))
        self.action_Sutta_Index.setText(_translate("LinksBrowserWindow", "Sutta Index"))
        self.action_Keep_Running_in_the_Background.setText(_translate("LinksBrowserWindow", "Keep Running in the Background"))
        self.action_Tray_Click_Opens_Window.setText(_translate("LinksBrowserWindow", "Tray Click Opens Window..."))
