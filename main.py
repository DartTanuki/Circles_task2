import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import random
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        print('ok')
        self.setWindowTitle('Задача 2')
        self.setGeometry(300, 300, 500, 400)
        self.unitui()

    def unitui(self):
        self.btn.clicked.connect(self.action)

    def action(self):
        print('Button Pressed')
        self.repaint()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        x = random.randint(50, 350)
        y = random.randint(50, 250)
        radius = random.randint(1, 150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())