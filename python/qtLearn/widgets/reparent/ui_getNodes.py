# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/reparent/getNodes.ui'
#
# Created: Mon Oct 16 23:43:55 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(395, 46)
        self.verticalLayout = QtGui.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.childNodesLayout = QtGui.QHBoxLayout()
        self.childNodesLayout.setObjectName("childNodesLayout")
        self.childNodesLabel = QtGui.QLabel(Widget)
        self.childNodesLabel.setObjectName("childNodesLabel")
        self.childNodesLayout.addWidget(self.childNodesLabel)
        self.verticalLayout.addLayout(self.childNodesLayout)
        self.parentNodeLayout = QtGui.QHBoxLayout()
        self.parentNodeLayout.setObjectName("parentNodeLayout")
        self.parentNodeLabel = QtGui.QLabel(Widget)
        self.parentNodeLabel.setObjectName("parentNodeLabel")
        self.parentNodeLayout.addWidget(self.parentNodeLabel)
        self.verticalLayout.addLayout(self.parentNodeLayout)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.childNodesLabel.setText(QtGui.QApplication.translate("Widget", "Children", None, QtGui.QApplication.UnicodeUTF8))
        self.parentNodeLabel.setText(QtGui.QApplication.translate("Widget", "Parent", None, QtGui.QApplication.UnicodeUTF8))

