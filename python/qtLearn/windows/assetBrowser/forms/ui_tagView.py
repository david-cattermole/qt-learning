# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\tagView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(172, 140)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tagsListWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsListWidget.sizePolicy().hasHeightForWidth())
        self.tagsListWidget.setSizePolicy(sizePolicy)
        self.tagsListWidget.setObjectName("tagsListWidget")
        item = QtWidgets.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.tagsListWidget.addItem(item)
        self.verticalLayout.addWidget(self.tagsListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Tags"))
        __sortingEnabled = self.tagsListWidget.isSortingEnabled()
        self.tagsListWidget.setSortingEnabled(False)
        item = self.tagsListWidget.item(0)
        item.setText(_translate("Form", "tag1"))
        item = self.tagsListWidget.item(1)
        item.setText(_translate("Form", "tag2"))
        item = self.tagsListWidget.item(2)
        item.setText(_translate("Form", "tag2"))
        item = self.tagsListWidget.item(3)
        item.setText(_translate("Form", "tag3"))
        item = self.tagsListWidget.item(4)
        item.setText(_translate("Form", "tag4"))
        item = self.tagsListWidget.item(5)
        item.setText(_translate("Form", "tag5"))
        self.tagsListWidget.setSortingEnabled(__sortingEnabled)

