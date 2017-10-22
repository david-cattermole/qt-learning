"""
https://stackoverflow.com/questions/12041980/properly-positioning-popup-widgets-in-pyqt
"""
from Qt import QtGui
from Qt import QtCore
import sys


class Popup(QtGui.QWidget):
    def __init__(self, parent=None, widget=None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QGridLayout(self)
        button = QtGui.QPushButton("Very Interesting Text Popup. Here's an arrow   ^")
        layout.addWidget(button)
        self.move(widget.rect().bottomLeft())


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Hit this button to show a popup', self)
        self.button.clicked.connect(self.handleOpenDialog)
        self.button.move(250, 50)
        self.resize(600, 200)

    def handleOpenDialog(self):
        self.popup = Popup(self, self.button)
        self.popup.show()


# NOTE: Will not work (with PySide at least) unless implemented as 'new style'
# class. I.e inherit from object
class PopupDialogMixin(object):
    def makePopup(self, callWidget):
        """
        Turns the dialog into a popup dialog.
        callWidget is the widget responsible for calling the dialog (e.g. a toolbar button)
        """
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
        self.setObjectName('ImportDialog')

        # Move the dialog to the widget that called it
        point = callWidget.rect().bottomRight()
        global_point = callWidget.mapToGlobal(point)
        self.move(global_point - QtCore.QPoint(self.width(), 0))


class Popup2(QtGui.QWidget, PopupDialogMixin):
    def __init__(self, parent=None, widget=None):
        super(Popup2, self).__init__(parent)
        layout = QtGui.QGridLayout(self)
        button = QtGui.QPushButton("Very Interesting Text Popup. Here's an arrow   ^")
        layout.addWidget(button)


class Window2(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Hit this button to show a popup', self)
        self.button.clicked.connect(self.handleOpenDialog)
        self.button.move(250, 50)
        self.resize(600, 200)

    def handleOpenDialog(self):
        self.popup = Popup2(self, self.button)
        self.popup.makePopup(self)
        self.popup.show()


def main(argv):
    app = QtGui.QApplication(argv)
    win = Window2()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = main(sys.argv)
