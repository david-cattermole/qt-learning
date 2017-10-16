# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/searchBar.ui'
#
# Created: Mon Oct 16 23:43:55 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(774, 33)
        self.horizontalLayout = QtGui.QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectFilterComboBox = QtGui.QComboBox(Widget)
        self.projectFilterComboBox.setObjectName("projectFilterComboBox")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.projectFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectFilterComboBox)
        self.userFilterComboBox = QtGui.QComboBox(Widget)
        self.userFilterComboBox.setObjectName("userFilterComboBox")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.userFilterComboBox.addItem("")
        self.horizontalLayout.addWidget(self.userFilterComboBox)
        self.searchText = QtGui.QLineEdit(Widget)
        self.searchText.setAutoFillBackground(False)
        self.searchText.setObjectName("searchText")
        self.horizontalLayout.addWidget(self.searchText)
        self.clearButton = QtGui.QPushButton(Widget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.searchBarTypeComboBox = QtGui.QComboBox(Widget)
        self.searchBarTypeComboBox.setObjectName("searchBarTypeComboBox")
        self.searchBarTypeComboBox.addItem("")
        self.searchBarTypeComboBox.addItem("")
        self.searchBarTypeComboBox.addItem("")
        self.horizontalLayout.addWidget(self.searchBarTypeComboBox)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(0, QtGui.QApplication.translate("Widget", "All Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(1, QtGui.QApplication.translate("Widget", "project1", None, QtGui.QApplication.UnicodeUTF8))
        self.projectFilterComboBox.setItemText(2, QtGui.QApplication.translate("Widget", "project2", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(0, QtGui.QApplication.translate("Widget", "Current User", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(1, QtGui.QApplication.translate("Widget", "All Users", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(2, QtGui.QApplication.translate("Widget", "Upstream Users", None, QtGui.QApplication.UnicodeUTF8))
        self.userFilterComboBox.setItemText(3, QtGui.QApplication.translate("Widget", "Dowstream Users", None, QtGui.QApplication.UnicodeUTF8))
        self.searchText.setText(QtGui.QApplication.translate("Widget", "Search Text Here", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Widget", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBarTypeComboBox.setItemText(0, QtGui.QApplication.translate("Widget", "Basic", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBarTypeComboBox.setItemText(1, QtGui.QApplication.translate("Widget", "Tag Finder", None, QtGui.QApplication.UnicodeUTF8))
        self.searchBarTypeComboBox.setItemText(2, QtGui.QApplication.translate("Widget", "Search Conditions", None, QtGui.QApplication.UnicodeUTF8))

