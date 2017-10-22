"""

Usage:
>>> import qtLearn.windows.fileBrowser.fileBrowserOpenWindow
>>> reload(qtLearn.windows.fileBrowser.fileBrowserOpenWindow)
>>> qtLearn.windows.fileBrowser.fileBrowserOpenWindow.main()
"""

import sys

import Qt.QtGui as QtGui

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.envFilter as envFilter
import qtLearn.windows.fileBrowser.forms.fileSelector as fileSelector
import qtLearn.windows.fileBrowser.forms.pathEdit as pathEdit
import qtLearn.windows.fileBrowser.forms.versionSelector as versionSelector
import qtLearn.windows.fileBrowser.ui_fileBrowserOpen as ui_fileBrowserOpen

# reload(uiUtils)
# reload(ui_fileBrowserOpen)


class MainLayout(QtGui.QWidget, ui_fileBrowserOpen.Ui_Form):
    def __init__(self):
        super(MainLayout, self).__init__()
        self.setupUi(self)

        self.envFilterForm = envFilter.EnvFilter()
        self.fileSelectorForm = fileSelector.FileSelector()
        self.versionSelectorForm = versionSelector.VersionSelector()
        self.pathEditForm = pathEdit.PathEdit()

        self.envFilterLayout.addWidget(self.envFilterForm)
        self.fileSelectorLayout.addWidget(self.fileSelectorForm)
        self.versionSelectorLayout.addWidget(self.versionSelectorForm)
        self.pathEditLayout.addWidget(self.pathEditForm)


baseModule, BaseWindow = uiUtils.getBaseWindow()


class FileBrowserOpenWindow(BaseWindow):
    def __init__(self, parent=None, name=None, title=None):
        super(FileBrowserOpenWindow, self).__init__(parent, name=name)
        self.setupUi(self)
        self.addSubForm(MainLayout)

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
    app, parent = uiUtils.getParent()

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

