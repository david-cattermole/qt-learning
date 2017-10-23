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
        Form.resize(774, 33)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectFilterComboBox = QtWidgets.QComboBox(Form)
        self.projectFilterComboBox.setObjectName("projectFilterComboBox")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectFilterComboBox)
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
        self.searchText.setObjectName("searchText")
        self.horizontalLayout.addWidget(self.searchText)
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.searchBarTypeComboBox = QtWidgets.QComboBox(Form)
        self.searchBarTypeComboBox.setObjectName("searchBarTypeComboBox")
        self.searchBarTypeComboBox.addItem("")
        self.searchBarTypeComboBox.addItem("")
        self.searchBarTypeComboBox.addItem("")
        self.horizontalLayout.addWidget(self.searchBarTypeComboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.projectFilterComboBox.setItemText(0, _translate("Form", "All Projects"))
        self.projectFilterComboBox.setItemText(1, _translate("Form", "project1"))
        self.projectFilterComboBox.setItemText(2, _translate("Form", "project2"))
        self.userFilterComboBox.setItemText(0, _translate("Form", "Current User"))
        self.userFilterComboBox.setItemText(1, _translate("Form", "All Users"))
        self.userFilterComboBox.setItemText(2, _translate("Form", "Upstream Users"))
        self.userFilterComboBox.setItemText(3, _translate("Form", "Dowstream Users"))
        self.searchText.setText(_translate("Form", "Search Text Here"))
        self.clearButton.setText(_translate("Form", "Clear"))
        self.searchBarTypeComboBox.setItemText(0, _translate("Form", "Basic"))
        self.searchBarTypeComboBox.setItemText(1, _translate("Form", "Tag Finder"))
        self.searchBarTypeComboBox.setItemText(2, _translate("Form", "Search Conditions"))

