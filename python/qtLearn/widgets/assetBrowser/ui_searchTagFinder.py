# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/widgets/assetBrowser/searchTagFinder.ui'
#
# Created: Mon Oct 16 23:43:55 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1034, 390)
        self.horizontalLayout = QtGui.QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtGui.QScrollArea(Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.scrollArea.setFont(font)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1264, 357))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget_11 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_11.sizePolicy().hasHeightForWidth())
        self.listWidget_11.setSizePolicy(sizePolicy)
        self.listWidget_11.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.listWidget_11.setFont(font)
        self.listWidget_11.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_11.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_11.setObjectName("listWidget_11")
        QtGui.QListWidgetItem(self.listWidget_11)
        QtGui.QListWidgetItem(self.listWidget_11)
        self.verticalLayout.addWidget(self.listWidget_11)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget_9 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_9.sizePolicy().hasHeightForWidth())
        self.listWidget_9.setSizePolicy(sizePolicy)
        self.listWidget_9.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.listWidget_9.setFont(font)
        self.listWidget_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_9.setAutoScroll(True)
        self.listWidget_9.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_9.setMovement(QtGui.QListView.Static)
        self.listWidget_9.setObjectName("listWidget_9")
        QtGui.QListWidgetItem(self.listWidget_9)
        QtGui.QListWidgetItem(self.listWidget_9)
        QtGui.QListWidgetItem(self.listWidget_9)
        QtGui.QListWidgetItem(self.listWidget_9)
        QtGui.QListWidgetItem(self.listWidget_9)
        self.verticalLayout_2.addWidget(self.listWidget_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.listWidget_10 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_10.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.listWidget_10.setFont(font)
        self.listWidget_10.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_10.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_10.setObjectName("listWidget_10")
        QtGui.QListWidgetItem(self.listWidget_10)
        QtGui.QListWidgetItem(self.listWidget_10)
        QtGui.QListWidgetItem(self.listWidget_10)
        QtGui.QListWidgetItem(self.listWidget_10)
        QtGui.QListWidgetItem(self.listWidget_10)
        QtGui.QListWidgetItem(self.listWidget_10)
        self.verticalLayout_3.addWidget(self.listWidget_10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.listWidget_13 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_13.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.listWidget_13.setFont(font)
        self.listWidget_13.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_13.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_13.setObjectName("listWidget_13")
        QtGui.QListWidgetItem(self.listWidget_13)
        QtGui.QListWidgetItem(self.listWidget_13)
        QtGui.QListWidgetItem(self.listWidget_13)
        QtGui.QListWidgetItem(self.listWidget_13)
        QtGui.QListWidgetItem(self.listWidget_13)
        QtGui.QListWidgetItem(self.listWidget_13)
        self.verticalLayout_4.addWidget(self.listWidget_13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.listWidget_3 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_3.sizePolicy().hasHeightForWidth())
        self.listWidget_3.setSizePolicy(sizePolicy)
        self.listWidget_3.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.listWidget_3.setFont(font)
        self.listWidget_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_3.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_3.setObjectName("listWidget_3")
        QtGui.QListWidgetItem(self.listWidget_3)
        QtGui.QListWidgetItem(self.listWidget_3)
        QtGui.QListWidgetItem(self.listWidget_3)
        QtGui.QListWidgetItem(self.listWidget_3)
        QtGui.QListWidgetItem(self.listWidget_3)
        QtGui.QListWidgetItem(self.listWidget_3)
        self.verticalLayout_5.addWidget(self.listWidget_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        self.verticalLayout_6.addWidget(self.listWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.listWidget_8 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_8.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidget_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.listWidget_8.setLineWidth(1)
        self.listWidget_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_8.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_8.setMovement(QtGui.QListView.Static)
        self.listWidget_8.setFlow(QtGui.QListView.TopToBottom)
        self.listWidget_8.setProperty("isWrapping", False)
        self.listWidget_8.setResizeMode(QtGui.QListView.Fixed)
        self.listWidget_8.setLayoutMode(QtGui.QListView.SinglePass)
        self.listWidget_8.setViewMode(QtGui.QListView.ListMode)
        self.listWidget_8.setUniformItemSizes(False)
        self.listWidget_8.setWordWrap(False)
        self.listWidget_8.setSelectionRectVisible(False)
        self.listWidget_8.setObjectName("listWidget_8")
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        QtGui.QListWidgetItem(self.listWidget_8)
        self.verticalLayout_7.addWidget(self.listWidget_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.listWidget_2 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_2.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidget_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        QtGui.QListWidgetItem(self.listWidget_2)
        self.verticalLayout_8.addWidget(self.listWidget_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.listWidget_4 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_4.sizePolicy().hasHeightForWidth())
        self.listWidget_4.setSizePolicy(sizePolicy)
        self.listWidget_4.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidget_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_4.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_4.setObjectName("listWidget_4")
        QtGui.QListWidgetItem(self.listWidget_4)
        QtGui.QListWidgetItem(self.listWidget_4)
        QtGui.QListWidgetItem(self.listWidget_4)
        QtGui.QListWidgetItem(self.listWidget_4)
        QtGui.QListWidgetItem(self.listWidget_4)
        QtGui.QListWidgetItem(self.listWidget_4)
        self.verticalLayout_9.addWidget(self.listWidget_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.listWidget_5 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_5.sizePolicy().hasHeightForWidth())
        self.listWidget_5.setSizePolicy(sizePolicy)
        self.listWidget_5.setMinimumSize(QtCore.QSize(120, 0))
        self.listWidget_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_5.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_5.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.listWidget_5.setObjectName("listWidget_5")
        QtGui.QListWidgetItem(self.listWidget_5)
        QtGui.QListWidgetItem(self.listWidget_5)
        QtGui.QListWidgetItem(self.listWidget_5)
        QtGui.QListWidgetItem(self.listWidget_5)
        QtGui.QListWidgetItem(self.listWidget_5)
        self.verticalLayout_10.addWidget(self.listWidget_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Widget", "Project", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_11.isSortingEnabled()
        self.listWidget_11.setSortingEnabled(False)
        self.listWidget_11.item(0).setText(QtGui.QApplication.translate("Widget", "project", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_11.item(1).setText(QtGui.QApplication.translate("Widget", "project 2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_11.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(QtGui.QApplication.translate("Widget", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_9.isSortingEnabled()
        self.listWidget_9.setSortingEnabled(False)
        self.listWidget_9.item(0).setText(QtGui.QApplication.translate("Widget", "sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_9.item(1).setText(QtGui.QApplication.translate("Widget", "sh", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_9.item(2).setText(QtGui.QApplication.translate("Widget", "br", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_9.item(3).setText(QtGui.QApplication.translate("Widget", "pw", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_9.item(4).setText(QtGui.QApplication.translate("Widget", "if", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_9.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(QtGui.QApplication.translate("Widget", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_10.isSortingEnabled()
        self.listWidget_10.setSortingEnabled(False)
        self.listWidget_10.item(0).setText(QtGui.QApplication.translate("Widget", "sh-0010", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_10.item(1).setText(QtGui.QApplication.translate("Widget", "sh-0020", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_10.item(2).setText(QtGui.QApplication.translate("Widget", "sh-0030", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_10.item(3).setText(QtGui.QApplication.translate("Widget", "sh-0040", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_10.item(4).setText(QtGui.QApplication.translate("Widget", "sh-0050", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_10.item(5).setText(QtGui.QApplication.translate("Widget", "sh-0060", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_10.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(QtGui.QApplication.translate("Widget", "User", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_13.isSortingEnabled()
        self.listWidget_13.setSortingEnabled(False)
        self.listWidget_13.item(0).setText(QtGui.QApplication.translate("Widget", "<all users>", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_13.item(1).setText(QtGui.QApplication.translate("Widget", "<current user>", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_13.item(2).setText(QtGui.QApplication.translate("Widget", "bob", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_13.item(3).setText(QtGui.QApplication.translate("Widget", "jane", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_13.item(4).setText(QtGui.QApplication.translate("Widget", "john", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_13.item(5).setText(QtGui.QApplication.translate("Widget", "sam", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_13.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(QtGui.QApplication.translate("Widget", "Name", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.item(0).setText(QtGui.QApplication.translate("Widget", "Name 1", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_3.item(1).setText(QtGui.QApplication.translate("Widget", "Name 2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_3.item(2).setText(QtGui.QApplication.translate("Widget", "Name 3", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_3.item(3).setText(QtGui.QApplication.translate("Widget", "Name 4", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_3.item(4).setText(QtGui.QApplication.translate("Widget", "Name 5", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_3.item(5).setText(QtGui.QApplication.translate("Widget", "Name 6", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(QtGui.QApplication.translate("Widget", "Subname", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("Widget", "null", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("Widget", "Subname 1", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(2).setText(QtGui.QApplication.translate("Widget", "Subname 2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(3).setText(QtGui.QApplication.translate("Widget", "Subname 3", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(4).setText(QtGui.QApplication.translate("Widget", "Subname 4", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(QtGui.QApplication.translate("Widget", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.setSortingEnabled(False)
        __sortingEnabled = self.listWidget_8.isSortingEnabled()
        self.listWidget_8.setSortingEnabled(False)
        self.listWidget_8.item(0).setText(QtGui.QApplication.translate("Widget", "Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(1).setText(QtGui.QApplication.translate("Widget", "Lens", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(2).setText(QtGui.QApplication.translate("Widget", "Media", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(3).setText(QtGui.QApplication.translate("Widget", "Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(4).setText(QtGui.QApplication.translate("Widget", "Shader", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(5).setText(QtGui.QApplication.translate("Widget", "WorkFile", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(6).setText(QtGui.QApplication.translate("Widget", "Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(7).setText(QtGui.QApplication.translate("Widget", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(8).setText(QtGui.QApplication.translate("Widget", "ImageSequence", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(9).setText(QtGui.QApplication.translate("Widget", "Texture", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(10).setText(QtGui.QApplication.translate("Widget", "Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.item(11).setText(QtGui.QApplication.translate("Widget", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_8.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(QtGui.QApplication.translate("Widget", "Variant", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.item(0).setText(QtGui.QApplication.translate("Widget", "null", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(1).setText(QtGui.QApplication.translate("Widget", "Variant 1", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(2).setText(QtGui.QApplication.translate("Widget", "Variant 2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.item(3).setText(QtGui.QApplication.translate("Widget", "Variant 3", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(QtGui.QApplication.translate("Widget", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        self.listWidget_4.item(0).setText(QtGui.QApplication.translate("Widget", "null", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_4.item(1).setText(QtGui.QApplication.translate("Widget", "Resolution 1", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_4.item(2).setText(QtGui.QApplication.translate("Widget", "Resolution 2", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_4.item(3).setText(QtGui.QApplication.translate("Widget", "Resolution 3", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_4.item(4).setText(QtGui.QApplication.translate("Widget", "Resolution 4", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_4.item(5).setText(QtGui.QApplication.translate("Widget", "Resolution 5", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(QtGui.QApplication.translate("Widget", "Version", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        self.listWidget_5.item(0).setText(QtGui.QApplication.translate("Widget", "all versions", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_5.item(1).setText(QtGui.QApplication.translate("Widget", "online versions", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_5.item(2).setText(QtGui.QApplication.translate("Widget", "deleted versions", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_5.item(3).setText(QtGui.QApplication.translate("Widget", "latest version", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_5.item(4).setText(QtGui.QApplication.translate("Widget", "approved versions", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_5.setSortingEnabled(__sortingEnabled)

