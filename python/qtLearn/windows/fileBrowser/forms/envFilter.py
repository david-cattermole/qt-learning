"""

"""

import Qt.QtGui as QtGui

import qtLearn.windows.fileBrowser.forms.ui_envFilter as ui_envFilter
reload(ui_envFilter)


class EnvFilter(QtGui.QWidget, ui_envFilter.Ui_Form):
    def __init__(self):
        super(EnvFilter, self).__init__()
        self.setupUi(self)
