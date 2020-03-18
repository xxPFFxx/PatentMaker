from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

# Класс открывающихся правил при нажатии на кнопку Rules
class Window_rules(QWidget):
    def __init__(self):
        super(Window_rules, self).__init__()
        self.setWindowTitle('Rules')
        self.setMinimumWidth(200)
        self.setMinimumHeight(50)
        self.label_rules = QtWidgets.QLabel(self)
        self.label_rules.setGeometry(QtCore.QRect(10, 10, 521, 701))
        self.label_rules.setText("")
        self.label_rules.setPixmap(QtGui.QPixmap("rules.png"))



