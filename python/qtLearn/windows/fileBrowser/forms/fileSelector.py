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

import sys

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.ui_fileSelector as ui_fileSelector
import qtLearn.windows.fileBrowser.nodes as nodes


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


def getFileNodes(path):
    # Example data
    rootNode = nodes.Node('root', data=path)

    # Matchmove
    data = {'department': 'matchmove'}
    matchmoveDept = DeptNode('matchmove', parent=rootNode, data=data)
    data.update(task='camera')
    camTask = TaskNode('camera', parent=matchmoveDept, data=data)
    data.update(task='matchmove')
    mmTask = TaskNode('matchmove', parent=matchmoveDept, data=data)
    data.update(task='camera')
    data.update(name='bg01')
    camBg1Name = FileNameNode('bg01', parent=camTask, data=data)
    data.update(name='bg02')
    camBg2Name = FileNameNode('bg02', parent=camTask, data=data)
    data.update(name='bg03')
    camBg3Name = FileNameNode('bg03', parent=camTask, data=data)
    data.update(name='bg04')
    camBg4Name = FileNameNode('bg04', parent=camTask, data=data)
    data.update(name='bg05')
    camBg5Name = FileNameNode('bg05', parent=camTask, data=data)
    data.update(task='matchmove')
    data.update(name='john')
    matchmoveName = FileNameNode('john', parent=mmTask, data=data)
    # print('data', data)
    # sys.stdout.flush()

    # Layout
    data = {'department': 'layout'}
    layoutDept = DeptNode('layout', parent=rootNode, data=data)
    data.update(task='layout')
    layoutTask = TaskNode('layout', parent=layoutDept, data=data)
    data.update(name='camera')
    cameraName = FileNameNode('camera', parent=layoutTask, data=data)
    data.update(name='environment')
    envName = FileNameNode('environment', parent=layoutTask, data=data)
    data.update(name='layout')
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
    data.update(task='rig')
    textureTask = TaskNode('texture', parent=lookdevDept, data=data)
    data.update(task='rig')
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


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super(SortFilterProxyModel, self).__init__()
        self._department = ''

    def department(self):
        return self._department

    def setDepartment(self, value):
        self._department = value
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        result = False
        srcModel = self.sourceModel()
        column = self.filterKeyColumn()
        if column < 0:
            column = 0
        index = srcModel.index(sourceRow, column, sourceParent)
        node = index.internalPointer()
        typeInfo = node.typeInfo
        if typeInfo == 'department':
            dept = self.department()
            if len(dept) == 0:
                result = True
            elif node.name() == dept:
                result = True
        else:
            pattern = self.filterRegExp().pattern()
            if len(pattern) == 0:
                result = True
            else:
                path = node.allTags()
                if pattern in path:
                    result = True
        return result


class FileSelector(QtWidgets.QWidget, ui_fileSelector.Ui_Form):
    setTag = QtCore.Signal(str, str)
    changedFile = QtCore.Signal(str)

    def __init__(self, parent, withFolderFilter=True, withSearchLine=True):
        super(FileSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')
        self._path = ''

        if withFolderFilter is True:
            self.folderComboBox.show()
            self.folderLabel.show()
        else:
            self.folderComboBox.hide()
            self.folderLabel.hide()

        if withSearchLine is True:
            self.folderComboBox.show()
            self.folderLabel.show()
        else:
            self.folderComboBox.hide()
            self.folderLabel.hide()

        self.rootNode = getFileNodes(self._path)
        self.fileModel = FileModel(self.rootNode, font=self.font)

        self.fileFilterModel = SortFilterProxyModel()
        self.fileFilterModel.setSourceModel(self.fileModel)
        self.fileFilterModel.setDynamicSortFilter(True)
        self.fileFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)

        self.treeView.setModel(self.fileFilterModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.treeView.setHeaderHidden(True)
        self.treeView.expandAll()

        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.currentChanged.connect(self.currentChangedFunc)

        self.searchLineEdit.textChanged.connect(self.searchTextChanged)

    def searchTextChanged(self, text):
        self.fileFilterModel.setFilterRegExp(text)
        # if len(text) == 0:
        self.treeView.expandAll()

    def departmentChanged(self, value):
        self.fileFilterModel.setDepartment(value)
        self.treeView.expandAll()

    def setPath(self, path):
        self._path = path
        rootNode = getFileNodes(self._path)
        self.versionModel.setRootNode(rootNode)
        self.treeView.expandAll()

    def currentChangedFunc(self, index, prevIndex):
        if not index.isValid():
            return
        index_map = self.fileFilterModel.mapToSource(index)
        node = index_map.internalPointer()
        if node is None:
            return
        data = node.data()
        if data is None:
            return
        changed = False
        if 'department' in data:
            self.setTag.emit('department', data['department'])
            changed = True
        if 'task' in data:
            self.setTag.emit('task', data['task'])
            changed = True
        if 'name' in data:
            self.setTag.emit('name', data['name'])
            changed = True
        if changed:
            self.changedFile.emit(data['name'])
        return
