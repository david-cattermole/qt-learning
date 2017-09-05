# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/reparent.ui'
#
# Created: Tue Jul 18 23:12:00 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 363)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nodesLayoutStub = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesLayoutStub.sizePolicy().hasHeightForWidth())
        self.nodesLayoutStub.setSizePolicy(sizePolicy)
        self.nodesLayoutStub.setFlat(False)
        self.nodesLayoutStub.setCheckable(False)
        self.nodesLayoutStub.setObjectName("nodesLayoutStub")
        self.verticalLayout.addWidget(self.nodesLayoutStub)
        self.timeRangeLayoutStub = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeRangeLayoutStub.sizePolicy().hasHeightForWidth())
        self.timeRangeLayoutStub.setSizePolicy(sizePolicy)
        self.timeRangeLayoutStub.setObjectName("timeRangeLayoutStub")
        self.verticalLayout.addWidget(self.timeRangeLayoutStub)
        self.subFrameLayoutStub = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subFrameLayoutStub.sizePolicy().hasHeightForWidth())
        self.subFrameLayoutStub.setSizePolicy(sizePolicy)
        self.subFrameLayoutStub.setObjectName("subFrameLayoutStub")
        self.verticalLayout.addWidget(self.subFrameLayoutStub)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesLayoutStub.setTitle(QtGui.QApplication.translate("Form", "Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.timeRangeLayoutStub.setTitle(QtGui.QApplication.translate("Form", "Time Range", None, QtGui.QApplication.UnicodeUTF8))
        self.subFrameLayoutStub.setTitle(QtGui.QApplication.translate("Form", "Sub-Frame", None, QtGui.QApplication.UnicodeUTF8))

