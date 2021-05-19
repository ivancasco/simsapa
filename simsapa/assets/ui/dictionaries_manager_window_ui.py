# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simsapa/assets/ui/dictionaries_manager_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DictionariesManagerWindow(object):
    def setupUi(self, DictionariesManagerWindow):
        DictionariesManagerWindow.setObjectName("DictionariesManagerWindow")
        DictionariesManagerWindow.resize(856, 581)
        DictionariesManagerWindow.setBaseSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(DictionariesManagerWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.splitter = QtWidgets.QSplitter(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.dictionary_sources_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.dictionary_sources_layout.setContentsMargins(0, 0, 0, 0)
        self.dictionary_sources_layout.setObjectName("dictionary_sources_layout")
        self.dictionary_sources_list = QtWidgets.QListView(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dictionary_sources_list.setFont(font)
        self.dictionary_sources_list.setObjectName("dictionary_sources_list")
        self.dictionary_sources_layout.addWidget(self.dictionary_sources_list)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.info_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.info_layout.setContentsMargins(0, 0, 0, 0)
        self.info_layout.setObjectName("info_layout")
        self.dict_cover = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.dict_cover.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dict_cover.setFont(font)
        self.dict_cover.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.dict_cover.setObjectName("dict_cover")
        self.info_layout.addWidget(self.dict_cover)
        self.dict_title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dict_title.setFont(font)
        self.dict_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.dict_title.setObjectName("dict_title")
        self.info_layout.addWidget(self.dict_title)
        self.dict_creator = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dict_creator.setFont(font)
        self.dict_creator.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.dict_creator.setObjectName("dict_creator")
        self.info_layout.addWidget(self.dict_creator)
        self.dict_version = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dict_version.setFont(font)
        self.dict_version.setObjectName("dict_version")
        self.info_layout.addWidget(self.dict_version)
        self.dict_description = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dict_description.setFont(font)
        self.dict_description.setObjectName("dict_description")
        self.info_layout.addWidget(self.dict_description)
        self.dict_message = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dict_message.setFont(font)
        self.dict_message.setObjectName("dict_message")
        self.info_layout.addWidget(self.dict_message)
        self.dict_update_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dict_update_button.sizePolicy().hasHeightForWidth())
        self.dict_update_button.setSizePolicy(sizePolicy)
        self.dict_update_button.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dict_update_button.setFont(font)
        self.dict_update_button.setObjectName("dict_update_button")
        self.info_layout.addWidget(self.dict_update_button)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.info_layout.addWidget(self.label)
        self.main_layout.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.main_layout)
        DictionariesManagerWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(DictionariesManagerWindow)
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
        self.menu_Library = QtWidgets.QMenu(self.menubar)
        self.menu_Library.setObjectName("menu_Library")
        DictionariesManagerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DictionariesManagerWindow)
        self.statusbar.setObjectName("statusbar")
        DictionariesManagerWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(DictionariesManagerWindow)
        self.toolBar.setObjectName("toolBar")
        DictionariesManagerWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(DictionariesManagerWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        DictionariesManagerWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.action_Copy = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Quit = QtWidgets.QAction(DictionariesManagerWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Sutta_Search = QtWidgets.QAction(DictionariesManagerWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/book"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Sutta_Search.setIcon(icon1)
        self.action_Sutta_Search.setObjectName("action_Sutta_Search")
        self.action_Dictionary_Search = QtWidgets.QAction(DictionariesManagerWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dictionary"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Dictionary_Search.setIcon(icon2)
        self.action_Dictionary_Search.setObjectName("action_Dictionary_Search")
        self.action_About = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_About.setObjectName("action_About")
        self.action_Website = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Website.setObjectName("action_Website")
        self.action_Close_Window = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Close_Window.setObjectName("action_Close_Window")
        self.action_Open = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Document_Reader = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Document_Reader.setObjectName("action_Document_Reader")
        self.action_Add = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Add.setObjectName("action_Add")
        self.action_Remove = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Remove.setObjectName("action_Remove")
        self.action_Open_Selected = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Open_Selected.setObjectName("action_Open_Selected")
        self.action_Library = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Library.setObjectName("action_Library")
        self.action_Notes = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Notes.setObjectName("action_Notes")
        self.action_Sync_to_Anki = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Sync_to_Anki.setObjectName("action_Sync_to_Anki")
        self.action_Export = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Export.setObjectName("action_Export")
        self.action_Import_from_File = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Import_from_File.setObjectName("action_Import_from_File")
        self.action_Add_from_URL = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Add_from_URL.setObjectName("action_Add_from_URL")
        self.action_Dictionaries_Manager = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Dictionaries_Manager.setObjectName("action_Dictionaries_Manager")
        self.action_Check_Updates = QtWidgets.QAction(DictionariesManagerWindow)
        self.action_Check_Updates.setObjectName("action_Check_Updates")
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
        self.menu_Windows.addAction(self.action_Notes)
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
        self.toolBar_2.addAction(self.action_Add_from_URL)
        self.toolBar_2.addAction(self.action_Import_from_File)
        self.toolBar_2.addAction(self.action_Check_Updates)
        self.toolBar_2.addAction(self.action_Sync_to_Anki)
        self.toolBar_2.addAction(self.action_Export)
        self.toolBar_2.addAction(self.action_Remove)

        self.retranslateUi(DictionariesManagerWindow)
        QtCore.QMetaObject.connectSlotsByName(DictionariesManagerWindow)

    def retranslateUi(self, DictionariesManagerWindow):
        _translate = QtCore.QCoreApplication.translate
        DictionariesManagerWindow.setWindowTitle(_translate("DictionariesManagerWindow", "Dictionaries Manager - Simsapa"))
        self.dict_cover.setText(_translate("DictionariesManagerWindow", "Cover"))
        self.dict_title.setText(_translate("DictionariesManagerWindow", "Title"))
        self.dict_creator.setText(_translate("DictionariesManagerWindow", "Creator"))
        self.dict_version.setText(_translate("DictionariesManagerWindow", "Version"))
        self.dict_description.setText(_translate("DictionariesManagerWindow", "Description"))
        self.dict_message.setText(_translate("DictionariesManagerWindow", "Message"))
        self.dict_update_button.setText(_translate("DictionariesManagerWindow", "Update"))
        self.menu_File.setTitle(_translate("DictionariesManagerWindow", "&File"))
        self.menu_Edit.setTitle(_translate("DictionariesManagerWindow", "&Edit"))
        self.menu_Windows.setTitle(_translate("DictionariesManagerWindow", "&Windows"))
        self.menu_Help.setTitle(_translate("DictionariesManagerWindow", "&Help"))
        self.menu_Library.setTitle(_translate("DictionariesManagerWindow", "&Library"))
        self.toolBar.setWindowTitle(_translate("DictionariesManagerWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("DictionariesManagerWindow", "toolBar_2"))
        self.action_Copy.setText(_translate("DictionariesManagerWindow", "&Copy"))
        self.action_Paste.setText(_translate("DictionariesManagerWindow", "&Paste"))
        self.action_Quit.setText(_translate("DictionariesManagerWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("DictionariesManagerWindow", "Ctrl+Q"))
        self.action_Sutta_Search.setText(_translate("DictionariesManagerWindow", "&Sutta Search"))
        self.action_Sutta_Search.setShortcut(_translate("DictionariesManagerWindow", "F5"))
        self.action_Dictionary_Search.setText(_translate("DictionariesManagerWindow", "&Dictionary Search"))
        self.action_Dictionary_Search.setShortcut(_translate("DictionariesManagerWindow", "F6"))
        self.action_About.setText(_translate("DictionariesManagerWindow", "&About"))
        self.action_Website.setText(_translate("DictionariesManagerWindow", "&Website"))
        self.action_Close_Window.setText(_translate("DictionariesManagerWindow", "&Close Window"))
        self.action_Open.setText(_translate("DictionariesManagerWindow", "&Open..."))
        self.action_Open.setShortcut(_translate("DictionariesManagerWindow", "Ctrl+O"))
        self.action_Document_Reader.setText(_translate("DictionariesManagerWindow", "D&ocument Reader"))
        self.action_Document_Reader.setToolTip(_translate("DictionariesManagerWindow", "Document Reader"))
        self.action_Document_Reader.setShortcut(_translate("DictionariesManagerWindow", "F7"))
        self.action_Add.setText(_translate("DictionariesManagerWindow", "&Add..."))
        self.action_Remove.setText(_translate("DictionariesManagerWindow", "&Remove"))
        self.action_Remove.setShortcut(_translate("DictionariesManagerWindow", "Del"))
        self.action_Open_Selected.setText(_translate("DictionariesManagerWindow", "&Open Selected"))
        self.action_Library.setText(_translate("DictionariesManagerWindow", "&Library"))
        self.action_Library.setShortcut(_translate("DictionariesManagerWindow", "F8"))
        self.action_Notes.setText(_translate("DictionariesManagerWindow", "&Notes"))
        self.action_Notes.setToolTip(_translate("DictionariesManagerWindow", "Notes"))
        self.action_Notes.setShortcut(_translate("DictionariesManagerWindow", "F9"))
        self.action_Sync_to_Anki.setText(_translate("DictionariesManagerWindow", "&Sync to Anki"))
        self.action_Export.setText(_translate("DictionariesManagerWindow", "&Export..."))
        self.action_Import_from_File.setText(_translate("DictionariesManagerWindow", "&Import from File..."))
        self.action_Add_from_URL.setText(_translate("DictionariesManagerWindow", "&Add from URL..."))
        self.action_Dictionaries_Manager.setText(_translate("DictionariesManagerWindow", "Dictionaries &Manager"))
        self.action_Dictionaries_Manager.setShortcut(_translate("DictionariesManagerWindow", "F10"))
        self.action_Check_Updates.setText(_translate("DictionariesManagerWindow", "&Check Updates"))
from simsapa.assets import icons_rc
