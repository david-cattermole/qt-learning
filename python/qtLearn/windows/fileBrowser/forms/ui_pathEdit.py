# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\qt-learning\ui\windows\fileBrowser\forms\pathEdit.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 40)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editCheckBox = QtWidgets.QCheckBox(Form)
        self.editCheckBox.setText("")
        self.editCheckBox.setObjectName("editCheckBox")
        self.horizontalLayout.addWidget(self.editCheckBox)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.editCheckBox.toggled['bool'].connect(self.lineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Path"))
        self.lineEdit.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">/data/project/seq/shot/working/dept/shot_name_ver_user_desc.ext</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">project = mazda</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">seq = sh</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">shot = sh0010</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">dept = layout</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">name = camera</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">ver = v001.001</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">user = davidc</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">desc = thisIsTheDescription</span></p><p><span style=\" font-family:\'Monospace\'; font-size:10pt;\">ext = mb</span></p></body></html>"))
        self.lineEdit.setText(_translate("Form", "/data/mazda/sh/sh0010/working/layout/sh0010_camera_v001.001_davidc_thisIsTheDescription.mb"))

