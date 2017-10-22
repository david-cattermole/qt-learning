"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_float2Attr as ui_float2Attr
reload(ui_float2Attr)


class Float2Attr(QtWidgets.QWidget, ui_float2Attr.Ui_Widget):
    def __init__(self, label=None):
        super(Float2Attr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)