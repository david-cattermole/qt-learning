"""

"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_projectSeqShotComboBox as ui_projectSeqShotComboBox


NONE_STRING = '<none>'


class ProjectSeqShotComboBox(QtWidgets.QWidget, ui_projectSeqShotComboBox.Ui_Widget):
    signalSetTagStart = QtCore.Signal()
    signalSetTag = QtCore.Signal(str, str)
    signalSetTagEnd = QtCore.Signal()

    def __init__(self):
        super(ProjectSeqShotComboBox, self).__init__()
        self.setupUi(self)
        self._data = {}

        # Project / Sequence / Shot Filter
        projData = self.getProjects()
        self.projModel = QtCore.QStringListModel(projData)
        self.projectComboBox.setModel(self.projModel)

        # Sequence
        seqData = self.getSequences()
        self.seqModel = QtCore.QStringListModel(seqData)
        self.sequenceComboBox.setModel(self.seqModel)

        # Shot
        shotData = self.getShots()
        self.shotModel = QtCore.QStringListModel(shotData)
        self.shotComboBox.setModel(self.shotModel)

        # Internal signal / slots
        self.projectComboBox.currentIndexChanged.connect(self.slotProjectChanged)
        self.sequenceComboBox.currentIndexChanged.connect(self.slotSequenceChanged)
        self.shotComboBox.currentIndexChanged.connect(self.slotShotChanged)

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

    def getProjects(self):
        return list(sorted([
            '<none>',
            'babydriver',
            'bladerunner',
            'dunkirk',
            'interstellar',
            'xmen',
        ]))

    def getSequences(self):
        seqs = []
        project = self.data().get('project', None)
        if project is None or project == NONE_STRING:
            seqs = ['<none>']
        else:
            seqs = list(sorted(['sh', 'fin']))
        return seqs

    def getShots(self):
        project = self.getDataValue('project')
        sequence = self.getDataValue('sequence')
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

    ############################################################################

    @QtCore.Slot(int)
    def slotProjectChanged(self, index):
        proj = self.projectComboBox.currentText()
        self.setDataValue('project', proj)
        self.signalSetTagStart.emit()
        self.signalSetTag.emit('project', proj)
        self.updateSequenceData()
        self.signalSetTagEnd.emit()

    @QtCore.Slot(int)
    def slotSequenceChanged(self, index):
        proj = self.projectComboBox.currentText()
        seq = self.sequenceComboBox.currentText()
        self.setDataValue('project', proj)
        self.setDataValue('sequence', seq)
        self.signalSetTagStart.emit()
        self.signalSetTag.emit('sequence', seq)
        self.updateShotData()
        self.signalSetTagEnd.emit()

    @QtCore.Slot(int)
    def slotShotChanged(self, index):
        shot = self.shotComboBox.currentText()
        self.setDataValue('shot', shot)
        self.signalSetTagStart.emit()
        self.signalSetTag.emit('shot', shot)
        self.signalSetTagEnd.emit()
        # self.updateDepartmentData()

    ############################################################################

    def updateSequenceData(self):
        seqs = self.getSequences()
        self.seqModel.setStringList(seqs)
        self.sequenceComboBox.setCurrentIndex(0)

    def updateShotData(self):
        shots = self.getShots()
        self.shotModel.setStringList(shots)
        self.shotComboBox.setCurrentIndex(0)


