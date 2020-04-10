from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


# Класс открывающихся правил при нажатии на кнопку Rules
class Window_rules(QWidget):
    def __init__(self, game):
        super(Window_rules, self).__init__()
        self.game = game
        self.setWindowTitle('Rules')
        self.label_rules = QtWidgets.QLabel(self)
        self.label_rules.setGeometry(QtCore.QRect(10, 10, 720, 960))
        self.label_rules.setText("")
        self.label_rules.setPixmap(QtGui.QPixmap(game.path + '/rules.png'))
        self.label_rules.setScaledContents(True)
