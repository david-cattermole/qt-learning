# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\base.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(422, 315)
        Window.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.options = QtWidgets.QWidget(self.centralwidget)
        self.options.setObjectName("options")
        self.optionsLayout = QtWidgets.QVBoxLayout(self.options)
        self.optionsLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsLayout.setSpacing(3)
        self.optionsLayout.setObjectName("optionsLayout")
        self.verticalLayout.addWidget(self.options)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createBtn.setObjectName("createBtn")
        self.horizontalLayout.addWidget(self.createBtn)
        self.applyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.applyBtn.setObjectName("applyBtn")
        self.horizontalLayout.addWidget(self.applyBtn)
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout.addWidget(self.resetBtn)
        self.helpBtn = QtWidgets.QPushButton(self.centralwidget)
        self.helpBtn.setObjectName("helpBtn")
        self.horizontalLayout.addWidget(self.helpBtn)
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 18))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(Window)
        self.statusBar.setObjectName("statusBar")
        Window.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(Window)
        self.toolBar.setObjectName("toolBar")
        Window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(Window)
        self.closeBtn.clicked.connect(Window.close)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.createBtn.setText(_translate("Window", "Create"))
        self.applyBtn.setText(_translate("Window", "Apply"))
        self.resetBtn.setText(_translate("Window", "Reset"))
        self.helpBtn.setText(_translate("Window", "Help"))
        self.closeBtn.setText(_translate("Window", "Close"))
        self.toolBar.setWindowTitle(_translate("Window", "toolBar"))

