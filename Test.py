import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QLabel

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # if len(app.arguments()) < 2:
    #     sys.stderr.write("Usage: %s <image file> <overlay file>\n" % sys.argv[0])
    #     sys.exit(1)

    image = QImage('patent.png')
    if image.isNull():
        sys.stderr.write("Failed to read image: %s\n" % app.arguments()[1])
        sys.exit(1)

    overlay = QImage('a.png')
    if overlay.isNull():
        sys.stderr.write("Failed to read image: %s\n" % app.arguments()[2])
        sys.exit(1)

    # if overlay.size() > image.size():
    #     overlay = overlay.scaled(image.size(), Qt.KeepAspectRatio)

    painter = QPainter()
    painter.begin(image)
    painter.drawImage(100, 100, overlay)
    painter.end()

    label = QLabel()
    label.setPixmap(QPixmap.fromImage(image))
    label.show()

    sys.exit(app.exec_())