# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\keyvalueView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 211)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.keyvalueTableWidget = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyvalueTableWidget.sizePolicy().hasHeightForWidth())
        self.keyvalueTableWidget.setSizePolicy(sizePolicy)
        self.keyvalueTableWidget.setObjectName("keyvalueTableWidget")
        self.keyvalueTableWidget.setColumnCount(2)
        self.keyvalueTableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.keyvalueTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.keyvalueTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.keyvalueTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.keyvalueTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.keyvalueTableWidget.setItem(0, 1, item)
        self.verticalLayout.addWidget(self.keyvalueTableWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        self.checkBox.toggled['bool'].connect(self.keyvalueTableWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "Key Value View"))
        item = self.keyvalueTableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.keyvalueTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Key"))
        item = self.keyvalueTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value"))
        __sortingEnabled = self.keyvalueTableWidget.isSortingEnabled()
        self.keyvalueTableWidget.setSortingEnabled(False)
        item = self.keyvalueTableWidget.item(0, 0)
        item.setText(_translate("Form", "ultimate_answer"))
        item = self.keyvalueTableWidget.item(0, 1)
        item.setText(_translate("Form", "42"))
        self.keyvalueTableWidget.setSortingEnabled(__sortingEnabled)

