# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/assetBrowser/forms/assetIncomingView.ui'
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
        self.assetsListWidget = QtGui.QListWidget(Form)
        self.assetsListWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.assetsListWidget.setObjectName("assetsListWidget")
        QtGui.QListWidgetItem(self.assetsListWidget)
        self.verticalLayout.addWidget(self.assetsListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.assetsListWidget.isSortingEnabled()
        self.assetsListWidget.setSortingEnabled(False)
        self.assetsListWidget.item(0).setText(QtGui.QApplication.translate("Form", "some asset", None, QtGui.QApplication.UnicodeUTF8))
        self.assetsListWidget.setSortingEnabled(__sortingEnabled)

