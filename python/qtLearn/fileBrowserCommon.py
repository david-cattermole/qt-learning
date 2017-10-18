"""

"""

import Qt.QtGui as QtGui

import qtLearn.widgets.fileBrowser.ui_envFilter
import qtLearn.widgets.fileBrowser.ui_fileSelector
import qtLearn.widgets.fileBrowser.ui_pathEdit

reload(qtLearn.widgets.fileBrowser.ui_envFilter)
reload(qtLearn.widgets.fileBrowser.ui_fileSelector)
reload(qtLearn.widgets.fileBrowser.ui_pathEdit)


class EnvFilter(QtGui.QWidget, qtLearn.widgets.fileBrowser.ui_envFilter.Ui_Form):
    def __init__(self):
        super(EnvFilter, self).__init__()
        self.setupUi(self)


class FileSelector(QtGui.QWidget, qtLearn.widgets.fileBrowser.ui_fileSelector.Ui_Form):
    def __init__(self):
        super(FileSelector, self).__init__()
        self.setupUi(self)


class PathEdit(QtGui.QWidget, qtLearn.widgets.fileBrowser.ui_pathEdit.Ui_Form):
    def __init__(self):
        super(PathEdit, self).__init__()
        self.setupUi(self)

