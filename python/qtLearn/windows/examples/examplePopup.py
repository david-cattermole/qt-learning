"""
https://stackoverflow.com/questions/4838890/python-pyqt-popup-window
"""

import sys
from PyQt4.Qt import *


class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)


class MainWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.cw = QWidget(self)
        self.setCentralWidget(self.cw)
        self.btn1 = QPushButton("Click me", self.cw)
        self.btn1.setGeometry(QRect(0, 0, 100, 30))
        self.connect(self.btn1, SIGNAL("clicked()"), self.doit)
        self.w = None

    def doit(self):
        print "Opening a new popup window..."
        self.w = MyPopup()
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.show()


class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
        self.main.show()

    def byebye( self ):
        self.exit(0)


def main(args):
    global app
    app = App(args)
    app.exec_()


if __name__ == "__main__":
    main(sys.argv)
