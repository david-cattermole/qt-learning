# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/assetIncomingView.ui'
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
        self.assetsListWidget = QtGui.QListWidget(Widget)
        self.assetsListWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.assetsListWidget.setObjectName("assetsListWidget")
        QtGui.QListWidgetItem(self.assetsListWidget)
        self.verticalLayout.addWidget(self.assetsListWidget)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.assetsListWidget.isSortingEnabled()
        self.assetsListWidget.setSortingEnabled(False)
        self.assetsListWidget.item(0).setText(QtGui.QApplication.translate("Widget", "some asset", None, QtGui.QApplication.UnicodeUTF8))
        self.assetsListWidget.setSortingEnabled(__sortingEnabled)

