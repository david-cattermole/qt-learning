"""
Environment filter. Sets the project / sequence / shot (and user and department)
"""

import getpass

import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets
import qtLearn.windows.fileBrowser.forms.ui_envFilter as ui_envFilter

NONE_STRING = '<none>'


class EnvFilter(QtWidgets.QWidget, ui_envFilter.Ui_Form):
    setTag = QtCore.Signal(str, str)

    changedProject = QtCore.Signal(str)
    changedSequence = QtCore.Signal(str, str)
    changedShot = QtCore.Signal(str)
    changedDepartment = QtCore.Signal(str)
    changedUser = QtCore.Signal(str)

    def __init__(self, parent, withDepartmentFilter=True, withUserFilter=True):
        super(EnvFilter, self).__init__()
        self.setupUi(self)
        self.parent = parent

        # Project
        projData = self.getProjects()
        # TODO: Refactor getProjects function location. Should we add this to
        # the class and allow the user to override it?
        self.projModel = QtCore.QStringListModel(projData)
        self.projectComboBox.setModel(self.projModel)

        # Sequence
        # TODO: Refactor getSequences function location. Should we add this to
        # the class and allow the user to override it?
        seqData = self.getSequences(None)
        self.seqModel = QtCore.QStringListModel(seqData)
        self.sequenceComboBox.setModel(self.seqModel)

        # Shot
        # TODO: Refactor getShots function location. Should we add this to
        # the class and allow the user to override it?
        shotData = self.getShots(None, None)
        self.shotModel = QtCore.QStringListModel(shotData)
        self.shotComboBox.setModel(self.shotModel)

        # Department
        # TODO: Should we pick a more generic name for the department filter?
        if withDepartmentFilter is True:
            # TODO: Refactor getDepartments function location.
            deptData = self.getDepartments()
            self.deptModel = QtCore.QStringListModel(deptData)
            self.departmentComboBox.setModel(self.deptModel)
        else:
            self.departmentComboBox.hide()
            self.departmentLabel.hide()

        # Users
        if withUserFilter is True:
            # TODO: Refactor getUsers function location.
            userData = self.getUsers()
            self.userModel = QtCore.QStringListModel(userData)
            self.userComboBox.setModel(self.userModel)
        else:
            self.userComboBox.hide()
            self.userLabel.hide()

        self.projectComboBox.currentIndexChanged.connect(self.projectChanged)
        self.sequenceComboBox.currentIndexChanged.connect(self.sequenceChanged)
        self.shotComboBox.currentIndexChanged.connect(self.shotChanged)
        self.departmentComboBox.currentIndexChanged.connect(self.departmentChanged)
        self.userComboBox.currentIndexChanged.connect(self.userChanged)

        self.changedProject.connect(self.updateSequenceData)
        self.changedSequence.connect(self.updateShotData)

    def getProjects(self):
        return list(sorted([
            '<none>',
            'babydriver',
            'bladerunner',
            'dunkirk',
            'interstellar',
            'xmen',
        ]))

    def getSequences(self, project):
        seqs = []
        if project is None or project == NONE_STRING:
            seqs = ['<none>']
        else:
            seqs = list(sorted(['sh', 'fin']))
        return seqs

    def getShots(self, project, sequence):
        shots = []
        if (project is None or sequence is None or
            project == NONE_STRING or sequence == NONE_STRING):
            shots = ['<none>']
        else:
            tmp_shots = [
                'fin0010', 'fin0020', 'fin0030', 'fin0040',
                'sh0010', 'sh0020', 'sh0030', 'sh0040',
                'sh0050', 'sh0060', 'sh0070', 'sh0080',
                'sh0090', 'sh0100', 'sh0110', 'sh0120',
            ]
            for shot in tmp_shots:
                if sequence in shot:
                    shots.append(shot)
            shots = list(sorted(shots))
        return shots

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

    def projectChanged(self):
        text = self.projectComboBox.currentText()
        self.changedProject.emit(text)
        self.setTag.emit('project', text)

    def sequenceChanged(self):
        proj = self.projectComboBox.currentText()
        seq = self.sequenceComboBox.currentText()
        self.changedSequence.emit(proj, seq)
        self.setTag.emit('sequence', seq)

    def shotChanged(self):
        text = self.shotComboBox.currentText()
        # self.changedShot.emit(text)
        self.setTag.emit('shot', text)

    def departmentChanged(self):
        dept = self.departmentComboBox.currentText()
        dept = dept.lower()
        if not dept.isalpha():
            dept = None
        self.changedDepartment.emit(dept)

    def userChanged(self):
        user = self.userComboBox.currentText()
        user = user.lower()
        if not user.isalpha():
            if 'current' in user:
                user = getpass.getuser()
                user = user.lower()
            else:
                user = None
        self.changedUser.emit(user)

    def updateSequenceData(self, project):
        seqs = self.getSequences(project)
        self.seqModel.setStringList(seqs)
        self.sequenceComboBox.setCurrentIndex(0)

    def updateShotData(self, project, sequence):
        shots = self.getShots(project, sequence)
        self.shotModel.setStringList(shots)
        self.shotComboBox.setCurrentIndex(0)


