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
        Form.resize(777, 38)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectComboBox = QtWidgets.QComboBox(Form)
        self.projectComboBox.setObjectName("projectComboBox")
        self.projectComboBox.addItem("")
        self.projectComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectComboBox)
        self.sequenceComboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.sequenceComboBox.setFont(font)
        self.sequenceComboBox.setObjectName("sequenceComboBox")
        self.sequenceComboBox.addItem("")
        self.horizontalLayout.addWidget(self.sequenceComboBox)
        self.shotComboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.shotComboBox.setFont(font)
        self.shotComboBox.setObjectName("shotComboBox")
        self.shotComboBox.addItem("")
        self.horizontalLayout.addWidget(self.shotComboBox)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.projectComboBox.setItemText(0, _translate("Form", "project"))
        self.projectComboBox.setItemText(1, _translate("Form", "current project"))
        self.sequenceComboBox.setItemText(0, _translate("Form", "seq"))
        self.shotComboBox.setItemText(0, _translate("Form", "shot"))
        self.departmentComboBox.setItemText(0, _translate("Form", "dept"))
        self.departmentComboBox.setItemText(1, _translate("Form", "all depts"))
        self.departmentComboBox.setItemText(2, _translate("Form", "layout"))
        self.departmentComboBox.setItemText(3, _translate("Form", "light"))
        self.departmentComboBox.setItemText(4, _translate("Form", "model"))
        self.departmentComboBox.setItemText(5, _translate("Form", "rig"))
        self.departmentComboBox.setItemText(6, _translate("Form", "rnd"))
        self.userComboBox.setItemText(0, _translate("Form", "user"))
        self.userComboBox.setItemText(1, _translate("Form", "current user"))
        self.userComboBox.setItemText(2, _translate("Form", "davidc"))
        self.userComboBox.setItemText(3, _translate("Form", "bob"))
        self.userComboBox.setItemText(4, _translate("Form", "john"))

