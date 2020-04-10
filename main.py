# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtGui import QTransform, QPixmap, QImage, QDrag, QPixmap, QPainter, QCursor, QFont, QBrush, QPen, QColor
from ClickableLabel import ClickableLabel
from Rules import Window_rules
from Game import Game
from PyQt5.QtCore import QMimeData, Qt, QRect, QTimer, QTime


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1340, 900)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        MainWindow.setMouseTracking(True) #new
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_edit = QtWidgets.QFrame(self.centralwidget)
        self.frame_edit.setGeometry(QtCore.QRect(20, 420, 271, 401))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.frame_edit.setFont(font)
        self.frame_edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edit.setObjectName("frame_edit")
        self.button_rules = QtWidgets.QPushButton(self.frame_edit)
        self.button_rules.setGeometry(QtCore.QRect(10, 320, 251, 71))
        self.button_rules.setObjectName("button_rules")
        self.button_clear = QtWidgets.QPushButton(self.frame_edit)
        self.button_clear.setGeometry(QtCore.QRect(10, 210, 251, 71))
        self.button_clear.setObjectName("button_clear")
        self.button_undo = QtWidgets.QPushButton(self.frame_edit)
        self.button_undo.setGeometry(QtCore.QRect(10, 30, 251, 71))
        self.button_undo.setObjectName("button_undo")
        self.button_redo = QtWidgets.QPushButton(self.frame_edit)
        self.button_redo.setGeometry(QtCore.QRect(10, 120, 251, 71))
        self.button_redo.setObjectName("button_redo")
        self.patentbox = QtWidgets.QComboBox(self.centralwidget)
        self.patentbox.setGeometry(QtCore.QRect(30, 120, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.patentbox.setFont(font)
        self.patentbox.setObjectName("patentbox")
        self.patentbox.addItem("")
        self.patentbox.addItem("")
        self.frame_lvl = QtWidgets.QFrame(self.centralwidget)
        self.frame_lvl.setGeometry(QtCore.QRect(210, 80, 101, 81))
        self.frame_lvl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lvl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lvl.setObjectName("frame_lvl")
        self.label_lvl = QtWidgets.QLabel(self.frame_lvl)
        self.label_lvl.setGeometry(QtCore.QRect(10, 0, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_lvl.setFont(font)
        self.label_lvl.setScaledContents(True)
        self.label_lvl.setObjectName("label_lvl")
        self.spin_lvl = QtWidgets.QSpinBox(self.frame_lvl)
        self.spin_lvl.setGeometry(QtCore.QRect(30, 40, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.spin_lvl.setFont(font)
        self.spin_lvl.setObjectName("spin_lvl")
        self.name_patent_box = QtWidgets.QGroupBox(self.centralwidget)
        self.name_patent_box.setGeometry(QtCore.QRect(310, 10, 721, 61))
        self.name_patent_box.setTitle("")
        self.name_patent_box.setObjectName("name_patent_box")
        self.name_patent = QtWidgets.QLabel(self.name_patent_box)
        self.name_patent.setGeometry(QtCore.QRect(0, 10, 721, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.name_patent.setFont(font)
        self.name_patent.setAlignment(QtCore.Qt.AlignCenter)
        self.name_patent.setObjectName("name_patent")
        self.difficulty_box = QtWidgets.QGroupBox(self.centralwidget)
        self.difficulty_box.setGeometry(QtCore.QRect(30, 30, 251, 41))
        self.difficulty_box.setTitle("")
        self.difficulty_box.setObjectName("difficulty_box")
        self.label_difficulty = QtWidgets.QLabel(self.difficulty_box)
        self.label_difficulty.setGeometry(QtCore.QRect(0, 0, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_difficulty.setFont(font)
        self.label_difficulty.setAlignment(QtCore.Qt.AlignCenter)
        self.label_difficulty.setObjectName("label_difficulty")
        self.frame_progress = QtWidgets.QFrame(self.centralwidget)
        self.frame_progress.setGeometry(QtCore.QRect(60, 280, 191, 131))
        self.frame_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_progress.setObjectName("frame_progress")
        self.label_progress = QtWidgets.QLabel(self.frame_progress)
        self.label_progress.setGeometry(QtCore.QRect(0, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_progress.setFont(font)
        self.label_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progress.setObjectName("label_progress")
        self.progressBar = QtWidgets.QProgressBar(self.frame_progress)
        self.progressBar.setGeometry(QtCore.QRect(20, 60, 171, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.frame_time = QtWidgets.QFrame(self.centralwidget)
        self.frame_time.setGeometry(QtCore.QRect(1070, 10, 201, 61))
        self.frame_time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_time.setObjectName("frame_time")
        self.label_time1 = QtWidgets.QLabel(self.frame_time)
        self.label_time1.setGeometry(QtCore.QRect(0, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_time1.setFont(font)
        self.label_time1.setObjectName("label_time1")
        self.label_time2 = QtWidgets.QLabel(self.frame_time)
        self.label_time2.setGeometry(QtCore.QRect(0, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_time2.setFont(font)
        self.label_time2.setObjectName("label_time2")
        self.label_clock1 = QtWidgets.QLabel(self.frame_time)
        self.label_clock1.setGeometry(QtCore.QRect(120, 0, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_clock1.setFont(font)
        self.label_clock1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clock1.setObjectName("label_clock1")
        self.label_clock2 = QtWidgets.QLabel(self.frame_time)
        self.label_clock2.setGeometry(QtCore.QRect(120, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_clock2.setFont(font)
        self.label_clock2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clock2.setObjectName("label_clock2")
        self.frame_raw = QtWidgets.QFrame(self.centralwidget)
        self.frame_raw.setGeometry(QtCore.QRect(1050, 70, 261, 791))
        self.frame_raw.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_raw.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_raw.setObjectName("frame_raw")
        self.frame_raw_basic = QtWidgets.QFrame(self.frame_raw)
        self.frame_raw_basic.setGeometry(QtCore.QRect(0, 240, 261, 321))
        self.frame_raw_basic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_raw_basic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_raw_basic.setObjectName("frame_raw_basic")
        self.label_C = ClickableLabel(self.frame_raw_basic)
        self.label_C.setGeometry(QtCore.QRect(40, 140, 50, 87))
        self.label_C.setText("")
        self.label_C.setPixmap(QtGui.QPixmap(self.current_game.path + '/c.png'))
        self.label_C.setScaledContents(True)
        self.label_C.setObjectName("label_C")
        self.label_F = ClickableLabel(self.frame_raw_basic)
        self.label_F.setGeometry(QtCore.QRect(150, 230, 50, 87))
        self.label_F.setText("")
        self.label_F.setPixmap(QtGui.QPixmap(self.current_game.path + '/f.png'))
        self.label_F.setScaledContents(True)
        self.label_F.setObjectName("label_F")
        self.label_A = ClickableLabel(self.frame_raw_basic)
        self.label_A.setGeometry(QtCore.QRect(40, 50, 50, 87))
        self.label_A.setText("")
        self.label_A.setPixmap(QtGui.QPixmap(self.current_game.path + '/a.png'))
        self.label_A.setScaledContents(True)
        self.label_A.setObjectName("label_A")
        self.label_B = ClickableLabel(self.frame_raw_basic)
        self.label_B.setGeometry(QtCore.QRect(150, 50, 50, 87))
        self.label_B.setText("")
        self.label_B.setPixmap(QtGui.QPixmap(self.current_game.path + '/b.png'))
        self.label_B.setScaledContents(True)
        self.label_B.setObjectName("label_B")
        self.label_D = ClickableLabel(self.frame_raw_basic)
        self.label_D.setGeometry(QtCore.QRect(150, 140, 50, 87))
        self.label_D.setText("")
        self.label_D.setPixmap(QtGui.QPixmap(self.current_game.path + '/d.png'))
        self.label_D.setScaledContents(True)
        self.label_D.setObjectName("label_D")
        self.label_E = ClickableLabel(self.frame_raw_basic)
        self.label_E.setGeometry(QtCore.QRect(40, 230, 50, 87))
        self.label_E.setText("")
        self.label_E.setPixmap(QtGui.QPixmap(self.current_game.path + '/e.png'))
        self.label_E.setScaledContents(True)
        self.label_E.setObjectName("label_E")
        self.label_basic = QtWidgets.QLabel(self.frame_raw_basic)
        self.label_basic.setGeometry(QtCore.QRect(95, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_basic.setFont(font)
        #self.label_basic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_basic.setObjectName("label_basic")
        self.frame_raw_add = QtWidgets.QFrame(self.frame_raw)
        self.frame_raw_add.setGeometry(QtCore.QRect(0, 560, 261, 301))
        self.frame_raw_add.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_raw_add.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_raw_add.setObjectName("frame_raw_add")
        self.label_N1 = ClickableLabel(self.frame_raw_add)
        self.label_N1.setGeometry(QtCore.QRect(40, 40, 50, 87))
        self.label_N1.setText("")
        self.label_N1.setPixmap(QtGui.QPixmap(self.current_game.path + '/n1.png'))
        self.label_N1.setScaledContents(True)
        self.label_N1.setObjectName("label_N1")
        self.label_N3 = ClickableLabel(self.frame_raw_add)
        self.label_N3.setGeometry(QtCore.QRect(40, 130, 50, 87))
        self.label_N3.setText("")
        self.label_N3.setPixmap(QtGui.QPixmap(self.current_game.path + '/n3.png'))
        self.label_N3.setScaledContents(True)
        self.label_N3.setObjectName("label_N3")
        self.label_N2 = ClickableLabel(self.frame_raw_add)
        self.label_N2.setGeometry(QtCore.QRect(150, 40, 50, 87))
        self.label_N2.setText("")
        self.label_N2.setPixmap(QtGui.QPixmap(self.current_game.path + '/n2.png'))
        self.label_N2.setScaledContents(True)
        self.label_N2.setObjectName("label_N2")
        self.label_N4 = ClickableLabel(self.frame_raw_add)
        self.label_N4.setGeometry(QtCore.QRect(150, 130, 50, 87))
        self.label_N4.setText("")
        self.label_N4.setPixmap(QtGui.QPixmap(self.current_game.path + '/n4.png'))
        self.label_N4.setScaledContents(True)
        self.label_N4.setObjectName("label_N4")
        # self.label_N5 = ClickableLabel(self.frame_raw_add)
        # self.label_N5.setGeometry(QtCore.QRect(40, 220, 50, 87))
        # self.label_N5.setText("")
        # self.label_N5.setPixmap(QtGui.QPixmap(self.current_game.path + '/n5.png'))
        # self.label_N5.setScaledContents(True)
        # self.label_N5.setObjectName("label_N5")
        # self.label_N6 = ClickableLabel(self.frame_raw_add)
        # self.label_N6.setGeometry(QtCore.QRect(150, 220, 50, 87))
        # self.label_N6.setText("")
        # self.label_N6.setPixmap(QtGui.QPixmap(self.current_game.path + '/n6.png'))
        # self.label_N6.setScaledContents(True)
        # self.label_N6.setObjectName("label_N6")
        self.label_add = QtWidgets.QLabel(self.frame_raw_add)
        self.label_add.setGeometry(QtCore.QRect(80, 0, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_add.setFont(font)
        #self.label_add.setAlignment(QtCore.Qt.AlignCenter)
        self.label_add.setObjectName("label_add")
        self.frame_active = QtWidgets.QFrame(self.frame_raw)
        self.frame_active.setGeometry(QtCore.QRect(0, 0, 261, 251))
        self.frame_active.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_active.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_active.setObjectName("frame_active")
        self.label_active = QtWidgets.QLabel(self.frame_active)
        self.label_active.setGeometry(QtCore.QRect(95, 10, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_active.setFont(font)
        #self.label_active.setAlignment(QtCore.Qt.AlignCenter)
        self.label_active.setObjectName("label_active")
        # self.label_raw_main = QtWidgets.QLabel(self.frame_active)
        # self.label_raw_main.setGeometry(QtCore.QRect(90, 40, 71, 81))
        # self.label_raw_main.setText("")
        # self.label_raw_main.setPixmap(QtGui.QPixmap("a.png"))
        # self.label_raw_main.setScaledContents(True)
        # self.label_raw_main.setObjectName("label_raw_main")
        self.button_left = QtWidgets.QPushButton(self.frame_active)
        self.button_left.setGeometry(QtCore.QRect(20, 210, 91, 31))
        self.button_left.setObjectName("button_left")
        self.button_right = QtWidgets.QPushButton(self.frame_active)
        self.button_right.setGeometry(QtCore.QRect(140, 210, 91, 31))
        self.button_right.setObjectName("button_right")
        self.frame_patent = QtWidgets.QFrame(self.centralwidget)
        self.frame_patent.setGeometry(QtCore.QRect(310, 70, 721, 761))
        self.frame_patent.setAutoFillBackground(False)
        self.frame_patent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_patent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_patent.setObjectName("frame_patent")
        self.patent = QtWidgets.QLabel(self.frame_patent)
        self.patent.setGeometry(QtCore.QRect(0, 0, 721, 761))
        self.patent.setText("")
        self.patent.setPixmap(QtGui.QPixmap("b.png"))
        self.patent.setScaledContents(True)
        self.patent.setObjectName("patent")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1340, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuCreators = QtWidgets.QMenu(self.menubar)
        self.menuCreators.setObjectName("menuCreators")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCreate_copy = QtWidgets.QAction(MainWindow)
        self.actionCreate_copy.setObjectName("actionCreate_copy")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionMade_by = QtWidgets.QAction(MainWindow)
        self.actionMade_by.setObjectName("actionMade_by")
        self.actionPogU = QtWidgets.QAction(MainWindow)
        self.actionPogU.setObjectName("actionPogU")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCreate_copy)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuCreators.addAction(self.actionPogU)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuCreators.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Весь новый код только ниже! -------------------------------

        self.progressBar.setValue(0)

        # Droppable label, можно заметить при перетягивании сыринки патент готов к дропу
        # Но не прописано нормальное действие по дропу, возникли трудности
        self.patent = DropLabel(self.frame_patent)
        self.patent.setGeometry(QtCore.QRect(0, 0, 721, 771))
        self.patent.setText("")
        self.patent.setPixmap(QtGui.QPixmap("patent.png"))
        self.patent.setScaledContents(True)
        self.patent.setOpenExternalLinks(False)
        self.patent.setObjectName("patent")

        # DRAG (only) raw main
        self.label_raw_main = DraggableLabel(self.frame_active)
        self.label_raw_main.setGeometry(QtCore.QRect(75, 40, 105, 176))
        self.label_raw_main.setText("")
        self.label_raw_main.setAlignment(Qt.AlignCenter)
        self.label_raw_main.setPixmap(QtGui.QPixmap("a.png"))
        self.label_raw_main.setScaledContents(True)
        self.label_raw_main.setObjectName("label_raw_main")

        # Обновление выбранного сырья при нажатии
        self.label_A.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/a.png'))
        self.label_B.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/b.png'))
        self.label_C.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/c.png'))
        self.label_D.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/d.png'))
        self.label_E.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/e.png'))
        self.label_F.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/f.png'))
        self.label_N1.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/n1.png'))
        self.label_N2.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/n2.png'))
        self.label_N3.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/n3.png'))
        self.label_N4.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/n4.png'))
        # self.label_N5.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/n5.png'))
        # self.label_N6.clicked.connect(lambda: self.update_raw_main_image(self.current_game.path + '/n6.png'))



        # Добавление кнопки Accept вручную
        self.button_accept = QtWidgets.QPushButton(self.centralwidget)
        self.button_accept.setGeometry(QtCore.QRect(55, 190, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.button_accept.setFont(font)
        self.button_accept.setObjectName("button_accept")
        self.button_accept.setText("Accept ✔")

        # Настройка функций на нажатие кнопок
        self.button_right.clicked.connect(self.turn_right)
        self.button_left.clicked.connect(self.turn_left)
        self.button_rules.clicked.connect(self.show_window_rules)
        self.button_accept.clicked.connect(self.change_patent)
        self.button_undo.clicked.connect(self.undo_action)
        self.button_redo.clicked.connect(self.redo_action)
        self.button_clear.clicked.connect(self.clear_action)

        # Настройка срабатываний shortcut'ов
        self.actionUndo.triggered.connect(lambda: self.undo_action())
        self.actionRedo.triggered.connect(lambda: self.redo_action())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PatentMaker 1.0"))
        self.button_rules.setText(_translate("MainWindow", "Rules"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
        self.button_undo.setText(_translate("MainWindow", "Undo ↶"))
        self.button_redo.setText(_translate("MainWindow", "Redo ↷"))
        self.patentbox.setItemText(0, _translate("MainWindow", self.game1.name))
        self.patentbox.setItemText(1, _translate("MainWindow", self.game2.name))
        self.label_lvl.setText(_translate("MainWindow", "Required level"))
        self.name_patent.setText(_translate("MainWindow", self.current_game.name))
        self.label_difficulty.setText(_translate("MainWindow", "Difficulty: " + self.current_game.difficulty))
        self.label_progress.setText(_translate("MainWindow", "Progress"))
        self.label_time1.setText(_translate("MainWindow", " Времени прошло:"))
        self.label_time2.setText(_translate("MainWindow", " Времени осталось:"))
        self.label_clock1.setText(_translate("MainWindow", "0:00:00"))
        self.label_clock2.setText(_translate("MainWindow", "0:00:00"))
        self.label_basic.setText(_translate("MainWindow", "Basic"))
        self.label_add.setText(_translate("MainWindow", "Additional"))
        self.label_active.setText(_translate("MainWindow", "Active"))
        self.button_left.setText(_translate("MainWindow", "Left"))
        self.button_right.setText(_translate("MainWindow", "Right"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuCreators.setTitle(_translate("MainWindow", "Creators"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCreate_copy.setText(_translate("MainWindow", "Create copy"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use?"))
        self.actionMade_by.setText(_translate("MainWindow", "Creators"))
        self.actionPogU.setText(_translate("MainWindow", "PogU"))

    def __init__(self):
        self.game1 = Game(1, 'Championat 28.02.2020', 'Easy')
        self.game2 = Game(2, "Training 27.02.2020", "Medium")
        self.current_game = self.game1
        self.image_raw_main = QImage(self.current_game.path + '/a.png')  # Переменная для текущего изображения в выбранном сырье
        self.angle = 0
        self.data = {self.game1.name: self.game1, self.game2.name: self.game2}
        self.visible_raws = []
        self.invisible_raws = []
        self.flag_clear = False
        self.current_required_level = 100  # пока что так, потом обработать, что без кнопки ассерт ничего не начинается
        # self.time_remaining_secs = 0 # надо, чтобы запустить (иначе драг лейбл крашнется, тк не найдет этого поля)
        # self.secs_passed = 0 # аналогично




    #timer block
    def popupFail(self):
        msg = QMessageBox()
        msg.setWindowTitle('Time is over!')
        msg.setText('Время закончилось! Патентная палата закрывается, но вы можете продлить время её работы еще на '
                    '10 минут. \nYes - Добавить 10 минут. \nReset - Удалить все наработки. \n'
                    'Ignore - Установить безлимитное время разработки.\n\nПримечание:\nПри возникновении неполадок в '
                    'работе программы требуется нажать "Enter"')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Reset | QMessageBox.Ignore)
        msg.setDetailedText('При выборе безлимитного времени в правом верхнем углу появится текущее время. Чтобы '
                            'вернуться к разработке на время, требуется выбрать параметры и нажать кнопку "Accept".')
        msg.setDefaultButton(QMessageBox.Yes)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()


    def popup_button(self, el):
        time_click = QTime.currentTime()
        secs_click = self.timeToSec(time_click.toString())
        difference = secs_click - self.secs_fail
        self.timer.stop()
        self.secs_start += difference  #корректировка времени пока пользователь "думал над кликом"

        button = el.text()
        if button == 'Ignore':
            self.label_time2.setText(" Текущее время")
            self.timer.timeout.connect(self.showCurrentTime)
            self.timer.start(1000)
        elif button == 'Reset':
            self.clear_action()
            self.label_clock1.setText("0:00:00")
            self.label_clock2.setText("0:00:00")
        elif button == '&Yes':
            self.time_remaining_secs += 10 * 60
            self.timer.timeout.connect(self.showTime)
            self.timer.start(1000)


    def showCurrentTime(self):
        time = QTime.currentTime()
        text = time.toString()
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:5] + ' ' + text[6:]
        self.label_clock2.setText(text)


    def timeToSec(self, text_time):
        text_time = [int(el) for el in text_time.split(':')]
        time_in_sec = text_time[0]*60*60 + text_time[1]*60 + text_time[2]
        return time_in_sec


    def fromSecToTime(self, secs):
        hours = secs // 3600
        secs = secs - (hours * 3600)
        #hours = self.addzero(hours)

        minutes = secs // 60
        minutes = self.addzero(minutes)

        sec = secs % 60
        sec = self.addzero(sec)

        newtime = str(hours) + ':' + minutes + ':' + sec
        return newtime


    def addzero(self, number):
        if number < 10:
            number = '0' + str(number)
        else:
            number = str(number)
        return number


    def showTime(self):
        time = QTime.currentTime()
        text = time.toString()
        self.secs_passed = self.timeToSec(text) - self.secs_start
        time_passed = self.fromSecToTime(self.secs_passed)
        time_remaining = self.fromSecToTime(self.time_remaining_secs - self.secs_passed)
        self.label_clock1.setText(time_passed)
        self.label_clock2.setText(time_remaining)
        if self.time_remaining_secs - self.secs_passed == 0:
            time_fail = QTime.currentTime()
            self.secs_fail = self.timeToSec(time_fail.toString())
            self.popupFail()

    # # # # # # # # # # # # # # # # # #

    # Поворот сырья направо
    def turn_right(self):
        self.angle += 60
        t = QTransform().rotate(self.angle)
        self.label_raw_main.setPixmap(QPixmap(self.image_raw_main).transformed(t))
        if self.angle % 180 == 60:
            self.label_raw_main.setGeometry(QtCore.QRect(30, 40, 210, 176))
        elif self.angle % 180 == 120:
            self.label_raw_main.setGeometry(QtCore.QRect(30, 40, 210, 176))
        else:
            self.label_raw_main.setGeometry(QtCore.QRect(75, 40, 105, 176))
        # self.image_raw_main = QPixmap(self.image_raw_main).transformed(t)
        # if (self.angle - 90) % 180 == 0:
        #     self.label_raw_main.setGeometry(QtCore.QRect(75, 60, 87, 50))
        # elif self.angle % 180 == 0:
        #     self.label_raw_main.setGeometry(QtCore.QRect(90, 40, 50, 87))
        # self.label_raw_main.setPixmap(self.image_raw_main)

    # Поворот сырья налево
    def turn_left(self):
        self.angle -= 60
        t = QTransform().rotate(self.angle)
        if self.angle % 180 == 60:
            self.label_raw_main.setGeometry(QtCore.QRect(30, 40, 210, 176))
        elif self.angle % 180 == 120:
            self.label_raw_main.setGeometry(QtCore.QRect(30, 40, 210, 176))
        else:
            self.label_raw_main.setGeometry(QtCore.QRect(75, 40, 105, 176))
        self.label_raw_main.setPixmap(QPixmap(self.image_raw_main).transformed(t))



        # self.image_raw_main = QPixmap(self.image_raw_main).transformed(t)
        # if (self.angle - 90) % 180 == 0:
        #     self.label_raw_main.setGeometry(QtCore.QRect(75, 60, 87, 50))
        # elif self.angle % 180 == 0:
        #     self.label_raw_main.setGeometry(QtCore.QRect(90, 40, 50, 87))
        # self.label_raw_main.setPixmap(self.image_raw_main)

    # Обновление изображения выбранного сырья
    def update_raw_main_image(self, path):
        self.image_raw_main = QImage(path)
        self.label_raw_main.setPixmap(QPixmap(self.image_raw_main))
        self.label_raw_main.setGeometry(QtCore.QRect(75, 40, 105, 176))
        self.angle = 0

    # Показ окна правил
    def show_window_rules(self):
        self.window = Window_rules(self.current_game)  # file Rules.py
        self.window.show()

    # Функционал кнопки Accept
    def change_patent(self):
        self.current_game = self.data[self.patentbox.currentText()]
        self.image_new_patent = QImage(self.current_game.path + '/patent.png')
        self.patent.setPixmap(QPixmap(self.image_new_patent))
        self.name_patent.setText(self.current_game.name)
        self.current_required_level = self.spin_lvl.value()
        self.label_difficulty.setText("Difficulty: " + self.current_game.difficulty)
        self.label_A.setPixmap(QPixmap(QImage(self.current_game.path + '/a.png')))
        self.label_B.setPixmap(QPixmap(QImage(self.current_game.path + '/b.png')))
        self.label_C.setPixmap(QPixmap(QImage(self.current_game.path + '/c.png')))
        self.label_D.setPixmap(QPixmap(QImage(self.current_game.path + '/d.png')))
        self.label_E.setPixmap(QPixmap(QImage(self.current_game.path + '/e.png')))
        self.label_F.setPixmap(QPixmap(QImage(self.current_game.path + '/f.png')))
        self.label_N1.setPixmap(QPixmap(QImage(self.current_game.path + '/n1.png')))
        self.label_N2.setPixmap(QPixmap(QImage(self.current_game.path + '/n2.png')))
        self.label_N3.setPixmap(QPixmap(QImage(self.current_game.path + '/n3.png')))
        self.label_N4.setPixmap(QPixmap(QImage(self.current_game.path + '/n4.png')))
        # self.label_N5.setPixmap(QPixmap(QImage(self.current_game.path + '/n5.png')))
        # self.label_N6.setPixmap(QPixmap(QImage(self.current_game.path + '/n6.png')))
        self.clear_action()
        # start time
        self.time_start = QTime.currentTime()
        self.text_start = self.time_start.toString()
        self.secs_start = self.timeToSec(self.text_start)
        self.time_remaining_secs = 30*60  # время на изготовку патента в секундах
        #timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.label_time2.setText(' Времени осталось:') #надо, просто надо


    def undo_action(self):
        if not self.flag_clear:
            try:
                self.invisible_raws.append(self.visible_raws[-1])
                self.visible_raws.pop(-1).setParent(None)
            except IndexError:
                print('Нечего Undить')  # TODO Окно / надпись с сообщением о невозможности Undo
        if self.flag_clear:
            try:
                for i in range(len(self.clear_raws)):
                    self.visible_raws.append(self.clear_raws[i])
                self.clear_raws.clear()
                self.show_current_raws()
                self.flag_clear = False
            except:
                pass
        self.progress()

    def redo_action(self):
        try:
            self.visible_raws.append(self.invisible_raws[-1])
            self.invisible_raws.pop(-1)
            self.show_current_raws()
        except IndexError:
            print('Нечего Redить')  # TODO Окно / надпись с сообщением о невозможности Redo
        self.progress()

    def clear_action(self):
        self.clear_raws = [el for el in self.visible_raws]
        self.flag_clear = True
        for elem in self.visible_raws:
            elem.setParent(None)
        self.visible_raws.clear()
        self.invisible_raws.clear()
        self.progress()
        # t = QTransform().rotate(30)
        # # self.pixmap = (QPixmap(QImage(self.current_game.path + '/a.png')).transformed(t))
        # # self.pixmap.save(self.current_game.path+'/a.png')
        # self.pixmap = (QPixmap(QImage(self.current_game.path + '/b.png')).transformed(t))
        # self.pixmap.save(self.current_game.path + '/b.png')
        # self.pixmap = (QPixmap(QImage(self.current_game.path + '/c.png')).transformed(t))
        # self.pixmap.save(self.current_game.path + '/c.png')
        # self.pixmap = (QPixmap(QImage(self.current_game.path + '/d.png')).transformed(QTransform().rotate(-30)))
        # self.pixmap.save(self.current_game.path + '/d.png')
        # self.pixmap = (QPixmap(QImage(self.current_game.path + '/e.png')).transformed(t))
        # self.pixmap.save(self.current_game.path + '/e.png')
        # self.pixmap = (QPixmap(QImage(self.current_game.path + '/f.png')).transformed(t))
        # self.pixmap.save(self.current_game.path + '/f.png')

    def show_current_raws(self):
        for elem in self.visible_raws:
            elem.setParent(self.frame_patent)
            elem.show()

    def progress(self):
        try:
            self.progressBar.setValue(int(2 * len(self.visible_raws) / self.current_required_level * 100))  # 2 * длину,
        # т.к. каждая сыринка это 2 уровня обычно
        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Level must be more than zero. Level was set to 50 by default.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
            self.current_required_level = 50
            self.progressBar.setValue(int(2 * len(self.visible_raws) / self.current_required_level * 100))

    def delete_raw(self):
        pass


class DraggableLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super(QtWidgets.QLabel, self).__init__(parent)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            global drag_start_position
            drag_start_position = event.pos()
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        # перетягивание на левую кнопку мыши + установка минимальной длины для начала перетягивания (4 пикселя)
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < 2:
            global correction
            correction = event.pos() - self.drag_start_position
        drag = QDrag(self)

        # QMimeData() - класс для хранения данных любого типа во время перетягивания
        mimedata = QMimeData()

        mimedata.setImageData(self.pixmap().toImage())  # изображение в качестве данных, которое потом можно будет дропнуть

        drag.setMimeData(mimedata)

        t = QTransform().rotate(ui.angle)
        pixmap = QPixmap(ui.image_raw_main.transformed(t))  #Все исправление в 3 строчки
        pixmap = pixmap.scaled(self.size())


        painter = QPainter(pixmap)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        painter.drawPixmap(self.rect(), self.grab())
        painter.end()

        drag.setPixmap(pixmap)  #именно здесь происходит прорисовка изображения, работает и без QPainter, но
        #Но он помогает восстановить качество картинки, по сути перерисовывая новую картинку поверх старой,
        #повреждено из за метода scaled. Картинка из этой строчки по сути является фоном, и именно в ней и была проблема
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)




        #другие способы прозрачности изображения (возможно пригодится в будущем):
        # способ два три четыре
        # painter.setRenderHint(QPainter.Antialiasing, True)
        # painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        # painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        # painter.setPen(QPen(QBrush(Qt.transparent), 0))
        # painter.setBrush(QBrush(Qt.transparent))
        # способ пять
        # pixmap.setMask(pixmap.createHeuristicMask())
        # уже не помню откуда это
        # painter.fillRect(pixmap.rect(), QColor(0, 0, 0, 0));


class DropLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    # def dragMoveEvent(self, event):
    #     print(ui.time_remaining_secs - ui.secs_passed)
    #     if ui.time_remaining_secs - ui.secs_passed == 1798:
    #         QtTest.QTest.mouseRelease(event.source(), Qt.LeftButton)

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            x = event.source().size().width()
            y = event.source().size().height()

            position = event.pos() - drag_start_position - correction

            # ui.frame_progress.move(event.pos())
            # ui.frame_progress.raise_()

            self.new_raw = Deletable_Draggable_DroppableLabel(ui.frame_patent)
            self.new_raw.setGeometry(QtCore.QRect(position.x(), position.y(), x, y)) #POGU 2


            # if ui.angle % 180 ==  60:
            #     self.new_raw.setGeometry(QtCore.QRect(position.x(), position.y(), 210, 176))
            # elif ui.angle % 180 == 120:
            #     self.new_raw.setGeometry(QtCore.QRect(position.x(), position.y(), 210, 176))
            # else:
            #     self.new_raw.setGeometry(QtCore.QRect(position.x(), position.y(), 105, 176))

           # t = QTransform().rotate(ui.angle)

            self.new_raw.setPixmap(QPixmap(event.mimeData().imageData()))
            self.new_raw.setScaledContents(True)

            # self.new_raw.show()

            ui.visible_raws.append(self.new_raw)
            ui.show_current_raws()
            ui.progress()

            # self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))


class Deletable_Draggable_DroppableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.show()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.RightButton:
            self.clicked.emit()
            QtWidgets.QLabel.mousePressEvent(self, QMouseEvent)
            self.setParent(None)
            n = ui.visible_raws.index(self)
            ui.invisible_raws.append(ui.visible_raws[n])
            ui.visible_raws.pop(n).setParent(None)
            ui.progressBar.setValue(int(2 * len(ui.visible_raws) / ui.current_required_level * 100))
        if QMouseEvent.button() == Qt.LeftButton:
            global drag_start_position
            drag_start_position = QMouseEvent.pos()
            self.drag_start_position = QMouseEvent.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < 2:
            global correction
            correction = event.pos() - self.drag_start_position
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setImageData(self.pixmap().toImage())  # изображение в качестве данных, которое потом можно будет дропнуть

        drag.setMimeData(mimedata)
        #t = QTransform().rotate(ui.angle)
        pixmap = QPixmap(drag.mimeData().imageData())  # POGU
        pixmap = pixmap.scaled(self.size())

        painter = QPainter(pixmap)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()

        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    # def rawAngle(self):
    #     if ui.angle % 180 == 60:
    #         self.new_raw.setGeometry(QtCore.QRect(self.position.x(), self.position.y(), 210, 176))
    #     elif ui.angle % 180 == 120:
    #         self.new_raw.setGeometry(QtCore.QRect(self.position.x(), self.position.y(), 210, 176))
    #     else:
    #         self.new_raw.setGeometry(QtCore.QRect(self.position.x(), self.position.y(), 105, 176))


    def dropEvent(self, event):
        if event.mimeData().hasImage():
            x = event.source().size().width()
            y = event.source().size().height()
            if str(type(event.source())) == "<class '__main__.DraggableLabel'>": #оставил так, тк в будущем есть идеи по другому отклику на драг уже дропнутых сыринок
                position = event.pos() + self.pos() - drag_start_position - correction
                self.new_raw = Deletable_Draggable_DroppableLabel(ui.frame_patent)
                self.new_raw.setGeometry(QtCore.QRect(position.x(), position.y(), x, y))
                # t = QTransform().rotate(ui.angle)
                self.new_raw.setPixmap(QPixmap(event.mimeData().imageData()))
                self.new_raw.setScaledContents(True)
            elif str(type(event.source())) == "<class '__main__.Deletable_Draggable_DroppableLabel'>":
                position = event.pos() + self.pos() - drag_start_position - correction
                self.new_raw = Deletable_Draggable_DroppableLabel(ui.frame_patent)
                self.new_raw.setGeometry(QtCore.QRect(position.x(), position.y(), x, y))
                # t = QTransform().rotate(ui.angle)
                self.new_raw.setPixmap(QPixmap(event.mimeData().imageData()))
                self.new_raw.setScaledContents(True)
            ui.visible_raws.append(self.new_raw)
            ui.show_current_raws()
            ui.progress()


            # ui.frame_progress.move(event.pos())
            # ui.frame_progress.raise_()
            # вариант решения без глобал переменных, но там чето много контролить надо, проблема осталась тут с дропом делдрагдроп на обычный патент, можешь ознакомиться
            # конечно она решалась с помощью метода event.target() в в дроп лейбле для патента отдельно, но там тоже нужно прописывать свои корректировки как тут ниже
            # if str(type(event.source())) == "<class '__main__.DraggableLabel'>":
            #     self.position = event.pos() - ui.label_raw_main.drag_start_position - ui.label_raw_main.correction
            #     self.new_raw = Deletable_Draggable_DroppableLabel(ui.frame_patent)
            #     self.rawAngle()
            #     t = QTransform().rotate(ui.angle)
            #     self.new_raw.setPixmap(QPixmap(ui.image_raw_main).transformed(t))
            #     self.new_raw.setScaledContents(True)
            #
            # elif str(type(event.source())) == "<class '__main__.Deletable_Draggable_DroppableLabel'>":
            #     self.position = event.pos() + self.pos() - drag_start_position2 - correction2
            #     self.new_raw = Deletable_Draggable_DroppableLabel(ui.frame_patent)
            #     self.rawAngle()
            #     t = QTransform().rotate(ui.angle)
            #
            #     self.new_raw.setPixmap(QPixmap(ui.image_raw_main).transformed(t))
            #     self.new_raw.setScaledContents(True)


if __name__ == "__main__":
    import sys



    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    #lala

#где-то глубоко возможно есть баг связанный с переходом времени через 0:00