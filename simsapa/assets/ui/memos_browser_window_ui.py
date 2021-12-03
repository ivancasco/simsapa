# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simsapa/assets/ui/memos_browser_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MemosBrowserWindow(object):
    def setupUi(self, MemosBrowserWindow):
        MemosBrowserWindow.setObjectName("MemosBrowserWindow")
        MemosBrowserWindow.resize(856, 623)
        MemosBrowserWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(MemosBrowserWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.central_widget)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.back_input = QtWidgets.QPlainTextEdit(self.central_widget)
        self.back_input.setMinimumSize(QtCore.QSize(0, 50))
        self.back_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.back_input.setObjectName("back_input")
        self.verticalLayout_4.addWidget(self.back_input)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.central_widget)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.front_input = QtWidgets.QPlainTextEdit(self.central_widget)
        self.front_input.setMinimumSize(QtCore.QSize(0, 50))
        self.front_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.front_input.setObjectName("front_input")
        self.verticalLayout_3.addWidget(self.front_input)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.main_layout.addLayout(self.horizontalLayout)
        self.searchbar_layout = QtWidgets.QHBoxLayout()
        self.searchbar_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.searchbar_layout.setObjectName("searchbar_layout")
        self.search_input = QtWidgets.QLineEdit(self.central_widget)
        self.search_input.setMinimumSize(QtCore.QSize(0, 35))
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setObjectName("search_input")
        self.searchbar_layout.addWidget(self.search_input)
        self.search_button = QtWidgets.QPushButton(self.central_widget)
        self.search_button.setMinimumSize(QtCore.QSize(0, 40))
        self.search_button.setObjectName("search_button")
        self.searchbar_layout.addWidget(self.search_button)
        self.main_layout.addLayout(self.searchbar_layout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.memos_list = QtWidgets.QListView(self.central_widget)
        self.memos_list.setMinimumSize(QtCore.QSize(0, 400))
        self.memos_list.setObjectName("memos_list")
        self.verticalLayout_2.addWidget(self.memos_list)
        self.main_layout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.main_layout)
        MemosBrowserWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MemosBrowserWindow)
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
        self.menu_Memos = QtWidgets.QMenu(self.menubar)
        self.menu_Memos.setObjectName("menu_Memos")
        MemosBrowserWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MemosBrowserWindow)
        self.statusbar.setObjectName("statusbar")
        MemosBrowserWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(MemosBrowserWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MemosBrowserWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.action_Copy = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtWidgets.QAction(MemosBrowserWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtWidgets.QAction(MemosBrowserWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtWidgets.QAction(MemosBrowserWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Dictionary_Search.setIcon(icon2)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtWidgets.QAction(MemosBrowserWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Add = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Add.setObjectName("action_Add")
        self.action_Remove = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Remove.setObjectName("action_Remove")
        self.action_Open_Selected = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Open_Selected.setObjectName("action_Open_Selected")
        self.action_Library = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Sync_to_Anki = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Sync_to_Anki.setObjectName("action_Sync_to_Anki")
        self.action_Memos = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Memos.setObjectName("action_Memos")
        self.action_Dictionaries_Manager = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.action_Clear = QtWidgets.QAction(MemosBrowserWindow)
        self.action_Clear.setObjectName("action_Clear")
        self.action_Links = QtWidgets.QAction(MemosBrowserWindow)
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
        self.menu_Memos.addAction(self.action_Sync_to_Anki)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Windows.menuAction())
        self.menubar.addAction(self.menu_Memos.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar_2.addAction(self.action_Add)
        self.toolBar_2.addAction(self.action_Clear)
        self.toolBar_2.addAction(self.action_Remove)
        self.toolBar_2.addAction(self.action_Sync_to_Anki)

        self.retranslateUi(MemosBrowserWindow)
        QtCore.QMetaObject.connectSlotsByName(MemosBrowserWindow)

    def retranslateUi(self, MemosBrowserWindow):
        _translate = QtCore.QCoreApplication.translate
        MemosBrowserWindow.setWindowTitle(_translate("MemosBrowserWindow", "Memos - Simsapa"))
        self.label_4.setText(_translate("MemosBrowserWindow", "Front"))
        self.label_3.setText(_translate("MemosBrowserWindow", "Back"))
        self.search_button.setText(_translate("MemosBrowserWindow", "Search"))
        self.menu_File.setTitle(_translate("MemosBrowserWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MemosBrowserWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("MemosBrowserWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("MemosBrowserWindow", "&Help"))
        self.menu_Memos.setTitle(_translate("MemosBrowserWindow", "&Memos"))
        self.toolBar_2.setWindowTitle(_translate("MemosBrowserWindow", "toolBar_2"))
        self.action_Copy.setText(_translate("MemosBrowserWindow", "&Copy"))
        self.action_Paste.setText(_translate("MemosBrowserWindow", "&Paste"))
        self.action_Quit.setText(_translate("MemosBrowserWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("MemosBrowserWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("MemosBrowserWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("MemosBrowserWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("MemosBrowserWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("MemosBrowserWindow", "F6"))
        self.action_About.setText(_translate("MemosBrowserWindow", "&About"))
        self.action_Website.setText(_translate("MemosBrowserWindow", "&Website"))
        self.action_Close_Window.setText(_translate("MemosBrowserWindow", "&Close Window"))
        self.action_Open.setText(_translate("MemosBrowserWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("MemosBrowserWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("MemosBrowserWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("MemosBrowserWindow", "Document Reader"))
        self.action_Document_Reader.setShortcut(_translate("MemosBrowserWindow", "F7"))
        self.action_Add.setText(_translate("MemosBrowserWindow", "&Add..."))
        self.action_Remove.setText(_translate("MemosBrowserWindow", "&Remove"))
        self.action_Remove.setShortcut(_translate("MemosBrowserWindow", "Del"))
        self.action_Open_Selected.setText(_translate("MemosBrowserWindow", "&Open Selected"))
        self.action_Library.setText(_translate("MemosBrowserWindow", "&Library"))
        self.action_Library.setShortcut(_translate("MemosBrowserWindow", "F8"))
        self.action_Sync_to_Anki.setText(_translate("MemosBrowserWindow", "&Sync to Anki"))
        self.action_Memos.setText(_translate("MemosBrowserWindow", "&Memos"))
        self.action_Memos.setToolTip(_translate("MemosBrowserWindow", "Notes"))
        self.action_Memos.setShortcut(_translate("MemosBrowserWindow", "F9"))
        self.action_Dictionaries_Manager.setText(_translate("MemosBrowserWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("MemosBrowserWindow", "F10"))
        self.action_Clear.setText(_translate("MemosBrowserWindow", "&Clear"))
        self.action_Links.setText(_translate("MemosBrowserWindow", "&Links"))
        self.action_Links.setShortcut(_translate("MemosBrowserWindow", "F11"))
from simsapa.assets import icons_rc