# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\fileBrowser\fileBrowserOpen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(532, 345)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainInfoLayout = QtWidgets.QVBoxLayout()
        self.mainInfoLayout.setContentsMargins(0, 0, 0, 0)
        self.mainInfoLayout.setSpacing(3)
        self.mainInfoLayout.setObjectName("mainInfoLayout")
        self.envFilterLayout = QtWidgets.QHBoxLayout()
        self.envFilterLayout.setContentsMargins(0, 0, 0, 0)
        self.envFilterLayout.setSpacing(3)
        self.envFilterLayout.setObjectName("envFilterLayout")
        self.mainInfoLayout.addLayout(self.envFilterLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.mainInfoLayout.addWidget(self.line)
        self.selectorLayout = QtWidgets.QHBoxLayout()
        self.selectorLayout.setContentsMargins(0, 0, 0, 0)
        self.selectorLayout.setSpacing(3)
        self.selectorLayout.setObjectName("selectorLayout")
        self.fileSelectorLayout = QtWidgets.QVBoxLayout()
        self.fileSelectorLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.fileSelectorLayout.setContentsMargins(0, 0, 0, 0)
        self.fileSelectorLayout.setSpacing(3)
        self.fileSelectorLayout.setObjectName("fileSelectorLayout")
        self.selectorLayout.addLayout(self.fileSelectorLayout)
        self.versionSelectorLayout = QtWidgets.QVBoxLayout()
        self.versionSelectorLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.versionSelectorLayout.setContentsMargins(0, 0, 0, 0)
        self.versionSelectorLayout.setSpacing(3)
        self.versionSelectorLayout.setObjectName("versionSelectorLayout")
        self.selectorLayout.addLayout(self.versionSelectorLayout)
        self.mainInfoLayout.addLayout(self.selectorLayout)
        self.pathEditLayout = QtWidgets.QVBoxLayout()
        self.pathEditLayout.setContentsMargins(0, 0, 0, 0)
        self.pathEditLayout.setSpacing(3)
        self.pathEditLayout.setObjectName("pathEditLayout")
        self.mainInfoLayout.addLayout(self.pathEditLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.mainInfoLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.mainInfoLayout)
        self.previewInfoLayout = QtWidgets.QVBoxLayout()
        self.previewInfoLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.previewInfoLayout.setSpacing(3)
        self.previewInfoLayout.setObjectName("previewInfoLayout")
        self.horizontalLayout.addLayout(self.previewInfoLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

