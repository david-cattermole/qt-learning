"""
https://gist.github.com/justinfx/1951709
"""

import sys
from PyQt4 import QtCore, QtGui


class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.resize(300, 200)

    def showEvent(self, event):
        print 'showEvent:', event
        geom = self.frameGeometry()
        geom.moveCenter(QtGui.QCursor.pos())
        self.setGeometry(geom)
        super(Dialog, self).showEvent(event)

    def keyPressEvent(self, event):
        print 'keyPressEvent:', event
        if event.key() == QtCore.Qt.Key_Escape:
            self.hide()
            event.accept()
        else:
            super(Dialog, self).keyPressEvent(event)


def main(argv):
    app = QtGui.QApplication(argv)

    d = Dialog()
    d.show()
    d.raise_()

    app.exec_()
