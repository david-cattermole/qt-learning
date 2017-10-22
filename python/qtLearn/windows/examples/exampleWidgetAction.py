"""
https://stackoverflow.com/questions/9076332/qt-pyqt-how-do-i-create-a-drop-down-widget-such-as-a-qlabel-qtextbrowser-etc
"""
import sys
from Qt import QtCore
from Qt import QtGui


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        layout = QtGui.QHBoxLayout(self)

        self.button = QtGui.QToolButton(self)
        self.button.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.button.setMenu(QtGui.QMenu(self.button))

        self.textBox = QtGui.QTextBrowser(self)
        action1 = QtGui.QWidgetAction(self.button)
        action1.setDefaultWidget(self.textBox)

        self.textLine = QtGui.QLineEdit(self)
        action2 = QtGui.QWidgetAction(self.button)
        action2.setDefaultWidget(self.textLine)

        self.button.menu().addAction(action1)
        self.button.menu().addAction(action2)
        layout.addWidget(self.button)


def main(argv):
    app = QtGui.QApplication(argv)
    window = Window()
    window.resize(100, 60)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)