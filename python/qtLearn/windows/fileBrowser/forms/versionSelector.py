"""

"""

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.nodes as nodes
import qtLearn.windows.fileBrowser.forms.ui_versionSelector as ui_versionSelector


class MajorVersionNode(nodes.Node):
    def __init__(self, version, data=None, parent=None):
        super(MajorVersionNode, self).__init__(version,
                                               parent=parent,
                                               selectable=False,
                                               editable=False,
                                               data=data)
        self._version = version
        self.typeInfo = 'majorversion'

    def icon(self):
        if self._icon is None:
            self._icon = QtGui.QIcon(QtGui.QPixmap(':/MajorVersion.png'))
        return self._icon

    def version(self):
        return self._version


class MinorVersionNode(nodes.Node):
    def __init__(self, version, user, desc, data=None, parent=None):
        super(MinorVersionNode, self).__init__(version,
                                               parent=parent,
                                               selectable=True,
                                               editable=False,
                                               data=data)
        self._version = version
        self._user = user
        self._desc = desc
        self.typeInfo = 'minorversion'

    def icon(self):
        if self._icon is None:
            self._icon = QtGui.QIcon(QtGui.QPixmap(':/MinorVersion.png'))
        return self._icon

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


def getVersions(path):
    versions = [
        ('v001.001', 'john', 'description'),
        ('v002.001', 'davidc', 'description'),
        ('v002.002', 'davidc', 'description'),
        ('v002.003', 'davidc', 'description'),
        ('v002.004', 'john', 'description'),
        ('v003.001', 'bob', 'description'),
    ]
    return versions


def convertVersionsToNodes(version_list):
    major_versions = {}
    minor_versions = {}
    rootNode = nodes.Node('root')
    for version in version_list:
        ver = version[0]
        major_ver = str(ver).split('.')[0]
        minor_ver = str(ver).split('.')[1]
        user = version[1]
        desc = version[2]

        # Create Major Version
        if major_ver in major_versions:
            majorNode = major_versions[major_ver]
        else:
            majorNode = MajorVersionNode(major_ver, parent=rootNode, data=major_ver)

        # Create Minor Version
        if ver in minor_versions:
            minorNode = minor_versions[major_ver]
        else:
            minorNode = MinorVersionNode(minor_ver, user, desc,
                                         parent=majorNode, data=ver)

        major_versions[major_ver] = majorNode
        minor_versions[ver] = minorNode
    return rootNode


class VersionModel(nodes.Model):
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
            elif isinstance(node, nodes.Node):
                name = node.name()

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
    versionSelected = QtCore.Signal(str, str)

    def __init__(self, parent):
        super(VersionSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')

        path = ''
        versions = getVersions(path)
        versionNodes = convertVersionsToNodes(versions)

        self.versionModel = VersionModel(versionNodes, font=self.font)
        self.versionFilterModel = QtCore.QSortFilterProxyModel()
        self.versionFilterModel.setSourceModel(self.versionModel)
        self.versionFilterModel.setDynamicSortFilter(True)
        self.versionFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.treeView.setModel(self.versionFilterModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(0, QtCore.Qt.DescendingOrder)
        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.selectionChanged.connect(self.selectionChangedFunc)

    def selectionChangedFunc(self, selected, deselected=None):
        for index in selected.indexes():
            if index.isValid():
                node = self.versionFilterModel.mapToSource(index).internalPointer()
                if node is not None:
                    dataSplit = node.data().split('.')
                    minor = dataSplit[1]
                    major = dataSplit[0]
                    self.versionSelected.emit('minor', minor)
                    self.versionSelected.emit('major', major)
