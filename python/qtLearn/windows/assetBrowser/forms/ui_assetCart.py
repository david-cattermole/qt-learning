# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\assetCart.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 288)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addButton = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_6.addWidget(self.addButton)
        self.replaceButton = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replaceButton.sizePolicy().hasHeightForWidth())
        self.replaceButton.setSizePolicy(sizePolicy)
        self.replaceButton.setObjectName("replaceButton")
        self.horizontalLayout_6.addWidget(self.replaceButton)
        self.removeButton = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_6.addWidget(self.removeButton)
        self.clearButton = QtWidgets.QToolButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_6.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.assetListWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetListWidget.sizePolicy().hasHeightForWidth())
        self.assetListWidget.setSizePolicy(sizePolicy)
        self.assetListWidget.setObjectName("assetListWidget")
        item = QtWidgets.QListWidgetItem()
        self.assetListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.assetListWidget.addItem(item)
        self.verticalLayout.addWidget(self.assetListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Asset Cart"))
        self.addButton.setText(_translate("Form", "Add"))
        self.replaceButton.setText(_translate("Form", "Replace"))
        self.removeButton.setText(_translate("Form", "Remove"))
        self.clearButton.setText(_translate("Form", "Clear..."))
        __sortingEnabled = self.assetListWidget.isSortingEnabled()
        self.assetListWidget.setSortingEnabled(False)
        item = self.assetListWidget.item(0)
        item.setText(_translate("Form", "john rig v001"))
        item = self.assetListWidget.item(1)
        item.setText(_translate("Form", "john rig v002"))
        self.assetListWidget.setSortingEnabled(__sortingEnabled)

