"""

Usage:
>>> import qtLearn.fileBrowserOpenWindow
>>> reload(qtLearn.fileBrowserOpenWindow)
>>> qtLearn.fileBrowserOpenWindow.main()
"""

import sys
from functools import partial

import Qt.QtGui as QtGui

import qtLearn.uiUtils
import qtLearn.nodesMayaWidget
import qtLearn.fileBrowserCommon as common
import qtLearn.windows.fileBrowser.ui_fileBrowserOpen
import qtLearn.widgets.fileBrowser.ui_versionSelector

reload(qtLearn.uiUtils)
reload(qtLearn.windows.fileBrowser.ui_fileBrowserOpen)
reload(qtLearn.widgets.fileBrowser.ui_versionSelector)


class VersionSelector(QtGui.QWidget, qtLearn.widgets.fileBrowser.ui_versionSelector.Ui_Form):
    def __init__(self):
        super(VersionSelector, self).__init__()
        self.setupUi(self)


class FileBrowserOpenLayout(QtGui.QWidget, qtLearn.windows.fileBrowser.ui_fileBrowserOpen.Ui_Form):
    def __init__(self):
        super(FileBrowserOpenLayout, self).__init__()
        self.setupUi(self)

        self.envFilterForm = common.EnvFilter()
        self.envFilterLayout.addWidget(self.envFilterForm)

        self.fileSelectorForm = common.FileSelector()
        self.fileSelectorLayout.addWidget(self.fileSelectorForm)

        self.versionSelectorForm = VersionSelector()
        self.versionSelectorLayout.addWidget(self.versionSelectorForm)

        self.pathEditForm = common.PathEdit()
        self.pathEditLayout.addWidget(self.pathEditForm)


baseModule, BaseWindow = qtLearn.uiUtils.getBaseWindow()


class FileBrowserOpenWindow(BaseWindow):
    def __init__(self, parent=None, name=None, title=None):
        super(FileBrowserOpenWindow, self).__init__(parent, name=name)
        self.setupUi(self)
        self.addSubForm(FileBrowserOpenLayout)

        if title is None:
            title = 'Open File...'
        self.setWindowTitle(title)

        # Hide irrelevant stuff
        self.baseHideMenuBar()
        self.baseHideStatusBar()
        self.baseHideProgressBar()
        self.baseHideStandardButtons()


ui = None


def main(show=True, widthHeight=(800, 500)):
    global ui
    print 'ui:', ui

    name = 'FileBrowserOpenWindow'
    app, parent = qtLearn.uiUtils.getParent()

    if ui is not None:
        ui.close()
    ui = FileBrowserOpenWindow(parent=parent, name=name)
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

