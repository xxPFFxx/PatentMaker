from PyQt5 import QtWidgets, QtCore


class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, QMouseEvent)
