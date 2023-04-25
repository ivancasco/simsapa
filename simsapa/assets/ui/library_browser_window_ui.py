# Form implementation generated from reading ui file 'simsapa/assets/ui/library_browser_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LibraryBrowserWindow(object):
    def setupUi(self, LibraryBrowserWindow):
        LibraryBrowserWindow.setObjectName("LibraryBrowserWindow")
        LibraryBrowserWindow.resize(856, 581)
        self.central_widget = QtWidgets.QWidget(parent=LibraryBrowserWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.searchbar_layout = QtWidgets.QHBoxLayout()
        self.searchbar_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.searchbar_layout.setObjectName("searchbar_layout")
        self.search_input = QtWidgets.QLineEdit(parent=self.central_widget)
        self.search_input.setMinimumSize(QtCore.QSize(0, 35))
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setObjectName("search_input")
        self.searchbar_layout.addWidget(self.search_input)
        self.search_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.search_button.setMinimumSize(QtCore.QSize(0, 40))
        self.search_button.setObjectName("search_button")
        self.searchbar_layout.addWidget(self.search_button)
        self.main_layout.addLayout(self.searchbar_layout)
        self.splitter = QtWidgets.QSplitter(parent=self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.documents_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.documents_layout.setContentsMargins(0, 0, 0, 0)
        self.documents_layout.setObjectName("documents_layout")
        self.documents_list = QtWidgets.QListView(parent=self.verticalLayoutWidget_2)
        self.documents_list.setObjectName("documents_list")
        self.documents_layout.addWidget(self.documents_list)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.info_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.info_layout.setContentsMargins(0, 0, 0, 0)
        self.info_layout.setObjectName("info_layout")
        self.doc_cover = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.doc_cover.setMinimumSize(QtCore.QSize(100, 0))
        self.doc_cover.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.doc_cover.setObjectName("doc_cover")
        self.info_layout.addWidget(self.doc_cover)
        self.doc_title = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.doc_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.doc_title.setObjectName("doc_title")
        self.info_layout.addWidget(self.doc_title)
        self.doc_author = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.doc_author.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.doc_author.setObjectName("doc_author")
        self.info_layout.addWidget(self.doc_author)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.info_layout.addWidget(self.label)
        self.main_layout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.main_layout)
        LibraryBrowserWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(parent=LibraryBrowserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Windows = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Windows.setObjectName("menu_Windows")
        self.menu_Help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Library = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Library.setObjectName("menu_Library")
        LibraryBrowserWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(parent=LibraryBrowserWindow)
        self.toolBar.setObjectName("toolBar")
        LibraryBrowserWindow.addToolBar(QtCore.Qt.ToolBarArea.LeftToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(parent=LibraryBrowserWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        LibraryBrowserWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)
        self.action_Copy = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtGui.QAction(parent=LibraryBrowserWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtGui.QAction(parent=LibraryBrowserWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtGui.QAction(parent=LibraryBrowserWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_Dictionary_Search.setIcon(icon2)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Add = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Add.setObjectName("action_Add")
        self.action_Remove = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Remove.setObjectName("action_Remove")
        self.action_Open_Selected = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Open_Selected.setObjectName("action_Open_Selected")
        self.action_Library = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Memos = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Memos.setObjectName("action_Memos")
        self.action_Dictionaries_Manager = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.action_Links = QtGui.QAction(parent=LibraryBrowserWindow)
        self.action_Links.setObjectName("action_Links")
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
        self.menu_Windows.addAction(self.action_Links)
        self.menu_Help.addAction(self.action_Website)
        self.menu_Help.addAction(self.action_About)
        self.menu_Library.addAction(self.action_Open_Selected)
        self.menu_Library.addAction(self.action_Add)
        self.menu_Library.addAction(self.action_Remove)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Library.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Sutta_Search)
        self.toolBar.addAction(self.action_Dictionary_Search)
        self.toolBar_2.addAction(self.action_Open_Selected)
        self.toolBar_2.addAction(self.action_Add)
        self.toolBar_2.addAction(self.action_Remove)

        self.retranslateUi(LibraryBrowserWindow)
        QtCore.QMetaObject.connectSlotsByName(LibraryBrowserWindow)

    def retranslateUi(self, LibraryBrowserWindow):
        _translate = QtCore.QCoreApplication.translate
        LibraryBrowserWindow.setWindowTitle(_translate("LibraryBrowserWindow", "Library - Simsapa"))
        self.search_button.setText(_translate("LibraryBrowserWindow", "Search"))
        self.doc_cover.setText(_translate("LibraryBrowserWindow", "Cover"))
        self.doc_title.setText(_translate("LibraryBrowserWindow", "Title"))
        self.doc_author.setText(_translate("LibraryBrowserWindow", "Author"))
        self.menu_File.setTitle(_translate("LibraryBrowserWindow", "&File"))
        self.menu_Edit.setTitle(_translate("LibraryBrowserWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("LibraryBrowserWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("LibraryBrowserWindow", "&Help"))
        self.menu_Library.setTitle(_translate("LibraryBrowserWindow", "&Library"))
        self.toolBar.setWindowTitle(_translate("LibraryBrowserWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("LibraryBrowserWindow", "toolBar_2"))
        self.action_Copy.setText(_translate("LibraryBrowserWindow", "&Copy"))
        self.action_Paste.setText(_translate("LibraryBrowserWindow", "&Paste"))
        self.action_Quit.setText(_translate("LibraryBrowserWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("LibraryBrowserWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("LibraryBrowserWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("LibraryBrowserWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("LibraryBrowserWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("LibraryBrowserWindow", "F6"))
        self.action_About.setText(_translate("LibraryBrowserWindow", "&About"))
        self.action_Website.setText(_translate("LibraryBrowserWindow", "&Website"))
        self.action_Close_Window.setText(_translate("LibraryBrowserWindow", "&Close Window"))
        self.action_Open.setText(_translate("LibraryBrowserWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("LibraryBrowserWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("LibraryBrowserWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("LibraryBrowserWindow", "Document Reader"))
        self.action_Document_Reader.setShortcut(_translate("LibraryBrowserWindow", "F7"))
        self.action_Add.setText(_translate("LibraryBrowserWindow", "&Add..."))
        self.action_Remove.setText(_translate("LibraryBrowserWindow", "&Remove"))
        self.action_Remove.setShortcut(_translate("LibraryBrowserWindow", "Del"))
        self.action_Open_Selected.setText(_translate("LibraryBrowserWindow", "&Open Selected"))
        self.action_Library.setText(_translate("LibraryBrowserWindow", "&Library"))
        self.action_Library.setShortcut(_translate("LibraryBrowserWindow", "F8"))
        self.action_Memos.setText(_translate("LibraryBrowserWindow", "&Memos"))
        self.action_Memos.setToolTip(_translate("LibraryBrowserWindow", "Memos"))
        self.action_Memos.setShortcut(_translate("LibraryBrowserWindow", "F9"))
        self.action_Dictionaries_Manager.setText(_translate("LibraryBrowserWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("LibraryBrowserWindow", "F10"))
        self.action_Links.setText(_translate("LibraryBrowserWindow", "&Links"))
        self.action_Links.setShortcut(_translate("LibraryBrowserWindow", "F11"))
