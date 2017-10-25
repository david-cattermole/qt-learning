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

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.forms.ui_fileSelector as ui_fileSelector
import qtLearn.windows.fileBrowser.nodes as nodes


class FileNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None,
                 enabled=True,
                 editable=False,
                 selectable=True,
                 checkable=False,
                 neverHasChildren=False):
        super(FileNode, self).__init__(name,
                                       data=data,
                                       parent=parent,
                                       editable=editable,
                                       selectable=selectable,
                                       checkable=checkable,
                                       neverHasChildren=neverHasChildren)
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/File.png'))
        self.typeInfo = 'file'


class DeptNode(nodes.Node):
    def __init__(self, name,
                 parent=None):
        super(DeptNode, self).__init__(name,
                                       parent=parent,
                                       editable=False,
                                       selectable=False)
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/Department.png'))
        self.typeInfo = 'department'


class TaskNode(nodes.Node):
    def __init__(self, name,
                 parent=None):
        super(TaskNode, self).__init__(name,
                                       parent=parent,
                                       editable=False,
                                       selectable=False)
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/Task.png'))
        self.typeInfo = 'task'


class FileNameNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None):
        super(FileNameNode, self).__init__(name,
                                           parent=parent,
                                           editable=False,
                                           selectable=True,
                                           data=data)
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/FileName.png'))
        self.typeInfo = 'filename'


def getFileNodes(path):
    # Example data
    rootNode = nodes.Node('root', data=path)

    # Matchmove
    matchmoveDept = DeptNode('matchmove', parent=rootNode)
    camTask = TaskNode('camera', parent=matchmoveDept)
    mmTask = TaskNode('matchmove', parent=matchmoveDept)
    camBg1Name = FileNameNode('bg01', parent=camTask, data='matchmove/camera/bg01')
    camBg2Name = FileNameNode('bg02', parent=camTask, data='matchmove/camera/bg02')
    camBg3Name = FileNameNode('bg03', parent=camTask, data='matchmove/camera/bg03')
    camBg4Name = FileNameNode('bg04', parent=camTask, data='matchmove/camera/bg04')
    camBg5Name = FileNameNode('bg05', parent=camTask, data='matchmove/camera/bg05')
    matchmoveName = FileNameNode('john', parent=mmTask, data='matchmove/matchmove/john')

    # Layout
    layoutDept = DeptNode('layout', parent=rootNode)
    layoutTask = TaskNode('layout', parent=layoutDept)
    cameraName = FileNameNode('camera', parent=layoutTask, data='layout/layout/camera')
    envName = FileNameNode('environment', parent=layoutTask, data='layout/layout/environment')
    layoutName = FileNameNode('layout', parent=layoutTask, data='layout/layout/layout')

    # Animation
    animDept = DeptNode('animation', parent=rootNode)
    animTask = TaskNode('anim', parent=animDept)
    animationName = FileNameNode('animation', parent=animTask, data='animation/anim/animation')

    # Lighting
    lightDept = DeptNode('light', parent=rootNode)
    lightTask = TaskNode('light', parent=lightDept)
    lightName = FileNameNode('light', parent=lightTask, data='light/light/light')

    # Effects
    effectsDept = DeptNode('effects', parent=rootNode)
    destTask = TaskNode('destruction', parent=effectsDept)
    waterTask = TaskNode('water', parent=effectsDept)
    fireTask = TaskNode('fire', parent=effectsDept)
    fxName = FileNameNode('fx', parent=destTask, data='fx/destruction/fx')
    fxName = FileNameNode('fx', parent=waterTask, data='fx/water/fx')
    fxName = FileNameNode('fx', parent=fireTask, data='fx/fire/fx')

    # Model
    modelDept = DeptNode('model', parent=rootNode)
    modelTask = TaskNode('model', parent=modelDept)
    sculptTask = TaskNode('sculpt', parent=modelDept)
    modelName = FileNameNode('model', parent=modelTask, data='model/model/model')
    sculptName = FileNameNode('sculpt', parent=sculptTask, data='model/sculpt/sculpt')

    # Rig
    rigDept = DeptNode('rig', parent=rootNode)
    rigTask = TaskNode('rig', parent=rigDept)
    johnName = FileNameNode('john', parent=rigTask, data='rig/rig/john')
    
    # Lookdev
    lookdevDept = DeptNode('lookdev', parent=rootNode)
    textureTask = TaskNode('texture', parent=lookdevDept)
    shaderTask = TaskNode('shader', parent=lookdevDept)
    textureName = FileNameNode('texture', parent=textureTask, data='lookdev/texture/texture')
    shaderName = FileNameNode('shader', parent=shaderTask, data='lookdev/shader/shader')
    
    # Pipeline
    pipelineDept = DeptNode('pipeline', parent=rootNode)
    pipelineTask = TaskNode('pipeline', parent=pipelineDept)
    pipelineName = FileNameNode('pipeline', parent=pipelineTask, data='pipeline/pipeline/pipeline')

    return rootNode


class FileModel(nodes.ItemModel):
    def __init__(self, root, font=None):
        super(FileModel, self).__init__(root, font=font)
        self._rootNode = root
        self._column_names = {
            0: 'Name',
        }

    def columnCount(self, parent):
        return 1


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

    def __init__(self, parent):
        super(FileSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        self._path = ''
        self.rootNode = getFileNodes(self._path)

        # Setup data, filter/sorting model.
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
        if len(text) == 0:
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
        dataSplit = node.data().split('/')
        if len(dataSplit) == 3:
            dept = dataSplit[0]
            task = dataSplit[1]
            name = dataSplit[2]
            self.setTag.emit('department', dept)
            self.setTag.emit('task', task)
            self.setTag.emit('name', name)
            self.changedFile.emit(data)
