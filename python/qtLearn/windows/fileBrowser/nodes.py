"""
Defines a basic node class able to be used for tree data models.
"""

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets


class Node(object):
    def __init__(self, name, parent=None,
                 data=None,
                 editable=False,
                 selectable=True):
        self._name = name
        self._children = []
        self._parent = parent
        self._editable = editable
        self._selectable = selectable
        self._data = data
        self._icon = None
        self.typeInfo = 'node'
        if parent is not None:
            parent.addChild(self)

    def icon(self):
        if self._icon is None:
            self._icon = QtGui.QIcon(QtGui.QPixmap(':/Node.png'))
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

    def name(self):
        return self._name

    def setName(self, name):
        self._name = name

    def data(self):
        return self._data

    def setData(self, value):
        self._data = value

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

    def child(self, row):
        return self._children[row]

    def childCount(self):
        return len(self._children)

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)


class Model(QtCore.QAbstractItemModel):
    def __init__(self, rootNode, font=None):
        super(Model, self).__init__()
        self._rootNode = rootNode
        self._column_names = {
            0: 'Column',
        }
        self._font = font

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
