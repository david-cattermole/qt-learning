# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/widgets/floatAttr.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(403, 20)
        self.horizontalLayout = QtGui.QHBoxLayout(Widget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Widget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        spacerItem = QtGui.QSpacerItem(250, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Widget", "Text", None, QtGui.QApplication.UnicodeUTF8))

