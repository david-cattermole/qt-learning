"""

"""

import Qt.QtGui as QtGui

import qtLearn.windows.fileBrowser.forms.ui_envFilter
import qtLearn.windows.fileBrowser.forms.ui_fileSelector
import qtLearn.windows.fileBrowser.forms.ui_pathEdit

reload(qtLearn.windows.fileBrowser.forms.ui_envFilter)
reload(qtLearn.windows.fileBrowser.forms.ui_fileSelector)
reload(qtLearn.windows.fileBrowser.forms.ui_pathEdit)


class EnvFilter(QtGui.QWidget, qtLearn.windows.fileBrowser.forms.ui_envFilter.Ui_Form):
    def __init__(self):
        super(EnvFilter, self).__init__()
        self.setupUi(self)


class FileSelector(QtGui.QWidget, qtLearn.windows.fileBrowser.forms.ui_fileSelector.Ui_Form):
    def __init__(self):
        super(FileSelector, self).__init__()
        self.setupUi(self)


class PathEdit(QtGui.QWidget, qtLearn.windows.fileBrowser.forms.ui_pathEdit.Ui_Form):
    def __init__(self):
        super(PathEdit, self).__init__()
        self.setupUi(self)

