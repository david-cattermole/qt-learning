# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/assetBrowser/forms/searchBar.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(514, 20)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectFilterComboBox = QtGui.QComboBox(Form)
        self.projectFilterComboBox.setObjectName("projectFilterComboBox")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectFilterComboBox)
        self.comboBox = QtGui.QComboBox(Form)
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
        self.userFilterComboBox = QtGui.QComboBox(Form)
        self.userFilterComboBox.setObjectName("userFilterComboBox")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.userFilterComboBox)
        self.searchText = QtGui.QLineEdit(Form)
        self.searchText.setAutoFillBackground(False)
        self.searchText.setObjectName("searchText")
        self.horizontalLayout.addWidget(self.searchText)
        self.clearButton = QtGui.QToolButton(Form)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(0, QtGui.QApplication.translate("Form", "All Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(1, QtGui.QApplication.translate("Form", "project1", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(2, QtGui.QApplication.translate("Form", "project2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "All Departments", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Form", "Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Form", "Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Form", "CFX", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Form", "FX", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("Form", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("Form", "Comp", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(0, QtGui.QApplication.translate("Form", "Current User", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(1, QtGui.QApplication.translate("Form", "All Users", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(2, QtGui.QApplication.translate("Form", "Upstream Users", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(3, QtGui.QApplication.translate("Form", "Dowstream Users", None, QtGui.QApplication.UnicodeUTF8))
        self.searchText.setPlaceholderText(QtGui.QApplication.translate("Form", "Search Text Here", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))

