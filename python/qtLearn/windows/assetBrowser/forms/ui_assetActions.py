# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/assetBrowser/forms/assetActions.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(136, 326)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetThumbnailIcon = QtGui.QGraphicsView(Form)
        self.assetThumbnailIcon.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetThumbnailIcon.sizePolicy().hasHeightForWidth())
        self.assetThumbnailIcon.setSizePolicy(sizePolicy)
        self.assetThumbnailIcon.setMaximumSize(QtCore.QSize(128, 128))
        self.assetThumbnailIcon.setObjectName("assetThumbnailIcon")
        self.verticalLayout.addWidget(self.assetThumbnailIcon)
        self.playButton = QtGui.QPushButton(Form)
        self.playButton.setObjectName("playButton")
        self.verticalLayout.addWidget(self.playButton)
        self.openButton = QtGui.QPushButton(Form)
        self.openButton.setObjectName("openButton")
        self.verticalLayout.addWidget(self.openButton)
        self.openBrowserButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openBrowserButton.sizePolicy().hasHeightForWidth())
        self.openBrowserButton.setSizePolicy(sizePolicy)
        self.openBrowserButton.setObjectName("openBrowserButton")
        self.verticalLayout.addWidget(self.openBrowserButton)
        self.sendButton = QtGui.QPushButton(Form)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout.addWidget(self.sendButton)
        spacerItem = QtGui.QSpacerItem(125, 71, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.playButton.setText(QtGui.QApplication.translate("Form", "Play....", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("Form", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.openBrowserButton.setText(QtGui.QApplication.translate("Form", "Browser...", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("Form", "Send...", None, QtGui.QApplication.UnicodeUTF8))

