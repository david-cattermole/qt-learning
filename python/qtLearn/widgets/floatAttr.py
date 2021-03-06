"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_floatAttr as ui_floatAttr
# reload(ui_floatAttr)


class FloatAttr(QtWidgets.QWidget, ui_floatAttr.Ui_Widget):
    def __init__(self, label=None):
        super(FloatAttr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)