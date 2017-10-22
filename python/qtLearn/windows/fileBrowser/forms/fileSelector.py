"""

"""

import Qt.QtGui as QtGui

import qtLearn.windows.fileBrowser.forms.ui_fileSelector as ui_fileSelector
reload(ui_fileSelector)


class FileSelector(QtGui.QWidget, ui_fileSelector.Ui_Form):
    def __init__(self):
        super(FileSelector, self).__init__()
        self.setupUi(self)
