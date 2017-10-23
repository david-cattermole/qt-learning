"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_float3Attr as ui_float3Attr
# reload(ui_float3Attr)


class Float3Attr(QtWidgets.QWidget, ui_float3Attr.Ui_Widget):
    def __init__(self, label=None):
        super(Float3Attr, self).__init__()
        self.setupUi(self)
        if label is not None:
            self.label.setText(label)