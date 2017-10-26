"""

Usage:
>>> import qtLearn.windows.fileBrowser.fileBrowserSaveWindow
>>> qtLearn.windows.fileBrowser.fileBrowserSaveWindow.main()
"""

import sys

import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.envFilter as envFilter
import qtLearn.windows.fileBrowser.forms.fileSelector as fileSelector
import qtLearn.windows.fileBrowser.forms.pathEdit as pathEdit
import qtLearn.windows.fileBrowser.forms.saveOptions as saveOptions
import qtLearn.windows.fileBrowser.ui_fileBrowserSave as ui_fileBrowserSave


class FileBrowserSaveLayout(QtWidgets.QWidget, ui_fileBrowserSave.Ui_Form):
    def __init__(self, parent):
        super(FileBrowserSaveLayout, self).__init__()
        self.setupUi(self)
        self.parent = parent

        self.envFilter = envFilter.EnvFilter(self)
        self.fileSelector = fileSelector.FileSelector(self)
        self.saveOptions = saveOptions.SaveOptions(self)
        self.pathEdit = pathEdit.PathEdit(self)

        self.envFilterLayout.addWidget(self.envFilter)
        self.fileSelectorLayout.addWidget(self.fileSelector)
        self.saveOptionsLayout.addWidget(self.saveOptions)
        self.pathEditLayout.addWidget(self.pathEdit)

        self.fileSelector.setTag.connect(self.pathEdit.setTag)
        # self.pathEdit.pathUpdated.connect(self.versionSelector.setPath)

        self.envFilter.setTag.connect(self.pathEdit.setTag)
        self.envFilter.changedDepartment.connect(self.fileSelector.departmentChanged)

        self.buttonBox.rejected.connect(self.rejected)
        self.buttonBox.accepted.connect(self.accepted)

    def rejected(self):
        return self.parent.close()

    def accepted(self):
        print('accepted')
        # TODO: What do we do to return the file path?
        return


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


def main(show=True, widthHeight=(750, 600)):
    global ui
    print('ui:', ui)

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

