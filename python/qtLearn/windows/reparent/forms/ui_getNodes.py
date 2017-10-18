# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/reparent/forms/getNodes.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 46)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.childNodesLayout = QtGui.QHBoxLayout()
        self.childNodesLayout.setObjectName("childNodesLayout")
        self.childNodesLabel = QtGui.QLabel(Form)
        self.childNodesLabel.setObjectName("childNodesLabel")
        self.childNodesLayout.addWidget(self.childNodesLabel)
        self.verticalLayout.addLayout(self.childNodesLayout)
        self.parentNodeLayout = QtGui.QHBoxLayout()
        self.parentNodeLayout.setObjectName("parentNodeLayout")
        self.parentNodeLabel = QtGui.QLabel(Form)
        self.parentNodeLabel.setObjectName("parentNodeLabel")
        self.parentNodeLayout.addWidget(self.parentNodeLabel)
        self.verticalLayout.addLayout(self.parentNodeLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.childNodesLabel.setText(QtGui.QApplication.translate("Form", "Children", None, QtGui.QApplication.UnicodeUTF8))
        self.parentNodeLabel.setText(QtGui.QApplication.translate("Form", "Parent", None, QtGui.QApplication.UnicodeUTF8))

