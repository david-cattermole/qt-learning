"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_integer2Attr as ui_integer2Attr
# reload(ui_integer2Attr)


class Integer2Attr(QtWidgets.QWidget, ui_integer2Attr.Ui_Widget):
    def __init__(self, label=None):
        super(Integer2Attr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)