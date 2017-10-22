"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_comboBox2Attr as ui_comboBox2Attr
reload(ui_comboBox2Attr)


class ComboBox2Attr(QtWidgets.QWidget, ui_comboBox2Attr.Ui_Widget):
    def __init__(self, label=None):
        super(ComboBox2Attr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)
