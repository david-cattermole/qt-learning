"""
https://stackoverflow.com/questions/4838890/python-pyqt-popup-window
"""

import sys
# from PyQt4.Qt import *
import Qt as Qt
import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets


class MyPopup(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QtWidgets.QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        QtWidgets.QMainWindow.__init__(self, *args)
        self.cw = QtWidgets.QWidget(self)
        self.setCentralWidget(self.cw)
        self.btn1 = QtWidgets.QPushButton("Click me", self.cw)
        self.btn1.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.connect(self.btn1, QtCore.SIGNAL("clicked()"), self.doit)
        self.w = None

    def doit(self):
        print("Opening a new popup window...")
        self.w = MyPopup()
        self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
        self.w.show()


class App(QtWidgets.QApplication):
    def __init__(self, *args):
        QtWidgets.QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.connect(self, QtCore.SIGNAL("lastWindowClosed()"), self.byebye)
        self.main.show()

    def byebye(self):
        self.exit(0)


def main(args):
    global app
    app = App(args)
    app.exec_()


if __name__ == "__main__":
    main(sys.argv)
