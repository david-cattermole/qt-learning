# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\assetDependenciesView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(183, 380)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.incomingListWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incomingListWidget.sizePolicy().hasHeightForWidth())
        self.incomingListWidget.setSizePolicy(sizePolicy)
        self.incomingListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.incomingListWidget.setObjectName("incomingListWidget")
        item = QtWidgets.QListWidgetItem()
        self.incomingListWidget.addItem(item)
        self.verticalLayout.addWidget(self.incomingListWidget)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.outgoingListWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outgoingListWidget.sizePolicy().hasHeightForWidth())
        self.outgoingListWidget.setSizePolicy(sizePolicy)
        self.outgoingListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outgoingListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outgoingListWidget.setObjectName("outgoingListWidget")
        item = QtWidgets.QListWidgetItem()
        self.outgoingListWidget.addItem(item)
        self.verticalLayout.addWidget(self.outgoingListWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        self.checkBox.toggled['bool'].connect(self.incomingListWidget.setVisible)
        self.checkBox.toggled['bool'].connect(self.outgoingListWidget.setVisible)
        self.checkBox.toggled['bool'].connect(self.label.setVisible)
        self.checkBox.toggled['bool'].connect(self.label_2.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "Asset Dependencies"))
        self.label.setText(_translate("Form", "Incoming"))
        __sortingEnabled = self.incomingListWidget.isSortingEnabled()
        self.incomingListWidget.setSortingEnabled(False)
        item = self.incomingListWidget.item(0)
        item.setText(_translate("Form", "some asset"))
        self.incomingListWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "Outgoing"))
        __sortingEnabled = self.outgoingListWidget.isSortingEnabled()
        self.outgoingListWidget.setSortingEnabled(False)
        item = self.outgoingListWidget.item(0)
        item.setText(_translate("Form", "another asset"))
        self.outgoingListWidget.setSortingEnabled(__sortingEnabled)

