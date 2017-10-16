# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/assetActions.ui'
#
# Created: Mon Oct 16 23:43:55 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(136, 326)
        self.verticalLayout = QtGui.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetThumbnailIcon = QtGui.QGraphicsView(Widget)
        self.assetThumbnailIcon.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetThumbnailIcon.sizePolicy().hasHeightForWidth())
        self.assetThumbnailIcon.setSizePolicy(sizePolicy)
        self.assetThumbnailIcon.setMaximumSize(QtCore.QSize(128, 128))
        self.assetThumbnailIcon.setObjectName("assetThumbnailIcon")
        self.verticalLayout.addWidget(self.assetThumbnailIcon)
        self.playButton = QtGui.QPushButton(Widget)
        self.playButton.setObjectName("playButton")
        self.verticalLayout.addWidget(self.playButton)
        self.openButton = QtGui.QPushButton(Widget)
        self.openButton.setObjectName("openButton")
        self.verticalLayout.addWidget(self.openButton)
        self.openBrowserButton = QtGui.QPushButton(Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openBrowserButton.sizePolicy().hasHeightForWidth())
        self.openBrowserButton.setSizePolicy(sizePolicy)
        self.openBrowserButton.setObjectName("openBrowserButton")
        self.verticalLayout.addWidget(self.openBrowserButton)
        self.sendButton = QtGui.QPushButton(Widget)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout.addWidget(self.sendButton)
        spacerItem = QtGui.QSpacerItem(125, 71, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.playButton.setText(QtGui.QApplication.translate("Widget", "Play....", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("Widget", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.openBrowserButton.setText(QtGui.QApplication.translate("Widget", "Browser...", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("Widget", "Send...", None, QtGui.QApplication.UnicodeUTF8))

