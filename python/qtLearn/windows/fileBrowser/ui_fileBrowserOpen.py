# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/fileBrowser/fileBrowserOpen.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(532, 345)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainInfoLayout = QtGui.QVBoxLayout()
        self.mainInfoLayout.setSpacing(3)
        self.mainInfoLayout.setMargin(0)
        self.mainInfoLayout.setObjectName("mainInfoLayout")
        self.envFilterLayout = QtGui.QHBoxLayout()
        self.envFilterLayout.setSpacing(3)
        self.envFilterLayout.setMargin(0)
        self.envFilterLayout.setObjectName("envFilterLayout")
        self.mainInfoLayout.addLayout(self.envFilterLayout)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.mainInfoLayout.addWidget(self.line)
        self.selectorLayout = QtGui.QHBoxLayout()
        self.selectorLayout.setSpacing(3)
        self.selectorLayout.setMargin(0)
        self.selectorLayout.setObjectName("selectorLayout")
        self.fileSelectorLayout = QtGui.QVBoxLayout()
        self.fileSelectorLayout.setSpacing(3)
        self.fileSelectorLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.fileSelectorLayout.setMargin(0)
        self.fileSelectorLayout.setObjectName("fileSelectorLayout")
        self.selectorLayout.addLayout(self.fileSelectorLayout)
        self.versionSelectorLayout = QtGui.QVBoxLayout()
        self.versionSelectorLayout.setSpacing(3)
        self.versionSelectorLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.versionSelectorLayout.setMargin(0)
        self.versionSelectorLayout.setObjectName("versionSelectorLayout")
        self.selectorLayout.addLayout(self.versionSelectorLayout)
        self.mainInfoLayout.addLayout(self.selectorLayout)
        self.pathEditLayout = QtGui.QVBoxLayout()
        self.pathEditLayout.setSpacing(3)
        self.pathEditLayout.setMargin(0)
        self.pathEditLayout.setObjectName("pathEditLayout")
        self.mainInfoLayout.addLayout(self.pathEditLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.mainInfoLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.mainInfoLayout)
        self.previewInfoLayout = QtGui.QVBoxLayout()
        self.previewInfoLayout.setSpacing(3)
        self.previewInfoLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.previewInfoLayout.setObjectName("previewInfoLayout")
        self.horizontalLayout.addLayout(self.previewInfoLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

