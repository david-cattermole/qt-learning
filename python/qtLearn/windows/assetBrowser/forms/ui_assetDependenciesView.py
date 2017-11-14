# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/Public/qt-learning/ui/windows/assetBrowser/forms/assetDependenciesView.ui'
#
# Created: Tue Nov 14 18:49:57 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(183, 380)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.incomingListWidget = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incomingListWidget.sizePolicy().hasHeightForWidth())
        self.incomingListWidget.setSizePolicy(sizePolicy)
        self.incomingListWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.incomingListWidget.setObjectName("incomingListWidget")
        QtGui.QListWidgetItem(self.incomingListWidget)
        self.verticalLayout.addWidget(self.incomingListWidget)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.outgoingListWidget = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outgoingListWidget.sizePolicy().hasHeightForWidth())
        self.outgoingListWidget.setSizePolicy(sizePolicy)
        self.outgoingListWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.outgoingListWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.outgoingListWidget.setObjectName("outgoingListWidget")
        QtGui.QListWidgetItem(self.outgoingListWidget)
        self.verticalLayout.addWidget(self.outgoingListWidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.incomingListWidget.setVisible)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.outgoingListWidget.setVisible)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.label.setVisible)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("toggled(bool)"), self.label_2.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Asset Dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Incoming", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.incomingListWidget.isSortingEnabled()
        self.incomingListWidget.setSortingEnabled(False)
        self.incomingListWidget.item(0).setText(QtGui.QApplication.translate("Form", "some asset", None, QtGui.QApplication.UnicodeUTF8))
        self.incomingListWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(QtGui.QApplication.translate("Form", "Outgoing", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.outgoingListWidget.isSortingEnabled()
        self.outgoingListWidget.setSortingEnabled(False)
        self.outgoingListWidget.item(0).setText(QtGui.QApplication.translate("Form", "another asset", None, QtGui.QApplication.UnicodeUTF8))
        self.outgoingListWidget.setSortingEnabled(__sortingEnabled)

