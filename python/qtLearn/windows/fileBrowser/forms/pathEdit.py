"""

"""

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.ui_pathEdit as ui_pathEdit


def computePath(pathFormat, tagData):
    assert isinstance(pathFormat, str)
    assert isinstance(tagData, dict)
    result = pathFormat
    for key, value in tagData.items():
        if key in result:
            k = '{' + key + '}'
            result = result.replace(k, value)
    return result


def computeToolTip(path, pathFormat, tagData):
    keyvalue_pairs = '\n'

    path_keys = []
    prev_len = 0
    tmp_path = pathFormat
    while len(tmp_path) != prev_len:
        prev_len = len(tmp_path)
        i = tmp_path.find('{')
        if i != -1:
            j = tmp_path.find('}')
            if j != -1:
                key = tmp_path[i:j+1]
                key = key.replace('{', '').replace('}', '')
                path_keys.append(key)
                tmp_path = tmp_path[j+1:]

    ordered_keys = []
    for k in path_keys:
        if k in tagData.keys():
            ordered_keys.append(k)

    for key in ordered_keys:
        value = '?'
        if key in tagData:
            value = tagData[key]
        keyvalue_pairs += '{k} = {v}\n'.format(k=key, v=value)

    tooltip = path + '\n'
    tooltip += keyvalue_pairs
    return tooltip.strip()


class PathEdit(QtWidgets.QWidget, ui_pathEdit.Ui_Form):
    pathUpdated = QtCore.Signal(str)

    def __init__(self, parent):
        super(PathEdit, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        self._tagData = {}
        self._pathFormat = '/{project}/{sequence}/{shot}/{department}/{name}_{major}.{minor}.{ext}'

        self.lineEdit.setFont(self.font)

    def pathFormat(self):
        return self._pathFormat

    def setPathFormat(self, value):
        self._pathFormat = value

    @QtCore.Slot(str, str)
    def setTag(self, tagName, tagValue):
        if tagName is None or len(tagName) == 0:
            return
        if not tagValue:
            return
        self._tagData[tagName] = tagValue
        self.updatePathText()
        return

    def updatePathText(self):
        path = computePath(self.pathFormat(), self._tagData)
        tooltip = computeToolTip(path, self.pathFormat(), self._tagData)

        self.lineEdit.setText(path)
        self.lineEdit.setToolTip(tooltip)

        self.pathUpdated.emit(path)
