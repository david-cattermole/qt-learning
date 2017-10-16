# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/davidc/dev/qt-learning/ui/windows/base.ui'
#
# Created: Mon Oct 16 23:43:55 2017
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(422, 315)
        self.centralwidget = QtGui.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.options = QtGui.QWidget(self.centralwidget)
        self.options.setObjectName("options")
        self.optionsLayout = QtGui.QVBoxLayout(self.options)
        self.optionsLayout.setObjectName("optionsLayout")
        self.verticalLayout.addWidget(self.options)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createBtn = QtGui.QPushButton(self.centralwidget)
        self.createBtn.setObjectName("createBtn")
        self.horizontalLayout.addWidget(self.createBtn)
        self.applyBtn = QtGui.QPushButton(self.centralwidget)
        self.applyBtn.setObjectName("applyBtn")
        self.horizontalLayout.addWidget(self.applyBtn)
        self.resetBtn = QtGui.QPushButton(self.centralwidget)
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout.addWidget(self.resetBtn)
        self.helpBtn = QtGui.QPushButton(self.centralwidget)
        self.helpBtn.setObjectName("helpBtn")
        self.horizontalLayout.addWidget(self.helpBtn)
        self.closeBtn = QtGui.QPushButton(self.centralwidget)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(Window)
        self.statusBar.setObjectName("statusBar")
        Window.setStatusBar(self.statusBar)

        self.retranslateUi(Window)
        QtCore.QObject.connect(self.closeBtn, QtCore.SIGNAL("clicked()"), Window.close)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(QtGui.QApplication.translate("Window", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.createBtn.setText(QtGui.QApplication.translate("Window", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.applyBtn.setText(QtGui.QApplication.translate("Window", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.resetBtn.setText(QtGui.QApplication.translate("Window", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.helpBtn.setText(QtGui.QApplication.translate("Window", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.closeBtn.setText(QtGui.QApplication.translate("Window", "Close", None, QtGui.QApplication.UnicodeUTF8))

