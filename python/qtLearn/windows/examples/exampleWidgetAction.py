"""
https://stackoverflow.com/questions/9076332/qt-pyqt-how-do-i-create-a-drop-down-widget-such-as-a-qlabel-qtextbrowser-etc
"""
import sys
from Qt import QtCore
from Qt import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        layout = QtWidgets.QHBoxLayout(self)

        self.button = QtWidgets.QToolButton(self)
        self.button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.button.setMenu(QtWidgets.QMenu(self.button))

        self.textBox = QtWidgets.QTextBrowser(self)
        action1 = QtWidgets.QWidgetAction(self.button)
        action1.setDefaultWidget(self.textBox)

        self.textLine = QtWidgets.QLineEdit(self)
        action2 = QtWidgets.QWidgetAction(self.button)
        action2.setDefaultWidget(self.textLine)

        self.button.menu().addAction(action1)
        self.button.menu().addAction(action2)
        layout.addWidget(self.button)


def main(argv):
    app = QtWidgets.QApplication(argv)
    window = Window()
    window.resize(100, 60)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)