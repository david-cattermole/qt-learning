"""

Usage:
>>> import qtLearn.windows.fileBrowser.fileBrowserSaveWindow
>>> reload(qtLearn.windows.fileBrowser.fileBrowserSaveWindow)
>>> qtLearn.windows.fileBrowser.fileBrowserSaveWindow.main()
"""

import sys

import Qt.QtGui as QtGui

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.envFilter as envFilter
import qtLearn.windows.fileBrowser.forms.fileSelector as fileSelector
import qtLearn.windows.fileBrowser.forms.pathEdit as pathEdit
import qtLearn.windows.fileBrowser.forms.saveOptions as saveOptions
import qtLearn.windows.fileBrowser.ui_fileBrowserSave as ui_fileBrowserSave

reload(uiUtils)
reload(ui_fileBrowserSave)


class FileBrowserSaveLayout(QtGui.QWidget, ui_fileBrowserSave.Ui_Form):
    def __init__(self):
        super(FileBrowserSaveLayout, self).__init__()
        self.setupUi(self)

        self.envFilterForm = envFilter.EnvFilter()
        self.fileSelectorForm = fileSelector.FileSelector()
        self.saveOptionsForm = saveOptions.SaveOptions()
        self.pathEditForm = pathEdit.PathEdit()

        self.envFilterLayout.addWidget(self.envFilterForm)
        self.fileSelectorLayout.addWidget(self.fileSelectorForm)
        self.saveOptionsLayout.addWidget(self.saveOptionsForm)
        self.pathEditLayout.addWidget(self.pathEditForm)


baseModule, BaseWindow = uiUtils.getBaseWindow()


class FileBrowserSaveWindow(BaseWindow):
    def __init__(self, parent=None, name=None, title=None):
        super(FileBrowserSaveWindow, self).__init__(parent, name=name)
        self.setupUi(self)
        self.addSubForm(FileBrowserSaveLayout)

        if title is None:
            title = 'Save File...'
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

    name = 'FileBrowserSaveWindow'
    app, parent = uiUtils.getParent()

    if ui is not None:
        ui.close()
    ui = FileBrowserSaveWindow(parent=parent, name=name)
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

