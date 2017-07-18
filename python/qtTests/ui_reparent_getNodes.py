# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qtTests/ui/reparent_getNodes.ui'
#
# Created: Tue Jul 18 08:04:42 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(329, 65)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.getChildNodesStub = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getChildNodesStub.sizePolicy().hasHeightForWidth())
        self.getChildNodesStub.setSizePolicy(sizePolicy)
        self.getChildNodesStub.setObjectName("getChildNodesStub")
        self.verticalLayout.addWidget(self.getChildNodesStub)
        self.getParentNodeStub = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getParentNodeStub.sizePolicy().hasHeightForWidth())
        self.getParentNodeStub.setSizePolicy(sizePolicy)
        self.getParentNodeStub.setObjectName("getParentNodeStub")
        self.verticalLayout.addWidget(self.getParentNodeStub)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

