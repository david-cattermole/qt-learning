# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/assetBrowser/forms/tagView.ui'
#
# Created: Tue Nov 14 19:29:10 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(172, 140)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tagsListWidget = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsListWidget.sizePolicy().hasHeightForWidth())
        self.tagsListWidget.setSizePolicy(sizePolicy)
        self.tagsListWidget.setObjectName("tagsListWidget")
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        QtGui.QListWidgetItem(self.tagsListWidget)
        self.verticalLayout.addWidget(self.tagsListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tagsListWidget.isSortingEnabled()
        self.tagsListWidget.setSortingEnabled(False)
        self.tagsListWidget.item(0).setText(QtGui.QApplication.translate("Form", "tag1", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(1).setText(QtGui.QApplication.translate("Form", "tag2", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(2).setText(QtGui.QApplication.translate("Form", "tag2", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(3).setText(QtGui.QApplication.translate("Form", "tag3", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(4).setText(QtGui.QApplication.translate("Form", "tag4", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.item(5).setText(QtGui.QApplication.translate("Form", "tag5", None, QtGui.QApplication.UnicodeUTF8))
        self.tagsListWidget.setSortingEnabled(__sortingEnabled)

