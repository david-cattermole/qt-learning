"""

Usage:
>>> import qtLearn.windows.reparent.reparentWindow
>>> qtLearn.windows.reparent.reparentWindow.main()
"""

import sys
import time

import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.widgets.nodesMayaWidget as nodeMayaWidget
import qtLearn.windows.reparent.forms.ui_getNodes as ui_getNodes
import qtLearn.windows.reparent.forms.ui_subFrame as ui_subFrame
import qtLearn.windows.reparent.forms.ui_timeRange as ui_timeRange
import qtLearn.windows.reparent.ui_reparent as ui_reparent

# reload(uiUtils)
# reload(nodeMayaWidget)
# reload(ui_reparent)
# reload(ui_getNodes)
# reload(ui_subFrame)
# reload(ui_timeRange)


class ReparentGetNodes(QtWidgets.QWidget, ui_getNodes.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentGetNodes, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

        self.childNodes = nodeMayaWidget.NodesMayaWidget()
        self.parentNode = nodeMayaWidget.NodesMayaWidget()

        self.childNodesLayout.addWidget(self.childNodes)
        self.parentNodeLayout.addWidget(self.parentNode)


class ReparentTimeRange(QtWidgets.QWidget, ui_timeRange.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentTimeRange, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


class ReparentSubFrame(QtWidgets.QWidget, ui_subFrame.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentSubFrame, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)


class ReparentLayout(QtWidgets.QWidget, ui_reparent.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(ReparentLayout, self).__init__(*args, **kwargs)  # parent,
        self.setupUi(self)

        self.nodesForm = ReparentGetNodes()
        self.timeRangeForm = ReparentTimeRange()
        self.subFrameForm = ReparentSubFrame()

        self.nodesLayout.addWidget(self.nodesForm)
        self.timeRangeLayout.addWidget(self.timeRangeForm)
        self.subFrameLayout.addWidget(self.subFrameForm)

        # data = ['Existing Times', 'All Times', 'Three', 'Four', 'Five']
        # model = QStringListModel(data)
        # self.timeRangeComboBox.setModel(model)

    def getStartFrame(self):
        print('getStartFrame')
        # return self.startFrameSpinBox.value()
        return

    def getEndFrame(self):
        print('getEndFrame')
        # return self.endFrameSpinBox.value()
        return


baseModule, BaseWindow = uiUtils.getBaseWindow()


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
        print('apply', start)
        for i in range(100):
            self.progressBar.setValue(i)
            time.sleep(0.01)
        self.progressBar.hide()
        return

    def reset(self):
        print('reset')
        return

    def help(self):
        print('help')
        return


ui = None


def main(show=True, widthHeight=(400, 540)):
    global ui
    print('ui:', ui)

    name = 'ReparentWindow'
    app, parent = uiUtils.getParent()

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

