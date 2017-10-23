"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_comboBox3Attr as ui_comboBox3Attr
# reload(ui_comboBox3Attr)


class ComboBox3Attr(QtWidgets.QWidget, ui_comboBox3Attr.Ui_Widget):
    def __init__(self, label=None):
        super(ComboBox3Attr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)
