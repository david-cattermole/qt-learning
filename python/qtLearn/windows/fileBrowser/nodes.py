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
                 toolTip=None,
                 statusTip=None,
                 parent=None,
                 icon=None,
                 enabled=True,
                 editable=False,
                 selectable=True,
                 checkable=False,
                 neverHasChildren=False):
        if icon is None:
            icon = QtGui.QIcon(QtGui.QPixmap(':/Node.png'))
        self._children = []
        self._parent = parent

        self._name = name
        self._toolTip = toolTip
        self._statusTip = statusTip
        self._data = data

        self._enabled = enabled
        self._checkable = checkable
        self._editable = editable
        self._selectable = selectable
        self._neverHasChildren = neverHasChildren

        self._icon = icon
        self.typeInfo = 'node'
        if parent is not None:
            parent.addChild(self)

    def name(self):
        return self._name

    def setName(self, name):
        self._name = name
        
    def toolTip(self):
        return self._toolTip

    def setToolTip(self, toolTip):
        self._toolTip = toolTip

    def statusTip(self):
        return self._statusTip

    def setStatusTip(self, statusTip):
        self._statusTip = statusTip

    def data(self):
        return self._data

    def setData(self, value):
        self._data = value

    def enabled(self):
        """Can the data be enabled?"""
        return self._enabled

    def setEnabled(self, value):
        self._enabled = value

    def checkable(self):
        """Can the data be checked?"""
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
        """Optimisation, only turn this to True if this is surely the last child"""
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

    def childTags(self):
        # TODO: Clean up this function and make a more efficient way of
        # generating these tags.
        result = ''
        for i in range(self.childCount()):
            node = self.child(i)
            if node.childCount() == 0:
                result += '|' + node.name()
            else:
                result += '|' + node.childTags()
        return result

    def allTags(self):
        # TODO: Clean up this function and make a more efficient way of
        # generating these tags.
        result = self.name()
        result += self.childTags()

        node = self.parent()
        while node:
            node = node.parent()
            # Allows us to skip the root node.
            if node is not None:
                result += '|' + node.name()
        return result

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)
        return


class ItemModel(QtCore.QAbstractItemModel):
    def __init__(self, rootNode, font=None):
        super(ItemModel, self).__init__()
        self._rootNode = None
        self._column_names = {
            0: 'Column',
        }
        self._node_attr_key = {
            'Column': 'name',
        }

        self._font = font

        self.setRootNode(rootNode)

    def rootNode(self):
        return self._rootNode

    def setRootNode(self, rootNode):
        super(ItemModel, self).beginResetModel()
        self._rootNode = rootNode
        super(ItemModel, self).endResetModel()

        topLeft = self.createIndex(0, 0)
        self.dataChanged.emit(topLeft, topLeft)

    def columnCount(self, parent):
        return len(self._column_names.keys())

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.childCount()

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            column_index = index.column()
            if column_index not in self._column_names:
                msg = '{0} was not in {1}'.format(column_index, self._column_names)
                raise ValueError(msg)
            column_name = self._column_names[column_index]
            if column_name not in self._node_attr_key:
                msg = '{0} was not in {1}'.format(column_name, self._node_attr_key)
                raise ValueError(msg)
            attr_name = self._node_attr_key[column_name]
            value = getattr(node, attr_name, None)
            if value is not None:
                value = value()
            # print('node getattr', node.name(), attr_name, value)
            # sys.stdout.flush()
            return value

        if role == QtCore.Qt.DecorationRole:
            # TODO: Can we refactor this similar to the DisplayRole above?
            if index.column() == 0:
                return node.icon()

        if role == QtCore.Qt.ToolTipRole:
            return node.toolTip()

        if role == QtCore.Qt.StatusTipRole:
            return node.statusTip()

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
        return self.createIndex(row, 0, parentNode)

    def index(self, row, column, parent):
        parentNode = self.getNode(parent)
        childItem = parentNode.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QtCore.QModelIndex()

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

