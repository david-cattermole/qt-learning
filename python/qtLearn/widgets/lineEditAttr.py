"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_lineEditAttr as ui_lineEditAttr
# reload(ui_lineEditAttr)


class LineEditAttr(QtWidgets.QWidget, ui_lineEditAttr.Ui_Widget):
    def __init__(self, label=None):
        super(LineEditAttr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)