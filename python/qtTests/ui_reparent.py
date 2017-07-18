# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qtTests/ui/reparent.ui'
#
# Created: Tue Jul 18 08:04:42 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 233)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nodesLayoutStub = QtGui.QWidget(Form)
        self.nodesLayoutStub.setObjectName("nodesLayoutStub")
        self.verticalLayout.addWidget(self.nodesLayoutStub)
        self.timeRangeLayoutStub = QtGui.QWidget(Form)
        self.timeRangeLayoutStub.setObjectName("timeRangeLayoutStub")
        self.verticalLayout.addWidget(self.timeRangeLayoutStub)
        self.subFrameLayoutStub = QtGui.QWidget(Form)
        self.subFrameLayoutStub.setObjectName("subFrameLayoutStub")
        self.verticalLayout.addWidget(self.subFrameLayoutStub)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

