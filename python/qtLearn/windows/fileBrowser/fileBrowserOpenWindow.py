"""
A file browser for displaying and selecting a file or asset.

Usage:
>>> import qtLearn.windows.fileBrowser.fileBrowserOpenWindow
>>> qtLearn.windows.fileBrowser.fileBrowserOpenWindow.main()
"""

import sys

import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.envFilter as envFilter
import qtLearn.windows.fileBrowser.forms.fileSelector as fileSelector
import qtLearn.windows.fileBrowser.forms.pathEdit as pathEdit
import qtLearn.windows.fileBrowser.forms.versionSelector as versionSelector
import qtLearn.windows.fileBrowser.forms.previewInfo as previewInfo
import qtLearn.windows.fileBrowser.ui_fileBrowserOpen as ui_fileBrowserOpen


class MainLayout(QtWidgets.QWidget, ui_fileBrowserOpen.Ui_Form):
    def __init__(self, parent, withPreviewInfo=True):
        super(MainLayout, self).__init__()
        self.setupUi(self)
        self.parent = parent
        pathFormat = '/projects/{project}/{sequence}/{shot}/{department}/{task}/{name}_{major}.{minor}.{ext}'

        self.envFilter = envFilter.EnvFilter(
            self,
            withDepartmentFilter=True,
            withUserFilter=True
        )
        self.envFilterLayout.addWidget(self.envFilter)

        self.fileSelector = fileSelector.FileSelector(
            self,
            withFolderFilter=True,
            folderFilterLabel='Task',
            folderFilterTagName='task',
            folderFilterNodeType='task',
            withSearchLine=True,
            pathFormat=pathFormat
        )
        self.fileSelectorLayout.addWidget(self.fileSelector)

        self.versionSelector = versionSelector.VersionSelector(
            self,
            withFileFormatFilter=True,
            fileFormatFilterTagName='ext',
            fileFormatFilterNodeType='minorversion',
            pathFormat=pathFormat
        )
        self.versionSelectorLayout.addWidget(self.versionSelector)

        self.pathEdit = pathEdit.PathEdit(
            self,
            pathFormat=pathFormat
        )
        self.pathEditLayout.addWidget(self.pathEdit)

        self.previewInfo = None
        if withPreviewInfo is True:
            self.previewInfo = previewInfo.PreviewInfo(self)
            self.previewInfoLayout.addWidget(self.previewInfo)

        self.envFilter.signalSetUser.connect(self.versionSelector.slotSetUserFilterValue)
        self.envFilter.signalSetDepartment.connect(self.fileSelector.slotSetFilterTagValue)
        self.envFilter.signalSetTagStart.connect(self.pathEdit.slotSetTagStart)
        self.envFilter.signalSetTag.connect(self.pathEdit.slotSetTag)
        self.envFilter.signalSetTagEnd.connect(self.pathEdit.slotSetTagEnd)

        self.fileSelector.signalSetTagStart.connect(self.pathEdit.slotSetTagStart)
        self.fileSelector.signalSetTag.connect(self.pathEdit.slotSetTag)
        self.fileSelector.signalSetTagEnd.connect(self.pathEdit.slotSetTagEnd)
        # self.fileSelector.signalSetFileName.connect(self.versionSelector.???)

        self.versionSelector.signalSetTagStart.connect(self.pathEdit.slotSetTagStart)
        self.versionSelector.signalSetTag.connect(self.pathEdit.slotSetTag)
        self.versionSelector.signalSetTagEnd.connect(self.pathEdit.slotSetTagEnd)
        # self.versionSelector.signalSetVersion.connect(self.pathEdit.slotSetVersion)

        self.pathEdit.signalPathUpdated.connect(self.fileSelector.slotSetPathData)
        self.pathEdit.signalPathUpdated.connect(self.versionSelector.slotSetPathData)

        self.buttonBox.rejected.connect(self.rejected)
        self.buttonBox.accepted.connect(self.accepted)

    def rejected(self):
        return self.parent.close()

    def accepted(self):
        print('accepted')
        # TODO: What do we do to return the file path?
        return


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
        self.baseHideToolBar()


ui = None


def main(show=True, widthHeight=(750, 600)):
    global ui
    # print('ui:', ui)

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
        uiUtils.setWindowWidthHeight(ui, widthHeight)

    # Enter Qt application main loop
    if app is not None:
        sys.exit(app.exec_())
    return ui

