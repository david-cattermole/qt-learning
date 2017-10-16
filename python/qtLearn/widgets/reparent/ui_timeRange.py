# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/reparent/timeRange.ui'
#
# Created: Mon Oct 16 23:43:55 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(350, 104)
        self.verticalLayout = QtGui.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeRangeLayout = QtGui.QHBoxLayout()
        self.timeRangeLayout.setObjectName("timeRangeLayout")
        self.timeRangeLabel = QtGui.QLabel(Widget)
        self.timeRangeLabel.setObjectName("timeRangeLabel")
        self.timeRangeLayout.addWidget(self.timeRangeLabel)
        self.timeRangeComboBox = QtGui.QComboBox(Widget)
        self.timeRangeComboBox.setObjectName("timeRangeComboBox")
        self.timeRangeLayout.addWidget(self.timeRangeComboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.timeRangeLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.timeRangeLayout)
        self.frameLayout = QtGui.QFormLayout()
        self.frameLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.frameLayout.setObjectName("frameLayout")
        self.startFrameLabel = QtGui.QLabel(Widget)
        self.startFrameLabel.setObjectName("startFrameLabel")
        self.frameLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.startFrameLabel)
        self.endFrameLabel = QtGui.QLabel(Widget)
        self.endFrameLabel.setObjectName("endFrameLabel")
        self.frameLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.endFrameLabel)
        self.endFrameSpinBox = QtGui.QSpinBox(Widget)
        self.endFrameSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.endFrameSpinBox.setMinimum(-999999)
        self.endFrameSpinBox.setMaximum(999999)
        self.endFrameSpinBox.setProperty("value", 1101)
        self.endFrameSpinBox.setObjectName("endFrameSpinBox")
        self.frameLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.endFrameSpinBox)
        self.startFrameSpinBox = QtGui.QSpinBox(Widget)
        self.startFrameSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.startFrameSpinBox.setMinimum(-999999)
        self.startFrameSpinBox.setMaximum(999999)
        self.startFrameSpinBox.setProperty("value", 1001)
        self.startFrameSpinBox.setObjectName("startFrameSpinBox")
        self.frameLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.startFrameSpinBox)
        self.verticalLayout.addLayout(self.frameLayout)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.timeRangeLabel.setText(QtGui.QApplication.translate("Widget", "Time Range", None, QtGui.QApplication.UnicodeUTF8))
        self.startFrameLabel.setText(QtGui.QApplication.translate("Widget", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.endFrameLabel.setText(QtGui.QApplication.translate("Widget", "End", None, QtGui.QApplication.UnicodeUTF8))

