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


class DeptNode(nodes.Node):
    def __init__(self, name,
                 parent=None):
        super(DeptNode, self).__init__(name,
                                       parent=parent,
                                       editable=False,
                                       selectable=False)
        self.typeInfo = 'department'

    def icon(self):
        if self._icon is None:
            self._icon = QtGui.QIcon(QtGui.QPixmap(':/Department.png'))
        return self._icon


class FileNameNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None):
        super(FileNameNode, self).__init__(name,
                                           parent=parent,
                                           editable=False,
                                           selectable=True,
                                           data=data)
        self.typeInfo = 'filename'

    def icon(self):
        if self._icon is None:
            self._icon = QtGui.QIcon(QtGui.QPixmap(':/FileName.png'))
        return self._icon


class FileModel(nodes.Model):
    def __init__(self, root, font=None):
        super(FileModel, self).__init__(root, font=font)
        self._rootNode = root
        self._column_names = {
            0: 'Name',
        }

    def columnCount(self, parent):
        return 1


class FileSelector(QtWidgets.QWidget, ui_fileSelector.Ui_Form):
    fileSelected = QtCore.Signal(str, str)

    def __init__(self, parent):
        super(FileSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        # Example data
        self.rootNode = nodes.Node('root')
        layoutDept = DeptNode('layout', parent=self.rootNode)
        cameraName = FileNameNode('camera', parent=layoutDept, data='layout/camera')
        envName = FileNameNode('environment', parent=layoutDept, data='layout/environment')
        layoutName = FileNameNode('layout', parent=layoutDept, data='layout/layout')
        animDept = DeptNode('animation', parent=self.rootNode)
        animationName = FileNameNode('animation', parent=animDept, data='animation/animation')
        lightDept = DeptNode('light', parent=self.rootNode)
        lightName = FileNameNode('light', parent=lightDept, data='light/light')

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
        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.selectionChanged.connect(self.selectionChangedFunc)

    def selectionChangedFunc(self, selected, deselected=None):
        for index in selected.indexes():
            if index.isValid():
                node = self.fileFilterModel.mapToSource(index).internalPointer()
                if node is not None:
                    dataSplit = node.data().split('/')
                    dept = dataSplit[0]
                    name = dataSplit[1]
                    self.fileSelected.emit('department', dept)
                    self.fileSelected.emit('name', name)
