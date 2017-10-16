"""

Usage:
>>> import qtLearn.reparentWindow
>>> reload(qtLearn.reparentWindow)
>>> qtLearn.reparentWindow.main()
"""

import sys
import time

import Qt.QtGui as QtGui

import qtLearn.uiUtils

# try:
#     from PySide.QtCore import *
#     from PySide.QtGui import *
#     from PySide import __version__
#     from shiboken import wrapInstance
#     # from PySide2.QtCore import *
#     # from PySide2.QtGui import *
#     # from PySide2.QtWidgets import *
#     # from PySide2 import __version__
#     # from shiboken2 import wrapInstance
# except ImportError:
#     from PyQt4.QtCore import *
#     from PyQt4.QtGui import *
reload(qtLearn.uiUtils)

import qtLearn.nodesMayaWidget
import qtLearn.windows.reparent.ui_reparent
import qtLearn.widgets.reparent.ui_getNodes
import qtLearn.widgets.reparent.ui_subFrame
import qtLearn.widgets.reparent.ui_timeRange

reload(qtLearn.nodesMayaWidget)
reload(qtLearn.windows.reparent.ui_reparent)
reload(qtLearn.widgets.reparent.ui_getNodes)
reload(qtLearn.widgets.reparent.ui_subFrame)
reload(qtLearn.widgets.reparent.ui_timeRange)


class ReparentGetNodes(QtGui.QWidget, qtLearn.widgets.reparent.ui_getNodes.Ui_Widget):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentGetNodes, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        self.childNodes = qtLearn.nodesMayaWidget.NodesMayaWidget()
        self.parentNode = qtLearn.nodesMayaWidget.NodesMayaWidget()

        self.childNodesLayout.addWidget(self.childNodes)
        self.parentNodeLayout.addWidget(self.parentNode)


class ReparentTimeRange(QtGui.QWidget, qtLearn.widgets.reparent.ui_timeRange.Ui_Widget):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentTimeRange, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


class ReparentSubFrame(QtGui.QWidget, qtLearn.widgets.reparent.ui_subFrame.Ui_Widget):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentSubFrame, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


class ReparentLayout(QtGui.QWidget, qtLearn.windows.reparent.ui_reparent.Ui_Widget):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentLayout, self).__init__(*args, **kwargs)  # parent,
        self.setupUi(self)

        self.nodesForm = ReparentGetNodes()
        self.timeRangeForm = ReparentTimeRange()
        self.subFrameForm = ReparentSubFrame()

        self.nodesLayout.addWidget(self.nodesForm)
        self.timeRangeLayout.addWidget(self.timeRangeForm)
        self.subFrameLayout.addWidget(self.subFrameForm)

        # self.nodesLayout = ReparentGetNodes(parent=self.nodesLayoutStub)
        # self.timeRangeLayout = ReparentTimeRange(parent=self.timeRangeLayoutStub)
        # self.subFrameLayout = ReparentSubFrame(parent=self.subFrameLayoutStub)

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


baseModule, BaseWindow = qtLearn.uiUtils.getBaseWindow()


class ReparentWindow(BaseWindow):
    def __init__(self, parent=None, name=None):
        super(ReparentWindow, self).__init__(parent, name=name)
        self.setupUi(self)
        self.addSubForm(ReparentLayout)

        self.setWindowTitle('Re-Parent')

        # NOTE: All buttons are hidden by default.
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
        start = self.subForm.getStartFrame()
        print 'apply', start
        for i in range(100):
            self.progressBar.setValue(i)
            time.sleep(0.01)
        self.progressBar.hide()
        return

    def reset(self):
        print 'reset'
        return

    def help(self):
        print 'help'
        return


ui = None


def main(show=True, widthHeight=(400, 540)):
    global ui
    print 'ui:', ui

    name = 'ReparentWindow'
    app, parent = qtLearn.uiUtils.getParent()

    if ui is not None:
        ui.close()
    ui = ReparentWindow(parent=parent, name=name)
    if not ui:
        return ui
    if show:
        ui.show()

    if widthHeight:
        pos = ui.pos()
        ui.setGeometry(pos.x(), pos.y(), widthHeight[0], widthHeight[1])

    # Enter Qt application main loop
    if app is not None:
        sys.exit(app.exec_())
    return ui

