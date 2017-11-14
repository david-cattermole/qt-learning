# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/fileBrowser/forms/envFilter.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(653, 20)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.projectSeqShotLayout = QtGui.QHBoxLayout()
        self.projectSeqShotLayout.setObjectName("projectSeqShotLayout")
        self.horizontalLayout.addLayout(self.projectSeqShotLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.departmentLabel = QtGui.QLabel(Form)
        self.departmentLabel.setObjectName("departmentLabel")
        self.horizontalLayout.addWidget(self.departmentLabel)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.userLabel = QtGui.QLabel(Form)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout.addWidget(self.userLabel)
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
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.departmentLabel.setBuddy(self.departmentComboBox)
        self.userLabel.setBuddy(self.userComboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.departmentComboBox, self.userComboBox)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentLabel.setText(QtGui.QApplication.translate("Form", "Department", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(0, QtGui.QApplication.translate("Form", "dept", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(1, QtGui.QApplication.translate("Form", "all depts", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(2, QtGui.QApplication.translate("Form", "layout", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(3, QtGui.QApplication.translate("Form", "light", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(4, QtGui.QApplication.translate("Form", "model", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(5, QtGui.QApplication.translate("Form", "rig", None, QtGui.QApplication.UnicodeUTF8))
        self.departmentComboBox.setItemText(6, QtGui.QApplication.translate("Form", "rnd", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("Form", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(0, QtGui.QApplication.translate("Form", "user", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(1, QtGui.QApplication.translate("Form", "current user", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(2, QtGui.QApplication.translate("Form", "davidc", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(3, QtGui.QApplication.translate("Form", "bob", None, QtGui.QApplication.UnicodeUTF8))
        self.userComboBox.setItemText(4, QtGui.QApplication.translate("Form", "john", None, QtGui.QApplication.UnicodeUTF8))

