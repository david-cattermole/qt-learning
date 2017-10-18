# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/fileBrowser/fileBrowserOpen.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(817, 327)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.envFilterLayout = QtGui.QHBoxLayout()
        self.envFilterLayout.setObjectName("envFilterLayout")
        self.verticalLayout_2.addLayout(self.envFilterLayout)
        self.selectorLayout = QtGui.QHBoxLayout()
        self.selectorLayout.setObjectName("selectorLayout")
        self.fileSelectorLayout = QtGui.QVBoxLayout()
        self.fileSelectorLayout.setObjectName("fileSelectorLayout")
        self.selectorLayout.addLayout(self.fileSelectorLayout)
        self.versionSelectorLayout = QtGui.QVBoxLayout()
        self.versionSelectorLayout.setObjectName("versionSelectorLayout")
        self.selectorLayout.addLayout(self.versionSelectorLayout)
        self.verticalLayout_2.addLayout(self.selectorLayout)
        self.pathEditLayout = QtGui.QVBoxLayout()
        self.pathEditLayout.setObjectName("pathEditLayout")
        self.verticalLayout_2.addLayout(self.pathEditLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

