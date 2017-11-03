"""
Displays a tree of possible files.

Inputs:
- Function for creating the tree names and adding arbitrary key-value pairs to the tree items.
- Define filtering function of the tree names based on a given string.
- Define if single or multiple selections are allowed.

Outputs:
- String to be returned that is associated with the file name given. Selected node must be an end-node, parent nodes cannot be selected.

TODO:
- Hook everything up.
"""

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.nodes as nodes
import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.ui_fileSelector as ui_fileSelector


class FileNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None,
                 icon=None,
                 enabled=True,
                 editable=False,
                 selectable=True,
                 checkable=False,
                 neverHasChildren=False):
        if icon is None:
            icon = QtGui.QIcon(QtGui.QPixmap(':/File.png'))
        super(FileNode, self).__init__(name,
                                       parent=parent,
                                       data=data,
                                       icon=icon,
                                       editable=editable,
                                       selectable=selectable,
                                       checkable=checkable,
                                       neverHasChildren=neverHasChildren)
        self.typeInfo = 'file'


class DeptNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None):
        icon = QtGui.QIcon(QtGui.QPixmap(':/Department.png'))
        super(DeptNode, self).__init__(name,
                                       parent=parent,
                                       data=data,
                                       icon=icon,
                                       editable=False,
                                       selectable=False)
        self.typeInfo = 'department'


class TaskNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None):
        icon = QtGui.QIcon(QtGui.QPixmap(':/Task.png'))
        super(TaskNode, self).__init__(name,
                                       parent=parent,
                                       data=data,
                                       icon=icon,
                                       editable=False,
                                       selectable=False)
        self.typeInfo = 'task'


class FileNameNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None):
        icon = QtGui.QIcon(QtGui.QPixmap(':/FileName.png'))
        super(FileNameNode, self).__init__(name,
                                           parent=parent,
                                           icon=icon,
                                           editable=False,
                                           selectable=True,
                                           data=data)
        self.typeInfo = 'filename'


class FileModel(nodes.ItemModel):
    def __init__(self, root, font=None):
        super(FileModel, self).__init__(root, font=font)
        self._rootNode = root
        self._column_names = {
            0: 'Name',
        }
        self._node_attr_key = {
            'Name': 'name',
        }

