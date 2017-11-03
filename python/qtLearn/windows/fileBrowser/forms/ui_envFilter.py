# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\fileBrowser\forms\envFilter.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(653, 20)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectSeqShotLayout = QtWidgets.QHBoxLayout()
        self.projectSeqShotLayout.setObjectName("projectSeqShotLayout")
        self.horizontalLayout.addLayout(self.projectSeqShotLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.departmentLabel = QtWidgets.QLabel(Form)
        self.departmentLabel.setObjectName("departmentLabel")
        self.horizontalLayout.addWidget(self.departmentLabel)
        self.departmentComboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.departmentComboBox.setFont(font)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.horizontalLayout.addWidget(self.departmentComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.userLabel = QtWidgets.QLabel(Form)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout.addWidget(self.userLabel)
        self.userComboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.userComboBox.setFont(font)
        self.userComboBox.setObjectName("userComboBox")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.userComboBox.addItem("")
        self.horizontalLayout.addWidget(self.userComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.userLabel.setBuddy(self.userComboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.departmentComboBox, self.userComboBox)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.departmentLabel.setText(_translate("Form", "Department"))
        self.departmentComboBox.setItemText(0, _translate("Form", "dept"))
        self.departmentComboBox.setItemText(1, _translate("Form", "all depts"))
        self.departmentComboBox.setItemText(2, _translate("Form", "layout"))
        self.departmentComboBox.setItemText(3, _translate("Form", "light"))
        self.departmentComboBox.setItemText(4, _translate("Form", "model"))
        self.departmentComboBox.setItemText(5, _translate("Form", "rig"))
        self.departmentComboBox.setItemText(6, _translate("Form", "rnd"))
        self.userLabel.setText(_translate("Form", "User"))
        self.userComboBox.setItemText(0, _translate("Form", "user"))
        self.userComboBox.setItemText(1, _translate("Form", "current user"))
        self.userComboBox.setItemText(2, _translate("Form", "davidc"))
        self.userComboBox.setItemText(3, _translate("Form", "bob"))
        self.userComboBox.setItemText(4, _translate("Form", "john"))

