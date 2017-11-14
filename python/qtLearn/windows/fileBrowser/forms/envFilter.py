"""
Environment filter. Sets the project / sequence / shot (and user and department)
"""

import getpass

import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets
import qtLearn.windows.fileBrowser.forms.ui_envFilter as ui_envFilter
import qtLearn.widgets.projectSeqShotComboBox as projectSeqShotComboBox

NONE_STRING = '<none>'


class EnvFilter(QtWidgets.QWidget, ui_envFilter.Ui_Form):
    signalSetTagStart = QtCore.Signal()
    signalSetTag = QtCore.Signal(str, str)
    signalSetTagEnd = QtCore.Signal()
    signalSetUser = QtCore.Signal(str)
    signalSetDepartment = QtCore.Signal(str)

    def __init__(self, parent, withDepartmentFilter=True, withUserFilter=True):
        super(EnvFilter, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self._data = {}

        # Project / Sequence / Shot Filter
        self.projSeqShotComboBox = projectSeqShotComboBox.ProjectSeqShotComboBox()
        self.projectSeqShotLayout.addWidget(self.projSeqShotComboBox)

        # Department
        # TODO: Should we pick a more generic name for the department filter?
        self.deptModel = None
        if withDepartmentFilter is True:
            deptData = self.getDepartments()
            self.deptModel = QtCore.QStringListModel(deptData)
            self.departmentComboBox.setModel(self.deptModel)
        else:
            self.departmentComboBox.hide()
            self.departmentLabel.hide()

        # Users
        self.userModel = None
        if withUserFilter is True:
            userData = self.getUsers()
            self.userModel = QtCore.QStringListModel(userData)
            self.userComboBox.setModel(self.userModel)
        else:
            self.userComboBox.hide()
            self.userLabel.hide()

        # signal / slots
        self.projSeqShotComboBox.signalSetTagStart.connect(self.slotSetTagStart)
        self.projSeqShotComboBox.signalSetTag.connect(self.slotSetTag)
        self.projSeqShotComboBox.signalSetTagEnd.connect(self.slotSetTagEnd)
        self.departmentComboBox.currentIndexChanged.connect(self.slotDepartmentChanged)
        self.userComboBox.currentIndexChanged.connect(self.slotUserChanged)

    ############################################################################

    def data(self):
        if self._data is None:
            return {}
        return self._data.copy()

    def setData(self, value):
        self._data = value

    def getDataValue(self, key, default=None):
        return self._data.get(key, default)

    def setDataValue(self, key, value):
        self._data[key] = value

    ############################################################################

    def getDepartments(self):
        return [
            '<all departments>', 'animation', 'matchmove', 'layout',
            'light', 'effects', 'model', 'rig', 'lookdev',
            'pipeline'
        ]

    def getUsers(self):
        return [
            '<all users>', '<current user>', 'davidc', 'bob', 'john', 'sally'
        ]

    ############################################################################

    @QtCore.Slot()
    def slotSetTagStart(self):
        self.signalSetTagStart.emit()
        return

    @QtCore.Slot(str, str)
    def slotSetTag(self, key, value):
        self.signalSetTag.emit(key, value)
        # if key == 'shot':
        #     self.updateDepartmentData()
        return

    @QtCore.Slot()
    def slotSetTagEnd(self):
        self.signalSetTagEnd.emit()
        return

    @QtCore.Slot(int)
    def slotDepartmentChanged(self, index):
        dept = self.departmentComboBox.currentText() or ''
        dept = dept.lower()
        if not dept.isalpha():
            dept = None
        self.setDataValue('department', dept)
        self.signalSetDepartment.emit(dept)
        self.updateUserData()

    @QtCore.Slot(int)
    def slotUserChanged(self, index):
        user = self.userComboBox.currentText() or ''
        user = user.lower()
        if not user.isalpha():
            if 'current' in user:
                user = getpass.getuser()
                user = user.lower()
            else:
                user = None
        self.setDataValue('user', user)
        self.signalSetUser.emit(user)

    ############################################################################

    def updateDepartmentData(self):
        if self.deptModel is None:
            return
        depts = self.getDepartments()
        self.deptModel.setStringList(depts)
        self.departmentComboBox.setCurrentIndex(0)

    def updateUserData(self):
        if self.userModel is None:
            return
        users = self.getUsers()
        self.userModel.setStringList(users)
        self.userComboBox.setCurrentIndex(0)


