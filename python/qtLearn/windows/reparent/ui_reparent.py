# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/reparent/reparent.ui'
#
# Created: Wed Oct 18 20:52:41 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(436, 430)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(4, 4, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nodesGroupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesGroupBox.sizePolicy().hasHeightForWidth())
        self.nodesGroupBox.setSizePolicy(sizePolicy)
        self.nodesGroupBox.setObjectName("nodesGroupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.nodesGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nodesLayout = QtGui.QVBoxLayout()
        self.nodesLayout.setObjectName("nodesLayout")
        self.verticalLayout_2.addLayout(self.nodesLayout)
        self.verticalLayout.addWidget(self.nodesGroupBox)
        self.timeRangeGroupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeRangeGroupBox.sizePolicy().hasHeightForWidth())
        self.timeRangeGroupBox.setSizePolicy(sizePolicy)
        self.timeRangeGroupBox.setObjectName("timeRangeGroupBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.timeRangeGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.timeRangeLayout = QtGui.QVBoxLayout()
        self.timeRangeLayout.setObjectName("timeRangeLayout")
        self.verticalLayout_4.addLayout(self.timeRangeLayout)
        self.verticalLayout.addWidget(self.timeRangeGroupBox)
        self.subFrameGroupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subFrameGroupBox.sizePolicy().hasHeightForWidth())
        self.subFrameGroupBox.setSizePolicy(sizePolicy)
        self.subFrameGroupBox.setObjectName("subFrameGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.subFrameGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.subFrameLayout = QtGui.QVBoxLayout()
        self.subFrameLayout.setObjectName("subFrameLayout")
        self.verticalLayout_3.addLayout(self.subFrameLayout)
        self.verticalLayout.addWidget(self.subFrameGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesGroupBox.setTitle(QtGui.QApplication.translate("Form", "Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.timeRangeGroupBox.setTitle(QtGui.QApplication.translate("Form", "Time Range", None, QtGui.QApplication.UnicodeUTF8))
        self.subFrameGroupBox.setTitle(QtGui.QApplication.translate("Form", "Sub-Frame", None, QtGui.QApplication.UnicodeUTF8))

