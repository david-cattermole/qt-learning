"""

Usage:
>>> import qtLearn.windows.fileBrowser.fileBrowserSaveWindow
>>> reload(qtLearn.windows.fileBrowser.fileBrowserSaveWindow)
>>> qtLearn.windows.fileBrowser.fileBrowserSaveWindow.main()
"""

import sys

import Qt.QtGui as QtGui

import qtLearn.uiUtils
import qtLearn.widgets.nodesMayaWidget
import qtLearn.windows.fileBrowser.fileBrowserCommon as common
import qtLearn.windows.fileBrowser.forms.ui_saveOptions
import qtLearn.windows.fileBrowser.ui_fileBrowserSave

reload(qtLearn.uiUtils)
reload(qtLearn.windows.fileBrowser.ui_fileBrowserSave)
reload(qtLearn.windows.fileBrowser.forms.ui_saveOptions)


class SaveOptions(QtGui.QWidget, qtLearn.windows.fileBrowser.forms.ui_saveOptions.Ui_Form):
    def __init__(self):
        super(SaveOptions, self).__init__()
        self.setupUi(self)


class FileBrowserSaveLayout(QtGui.QWidget, qtLearn.windows.fileBrowser.ui_fileBrowserSave.Ui_Form):
    def __init__(self):
        super(FileBrowserSaveLayout, self).__init__()
        self.setupUi(self)

        self.envFilterForm = common.EnvFilter()
        self.envFilterLayout.addWidget(self.envFilterForm)

        self.fileSelectorForm = common.FileSelector()
        self.fileSelectorLayout.addWidget(self.fileSelectorForm)

        self.saveOptionsForm = SaveOptions()
        self.saveOptionsLayout.addWidget(self.saveOptionsForm)

        self.pathEditForm = common.PathEdit()
        self.pathEditLayout.addWidget(self.pathEditForm)


baseModule, BaseWindow = qtLearn.uiUtils.getBaseWindow()


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
    app, parent = qtLearn.uiUtils.getParent()

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

