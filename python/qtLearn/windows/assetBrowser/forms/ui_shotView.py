# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\assetBrowser\forms\shotView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 232)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.shotsTreeWidget = QtWidgets.QTreeWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotsTreeWidget.sizePolicy().hasHeightForWidth())
        self.shotsTreeWidget.setSizePolicy(sizePolicy)
        self.shotsTreeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shotsTreeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.shotsTreeWidget.setObjectName("shotsTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.shotsTreeWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        self.checkBox.toggled['bool'].connect(self.shotsTreeWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "Shot View"))
        self.shotsTreeWidget.headerItem().setText(0, _translate("Form", "Sequences / Shots"))
        __sortingEnabled = self.shotsTreeWidget.isSortingEnabled()
        self.shotsTreeWidget.setSortingEnabled(False)
        self.shotsTreeWidget.topLevelItem(0).setText(0, _translate("Form", "sh"))
        self.shotsTreeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "sh0010"))
        self.shotsTreeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "sh0020"))
        self.shotsTreeWidget.topLevelItem(1).setText(0, _translate("Form", "fin"))
        self.shotsTreeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "fin010"))
        self.shotsTreeWidget.setSortingEnabled(__sortingEnabled)

