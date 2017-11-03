"""
A path text box that will point to a file or directory.
"""

import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets

import qtLearn.paths as paths
import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.ui_pathEdit as ui_pathEdit



def computeToolTip(pth, pathFormat, tags):
    assert isinstance(pth, paths.Path)
    assert isinstance(pathFormat, paths.PathFormat)
    assert isinstance(tags, dict)
    tooltip = pth.getPath(showMissingKeys=True) + '\n'

    ordered_keys = pth.getTagKeysOrdered()
    # ordered_keys = filter(lambda x: x in tagData.keys(), path_keys)
    keyvalue_pairs = '\n'
    for key in ordered_keys:
        value = '?'
        if key in tags:
            value = tags[key]
        if value is None:
            value = '?'
        keyvalue_pairs += '{k} = {v}\n'.format(k=key, v=value)
    tooltip += keyvalue_pairs

    return tooltip.strip()


class PathEdit(QtWidgets.QWidget, ui_pathEdit.Ui_Form):
    signalPathUpdated = QtCore.Signal(dict)

    def __init__(self, parent, pathFormat=None):
        super(PathEdit, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')
        self._tagData = {}
        self._tagChanged = {}
        self._isModifyingTags = False

        self._pathFormat = pathFormat
        if pathFormat is None:
            self._pathFormat = '/projects/{project}/{sequence}/{shot}/{department}/{task}/{name}_{major}.{minor}.{ext}'

        self.font.setPointSize(11)
        self.lineEdit.setFont(self.font)
        self.lineEdit.setText(self._pathFormat)

        # self.lineEdit.textEdited.connect(self.slotPathTextUpdated)

    ############################################################################

    def getTagValue(self, key, default=None):
        return self._tagData.get(key, default)

    def setTagValue(self, key, value):
        self._tagData[key] = value
        return

    def getTags(self):
        if self._tagData is None:
            return {}
        return self._tagData.copy()

    def setTags(self, value):
        self._tagData = value.copy()
        return

    def pathFormat(self):
        return self._pathFormat

    def setPathFormat(self, value):
        self._pathFormat = value

    def isModifyingTags(self):
        return self._isModifyingTags

    def setIsModifyingTags(self, value):
        self._isModifyingTags = value

    ############################################################################

    @QtCore.Slot()
    def slotSetTagStart(self):
        # print('PathEdit slotSetTagStart')
        self.setIsModifyingTags(True)
        return

    @QtCore.Slot(str, str)
    def slotSetTag(self, tagName, tagValue):
        # print('PathEdit slotSetTag:', repr(tagName), repr(tagValue))
        if self.isModifyingTags() is False:
            return
        if tagName is None or len(tagName) == 0:
            return
        if isinstance(tagValue, str) and len(tagValue) == 0:
            return
        self.setTagValue(tagName, tagValue)
        self._tagChanged[tagName] = True
        return

    @QtCore.Slot()
    def slotSetTagEnd(self):
        # print('PathEdit slotSetTagEnd')
        self.setIsModifyingTags(False)
        self.updatePathText()
        self._tagChanged = {}
        return

    # @QtCore.Slot(str)
    # def slotPathTextUpdated(self, text):
    #     # print('PathEdit slotPathTextUpdated 1', text)
    #     fmt = paths.PathFormat(self.pathFormat())
    #     pth = paths.Path(text, format=fmt)
    #     path = pth.getPath(showMissingKeys=True)
    #     pos = self.lineEdit.cursorPosition()
    #     self.lineEdit.setText(path)
    #     self.lineEdit.setCursorPosition(pos)
    #     # print('PathEdit slotPathTextUpdated 2', path)
    #     # self.updatePathText()
    #     return

    ############################################################################

    def updatePathText(self):
        if len(self._tagChanged) == 0:
            return

        tagData = self.getTags().copy()
        fmt = paths.PathFormat(self.pathFormat())
        orderedKeys = fmt.computeOrderedTagKeys()
        index = -1
        for i, key in enumerate(orderedKeys):
            if key in tagData:
                if self._tagChanged.get(key) is not True:
                    continue
                value = tagData.get(key)
                if value is None:
                    continue
                index = i

        # print('PathEdit updatePathText last index:', index)
        # print('PathEdit updatePathText tagChanged:', self._tagChanged)
        if index < 0:
            return

        resetKeys = orderedKeys[index+1:]
        for key in resetKeys:
            tagData[key] = None
        self.setTags(tagData)

        pth = paths.Path(tagData, format=fmt)
        tooltip = computeToolTip(pth, fmt, tagData)

        path = pth.getPath(showMissingKeys=True)
        # print('PathEdit updatePathText path:', path)
        # print('PathEdit updatePathText path tags:', pth.getTags())
        # print('PathEdit updatePathText path tag values:', pth.getTagValuesOrdered())
        # print('PathEdit updatePathText path tag keys:', pth.getTagKeysOrdered())
        self.lineEdit.setText(path)
        self.lineEdit.setToolTip(tooltip)

        # tagData['path'] = path
        # tagData['tooltip'] = tooltip
        self.signalPathUpdated.emit(tagData)
        print('PathEdit updatePathText path:', repr(path), tagData)
