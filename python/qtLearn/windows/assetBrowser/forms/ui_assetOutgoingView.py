# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/assetBrowser/forms/assetOutgoingView.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(123, 141)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.assetsListWidget = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetsListWidget.sizePolicy().hasHeightForWidth())
        self.assetsListWidget.setSizePolicy(sizePolicy)
        self.assetsListWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.assetsListWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.assetsListWidget.setObjectName("assetsListWidget")
        QtGui.QListWidgetItem(self.assetsListWidget)
        self.verticalLayout.addWidget(self.assetsListWidget)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.assetsListWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Asset Outgoing View", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.assetsListWidget.isSortingEnabled()
        self.assetsListWidget.setSortingEnabled(False)
        self.assetsListWidget.item(0).setText(QtGui.QApplication.translate("Form", "another asset", None, QtGui.QApplication.UnicodeUTF8))
        self.assetsListWidget.setSortingEnabled(__sortingEnabled)

