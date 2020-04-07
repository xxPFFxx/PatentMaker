from PyQt5 import QtWidgets, QtCore


# Класс кликабельных label-ов для сыринок
class ClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, QMouseEvent)

# class DeletableLabel(QtWidgets.QLabel):
#     clicked = QtCore.pyqtSignal()
#
#     def mousePressEvent(self, QMouseEvent):
#         if QMouseEvent.button() == QtCore.Qt.LeftButton:
#             self.clicked.emit()
#             QtWidgets.QLabel.mousePressEvent(self, QMouseEvent)
#             self.setParent(None)

