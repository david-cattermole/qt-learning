"""

"""

import Qt.QtGui as QtGui

import qtLearn.windows.fileBrowser.forms.ui_versionSelector as ui_versionSelector
reload(ui_versionSelector)


class VersionSelector(QtGui.QWidget, ui_versionSelector.Ui_Form):
    def __init__(self):
        super(VersionSelector, self).__init__()
        self.setupUi(self)
