# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\searchBar.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(514, 20)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectFilterComboBox = QtWidgets.QComboBox(Form)
        self.projectFilterComboBox.setObjectName("projectFilterComboBox")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectFilterComboBox)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.userFilterComboBox = QtWidgets.QComboBox(Form)
        self.userFilterComboBox.setObjectName("userFilterComboBox")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.userFilterComboBox)
        self.searchText = QtWidgets.QLineEdit(Form)
        self.searchText.setAutoFillBackground(False)
        self.searchText.setInputMask("")
        self.searchText.setText("")
        self.searchText.setObjectName("searchText")
        self.horizontalLayout.addWidget(self.searchText)
        self.clearButton = QtWidgets.QToolButton(Form)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.projectFilterComboBox.setItemText(0, _translate("Form", "All Projects"))
        self.projectFilterComboBox.setItemText(1, _translate("Form", "project1"))
        self.projectFilterComboBox.setItemText(2, _translate("Form", "project2"))
        self.comboBox.setItemText(0, _translate("Form", "All Departments"))
        self.comboBox.setItemText(1, _translate("Form", "Camera"))
        self.comboBox.setItemText(2, _translate("Form", "Layout"))
        self.comboBox.setItemText(3, _translate("Form", "Animation"))
        self.comboBox.setItemText(4, _translate("Form", "CFX"))
        self.comboBox.setItemText(5, _translate("Form", "FX"))
        self.comboBox.setItemText(6, _translate("Form", "Light"))
        self.comboBox.setItemText(7, _translate("Form", "Comp"))
        self.userFilterComboBox.setItemText(0, _translate("Form", "Current User"))
        self.userFilterComboBox.setItemText(1, _translate("Form", "All Users"))
        self.userFilterComboBox.setItemText(2, _translate("Form", "Upstream Users"))
        self.userFilterComboBox.setItemText(3, _translate("Form", "Dowstream Users"))
        self.searchText.setPlaceholderText(_translate("Form", "Search Text Here"))
        self.clearButton.setText(_translate("Form", "Clear"))

