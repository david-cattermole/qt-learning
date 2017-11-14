# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/fileBrowser/forms/previewInfo.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 577)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iconButton = QtGui.QToolButton(Form)
        self.iconButton.setMinimumSize(QtCore.QSize(128, 128))
        self.iconButton.setMaximumSize(QtCore.QSize(128, 128))
        self.iconButton.setCheckable(False)
        self.iconButton.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.iconButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.iconButton.setArrowType(QtCore.Qt.NoArrow)
        self.iconButton.setObjectName("iconButton")
        self.horizontalLayout_2.addWidget(self.iconButton)
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(Form)
        self.line.setEnabled(True)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.optionAttrLayout = QtGui.QVBoxLayout()
        self.optionAttrLayout.setSpacing(3)
        self.optionAttrLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.optionAttrLayout.setObjectName("optionAttrLayout")
        self.verticalLayout.addLayout(self.optionAttrLayout)
        spacerItem1 = QtGui.QSpacerItem(0, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.iconButton.setText(QtGui.QApplication.translate("Form", "Icon Here", None, QtGui.QApplication.UnicodeUTF8))

