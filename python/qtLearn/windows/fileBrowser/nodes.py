"""
Defines a basic node class able to be used for tree data models.
"""

import sys

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets


class Node(object):
    def __init__(self, name,
                 data=None,
                 parent=None,
                 enabled=True,
                 editable=False,
                 selectable=True,
                 checkable=False,
                 neverHasChildren=False):
        self._name = name
        self._children = []
        self._parent = parent
        self._enabled = enabled
        self._checkable = checkable
        self._editable = editable
        self._selectable = selectable
        self._neverHasChildren = neverHasChildren
        self._data = data
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/Node.png'))
        self.typeInfo = 'node'
        if parent is not None:
            parent.addChild(self)

    def name(self):
        return self._name

    def setName(self, name):
        self._name = name

    def data(self):
        return self._data

    def setData(self, value):
        self._data = value

    def enabled(self):
        """Can the data be edited?"""
        return self._enabled

    def setEnabled(self, value):
        self._enabled = value

    def checkable(self):
        """Can the data be edited?"""
        return self._checkable

    def setCheckable(self, value):
        self._checkable = value

    def editable(self):
        """Can the data be edited?"""
        return self._editable

    def setEditable(self, value):
        self._editable = value

    def selectable(self):
        """Can the data be selected?"""
        return self._selectable

    def setSelectable(self, value):
        self._selectable = value

    def neverHasChildren(self):
        """Can the data be edited?"""
        return self._neverHasChildren

    def setNeverHasChildren(self, value):
        self._neverHasChildren = value

    def icon(self):
        return self._icon

    def addChild(self, child):
        self._children.append(child)

    def insertChild(self, position, child):
        if position < 0 or position > len(self._children):
            return False
        self._children.insert(position, child)
        child._parent = self
        return True

    def removeChild(self, position):
        if position < 0 or position > len(self._children):
            return False
        child = self._children.pop(position)
        child._parent = None
        return True

    def child(self, row):
        return self._children[row]

    def childCount(self):
        return len(self._children)

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)
        return


class ItemModel(QtCore.QAbstractItemModel):
    def __init__(self, rootNode, font=None):
        super(ItemModel, self).__init__()
        self._rootNode = None  # Node('root')
        self._column_names = {
            0: 'Column',
        }
        self._font = font

        self.setRootNode(rootNode)

    def rootNode(self):
        return self._rootNode

    def setRootNode(self, rootNode):
        # print('setRootNode:', rootNode.name(), repr(rootNode.data()))
        # sys.stdout.flush()

        super(ItemModel, self).beginResetModel()
        self._rootNode = rootNode
        super(ItemModel, self).endResetModel()

        topLeft = self.createIndex(0, 0)
        self.dataChanged.emit(topLeft, topLeft)

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
                return node.icon()

        if role == QtCore.Qt.FontRole:
            if self._font is not None:
                return self._font

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            node = index.internalPointer()
            if not node.editable():
                return False
            if role == QtCore.Qt.EditRole:
                node.setName(value)
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            return self._column_names.get(section, 'Column')

    def flags(self, index):
        v = QtCore.Qt.NoItemFlags
        node = index.internalPointer()
        if node.enabled():
            v = v | QtCore.Qt.ItemIsEnabled
        if node.checkable():
            v = v | QtCore.Qt.ItemIsUserCheckable
        if node.neverHasChildren():
            v = v | QtCore.Qt.ItemNeverHasChildren
        if node.selectable():
            v = v | QtCore.Qt.ItemIsSelectable
        if node.editable():
            v = v | QtCore.Qt.ItemIsEditable
        return v

    def parent(self, index):
        node = self.getNode(index)  # index.internalPointer()
        if node is None:
            return QtCore.QModelIndex()
        parentNode = node.parent()
        if parentNode == self._rootNode:
            return QtCore.QModelIndex()
        if parentNode is None:
            return QtCore.QModelIndex()
        row = parentNode.row()
        # print('node:', node.name(), node.data())
        # print('parentNode:', parentNode.name())
        # sys.stdout.flush()
        return self.createIndex(row, 0, parentNode)

    # def parent(self, index):
    #     if not index.isValid():
    #         return QtCore.QModelIndex()
    #     node = self.getNode(index)  # index.internalPointer()
    #     parentNode = node.parent()
    #     if parentNode is None:
    #         return QtCore.QModelIndex()
    #     else:
    #         row = parentNode.row()
    #         if row is None:
    #             return QtCore.QModelIndex()
    #
    #         print('node:', node.name(), node.data())
    #         print('parentNode:', parentNode.name())
    #         sys.stdout.flush()
    #
    #         return self.createIndex(row, 0, parentNode)

    def index(self, row, column, parent):
        parentNode = self.getNode(parent)
        childItem = parentNode.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QtCore.QModelIndex()

    # def index(self, row, column, parent):
    #     if not parent.isValid():
    #         return self.createIndex(row, column, self._rootNode)
    #     parentNode = parent.internalPointer()
    #     return self.createIndex(row, column, parentNode.child(row))

    def getNode(self, index):
        node = None
        if index.isValid():
            node = index.internalPointer()
            if node is not None:
                return node
        return self._rootNode

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        parentNode = self.getNode(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success = None
        for row in range(rows):
            childCount = parentNode.childCount()
            childNode = Node("untitled" + str(childCount))
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

    def reset(self):
        # self._rootNode = self._rootNode
        super(ItemModel, self).reset(self)

