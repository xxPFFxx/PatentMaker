import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QImage
from PyQt5.QtCore import QMimeData, Qt, QRect

class DraggableLabel(QLabel):
    def __init__(self, parent, image):
        super(QLabel, self).__init__(parent)
        self.setPixmap(QPixmap(image))
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        # перетягивание на левую кнопку мыши + установка минимальной длины для начала перетягивания (4 пикселя)
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)

        # QMimeData() - класс для хранения данных любого типа во время перетягивания
        mimedata = QMimeData()

        mimedata.setImageData(
            self.pixmap().toImage())  # изображение в качестве данных, которое потом можно будет дропнуть

        drag.setMimeData(mimedata)

        pixmap = QPixmap(self.size())

        # painter - рисование изображения во время перетягивания
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()

        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)


class DropLabel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage():
            self.qpoint = str(event.pos())
            self.pos = self.qpoint[20:len(self.qpoint) - 1]
            self.x, self.y = self.pos.split(', ')
            self.x, self.y = int(self.x), int(self.y)  # достали координаты drop из объекта PyQt5.QtCore.QPoint(x, y)
            print("Координаты дропа:", self.x, self.y)


            # self.new_raw = QtWidgets.QLabel(Ui_MainWindow.centralwidget)
            # self.new_raw.setGeometry(QtCore.QRect(self.x, self.y, 71, 81))
            # self.new_raw.setPixmap(QtGui.QPixmap("a.png"))
            # self.new_raw.setScaledContents(True)
            # self.setPixmap(QPixmap.fromImage(QImage(event.mimeData().imageData())))
