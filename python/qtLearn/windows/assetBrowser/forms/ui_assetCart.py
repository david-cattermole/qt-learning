# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/assetBrowser/forms/assetCart.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addButton = QtGui.QPushButton(Form)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_6.addWidget(self.addButton)
        self.replaceButton = QtGui.QPushButton(Form)
        self.replaceButton.setObjectName("replaceButton")
        self.horizontalLayout_6.addWidget(self.replaceButton)
        self.clearButton = QtGui.QPushButton(Form)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_6.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.assetListWidget = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetListWidget.sizePolicy().hasHeightForWidth())
        self.assetListWidget.setSizePolicy(sizePolicy)
        self.assetListWidget.setObjectName("assetListWidget")
        QtGui.QListWidgetItem(self.assetListWidget)
        QtGui.QListWidgetItem(self.assetListWidget)
        self.verticalLayout.addWidget(self.assetListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Asset Cart", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setText(QtGui.QApplication.translate("Form", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.assetListWidget.isSortingEnabled()
        self.assetListWidget.setSortingEnabled(False)
        self.assetListWidget.item(0).setText(QtGui.QApplication.translate("Form", "john rig v001", None, QtGui.QApplication.UnicodeUTF8))
        self.assetListWidget.item(1).setText(QtGui.QApplication.translate("Form", "john rig v002", None, QtGui.QApplication.UnicodeUTF8))
        self.assetListWidget.setSortingEnabled(__sortingEnabled)

