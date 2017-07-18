# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qtTests/ui/reparent_timeRange.ui'
#
# Created: Tue Jul 18 08:04:42 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 104)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeRangeLayout = QtGui.QHBoxLayout()
        self.timeRangeLayout.setObjectName("timeRangeLayout")
        self.timeRangeLabel = QtGui.QLabel(Form)
        self.timeRangeLabel.setObjectName("timeRangeLabel")
        self.timeRangeLayout.addWidget(self.timeRangeLabel)
        self.timeRangeComboBox = QtGui.QComboBox(Form)
        self.timeRangeComboBox.setObjectName("timeRangeComboBox")
        self.timeRangeLayout.addWidget(self.timeRangeComboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.timeRangeLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.timeRangeLayout)
        self.frameLayout = QtGui.QFormLayout()
        self.frameLayout.setObjectName("frameLayout")
        self.startFrameLabel = QtGui.QLabel(Form)
        self.startFrameLabel.setObjectName("startFrameLabel")
        self.frameLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.startFrameLabel)
        self.startFrameSpinBox = QtGui.QSpinBox(Form)
        self.startFrameSpinBox.setMinimum(-999999)
        self.startFrameSpinBox.setMaximum(999999)
        self.startFrameSpinBox.setProperty("value", 1001)
        self.startFrameSpinBox.setObjectName("startFrameSpinBox")
        self.frameLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.startFrameSpinBox)
        self.endFrameLabel = QtGui.QLabel(Form)
        self.endFrameLabel.setObjectName("endFrameLabel")
        self.frameLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.endFrameLabel)
        self.endFrameSpinBox = QtGui.QSpinBox(Form)
        self.endFrameSpinBox.setMinimum(-999999)
        self.endFrameSpinBox.setMaximum(999999)
        self.endFrameSpinBox.setProperty("value", 1101)
        self.endFrameSpinBox.setObjectName("endFrameSpinBox")
        self.frameLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.endFrameSpinBox)
        self.verticalLayout.addLayout(self.frameLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.timeRangeLabel.setText(QtGui.QApplication.translate("Form", "Time Range", None, QtGui.QApplication.UnicodeUTF8))
        self.startFrameLabel.setText(QtGui.QApplication.translate("Form", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.endFrameLabel.setText(QtGui.QApplication.translate("Form", "End", None, QtGui.QApplication.UnicodeUTF8))

