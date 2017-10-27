"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_lineEditAttr as ui_lineEditAttr
# reload(ui_lineEditAttr)


class LineEditAttr(QtWidgets.QWidget, ui_lineEditAttr.Ui_Widget):
    def __init__(self, withLabel=True, label=None, withButton=False,
                 buttonText=None, buttonIcon=None):
        super(LineEditAttr, self).__init__()
        self.setupUi(self)

        self.label.setVisible(withLabel)
        if withLabel is True:
            if label is not None:
                self.label.setText(label)

        self.toolButton.setVisible(withButton)
        if withButton is True:
            if buttonText is not None:
                self.toolButton.setText(buttonText)
            if buttonIcon is not None:
                self.toolButton.setIcon(buttonIcon)