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
                 data = None,
                 enabled = True,
                 editable = False,
                 selectable = True,
                 checkable = False,
                 neverHasChildren = False):
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


class FileSelector(QtWidgets.QWidget, ui_fileSelector.Ui_Form):
    setTag = QtCore.Signal(str, str)

    def __init__(self, parent):
        super(FileSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        self._path = ''
        self.rootNode = getFileNodes(self._path)

        # Setup data, filter/sorting model.
        self.fileModel = FileModel(self.rootNode, font=self.font)
        self.fileFilterModel = QtCore.QSortFilterProxyModel()
        self.fileFilterModel.setSourceModel(self.fileModel)
        self.fileFilterModel.setDynamicSortFilter(True)
        self.fileFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.searchLineEdit.textChanged.connect(self.fileFilterModel.setFilterRegExp)
        self.treeView.setModel(self.fileFilterModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.treeView.expandAll()

        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.currentChanged.connect(self.currentChangedFunc)

    def setPath(self, path):
        # print('VersionSelector setPath:', path)
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

    # def selectionChangedFunc(self, selected, deselected=None):
    #     for index in selected.indexes():
    #         if not index.isValid():
    #             continue
    #         index_map = self.fileFilterModel.mapToSource(index)
    #         node = index_map.internalPointer()
    #         if node is None:
    #             continue
    #         dataSplit = node.data().split('/')
    #         # print('fileSelector selectionChangedFunc:', dataSplit)
    #         if len(dataSplit) == 3:
    #             dept = dataSplit[0]
    #             task = dataSplit[1]
    #             name = dataSplit[2]
    #             self.setTag.emit('department', dept)
    #             self.setTag.emit('task', task)
    #             self.setTag.emit('name', name)
