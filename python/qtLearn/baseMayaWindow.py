"""
The base window for usage inside Maya.
All windows inside Maya should sub-class from BaseMayaWindow.

Run the default MayaBaseWindow:
>>> import qtLearn.baseMayaWindow
>>> reload(qtLearn.baseMayaWindow)
>>> qtLearn.baseMayaWindow.create()

Using the :
>>> import qtLearn.windows.myTool.ui_myTool
>>> import qtLearn.baseMayaWindow
>>>
>>> class MyToolLayout(QWidget, qtLearn.windows.myTool.ui_myTool.Ui_Widget):
>>>     def __init__(self, parent=None, *args, **kwargs):
>>>         super(MyToolLayout, self).__init__(parent=parent, *args, **kwargs)
>>>         self.setupUi(self)
>>>
>>> class MyToolWindow(qtLearn.baseMayaWindow.BaseMayaWindow):
>>>     def __init__(self, parent=None, *args, **kwargs):
>>>         super(MyToolWindow, self).__init__(parent=parent, subLayout=MyToolLayout, *args, **kwargs)
>>>         self.setWindowTitle('Re-Parent')
>>>         self.applyBtn.clicked.connect(self.apply)
>>>     def apply(self):
>>>         print 'apply'

Run Maya Demo Example (inside Maya):
>>> import sys
>>> import os.path
>>> sys.path.insert(0,  os.path.join(os.environ['MAYA_LOCATION'], 'devkit', 'pythonScripts' ) )
>>> import widgetHierarchy
>>> w = widgetHierarchy.main()
"""

from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

# TODO: Can we get this from Qt.py?
try:
    from shiboken2 import wrapInstance
except ImportError:
    from shiboken import wrapInstance

import qtLearn.windows.ui_base
reload(qtLearn.windows.ui_base)


def getMayaMainWindow():
    mainWindowPtr = omui.MQtUtil.mainWindow()
    mainWindow = wrapInstance(long(mainWindowPtr), QtGui.QWidget)
    return mainWindow


def findWidget(name, clsTyp):
    ptr = omui.MQtUtil.findControl(name)
    widget = None
    if ptr:
        widget = wrapInstance(long(ptr), clsTyp)
    return widget


class BaseMayaWindow(MayaQWidgetBaseMixin,
                     QtGui.QMainWindow,
                     qtLearn.windows.ui_base.Ui_Window):
    def __init__(self, parent, name=None):
        super(BaseMayaWindow, self).__init__()

        # Destroy this widget when closed. Otherwise it will stay around.
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

        # Call the UI file contents.
        self.setupUi(self)
        if name:
            self.setObjectName(name)

    def baseHideStandardButtons(self):
        self.createBtn.hide()
        self.applyBtn.hide()
        self.resetBtn.hide()
        self.helpBtn.hide()
        self.closeBtn.hide()
        return

    def baseHideMenuBar(self):
        self.menubar.hide()
        return

    def baseHideProgressBar(self):
        self.progressBar.hide()
        return

    def baseHideStatusBar(self):
        self.statusBar.hide()
        return

    def addSubForm(self, SubForm):
        if SubForm is None:
            return None
        self.subForm = SubForm()
        self.optionsLayout.addWidget(self.subForm)
        return True


window = None


def delete():
    # TODO: Is this deprecated???
    global window
    if window is None:
        return

    name = 'BaseMayaWindow'
    window = findWidget(name, QtGui.QWidget)
    if window:
        # window.close()  # or .deleteLater() ?
        window.deleteLater()

    window = None
    return


def create(show=True):
    # TODO: Is this deprecated???
    global window
    delete()

    name = 'BaseMayaWindow'
    window = BaseMayaWindow(name=name)
    if show:
        window.show()

    return window
