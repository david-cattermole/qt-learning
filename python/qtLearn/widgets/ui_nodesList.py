# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\widgets\nodesList.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(418, 62)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.buttonsVerticalLayout = QtWidgets.QVBoxLayout()
        self.buttonsVerticalLayout.setObjectName("buttonsVerticalLayout")
        self.getSelectionButton = QtWidgets.QPushButton(Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getSelectionButton.sizePolicy().hasHeightForWidth())
        self.getSelectionButton.setSizePolicy(sizePolicy)
        self.getSelectionButton.setFlat(False)
        self.getSelectionButton.setObjectName("getSelectionButton")
        self.buttonsVerticalLayout.addWidget(self.getSelectionButton)
        self.clearButton = QtWidgets.QPushButton(Widget)
        self.clearButton.setObjectName("clearButton")
        self.buttonsVerticalLayout.addWidget(self.clearButton)
        self.horizontalLayout.addLayout(self.buttonsVerticalLayout)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.getSelectionButton.setText(_translate("Widget", "Get Sel"))
        self.clearButton.setText(_translate("Widget", "Clear"))