class FileSelector(QtWidgets.QWidget, ui_fileSelector.Ui_Form):
    signalSetTagStart = QtCore.Signal()
    signalSetTag = QtCore.Signal(str, str)
    signalSetTagEnd = QtCore.Signal()
    signalSetFileName = QtCore.Signal(dict)

    def __init__(self, parent,
                 withFolderFilter=True,
                 folderFilterLabel=None,
                 folderFilterTagName=None,
                 folderFilterNodeType=None,
                 withSearchLine=True,
                 pathFormat=None):
        super(FileSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')
        self._data = {}
        self._path = ''

        self._pathFormat = pathFormat
        if pathFormat is None:
            self._pathFormat = '/projects/{project}/{sequence}/{shot}/{department}/{task}/{name}_{major}.{minor}.{ext}'

        self.folderModel = None
        if withFolderFilter is True:
            self.folderComboBox.show()
            self.folderLabel.show()
            if isinstance(folderFilterLabel, str):
                self.folderLabel.setText(folderFilterLabel)
            else:
                raise ValueError
            filterData = self.getFolderFilterData()
            self.folderModel = QtCore.QStringListModel(filterData)
            self.folderComboBox.setModel(self.folderModel)
        else:
            self.folderComboBox.hide()
            self.folderLabel.hide()

        if withSearchLine is True:
            self.searchLineEdit.show()
        else:
            self.searchLineEdit.hide()

        self.rootNode = self.getFileNodes()
        self.fileModel = FileModel(self.rootNode, font=self.font)

        self.fileFilterModel = nodes.SortFilterProxyModel()
        self.fileFilterModel.setSourceModel(self.fileModel)
        self.fileFilterModel.setDynamicSortFilter(True)
        self.fileFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)

        self._folderFilterTagName = None
        if folderFilterTagName is not None:
            if isinstance(folderFilterTagName, str):
                self._folderFilterTagName = folderFilterTagName
            else:
                raise ValueError
        self.fileFilterModel.setFilterTagName(self._folderFilterTagName)

        self._folderFilterNodeType = None
        if folderFilterNodeType is not None:
            if isinstance(folderFilterNodeType, str):
                self._folderFilterNodeType = folderFilterNodeType
            else:
                raise ValueError
        self.fileFilterModel.setFilterTagNodeType(self._folderFilterNodeType)

        self.treeView.setModel(self.fileFilterModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.treeView.setHeaderHidden(True)
        self.treeView.expandAll()

        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.currentChanged.connect(self.slotCurrentChanged)
        # self.selectionModel.selectionChanged.connect(self.slotSelectionChanged)

        self.searchLineEdit.textChanged.connect(self.slotSearchTextChanged)

        self.folderComboBox.currentIndexChanged.connect(self.slotFolderFilterChanged)

        # self.folderFilterChanged.connect(self.setDepartment)

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

    def getFolderFilterTagName(self):
        # print('getFolderFilterTagName')
        return self._folderFilterTagName

    def getFolderFilterTagNodeType(self):
        # print('getFolderFilterTagNodeType')
        return self._folderFilterNodeType

    ############################################################################

    def getFolderFilterData(self):
        return [
            '<all tasks>', 'anim', 'matchmove', 'layout',
            'light', 'effects', 'model', 'rig', 'lookdev',
            'pipeline'
        ]

    def getFileNodes(self):
        path = self.getDataValue('path')

        # Example data
        rootNode = nodes.Node('root', data=path)

        # Matchmove
        data = {'department': 'matchmove'}
        matchmoveDept = DeptNode('matchmove', parent=rootNode, data=data)
        data['task'] = 'camera'
        camTask = TaskNode('camera', parent=matchmoveDept, data=data)
        data['name'] = 'bg01'
        camBg1Name = FileNameNode('bg01', parent=camTask, data=data)
        data['name'] = 'bg02'
        camBg2Name = FileNameNode('bg02', parent=camTask, data=data)
        data['name'] = 'bg03'
        camBg3Name = FileNameNode('bg03', parent=camTask, data=data)
        data['name'] = 'bg04'
        camBg4Name = FileNameNode('bg04', parent=camTask, data=data)
        data['name'] = 'bg05'
        camBg5Name = FileNameNode('bg05', parent=camTask, data=data)
        data['task'] = 'matchmove'
        mmTask = TaskNode('matchmove', parent=matchmoveDept, data=data)
        data['name'] = 'john'
        matchmoveName = FileNameNode('john', parent=mmTask, data=data)

        # Layout
        data = {'department': 'layout'}
        layoutDept = DeptNode('layout', parent=rootNode, data=data)
        data['task'] = 'layout'
        layoutTask = TaskNode('layout', parent=layoutDept, data=data)
        data['name'] = 'camera'
        cameraName = FileNameNode('camera', parent=layoutTask, data=data)
        data['name'] = 'environment'
        envName = FileNameNode('environment', parent=layoutTask, data=data)
        data['name'] = 'layout'
        layoutName = FileNameNode('layout', parent=layoutTask, data=data)

        # Animation
        data = {'department': 'animation'}
        animDept = DeptNode('animation', parent=rootNode, data=data)
        data.update(task='anim')
        animTask = TaskNode('anim', parent=animDept, data=data)
        data.update(name='animation')
        animationName = FileNameNode('animation', parent=animTask, data=data)

        # Lighting
        data = {'department': 'light'}
        lightDept = DeptNode('light', parent=rootNode, data=data)
        data.update(task='light')
        lightTask = TaskNode('light', parent=lightDept, data=data)
        data.update(name='light')
        lightName = FileNameNode('light', parent=lightTask, data=data)

        # Effects
        data = {'department': 'effects'}
        effectsDept = DeptNode('effects', parent=rootNode)

        data = {'department': 'effects', 'task': 'destruction'}
        destTask = TaskNode('destruction', parent=effectsDept, data=data)
        data.update(name='fx')
        fxName = FileNameNode('fx', parent=destTask, data=data)

        data = {'department': 'effects', 'task': 'water'}
        waterTask = TaskNode('water', parent=effectsDept, data=data)
        data.update(name='fx')
        fxName = FileNameNode('fx', parent=waterTask, data=data)

        data = {'department': 'effects', 'task': 'fire'}
        fireTask = TaskNode('fire', parent=effectsDept, data=data)
        data.update(name='fx')
        fxName = FileNameNode('fx', parent=fireTask, data=data)

        # Model
        data = {'department': 'model'}
        modelDept = DeptNode('model', parent=rootNode, data=data)

        data.update(task='model')
        modelTask = TaskNode('model', parent=modelDept, data=data)

        data.update(task='sculpt')
        sculptTask = TaskNode('sculpt', parent=modelDept, data=data)

        data.update(task='proxy')
        proxyTask = TaskNode('proxy', parent=modelDept, data=data)

        data.update(name='model')
        modelName = FileNameNode('model', parent=modelTask, data=data)

        data.update(name='sculpt')
        sculptName = FileNameNode('sculpt', parent=sculptTask, data=data)

        data.update(name='model')
        proxyName = FileNameNode('model', parent=proxyTask, data=data)

        # Rig
        data = {'department': 'rig'}
        rigDept = DeptNode('rig', parent=rootNode, data=data)
        data.update(task='rig')
        rigTask = TaskNode('rig', parent=rigDept, data=data)
        data.update(name='john')
        johnName = FileNameNode('john', parent=rigTask, data=data)

        # Lookdev
        data = {'department': 'lookdev'}
        lookdevDept = DeptNode('lookdev', parent=rootNode, data=data)
        data.update(task='texture')
        textureTask = TaskNode('texture', parent=lookdevDept, data=data)
        data.update(task='shader')
        shaderTask = TaskNode('shader', parent=lookdevDept, data=data)
        data.update(name='texture')
        textureName = FileNameNode('texture', parent=textureTask, data=data)
        data.update(name='shader')
        shaderName = FileNameNode('shader', parent=shaderTask, data=data)

        # Pipeline
        data = {'department': 'pipeline'}
        pipelineDept = DeptNode('pipeline', parent=rootNode, data=data)
        data.update(task='pipeline')
        pipelineTask = TaskNode('pipeline', parent=pipelineDept, data=data)
        data.update(name='pipeline')
        pipelineName = FileNameNode('pipeline', parent=pipelineTask, data=data)

        return rootNode

    ############################################################################

    @QtCore.Slot(str)
    def slotSearchTextChanged(self, text):
        self.fileFilterModel.setFilterRegExp(text)
        self.treeView.expandAll()

    @QtCore.Slot(int)
    def slotFolderFilterChanged(self, index):
        folderFilter = self.folderComboBox.currentText()
        folderFilter = folderFilter.lower()
        if not folderFilter.isalpha():
            folderFilter = None
        self.fileFilterModel.setFilterTagValue(folderFilter)
        self.treeView.expandAll()

    @QtCore.Slot(str)
    def slotSetFilterTagValue(self, value):
        self.fileFilterModel.setFilterTagValue(value)
        self.treeView.expandAll()

    @QtCore.Slot(dict)
    def slotSetPathData(self, tags):
        # print('FileSelector slotSetPathData', tags)
        if not isinstance(tags, dict):
            return
        self._data.update(**tags)
        changed = bool(len(tags.keys()))
        if changed:
            rootNode = self.getFileNodes()
            self.fileModel.setRootNode(rootNode)
            self.treeView.expandAll()
        return

    @QtCore.Slot(QtCore.QModelIndex, QtCore.QModelIndex)
    def slotCurrentChanged(self, index, prevIndex):
        # print('FileSelector currentChanged START', repr(index), repr(prevIndex))

        if not index.isValid():
            return
        index_map = self.fileFilterModel.mapToSource(index)
        node = index_map.internalPointer()
        if node is None:
            return
        nodeData = node.data()
        if nodeData is None:
            return

        # Emit tag signals
        self.signalSetTagStart.emit()
        for key in nodeData.keys():
            newValue = nodeData.get(key)
            self.setDataValue(key, nodeData[key])
            self.signalSetTag.emit(key, newValue)
        self.signalSetTagEnd.emit()
        # print('FileSelector currentChanged nodeData', repr(nodeData))

        # print('FileSelector currentChanged END')
        return

    # @QtCore.Slot(QtCore.QItemSelection, QtCore.QItemSelection)
    # def slotSelectionChanged(self, selected, deselected):
    #     print('FileSelector selectionChanged START', repr(selected), repr(deselected))
    #
    #     indexes = selected.indexes()
    #     for index in indexes:
    #         print('FileSelector selectionChanged index', repr(index), index.isValid())
    #         if index.isValid() is False:
    #             return
    #         # index_map = self.fileFilterModel.mapToSource(index)
    #         # node = index_map.internalPointer()
    #         node = index.internalPointer()
    #         if node is None:
    #             return
    #         nodeName = node.name()
    #         nodeData = node.data()
    #         if nodeData is None:
    #             return
    #
    #         # Emit tag signals
    #         self.signalSetTagStart.emit()
    #         for key in nodeData.keys():
    #             newValue = nodeData.get(key)
    #             self.setDataValue(key, nodeData[key])
    #             self.signalSetTag.emit(key, newValue)
    #         self.signalSetTagEnd.emit()
    #         print('FileSelector selectionChanged nodeData', repr(nodeName), repr(nodeData))
    #
    #     print('FileSelector selectionChanged END')
    #     return