# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\fileBrowser\forms\versionSelector.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(338, 215)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.fileFormatLabel = QtWidgets.QLabel(Form)
        self.fileFormatLabel.setObjectName("fileFormatLabel")
        self.horizontalLayout.addWidget(self.fileFormatLabel)
        self.fileFormatComboBox = QtWidgets.QComboBox(Form)
        self.fileFormatComboBox.setObjectName("fileFormatComboBox")
        self.fileFormatComboBox.addItem("")
        self.fileFormatComboBox.addItem("")
        self.fileFormatComboBox.addItem("")
        self.horizontalLayout.addWidget(self.fileFormatComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeView = QtWidgets.QTreeView(Form)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fileFormatLabel.setText(_translate("Form", "File Format"))
        self.fileFormatComboBox.setItemText(0, _translate("Form", "<all file formats>"))
        self.fileFormatComboBox.setItemText(1, _translate("Form", "Maya Binary"))
        self.fileFormatComboBox.setItemText(2, _translate("Form", "Maya ASCII"))

