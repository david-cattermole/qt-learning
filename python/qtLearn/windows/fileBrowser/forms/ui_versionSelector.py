# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/fileBrowser/forms/versionSelector.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(338, 215)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.fileFormatLabel = QtGui.QLabel(Form)
        self.fileFormatLabel.setObjectName("fileFormatLabel")
        self.horizontalLayout.addWidget(self.fileFormatLabel)
        self.fileFormatComboBox = QtGui.QComboBox(Form)
        self.fileFormatComboBox.setObjectName("fileFormatComboBox")
        self.fileFormatComboBox.addItem("")
        self.fileFormatComboBox.addItem("")
        self.fileFormatComboBox.addItem("")
        self.horizontalLayout.addWidget(self.fileFormatComboBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeView = QtGui.QTreeView(Form)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.fileFormatLabel.setText(QtGui.QApplication.translate("Form", "File Format", None, QtGui.QApplication.UnicodeUTF8))
        self.fileFormatComboBox.setItemText(0, QtGui.QApplication.translate("Form", "<all file formats>", None, QtGui.QApplication.UnicodeUTF8))
        self.fileFormatComboBox.setItemText(1, QtGui.QApplication.translate("Form", "Maya Binary", None, QtGui.QApplication.UnicodeUTF8))
        self.fileFormatComboBox.setItemText(2, QtGui.QApplication.translate("Form", "Maya ASCII", None, QtGui.QApplication.UnicodeUTF8))

