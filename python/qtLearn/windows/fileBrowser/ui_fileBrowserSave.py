# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\fileBrowser\fileBrowserSave.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(518, 334)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.envFilterLayout = QtWidgets.QHBoxLayout()
        self.envFilterLayout.setContentsMargins(0, 0, 0, 0)
        self.envFilterLayout.setSpacing(0)
        self.envFilterLayout.setObjectName("envFilterLayout")
        self.verticalLayout_2.addLayout(self.envFilterLayout)
        self.selectorLayout = QtWidgets.QHBoxLayout()
        self.selectorLayout.setContentsMargins(0, 0, 0, 0)
        self.selectorLayout.setSpacing(0)
        self.selectorLayout.setObjectName("selectorLayout")
        self.fileSelectorLayout = QtWidgets.QVBoxLayout()
        self.fileSelectorLayout.setContentsMargins(0, 0, 0, 0)
        self.fileSelectorLayout.setSpacing(0)
        self.fileSelectorLayout.setObjectName("fileSelectorLayout")
        self.selectorLayout.addLayout(self.fileSelectorLayout)
        self.saveOptionsFrame = QtWidgets.QFrame(Form)
        self.saveOptionsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.saveOptionsFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.saveOptionsFrame.setObjectName("saveOptionsFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.saveOptionsFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.saveOptionsLayout = QtWidgets.QVBoxLayout()
        self.saveOptionsLayout.setContentsMargins(0, 0, 0, 0)
        self.saveOptionsLayout.setSpacing(0)
        self.saveOptionsLayout.setObjectName("saveOptionsLayout")
        self.verticalLayout.addLayout(self.saveOptionsLayout)
        self.selectorLayout.addWidget(self.saveOptionsFrame)
        self.verticalLayout_2.addLayout(self.selectorLayout)
        self.pathEditLayout = QtWidgets.QVBoxLayout()
        self.pathEditLayout.setContentsMargins(0, 0, 0, 0)
        self.pathEditLayout.setSpacing(0)
        self.pathEditLayout.setObjectName("pathEditLayout")
        self.verticalLayout_2.addLayout(self.pathEditLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

