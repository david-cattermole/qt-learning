"""

"""

import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets
import qtLearn.windows.fileBrowser.forms.ui_envFilter as ui_envFilter


def getProjects():
    return list(sorted([
        'project1',
        'project2',
        'project3',
        'project4',
        'project5',
    ]))


def getSequences():
    return list(sorted([
        'sh', 'fin'
    ]))


def getShots():
    return list(sorted([
        'fin0010', 'fin0020', 'fin0030', 'fin0040',
        'sh0010', 'sh0020', 'sh0030', 'sh0040',
        'sh0050', 'sh0060', 'sh0070', 'sh0080',
        'sh0090', 'sh0100', 'sh0110', 'sh0120',
    ]))


def getDepartments():
    return [
        '<all departments>', 'animation', 'matchmove', 'layout',
        'light', 'fx', 'model', 'rig', 'lookdev',
        'pipeline'
    ]


def getUsers():
    return [
        '<all users>', '<current user>', 'davidc', 'bob', 'john', 'sally'
    ]


class EnvFilter(QtWidgets.QWidget, ui_envFilter.Ui_Form):
    def __init__(self, parent):
        super(EnvFilter, self).__init__()
        self.setupUi(self)
        self.parent = parent

        # Project ComboBox
        projData = getProjects()
        projModel = QtCore.QStringListModel(projData)
        self.projectComboBox.setModel(projModel)

        # Sequence ComboBox
        seqData = getSequences()
        seqModel = QtCore.QStringListModel(seqData)
        self.sequenceComboBox.setModel(seqModel)

        # Shot ComboBox
        shotData = getShots()
        shotModel = QtCore.QStringListModel(shotData)
        self.shotComboBox.setModel(shotModel)

        # Department ComboBox
        deptData = getDepartments()
        deptModel = QtCore.QStringListModel(deptData)
        self.departmentComboBox.setModel(deptModel)

        # Users ComboBox
        userData = getUsers()
        userModel = QtCore.QStringListModel(userData)
        self.userComboBox.setModel(userModel)

