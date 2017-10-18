"""

Usage:
>>> import qtLearn.windows.reparent.reparentWindow
>>> reload(qtLearn.windows.reparent.reparentWindow)
>>> qtLearn.windows.reparent.reparentWindow.main()
"""

import sys
import time

import Qt.QtGui as QtGui

import qtLearn.uiUtils

import qtLearn.nodesMayaWidget
import qtLearn.windows.reparent.ui_reparent
import qtLearn.windows.reparent.forms.ui_getNodes
import qtLearn.windows.reparent.forms.ui_subFrame
import qtLearn.windows.reparent.forms.ui_timeRange


reload(qtLearn.uiUtils)
reload(qtLearn.nodesMayaWidget)
reload(qtLearn.windows.reparent.ui_reparent)
reload(qtLearn.windows.reparent.forms.ui_getNodes)
reload(qtLearn.windows.reparent.forms.ui_subFrame)
reload(qtLearn.windows.reparent.forms.ui_timeRange)


class ReparentGetNodes(QtGui.QWidget, qtLearn.windows.reparent.forms.ui_getNodes.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentGetNodes, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        self.childNodes = qtLearn.nodesMayaWidget.NodesMayaWidget()
        self.parentNode = qtLearn.nodesMayaWidget.NodesMayaWidget()

        self.childNodesLayout.addWidget(self.childNodes)
        self.parentNodeLayout.addWidget(self.parentNode)


class ReparentTimeRange(QtGui.QWidget, qtLearn.windows.reparent.forms.ui_timeRange.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentTimeRange, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


class ReparentSubFrame(QtGui.QWidget, qtLearn.windows.reparent.forms.ui_subFrame.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentSubFrame, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


class ReparentLayout(QtGui.QWidget, qtLearn.windows.reparent.ui_reparent.Ui_Form):
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

        # Standard Buttons
        self.baseHideStandardButtons()
        self.applyBtn.show()
        self.resetBtn.show()
        self.helpBtn.show()
        self.closeBtn.show()
        self.applyBtn.setText('Run')

        self.applyBtn.clicked.connect(self.apply)
        self.resetBtn.clicked.connect(self.reset)
        self.helpBtn.clicked.connect(self.help)

        # Hide irrelevant stuff
        self.baseHideMenuBar()
        self.baseHideStatusBar()
        self.baseHideProgressBar()

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

