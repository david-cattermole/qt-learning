"""

"""

import random

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.nodes as nodes
import qtLearn.windows.fileBrowser.forms.ui_versionSelector as ui_versionSelector


class VersionNode(nodes.Node):
    def __init__(self, name,
                 parent=None,
                 data=None,
                 enabled=True,
                 editable=False,
                 selectable=True,
                 checkable=False,
                 neverHasChildren=False):
        super(VersionNode, self).__init__(name,
                                          data=data,
                                          parent=parent,
                                          enabled=enabled,
                                          selectable=selectable,
                                          editable=editable,
                                          checkable=checkable,
                                          neverHasChildren=neverHasChildren)
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/Version.png'))
        self.typeInfo = 'version'


class MajorVersionNode(VersionNode):
    def __init__(self, name, data=None, parent=None):
        super(MajorVersionNode, self).__init__(name,
                                               data=data,
                                               parent=parent,
                                               selectable=False,
                                               editable=False)
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/MajorVersion.png'))
        self.typeInfo = 'majorversion'


class MinorVersionNode(VersionNode):
    def __init__(self, name, user, desc, data=None, parent=None):
        super(MinorVersionNode, self).__init__(name,
                                               data=data,
                                               parent=parent,
                                               selectable=True,
                                               editable=False)
        self._user = user
        self._desc = desc
        self._icon = QtGui.QIcon(QtGui.QPixmap(':/MinorVersion.png'))
        self.typeInfo = 'minorversion'

    def user(self):
        return self._user

    def description(self):
        return self._desc


def getVersions(path):
    versions_1 = [
        ('v001.001', 'john', 'description'),
        ('v002.001', 'davidc', 'description'),
        ('v002.002', 'davidc', 'description'),
        ('v002.003', 'davidc', 'description'),
        ('v002.004', 'john', 'description'),
        ('v003.001', 'bob', 'description'),
    ]
    versions_2 = [
        ('v001.001', 'davidc', 'description'),
    ]
    versions_3 = [
        ('v001.001', 'davidc', 'description'),
        ('v002.001', 'davidc', 'description'),
        ('v003.001', 'davidc', 'description'),
        ('v004.001', 'davidc', 'description'),
        ('v005.001', 'davidc', 'description'),
        ('v006.001', 'davidc', 'description'),
        ('v007.001', 'davidc', 'description'),
        ('v008.001', 'davidc', 'description'),
        ('v009.001', 'davidc', 'description'),
        ('v010.001', 'davidc', 'description'),
        ('v011.001', 'davidc', 'description'),
        ('v012.001', 'davidc', 'description'),
    ]
    versions_4 = [
        ('v001.001', 'bob', 'description'),
        ('v001.002', 'bob', 'description'),
        ('v001.003', 'bob', 'description'),
        ('v001.004', 'bob', 'description'),
        ('v001.005', 'bob', 'description'),
        ('v001.006', 'bob', 'description'),
        ('v001.007', 'bob', 'description'),
        ('v001.008', 'bob', 'description'),
        ('v001.009', 'bob', 'description'),
        ('v001.010', 'bob', 'description'),
        ('v002.001', 'bob', 'description'),
    ]
    versions = [versions_1, versions_2, versions_3, versions_4]
    version = random.choice(versions)
    return version


def getVersionNodes(path):
    versions = getVersions(path)

    major_versions = {}
    minor_versions = {}
    rootNode = nodes.Node('ROOT')
    for version in versions:
        ver = version[0]
        split = str(ver).split('.')
        major_ver = split[0]
        minor_ver = split[1]
        user = version[1]
        desc = version[2]

        # Create Major Version
        if major_ver in major_versions:
            majorNode = major_versions[major_ver]
        else:
            majorNode = MajorVersionNode(major_ver,
                                         parent=rootNode,
                                         data=major_ver)

        # Create Minor Version
        if ver in minor_versions:
            minorNode = minor_versions[major_ver]
        else:
            minorNode = MinorVersionNode(minor_ver, user, desc,
                                         parent=majorNode,
                                         data=ver)

        major_versions[major_ver] = majorNode
        minor_versions[ver] = minorNode
    return rootNode


class VersionModel(nodes.ItemModel):
    def __init__(self, root, font=None):
        super(VersionModel, self).__init__(root, font=font)
        self._root_node = root
        self._column_names = {
            0: 'Version',
            1: 'User',
            2: 'Description',
        }

    def columnCount(self, parent):
        return 3

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            column = index.column()
            name = node.name()
            user = ''
            desc = ''
            if isinstance(node, MinorVersionNode):
                user = node.user()
                desc = node.description()

            if column == 0:
                return name
            elif column == 1:
                return user
            elif column == 2:
                return desc

        if role == QtCore.Qt.DecorationRole:
            if index.column() == 0:
                return node.icon()
        return None


class VersionSelector(QtWidgets.QWidget, ui_versionSelector.Ui_Form):
    setTag = QtCore.Signal(str, str)

    def __init__(self, parent):
        super(VersionSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        self._path = ''
        rootNode = nodes.Node('root', data=self._path)

        # Setup data, filter/sorting model.
        self.versionModel = VersionModel(rootNode, font=self.font)
        self.versionFilterModel = QtCore.QSortFilterProxyModel()
        self.versionFilterModel.setSourceModel(self.versionModel)
        self.versionFilterModel.setDynamicSortFilter(True)
        self.versionFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.treeView.setModel(self.versionFilterModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(0, QtCore.Qt.DescendingOrder)
        self.treeView.expandAll()

        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.currentChanged.connect(self.currentChangedFunc)

    def setPath(self, path):
        self._path = path
        rootNode = getVersionNodes(self._path)
        self.versionModel.setRootNode(rootNode)
        self.treeView.expandAll()

    def currentChangedFunc(self, index, prevIndex):
        if not index.isValid():
            return
        index_map = self.versionFilterModel.mapToSource(index)
        node = index_map.internalPointer()
        if node is None:
            return
        data = node.data()
        if data is None:
            return
        dataSplit = data.split('.')
        if len(dataSplit) == 2:
            minor = dataSplit[1]
            major = dataSplit[0]
            self.setTag.emit('minor', minor)
            self.setTag.emit('major', major)

