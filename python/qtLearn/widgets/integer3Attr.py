"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_integer3Attr as ui_integer3Attr
reload(ui_integer3Attr)


class Integer3Attr(QtWidgets.QWidget, ui_integer3Attr.Ui_Widget):
    def __init__(self, label=None):
        super(Integer3Attr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)