# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\reparent\reparent.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(4, 4, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nodesGroupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesGroupBox.sizePolicy().hasHeightForWidth())
        self.nodesGroupBox.setSizePolicy(sizePolicy)
        self.nodesGroupBox.setObjectName("nodesGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.nodesGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nodesLayout = QtWidgets.QVBoxLayout()
        self.nodesLayout.setObjectName("nodesLayout")
        self.verticalLayout_2.addLayout(self.nodesLayout)
        self.verticalLayout.addWidget(self.nodesGroupBox)
        self.timeRangeGroupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeRangeGroupBox.sizePolicy().hasHeightForWidth())
        self.timeRangeGroupBox.setSizePolicy(sizePolicy)
        self.timeRangeGroupBox.setObjectName("timeRangeGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.timeRangeGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.timeRangeLayout = QtWidgets.QVBoxLayout()
        self.timeRangeLayout.setObjectName("timeRangeLayout")
        self.verticalLayout_4.addLayout(self.timeRangeLayout)
        self.verticalLayout.addWidget(self.timeRangeGroupBox)
        self.subFrameGroupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subFrameGroupBox.sizePolicy().hasHeightForWidth())
        self.subFrameGroupBox.setSizePolicy(sizePolicy)
        self.subFrameGroupBox.setObjectName("subFrameGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.subFrameGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.subFrameLayout = QtWidgets.QVBoxLayout()
        self.subFrameLayout.setObjectName("subFrameLayout")
        self.verticalLayout_3.addLayout(self.subFrameLayout)
        self.verticalLayout.addWidget(self.subFrameGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nodesGroupBox.setTitle(_translate("Form", "Nodes"))
        self.timeRangeGroupBox.setTitle(_translate("Form", "Time Range"))
        self.subFrameGroupBox.setTitle(_translate("Form", "Sub-Frame"))

