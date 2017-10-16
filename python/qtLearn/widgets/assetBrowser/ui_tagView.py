# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/tagView.ui'
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
        self.tagsListWidget = QtGui.QListWidget(Widget)
        self.tagsListWidget.setObjectName("tagsListWidget")
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        self.verticalLayout.addWidget(self.tagsListWidget)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tagsListWidget.isSortingEnabled()
        self.tagsListWidget.setSortingEnabled(False)
        self.tagsListWidget.item(0).setText(QtGui.QApplication.translate("Widget", "tag1", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(1).setText(QtGui.QApplication.translate("Widget", "tag2", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(2).setText(QtGui.QApplication.translate("Widget", "tag2", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(3).setText(QtGui.QApplication.translate("Widget", "tag3", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(4).setText(QtGui.QApplication.translate("Widget", "tag4", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(5).setText(QtGui.QApplication.translate("Widget", "tag5", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.setSortingEnabled(__sortingEnabled)

