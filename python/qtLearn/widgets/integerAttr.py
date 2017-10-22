"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_integerAttr as ui_integerAttr
reload(ui_integerAttr)


class IntegerAttr(QtWidgets.QWidget, ui_integerAttr.Ui_Widget):
    def __init__(self, label=None):
        super(IntegerAttr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)