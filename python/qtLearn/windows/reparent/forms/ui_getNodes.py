# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\reparent\forms\getNodes.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 46)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.childNodesLayout = QtWidgets.QHBoxLayout()
        self.childNodesLayout.setObjectName("childNodesLayout")
        self.childNodesLabel = QtWidgets.QLabel(Form)
        self.childNodesLabel.setObjectName("childNodesLabel")
        self.childNodesLayout.addWidget(self.childNodesLabel)
        self.verticalLayout.addLayout(self.childNodesLayout)
        self.parentNodeLayout = QtWidgets.QHBoxLayout()
        self.parentNodeLayout.setObjectName("parentNodeLayout")
        self.parentNodeLabel = QtWidgets.QLabel(Form)
        self.parentNodeLabel.setObjectName("parentNodeLabel")
        self.parentNodeLayout.addWidget(self.parentNodeLabel)
        self.verticalLayout.addLayout(self.parentNodeLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.childNodesLabel.setText(_translate("Form", "Children"))
        self.parentNodeLabel.setText(_translate("Form", "Parent"))

