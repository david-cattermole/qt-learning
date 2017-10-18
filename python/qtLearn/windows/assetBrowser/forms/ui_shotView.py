# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/assetBrowser/forms/shotView.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shotsTreeWidget = QtGui.QTreeWidget(Form)
        self.shotsTreeWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.shotsTreeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.shotsTreeWidget.setObjectName("shotsTreeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.shotsTreeWidget)
        self.addShotsButton = QtGui.QPushButton(Form)
        self.addShotsButton.setObjectName("addShotsButton")
        self.verticalLayout.addWidget(self.addShotsButton)
        self.clearAllButton = QtGui.QPushButton(Form)
        self.clearAllButton.setObjectName("clearAllButton")
        self.verticalLayout.addWidget(self.clearAllButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("Form", "Sequences / Shots", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.shotsTreeWidget.isSortingEnabled()
        self.shotsTreeWidget.setSortingEnabled(False)
        self.shotsTreeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Form", "sh", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("Form", "sh0010", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("Form", "sh0020", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Form", "fin", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("Form", "fin010", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.setSortingEnabled(__sortingEnabled)
        self.addShotsButton.setText(QtGui.QApplication.translate("Form", "Add Shots...", None, QtGui.QApplication.UnicodeUTF8))
        self.clearAllButton.setText(QtGui.QApplication.translate("Form", "Clear All...", None, QtGui.QApplication.UnicodeUTF8))

