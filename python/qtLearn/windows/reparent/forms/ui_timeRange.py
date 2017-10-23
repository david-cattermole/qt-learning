# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\reparent\forms\timeRange.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 104)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeRangeLayout = QtWidgets.QHBoxLayout()
        self.timeRangeLayout.setObjectName("timeRangeLayout")
        self.timeRangeLabel = QtWidgets.QLabel(Form)
        self.timeRangeLabel.setObjectName("timeRangeLabel")
        self.timeRangeLayout.addWidget(self.timeRangeLabel)
        self.timeRangeComboBox = QtWidgets.QComboBox(Form)
        self.timeRangeComboBox.setObjectName("timeRangeComboBox")
        self.timeRangeLayout.addWidget(self.timeRangeComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timeRangeLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.timeRangeLayout)
        self.frameLayout = QtWidgets.QFormLayout()
        self.frameLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.frameLayout.setObjectName("frameLayout")
        self.startFrameLabel = QtWidgets.QLabel(Form)
        self.startFrameLabel.setObjectName("startFrameLabel")
        self.frameLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startFrameLabel)
        self.endFrameLabel = QtWidgets.QLabel(Form)
        self.endFrameLabel.setObjectName("endFrameLabel")
        self.frameLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.endFrameLabel)
        self.endFrameSpinBox = QtWidgets.QSpinBox(Form)
        self.endFrameSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.endFrameSpinBox.setMinimum(-999999)
        self.endFrameSpinBox.setMaximum(999999)
        self.endFrameSpinBox.setProperty("value", 1101)
        self.endFrameSpinBox.setObjectName("endFrameSpinBox")
        self.frameLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endFrameSpinBox)
        self.startFrameSpinBox = QtWidgets.QSpinBox(Form)
        self.startFrameSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.startFrameSpinBox.setMinimum(-999999)
        self.startFrameSpinBox.setMaximum(999999)
        self.startFrameSpinBox.setProperty("value", 1001)
        self.startFrameSpinBox.setObjectName("startFrameSpinBox")
        self.frameLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startFrameSpinBox)
        self.verticalLayout.addLayout(self.frameLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeRangeLabel.setText(_translate("Form", "Time Range"))
        self.startFrameLabel.setText(_translate("Form", "Start"))
        self.endFrameLabel.setText(_translate("Form", "End"))

