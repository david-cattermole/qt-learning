# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/fileBrowser/forms/versionSelector.ui'
#
# Created: Sun Oct 22 22:21:46 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 215)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtGui.QTreeWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.treeWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Form", "version", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Form", "user", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Form", "v001", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).setText(1, QtGui.QApplication.translate("Form", "john", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("Form", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(1, QtGui.QApplication.translate("Form", "bob", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(2, QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Form", "v002", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(1, QtGui.QApplication.translate("Form", "davidc", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("Form", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(1, QtGui.QApplication.translate("Form", "davidc", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(2, QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("Form", "002", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).setText(1, QtGui.QApplication.translate("Form", "davidc", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).setText(2, QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("Form", "003", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).setText(1, QtGui.QApplication.translate("Form", "davidc", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).setText(2, QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).setText(0, QtGui.QApplication.translate("Form", "004", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).setText(1, QtGui.QApplication.translate("Form", "john", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(3).setText(2, QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(0, QtGui.QApplication.translate("Form", "v003", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).setText(1, QtGui.QApplication.translate("Form", "bob", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).child(0).setText(0, QtGui.QApplication.translate("Form", "001", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).child(0).setText(1, QtGui.QApplication.translate("Form", "bob", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(2).child(0).setText(2, QtGui.QApplication.translate("Form", "description", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

