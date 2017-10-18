# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/fileBrowser/fileBrowserSave.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(817, 335)
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
        self.saveOptionsFrame = QtGui.QFrame(Form)
        self.saveOptionsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.saveOptionsFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.saveOptionsFrame.setObjectName("saveOptionsFrame")
        self.verticalLayout = QtGui.QVBoxLayout(self.saveOptionsFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.saveOptionsLayout = QtGui.QVBoxLayout()
        self.saveOptionsLayout.setObjectName("saveOptionsLayout")
        self.verticalLayout.addLayout(self.saveOptionsLayout)
        self.selectorLayout.addWidget(self.saveOptionsFrame)
        self.verticalLayout_2.addLayout(self.selectorLayout)
        self.pathEditLayout = QtGui.QVBoxLayout()
        self.pathEditLayout.setObjectName("pathEditLayout")
        self.verticalLayout_2.addLayout(self.pathEditLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

