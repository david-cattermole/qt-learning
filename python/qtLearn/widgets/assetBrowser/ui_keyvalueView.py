# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/keyvalueView.ui'
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
        self.keyvalueTableWidget = QtGui.QTableWidget(Widget)
        self.keyvalueTableWidget.setObjectName("keyvalueTableWidget")
        self.keyvalueTableWidget.setColumnCount(2)
        self.keyvalueTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setItem(0, 1, item)
        self.verticalLayout.addWidget(self.keyvalueTableWidget)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Widget", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Widget", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Widget", "Value", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.keyvalueTableWidget.isSortingEnabled()
        self.keyvalueTableWidget.setSortingEnabled(False)
        self.keyvalueTableWidget.item(0, 0).setText(QtGui.QApplication.translate("Widget", "ultimate_answer", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.item(0, 1).setText(QtGui.QApplication.translate("Widget", "42", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.setSortingEnabled(__sortingEnabled)

