# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/widgets/projectSeqShotComboBox.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(261, 20)
        self.horizontalLayout = QtGui.QHBoxLayout(Widget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.projectComboBox = QtGui.QComboBox(Widget)
        self.projectComboBox.setObjectName("projectComboBox")
        self.projectComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectComboBox)
        self.sequenceComboBox = QtGui.QComboBox(Widget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.sequenceComboBox.setFont(font)
        self.sequenceComboBox.setObjectName("sequenceComboBox")
        self.sequenceComboBox.addItem("")
        self.horizontalLayout.addWidget(self.sequenceComboBox)
        self.shotComboBox = QtGui.QComboBox(Widget)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.shotComboBox.setFont(font)
        self.shotComboBox.setObjectName("shotComboBox")
        self.shotComboBox.addItem("")
        self.horizontalLayout.addWidget(self.shotComboBox)
        self.label.setBuddy(self.projectComboBox)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        Widget.setTabOrder(self.projectComboBox, self.sequenceComboBox)
        Widget.setTabOrder(self.sequenceComboBox, self.shotComboBox)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Widget", "Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.projectComboBox.setItemText(0, QtGui.QApplication.translate("Widget", "project", None, QtGui.QApplication.UnicodeUTF8))
        self.sequenceComboBox.setItemText(0, QtGui.QApplication.translate("Widget", "seq", None, QtGui.QApplication.UnicodeUTF8))
        self.shotComboBox.setItemText(0, QtGui.QApplication.translate("Widget", "shot", None, QtGui.QApplication.UnicodeUTF8))

