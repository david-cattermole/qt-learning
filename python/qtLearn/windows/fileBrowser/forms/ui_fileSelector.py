# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/fileBrowser/forms/fileSelector.ui'
#
# Created: Sun Oct 22 22:21:46 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 215)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.treeWidget_2 = QtGui.QTreeWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.treeWidget_2.setFont(font)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.treeWidget_2.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.treeWidget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(0, QtGui.QApplication.translate("Form", "filename", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, QtGui.QApplication.translate("Form", "layout", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("Form", "camera", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("Form", "environment", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("Form", "layout", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)

