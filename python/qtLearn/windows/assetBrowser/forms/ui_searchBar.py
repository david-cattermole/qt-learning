# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/assetBrowser/forms/searchBar.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(774, 33)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectFilterComboBox = QtGui.QComboBox(Form)
        self.projectFilterComboBox.setObjectName("projectFilterComboBox")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectFilterComboBox)
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
        self.clearButton = QtGui.QPushButton(Form)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.searchBarTypeComboBox = QtGui.QComboBox(Form)
        self.searchBarTypeComboBox.setObjectName("searchBarTypeComboBox")
        self.searchBarTypeComboBox.addItem("")
        self.searchBarTypeComboBox.addItem("")
        self.searchBarTypeComboBox.addItem("")
        self.horizontalLayout.addWidget(self.searchBarTypeComboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(0, QtGui.QApplication.translate("Form", "All Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(1, QtGui.QApplication.translate("Form", "project1", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(2, QtGui.QApplication.translate("Form", "project2", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(0, QtGui.QApplication.translate("Form", "Current User", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(1, QtGui.QApplication.translate("Form", "All Users", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(2, QtGui.QApplication.translate("Form", "Upstream Users", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(3, QtGui.QApplication.translate("Form", "Dowstream Users", None, QtGui.QApplication.UnicodeUTF8))
        self.searchText.setText(QtGui.QApplication.translate("Form", "Search Text Here", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBarTypeComboBox.setItemText(0, QtGui.QApplication.translate("Form", "Basic", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBarTypeComboBox.setItemText(1, QtGui.QApplication.translate("Form", "Tag Finder", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBarTypeComboBox.setItemText(2, QtGui.QApplication.translate("Form", "Search Conditions", None, QtGui.QApplication.UnicodeUTF8))

