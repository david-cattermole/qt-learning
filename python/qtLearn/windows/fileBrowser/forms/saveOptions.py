"""

"""

import Qt.QtGui as QtGui

import qtLearn.widgets.attributeHelper as attributeHelper
import qtLearn.windows.fileBrowser.forms.ui_saveOptions as ui_saveOptions
reload(ui_saveOptions)


class SaveOptions(QtGui.QWidget, ui_saveOptions.Ui_Form):
    def __init__(self):
        super(SaveOptions, self).__init__()
        self.setupUi(self)

        attrHelper = attributeHelper.AttributeHelper()
        attrHelper.setLayout(self.optionAttrWidgets)

        self.versionAttr = attrHelper.addComboBox2Attr(label='Version')
        self.formatAttr = attrHelper.addComboBoxAttr(label='File Format')
        self.descriptionAttr = attrHelper.addLineEditAttr(label='Description')
