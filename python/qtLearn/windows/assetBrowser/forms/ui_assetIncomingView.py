# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\assetIncomingView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(122, 127)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.assetsListWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetsListWidget.sizePolicy().hasHeightForWidth())
        self.assetsListWidget.setSizePolicy(sizePolicy)
        self.assetsListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.assetsListWidget.setObjectName("assetsListWidget")
        item = QtWidgets.QListWidgetItem()
        self.assetsListWidget.addItem(item)
        self.verticalLayout.addWidget(self.assetsListWidget)

        self.retranslateUi(Form)
        self.checkBox.toggled['bool'].connect(self.assetsListWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "Asset Incoming View"))
        __sortingEnabled = self.assetsListWidget.isSortingEnabled()
        self.assetsListWidget.setSortingEnabled(False)
        item = self.assetsListWidget.item(0)
        item.setText(_translate("Form", "some asset"))
        self.assetsListWidget.setSortingEnabled(__sortingEnabled)

