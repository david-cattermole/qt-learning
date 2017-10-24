"""

"""

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.ui_pathEdit as ui_pathEdit


class PathEdit(QtWidgets.QWidget, ui_pathEdit.Ui_Form):
    def __init__(self, parent):
        super(PathEdit, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        self._tagData = {}
        self._pathFormat = '/{project}/{sequence}/{shot}/{department}/{name}_{major}.{minor}.{ext}'

        self.lineEdit.setFont(self.font)

    def setPathFormat(self, value):
        # print('setPathRule:', value)
        self._pathFormat = value

    @QtCore.Slot(str, str)
    def updateTag(self, tagName, tagValue):
        # print('updateFileName:', tagName, tagValue)
        if tagName is None or len(tagName) == 0:
            return
        if not tagValue:
            return
        self._tagData[tagName] = tagValue
        self.updatePathText()
        return

    def updatePathText(self):
        # print('updatePathText:', self.textEdit.toPlainText(), self._tagData)
        path = self._pathFormat
        tooltip = self._pathFormat
        for key, value in self._tagData.items():
            if key in path:
                k = '{' + key + '}'
                path = path.replace(k, value)
        tooltip = path
        self.lineEdit.setText(path)
        self.lineEdit.setToolTip(tooltip)
