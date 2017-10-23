"""

"""

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import \
    qtLearn.windows.fileBrowser.forms.ui_versionSelector as ui_versionSelector
import qtLearn.windows.fileBrowser.nodes as nodes


# reload(ui_versionSelector)


# class Node(object):
#     def __init__(self, name, parent=None):
#         self._name = name
#         self._children = []
#         self._parent = parent
#         self.typeInfo = 'node'
#         if parent is not None:
#             parent.addChild(self)
#
#     def addChild(self, child):
#         self._children.append(child)
#
#     def insertChild(self, position, child):
#         if position < 0 or position > len(self._children):
#             return False
#         self._children.insert(position, child)
#         child._parent = self
#         return True
#
#     def removeChild(self, position):
#         if position < 0 or position > len(self._children):
#             return False
#         child = self._children.pop(position)
#         child._parent = None
#         return True
#
#     def name(self):
#         return self._name
#
#     def setName(self, name):
#         self._name = name
#
#     def child(self, row):
#         return self._children[row]
#
#     def childCount(self):
#         return len(self._children)
#
#     def parent(self):
#         return self._parent
#
#     def row(self):
#         if self._parent is not None:
#             return self._parent._children.index(self)


class MajorVersionNode(nodes.Node):
    def __init__(self, version, parent=None):
        super(MajorVersionNode, self).__init__(version,
                                               parent=parent,
                                               selectable=False,
                                               editable=False)
        self._version = version
        self.typeInfo = 'majorversion'

    def version(self):
        return self._version


class MinorVersionNode(nodes.Node):
    def __init__(self, version, user, desc, parent=None):
        super(MinorVersionNode, self).__init__(version,
                                               parent=parent,
                                               selectable=True,
                                               editable=False)
        self._version = version
        self._user = user
        self._desc = desc
        self.typeInfo = 'minorversion'

    def version(self):
        return self._version

    def user(self):
        return self._user

    def description(self):
        return self._desc

    def full_version(self):
        major_node = self.parent.parent()
        minor_node = self
        ver = '{0}.{1}'
        ver = ver.format(major_node.version(),
                         minor_node.version())
        return ver


def getVersions():
    versions = [
        ('v001.001', 'john', 'description'),
        ('v002.001', 'davidc', 'description'),
        ('v002.002', 'davidc', 'description'),
        ('v002.003', 'davidc', 'description'),
        ('v002.004', 'john', 'description'),
        ('v003.001', 'bob', 'description'),
    ]

    major_versions = {}
    minor_versions = {}
    rootNode = nodes.Node('root')
    for version in versions:
        ver = version[0]
        major_ver = str(ver).split('.')[0]
        minor_ver = str(ver).split('.')[1]
        user = version[1]
        desc = version[2]

        # Create Major Version
        if major_ver in major_versions:
            majorNode = major_versions[major_ver]
        else:
            majorNode = MajorVersionNode(major_ver, parent=rootNode)

        # Create Minor Version
        if ver in minor_versions:
            minorNode = minor_versions[major_ver]
        else:
            minorNode = MinorVersionNode(minor_ver, user, desc,
                                         parent=majorNode)

        major_versions[major_ver] = majorNode
        minor_versions[ver] = minorNode
    return rootNode


class VersionModel(QtCore.QAbstractItemModel):
    def __init__(self, root_node):
        super(VersionModel, self).__init__()
        self._root_node = root_node
        self._column_names = {
            0: 'Version',
            1: 'User',
            2: 'Description',
        }
        self._type_icons = {
            'minorversion': QtGui.QIcon(QtGui.QPixmap(':/MinorVersion.png')),
            'majorversion': QtGui.QIcon(QtGui.QPixmap(':/MajorVersion.png')),
            'node': QtGui.QIcon(QtGui.QPixmap(':/Node.png')),
        }

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self._root_node
        else:
            parentNode = parent.internalPointer()
        return parentNode.childCount()

    def columnCount(self, parent):
        return 3

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        name = ''
        user = ''
        desc = ''

        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            column = index.column()
            if isinstance(node, MajorVersionNode):
                name = node.version()
            elif isinstance(node, MinorVersionNode):
                name = node.version()
                user = node.user()
                desc = node.description()
            elif isinstance(node, Node):
                name = node.name()

            if column == 0:
                return name
            elif column == 1:
                return user
            elif column == 2:
                return desc
            else:
                return ''

        if role == QtCore.Qt.DecorationRole:
            if index.column() == 0:
                return self._type_icons.get(node.typeInfo)
        return None

    def parent(self, index):
        node = index.internalPointer()
        parentNode = node.parent()
        if parentNode == self._root_node:
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
        return self._root_node

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            return self._column_names.get(section, 'Column')
        return None

    def flags(self, index):
        v = QtCore.Qt.ItemIsEnabled
        node = index.internalPointer()
        if node.selectable():
            v = v | QtCore.Qt.ItemIsSelectable
        if node.editable():
            v = v | QtCore.Qt.ItemIsEditable
        return v

        # def flags(self, index):
        #     node = index.internalPointer()
        #     if isinstance(node, MinorVersionNode):
        #         return QtCore.Qt.ItemIsEnabled | \
        #                QtCore.Qt.ItemIsSelectable | \
        #                QtCore.Qt.ItemIsEditable
        #     return QtCore.Qt.ItemIsEnabled


class VersionSelector(QtWidgets.QWidget, ui_versionSelector.Ui_Form):
    def __init__(self):
        super(VersionSelector, self).__init__()
        self.setupUi(self)

        versions = getVersions()
        model = VersionModel(versions)
        self.treeView.setModel(model)
