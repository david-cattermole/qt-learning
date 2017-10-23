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

import qtLearn.windows.fileBrowser.forms.ui_fileSelector as ui_fileSelector
import qtLearn.windows.fileBrowser.nodes as nodes


# reload(ui_fileSelector)


class DeptNode(nodes.Node):
    def __init__(self, name,
                 parent=None):
        super(DeptNode, self).__init__(name,
                                       parent=parent,
                                       editable=False,
                                       selectable=False)
        self.typeInfo = 'department'


class FileNameNode(nodes.Node):
    def __init__(self, name,
                 parent=None):
        super(FileNameNode, self).__init__(name,
                                           parent=parent,
                                           editable=False,
                                           selectable=True)
        self.typeInfo = 'filename'


class FileModel(QtCore.QAbstractItemModel):
    def __init__(self, root, parent=None):
        super(FileModel, self).__init__(parent)
        self._rootNode = root
        self._column_names = {
            0: 'Name',
        }
        self._type_icons = {
            'department': QtGui.QIcon(QtGui.QPixmap(':/Department.png')),
            'filename': QtGui.QIcon(QtGui.QPixmap(':/FileName.png')),
            'node': QtGui.QIcon(QtGui.QPixmap(':/Node.png')),
        }

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.childCount()

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            if index.column() == 0:
                return node.name()

        if role == QtCore.Qt.DecorationRole:
            if index.column() == 0:
                self._type_icons.get(node.typeInfo, None)

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            node = index.internalPointer()
            if not node.editable():
                return False
            if role == QtCore.Qt.EditRole:
                node.setName(value)
                return True
        return False

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            return self._column_names.get(section, 'Column')

    def flags(self, index):
        v = QtCore.Qt.ItemIsEnabled
        node = index.internalPointer()
        if node.selectable():
            v = v | QtCore.Qt.ItemIsSelectable
        if node.editable():
            v = v | QtCore.Qt.ItemIsEditable
        return v

    def parent(self, index):
        node = index.internalPointer()
        parentNode = node.parent()
        if parentNode == self._rootNode:
            return QtCore.QModelIndex()
        return self.createIndex(parentNode.row(), 0, parentNode)

    def index(self, row, column, parent):
        parentNode = self.getNode(parent)
        childItem = parentNode.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def getNode(self, index):
        if index.isValid():
            node = index.internalPointer()
            if node:
                return node
        return self._rootNode

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        parentNode = self.getNode(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success = None
        for row in range(rows):
            childCount = parentNode.childCount()
            childNode = nodes.Node("untitled" + str(childCount))
            success = parentNode.insertChild(position, childNode)
        self.endInsertRows()
        return success

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        parentNode = self.getNode(parent)
        self.beginRemoveRows(parent, position, position + rows - 1)
        success = None
        for row in range(rows):
            success = parentNode.removeChild(position)
        self.endRemoveRows()
        return success


class FileSelector(QtWidgets.QWidget, ui_fileSelector.Ui_Form):
    def __init__(self):
        super(FileSelector, self).__init__()
        self.setupUi(self)

        # Example data
        rootNode = nodes.Node('root')
        layoutDept = DeptNode('layout', rootNode)
        cameraName = FileNameNode('camera', layoutDept)
        envName = FileNameNode('environment', layoutDept)
        layoutName = FileNameNode('layout', layoutDept)
        animDept = DeptNode('animation', rootNode)
        animationName = FileNameNode('animation', animDept)
        lightDept = DeptNode('light', rootNode)
        lightName = FileNameNode('light', lightDept)

        # Setup data, filter/sorting model.
        self.fileModel = FileModel(rootNode)
        self.fileFilterModel = QtCore.QSortFilterProxyModel()
        self.fileFilterModel.setSourceModel(self.fileModel)
        self.fileFilterModel.setDynamicSortFilter(True)
        self.fileFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.treeView.setModel(self.fileFilterModel)
        self.treeView.setSortingEnabled(True)
        self.searchLineEdit.textChanged.connect(self.fileFilterModel.setFilterRegExp)
