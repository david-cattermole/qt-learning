"""

Usage:
>>> import qtTests.mayaBaseWindow
>>> reload(qtTests.mayaBaseWindow)
>>> qtTests.mayaBaseWindow.main()

>>> import sys
>>> import os.path
>>> sys.path.insert(0,  os.path.join(os.environ['MAYA_LOCATION'], 'devkit', 'pythonScripts' ) )
>>> import widgetHierarchy
>>> w = widgetHierarchy.main()
"""

from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2 import __version__
    from shiboken2 import wrapInstance
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide import __version__
    from shiboken import wrapInstance

import qtTests.ui_baseWindow
reload(qtTests.ui_baseWindow)

def getMayaMainWindow():
    mainWindowPtr = omui.MQtUtil.mainWindow()
    mainWindow = wrapInstance(long(mainWindowPtr), QWidget)
    return mainWindow


def findWidget(name, clsTyp):
    ptr = omui.MQtUtil.findControl(name)
    widget = None
    if ptr:
        widget = wrapInstance(long(ptr), clsTyp)
    return widget


class MayaBaseWindow(MayaQWidgetBaseMixin,
                     QMainWindow,
                     qtTests.ui_baseWindow.Ui_MainWindow):
    def __init__(self, name=None, rootWidget=None, subLayout=None, *args, **kwargs):
        # print 'MayaBaseWindow:', self.__class__
        super(MayaBaseWindow, self).__init__(*args, **kwargs)

        # Destroy this widget when closed. Otherwise it will stay around.
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        # Determine root widget to scan
        mayaWin = getMayaMainWindow()
        if rootWidget != None:
            self.rootWidget = rootWidget
        else:
            self.rootWidget = mayaWin

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


def main(show=True):
    name = 'MayaBaseWindow'
    window = findWidget(name, QWidget)
    if window:
        window.close()  # or .deleteLater() ?
    ui = createMayaBaseWindow(name=name)
    if show:
        ui.show()
    return ui
