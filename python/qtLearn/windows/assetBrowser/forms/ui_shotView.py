# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/assetBrowser/forms/shotView.ui'
#
# Created: Tue Nov 14 19:29:10 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(256, 232)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.shotsTreeWidget = QtGui.QTreeWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotsTreeWidget.sizePolicy().hasHeightForWidth())
        self.shotsTreeWidget.setSizePolicy(sizePolicy)
        self.shotsTreeWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.shotsTreeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.shotsTreeWidget.setObjectName("shotsTreeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.shotsTreeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.shotsTreeWidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.shotsTreeWidget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Shot View", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("Form", "Sequences / Shots", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.shotsTreeWidget.isSortingEnabled()
        self.shotsTreeWidget.setSortingEnabled(False)
        self.shotsTreeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Form", "sh", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("Form", "sh0010", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("Form", "sh0020", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Form", "fin", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("Form", "fin010", None, QtGui.QApplication.UnicodeUTF8))
        self.shotsTreeWidget.setSortingEnabled(__sortingEnabled)

