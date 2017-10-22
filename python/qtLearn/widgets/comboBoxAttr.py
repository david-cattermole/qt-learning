"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_comboBoxAttr as ui_comboBoxAttr
reload(ui_comboBoxAttr)


class ComboBoxAttr(QtWidgets.QWidget, ui_comboBoxAttr.Ui_Widget):
    def __init__(self, label=None):
        super(ComboBoxAttr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)
