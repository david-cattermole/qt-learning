# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/shotView.ui'
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
        self.shotsTreeWidget = QtGui.QTreeWidget(Widget)
        self.shotsTreeWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.shotsTreeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.shotsTreeWidget.setObjectName("shotsTreeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.shotsTreeWidget)
        self.addShotsButton = QtGui.QPushButton(Widget)
        self.addShotsButton.setObjectName("addShotsButton")
        self.verticalLayout.addWidget(self.addShotsButton)
        self.clearAllButton = QtGui.QPushButton(Widget)
        self.clearAllButton.setObjectName("clearAllButton")
        self.verticalLayout.addWidget(self.clearAllButton)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("Widget", "Sequences / Shots", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.shotsTreeWidget.isSortingEnabled()
        self.shotsTreeWidget.setSortingEnabled(False)
        self.shotsTreeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Widget", "sh", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("Widget", "sh0010", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("Widget", "sh0020", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Widget", "fin", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("Widget", "fin010", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.setSortingEnabled(__sortingEnabled)
        self.addShotsButton.setText(QtGui.QApplication.translate("Widget", "Add Shots...", None, QtGui.QApplication.UnicodeUTF8))
        self.clearAllButton.setText(QtGui.QApplication.translate("Widget", "Clear All...", None, QtGui.QApplication.UnicodeUTF8))

