# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\assetOutgoingView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetsListWidget = QtWidgets.QListWidget(Form)
        self.assetsListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.assetsListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.assetsListWidget.setObjectName("assetsListWidget")
        item = QtWidgets.QListWidgetItem()
        self.assetsListWidget.addItem(item)
        self.verticalLayout.addWidget(self.assetsListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.assetsListWidget.isSortingEnabled()
        self.assetsListWidget.setSortingEnabled(False)
        item = self.assetsListWidget.item(0)
        item.setText(_translate("Form", "another asset"))
        self.assetsListWidget.setSortingEnabled(__sortingEnabled)

