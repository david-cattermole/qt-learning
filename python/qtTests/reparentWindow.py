"""

Usage:
>>> import qtTests.reparentWindow
>>> reload(qtTests.reparentWindow)
>>> qtTests.reparentWindow.main()
"""

import os
import time
from maya import OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

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

import qtTests.mayaGetNodesWidget
import qtTests.ui_reparent
import qtTests.ui_reparent_getNodes
import qtTests.mayaBaseWindow

reload(qtTests.mayaGetNodesWidget)
reload(qtTests.ui_reparent)
reload(qtTests.ui_reparent_getNodes)
reload(qtTests.mayaBaseWindow)


# class ReparentForm(QWidget, qtTests.ui_reparent.Ui_Form):
#     def __init__(self, parent=None, *args, **kwargs):
#         print 'ReparentForm:', self.__class__
#         if parent is None:
#             parent = qtTests.mayaBaseWindow.getMayaMainWindow()
#         super(ReparentForm, self).__init__(parent=parent, *args, **kwargs)
#         self.setupUi(parent)
#
#         data = ['Existing Times', 'All Times', 'Three', 'Four', 'Five']
#         model = QStringListModel(data)
#         self.timeRangeComboBox.setModel(model)
#
#     def getStartFrame(self):
#         return self.startFrameSpinBox.value()
#
#     def getEndFrame(self):
#         return self.endFrameSpinBox.value()


class ReparentGetNodes(QWidget, qtTests.ui_reparent_getNodes.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentGetNodes, self).__init__(parent=parent, *args, **kwargs)
        self.setupUi(parent)
        self.getChildNodesStub = qtTests.mayaGetNodesWidget.MayaGetNodesWidget(parent=self.getChildNodesStub)
        self.getParentNodeStub = qtTests.mayaGetNodesWidget.MayaGetNodesWidget(parent=self.getParentNodeStub)


class ReparentForm(QWidget, qtTests.ui_reparent.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentForm, self).__init__(parent=parent, *args, **kwargs)
        self.setupUi(self)
        # self.nodesLayoutStub.setParent(self)
        self.nodesLayoutStub = ReparentGetNodes(parent=self.nodesLayoutStub)
        # self.timeRangeLayout = None
        # self.subFrameLayout = None

        # data = ['Existing Times', 'All Times', 'Three', 'Four', 'Five']
        # model = QStringListModel(data)
        # self.timeRangeComboBox.setModel(model)

    def getStartFrame(self):
        print 'getStartFrame'
        # return self.startFrameSpinBox.value()
        return

    def getEndFrame(self):
        print 'getEndFrame'
        # return self.endFrameSpinBox.value()
        return


class ReparentWindow(qtTests.mayaBaseWindow.MayaBaseWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentWindow, self).__init__(parent=parent,
                                             subLayout=ReparentForm,
                                             *args, **kwargs)
        self.setWindowTitle('Re-Parent')

        self.createBtn.hide()
        self.applyBtn.show()
        self.resetBtn.show()
        self.helpBtn.show()
        self.closeBtn.show()
        self.applyBtn.setText('Run')

        self.applyBtn.clicked.connect(self.apply)
        self.resetBtn.clicked.connect(self.reset)
        self.helpBtn.clicked.connect(self.help)

    def apply(self):
        self.progressBar.show()
        start = self.subLayout.getStartFrame()
        print 'apply', start
        for i in range(100):
            self.progressBar.setValue(i)
            time.sleep(0.01)
        self.progressBar.hide()

    def reset(self):
        print 'reset'

    def help(self):
        print 'help'


def main(show=True, widthHeight=(400, 540)):
    name = 'ReparentWindow'
    window = qtTests.mayaBaseWindow.findWidget(name, QWidget)
    if window:
        window.close()
    ui = ReparentWindow(name=name)
    if show:
        ui.show()
    if widthHeight:
        pos = ui.pos()
        ui.setGeometry(pos.x(), pos.y(), widthHeight[0], widthHeight[1])
    # if width:
    #     # ui.setFixedWidth(width)
    #     # ui.setMinimumWidth(width)
    # if height:
    #     # ui.setFixedHeight(height)
    #     # ui.setMinimumHeight(height)
    return ui
