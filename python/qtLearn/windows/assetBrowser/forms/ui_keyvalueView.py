# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/assetBrowser/forms/keyvalueView.ui'
#
# Created: Tue Nov 14 18:49:58 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 211)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.keyvalueTableWidget = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyvalueTableWidget.sizePolicy().hasHeightForWidth())
        self.keyvalueTableWidget.setSizePolicy(sizePolicy)
        self.keyvalueTableWidget.setObjectName("keyvalueTableWidget")
        self.keyvalueTableWidget.setColumnCount(2)
        self.keyvalueTableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.keyvalueTableWidget.setItem(0, 1, item)
        self.verticalLayout.addWidget(self.keyvalueTableWidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.keyvalueTableWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Key Value View", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Value", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.keyvalueTableWidget.isSortingEnabled()
        self.keyvalueTableWidget.setSortingEnabled(False)
        self.keyvalueTableWidget.item(0, 0).setText(QtGui.QApplication.translate("Form", "ultimate_answer", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.item(0, 1).setText(QtGui.QApplication.translate("Form", "42", None, QtGui.QApplication.UnicodeUTF8))
        self.keyvalueTableWidget.setSortingEnabled(__sortingEnabled)

