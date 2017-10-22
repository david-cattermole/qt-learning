# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/widgets/float3Attr.ui'
#
# Created: Sun Oct 22 22:21:47 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(393, 33)
        self.horizontalLayout = QtGui.QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox_1 = QtGui.QDoubleSpinBox(Widget)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.horizontalLayout.addWidget(self.doubleSpinBox_1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(Widget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout.addWidget(self.doubleSpinBox_2)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(Widget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.horizontalLayout.addWidget(self.doubleSpinBox_3)
        spacerItem = QtGui.QSpacerItem(237, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Widget", "Text", None, QtGui.QApplication.UnicodeUTF8))

