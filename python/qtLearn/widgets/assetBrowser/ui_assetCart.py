# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/assetCart.ui'
#
# Created: Mon Oct 16 23:43:55 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addButton = QtGui.QPushButton(Widget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_6.addWidget(self.addButton)
        self.replaceButton = QtGui.QPushButton(Widget)
        self.replaceButton.setObjectName("replaceButton")
        self.horizontalLayout_6.addWidget(self.replaceButton)
        self.clearButton = QtGui.QPushButton(Widget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_6.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.assetListWidget = QtGui.QListWidget(Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetListWidget.sizePolicy().hasHeightForWidth())
        self.assetListWidget.setSizePolicy(sizePolicy)
        self.assetListWidget.setObjectName("assetListWidget")
        QtGui.QListWidgetItem(self.assetListWidget)
        QtGui.QListWidgetItem(self.assetListWidget)
        self.verticalLayout.addWidget(self.assetListWidget)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Widget", "Asset Cart", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Widget", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setText(QtGui.QApplication.translate("Widget", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Widget", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.assetListWidget.isSortingEnabled()
        self.assetListWidget.setSortingEnabled(False)
        self.assetListWidget.item(0).setText(QtGui.QApplication.translate("Widget", "john rig v001", None, QtGui.QApplication.UnicodeUTF8))
        self.assetListWidget.item(1).setText(QtGui.QApplication.translate("Widget", "john rig v002", None, QtGui.QApplication.UnicodeUTF8))
        self.assetListWidget.setSortingEnabled(__sortingEnabled)

