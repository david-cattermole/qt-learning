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
        Form.resize(136, 326)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetThumbnailIcon = QtWidgets.QGraphicsView(Form)
        self.assetThumbnailIcon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetThumbnailIcon.sizePolicy().hasHeightForWidth())
        self.assetThumbnailIcon.setSizePolicy(sizePolicy)
        self.assetThumbnailIcon.setMaximumSize(QtCore.QSize(128, 128))
        self.assetThumbnailIcon.setObjectName("assetThumbnailIcon")
        self.verticalLayout.addWidget(self.assetThumbnailIcon)
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setObjectName("playButton")
        self.verticalLayout.addWidget(self.playButton)
        self.openButton = QtWidgets.QPushButton(Form)
        self.openButton.setObjectName("openButton")
        self.verticalLayout.addWidget(self.openButton)
        self.openBrowserButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openBrowserButton.sizePolicy().hasHeightForWidth())
        self.openBrowserButton.setSizePolicy(sizePolicy)
        self.openBrowserButton.setObjectName("openBrowserButton")
        self.verticalLayout.addWidget(self.openBrowserButton)
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout.addWidget(self.sendButton)
        spacerItem = QtWidgets.QSpacerItem(125, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.playButton.setText(_translate("Form", "Play...."))
        self.openButton.setText(_translate("Form", "Open..."))
        self.openBrowserButton.setText(_translate("Form", "Browser..."))
        self.sendButton.setText(_translate("Form", "Send..."))

