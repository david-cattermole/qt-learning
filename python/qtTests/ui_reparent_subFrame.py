# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qtTests/ui/reparent_subFrame.ui'
#
# Created: Tue Jul 18 08:04:42 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(349, 66)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subFrameLayout = QtGui.QHBoxLayout()
        self.subFrameLayout.setObjectName("subFrameLayout")
        self.subFrameLabel = QtGui.QLabel(Form)
        self.subFrameLabel.setObjectName("subFrameLabel")
        self.subFrameLayout.addWidget(self.subFrameLabel)
        self.subFrameComboBox = QtGui.QComboBox(Form)
        self.subFrameComboBox.setObjectName("subFrameComboBox")
        self.subFrameLayout.addWidget(self.subFrameComboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.subFrameLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.subFrameLayout)
        self.subFrameOptionsLayout = QtGui.QFormLayout()
        self.subFrameOptionsLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.subFrameOptionsLayout.setObjectName("subFrameOptionsLayout")
        self.samplesLabel = QtGui.QLabel(Form)
        self.samplesLabel.setObjectName("samplesLabel")
        self.subFrameOptionsLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.samplesLabel)
        self.samplesSpinBox = QtGui.QSpinBox(Form)
        self.samplesSpinBox.setObjectName("samplesSpinBox")
        self.subFrameOptionsLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.samplesSpinBox)
        self.verticalLayout.addLayout(self.subFrameOptionsLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.subFrameLabel.setText(QtGui.QApplication.translate("Form", "Sub-Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.samplesLabel.setText(QtGui.QApplication.translate("Form", "Samples", None, QtGui.QApplication.UnicodeUTF8))

