"""
Preview information UI element.
"""

import sys

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.widgets.attributeHelper as attributeHelper
import qtLearn.windows.fileBrowser.forms.ui_previewInfo as ui_previewInfo


class PreviewInfo(QtWidgets.QWidget, ui_previewInfo.Ui_Form):
    pathUpdated = QtCore.Signal(str)

    def __init__(self, parent):
        super(PreviewInfo, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        # Attributes
        attrHelper = attributeHelper.AttributeHelper()
        attrHelper.setLayout(self.optionAttrLayout)
        self.createdDateAttr = attrHelper.addLineEditAttr(label='Created Date')
        self.createdByUserAttr = attrHelper.addLineEditAttr(label='Created By')
        self.latestVersionAttr = attrHelper.addLineEditAttr(label='Latest Version')
        self.approvedVersionAttr = attrHelper.addLineEditAttr(label='Approved Version')
        self.fileFormatAttr = attrHelper.addLineEditAttr(label='File Format')
