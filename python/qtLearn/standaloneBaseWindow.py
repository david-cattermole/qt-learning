"""

Usage:
>>> import qtLearn.standaloneBaseWindow
>>> reload(qtLearn.standaloneBaseWindow)
>>> qtLearn.standaloneBaseWindow.main()
"""

import sys

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide import __version__
    from shiboken import wrapInstance
    # from PySide2.QtCore import *
    # from PySide2.QtGui import *
    # from PySide2.QtWidgets import *
    # from PySide2 import __version__
    # from shiboken2 import wrapInstance
except ImportError:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

import qtLearn.ui_baseWindow
reload(qtLearn.ui_baseWindow)


class StandaloneBaseWindow(QMainWindow,
                           qtLearn.ui_baseWindow.Ui_MainWindow):
    def __init__(self, name=None, subLayout=None, *args, **kwargs):
        super(StandaloneBaseWindow, self).__init__(*args, **kwargs)

        # Destroy this widget when closed. Otherwise it will stay around.
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        # Call the UI file contents.
        self.setupUi(self)
        if name:
            self.setObjectName(name)

        # self.createBtn.hide()
        self.applyBtn.hide()
        self.resetBtn.hide()
        self.helpBtn.hide()
        # self.closeBtn.hide()

        self.menubar.hide()
        self.progressBar.hide()

        if subLayout:
            self.subLayout = subLayout(parent=self.options)
        return


def main():
    name = 'StandaloneBaseWindow'
    app = QApplication(sys.argv)
    ui = StandaloneBaseWindow(name=name)
    ui.show()
    return sys.exit(app.exec_())


if __name__ == '__main__':
    main()
