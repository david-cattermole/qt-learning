"""

"""

import Qt.QtGui as QtGui

import qtLearn.windows.fileBrowser.forms.ui_pathEdit
reload(qtLearn.windows.fileBrowser.forms.ui_pathEdit)


class PathEdit(QtGui.QWidget, qtLearn.windows.fileBrowser.forms.ui_pathEdit.Ui_Form):
    def __init__(self):
        super(PathEdit, self).__init__()
        self.setupUi(self)

