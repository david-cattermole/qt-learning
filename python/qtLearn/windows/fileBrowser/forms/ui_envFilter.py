# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/fileBrowser/forms/envFilter.ui'
#
# Created: Sun Oct 22 22:21:46 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(777, 33)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectComboBox = QtGui.QComboBox(Form)
        self.projectComboBox.setObjectName("projectComboBox")
        self.projectComboBox.addItem("")
        self.projectComboBox.addItem("")
        self.horizontalLayout.addWidget(self.projectComboBox)
        self.sequenceComboBox = QtGui.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.sequenceComboBox.setFont(font)
        self.sequenceComboBox.setObjectName("sequenceComboBox")
        self.sequenceComboBox.addItem("")
        self.horizontalLayout.addWidget(self.sequenceComboBox)
        self.shotComboBox = QtGui.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.shotComboBox.setFont(font)
        self.shotComboBox.setObjectName("shotComboBox")
        self.shotComboBox.addItem("")
        self.horizontalLayout.addWidget(self.shotComboBox)
        self.departmentComboBox = QtGui.QComboBox(Form)
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
        self.userComboBox = QtGui.QComboBox(Form)
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
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.projectComboBox.setItemText(0, QtGui.QApplication.translate("Form", "project", None, QtGui.QApplication.UnicodeUTF8))
        self.projectComboBox.setItemText(1, QtGui.QApplication.translate("Form", "current project", None, QtGui.QApplication.UnicodeUTF8))
        self.sequenceComboBox.setItemText(0, QtGui.QApplication.translate("Form", "seq", None, QtGui.QApplication.UnicodeUTF8))
        self.shotComboBox.setItemText(0, QtGui.QApplication.translate("Form", "shot", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(0, QtGui.QApplication.translate("Form", "dept", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(1, QtGui.QApplication.translate("Form", "all depts", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(2, QtGui.QApplication.translate("Form", "layout", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(3, QtGui.QApplication.translate("Form", "light", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(4, QtGui.QApplication.translate("Form", "model", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(5, QtGui.QApplication.translate("Form", "rig", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(6, QtGui.QApplication.translate("Form", "rnd", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(0, QtGui.QApplication.translate("Form", "user", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(1, QtGui.QApplication.translate("Form", "current user", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(2, QtGui.QApplication.translate("Form", "davidc", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(3, QtGui.QApplication.translate("Form", "bob", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(4, QtGui.QApplication.translate("Form", "john", None, QtGui.QApplication.UnicodeUTF8))

