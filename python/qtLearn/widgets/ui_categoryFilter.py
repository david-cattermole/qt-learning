# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/categoryFilter.ui'
#
# Created: Wed Oct 18 20:52:42 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(422, 422)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtGui.QLineEdit(Widget)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.horizontalSlider = QtGui.QSlider(Widget)
        self.horizontalSlider.setMaximum(8)
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtGui.QTreeWidget(Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.listWidget_2 = QtGui.QListWidget(Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Widget", "Filter Text", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Widget", "1", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("Widget", "Category 2", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("Widget", "Sub-Category 2", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("Widget", "Category 1", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("Widget", "Sub-Category 1", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.item(0).setText(QtGui.QApplication.translate("Widget", "item 1", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(1).setText(QtGui.QApplication.translate("Widget", "item 2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(2).setText(QtGui.QApplication.translate("Widget", "item 3", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(3).setText(QtGui.QApplication.translate("Widget", "item 4", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(4).setText(QtGui.QApplication.translate("Widget", "item 5", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(5).setText(QtGui.QApplication.translate("Widget", "item 6", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(6).setText(QtGui.QApplication.translate("Widget", "item 7", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

