"""

"""

import Qt.QtWidgets as QtWidgets

import qtLearn.windows.fileBrowser.forms.ui_pathEdit as ui_pathEdit
# reload(ui_pathEdit)


class PathEdit(QtWidgets.QWidget, ui_pathEdit.Ui_Form):
    def __init__(self):
        super(PathEdit, self).__init__()
        self.setupUi(self)

