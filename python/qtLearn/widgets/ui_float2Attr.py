# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\widgets\float2Attr.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(403, 20)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(Widget)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.horizontalLayout.addWidget(self.doubleSpinBox_1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Widget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout.addWidget(self.doubleSpinBox_2)
        spacerItem = QtWidgets.QSpacerItem(237, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.label.setText(_translate("Widget", "Text"))

