"""
https://gist.github.com/justinfx/1951709
"""

import sys
import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.resize(300, 200)

    def showEvent(self, event):
        print('showEvent:', event)
        geom = self.frameGeometry()
        geom.moveCenter(QtWidgets.QCursor.pos())
        self.setGeometry(geom)
        super(Dialog, self).showEvent(event)

    def keyPressEvent(self, event):
        print('keyPressEvent:', event)
        if event.key() == QtCore.Qt.Key_Escape:
            self.hide()
            event.accepted()
        else:
            super(Dialog, self).keyPressEvent(event)


def main(argv):
    app = QtWidgets.QApplication(argv)

    d = Dialog()
    d.show()
    d.raise_()

    app.exec_()
