# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\shotView.ui'
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
        self.shotsTreeWidget = QtWidgets.QTreeWidget(Form)
        self.shotsTreeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.shotsTreeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.shotsTreeWidget.setObjectName("shotsTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.shotsTreeWidget)
        self.addShotsButton = QtWidgets.QPushButton(Form)
        self.addShotsButton.setObjectName("addShotsButton")
        self.verticalLayout.addWidget(self.addShotsButton)
        self.clearAllButton = QtWidgets.QPushButton(Form)
        self.clearAllButton.setObjectName("clearAllButton")
        self.verticalLayout.addWidget(self.clearAllButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.shotsTreeWidget.headerItem().setText(0, _translate("Form", "Sequences / Shots"))
        __sortingEnabled = self.shotsTreeWidget.isSortingEnabled()
        self.shotsTreeWidget.setSortingEnabled(False)
        self.shotsTreeWidget.topLevelItem(0).setText(0, _translate("Form", "sh"))
        self.shotsTreeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "sh0010"))
        self.shotsTreeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "sh0020"))
        self.shotsTreeWidget.topLevelItem(1).setText(0, _translate("Form", "fin"))
        self.shotsTreeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "fin010"))
        self.shotsTreeWidget.setSortingEnabled(__sortingEnabled)
        self.addShotsButton.setText(_translate("Form", "Add Shots..."))
        self.clearAllButton.setText(_translate("Form", "Clear All..."))

