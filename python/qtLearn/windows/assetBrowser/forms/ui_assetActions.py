# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\assetActions.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 109)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.copyPasteLayout = QtWidgets.QHBoxLayout()
        self.copyPasteLayout.setSpacing(3)
        self.copyPasteLayout.setObjectName("copyPasteLayout")
        self.copyToClipboardButton = QtWidgets.QToolButton(self.frame)
        self.copyToClipboardButton.setObjectName("copyToClipboardButton")
        self.copyPasteLayout.addWidget(self.copyToClipboardButton)
        self.pasteFromClipboardButton = QtWidgets.QToolButton(self.frame)
        self.pasteFromClipboardButton.setObjectName("pasteFromClipboardButton")
        self.copyPasteLayout.addWidget(self.pasteFromClipboardButton)
        self.verticalLayout_2.addLayout(self.copyPasteLayout)
        self.line_1 = QtWidgets.QFrame(self.frame)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.verticalLayout_2.addWidget(self.line_1)
        self.openLayout = QtWidgets.QHBoxLayout()
        self.openLayout.setSpacing(3)
        self.openLayout.setObjectName("openLayout")
        self.openButton = QtWidgets.QToolButton(self.frame)
        self.openButton.setObjectName("openButton")
        self.openLayout.addWidget(self.openButton)
        self.loadButton = QtWidgets.QToolButton(self.frame)
        self.loadButton.setObjectName("loadButton")
        self.openLayout.addWidget(self.loadButton)
        self.playButton = QtWidgets.QToolButton(self.frame)
        self.playButton.setObjectName("playButton")
        self.openLayout.addWidget(self.playButton)
        self.verticalLayout_2.addLayout(self.openLayout)
        self.processLayout = QtWidgets.QHBoxLayout()
        self.processLayout.setSpacing(3)
        self.processLayout.setObjectName("processLayout")
        self.reviewButton = QtWidgets.QToolButton(self.frame)
        self.reviewButton.setObjectName("reviewButton")
        self.processLayout.addWidget(self.reviewButton)
        self.sendButton = QtWidgets.QToolButton(self.frame)
        self.sendButton.setObjectName("sendButton")
        self.processLayout.addWidget(self.sendButton)
        self.approveButton = QtWidgets.QToolButton(self.frame)
        self.approveButton.setObjectName("approveButton")
        self.processLayout.addWidget(self.approveButton)
        self.verticalLayout_2.addLayout(self.processLayout)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.deleteLayout = QtWidgets.QHBoxLayout()
        self.deleteLayout.setSpacing(3)
        self.deleteLayout.setObjectName("deleteLayout")
        self.deleteButton = QtWidgets.QToolButton(self.frame)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteLayout.addWidget(self.deleteButton)
        self.verticalLayout_2.addLayout(self.deleteLayout)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.copyToClipboardButton.setText(_translate("Form", "Copy"))
        self.pasteFromClipboardButton.setText(_translate("Form", "Paste"))
        self.openButton.setText(_translate("Form", "Open..."))
        self.loadButton.setText(_translate("Form", "Load..."))
        self.playButton.setText(_translate("Form", "Play...."))
        self.reviewButton.setText(_translate("Form", "Review..."))
        self.sendButton.setText(_translate("Form", "Send..."))
        self.approveButton.setText(_translate("Form", "Approve..."))
        self.deleteButton.setText(_translate("Form", "Delete..."))

