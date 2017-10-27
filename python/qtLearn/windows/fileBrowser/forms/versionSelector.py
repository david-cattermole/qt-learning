"""
Allows users to pick a specific version of a file / asset.
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
                 icon=None,
                 enabled=True,
                 editable=False,
                 selectable=True,
                 checkable=False,
                 neverHasChildren=False):
        if icon is None:
            icon = QtGui.QIcon(QtGui.QPixmap(':/Version.png'))
        super(VersionNode, self).__init__(name,
                                          data=data,
                                          parent=parent,
                                          icon=icon,
                                          enabled=enabled,
                                          selectable=selectable,
                                          editable=editable,
                                          checkable=checkable,
                                          neverHasChildren=neverHasChildren)
        self.typeInfo = 'version'


class MajorVersionNode(VersionNode):
    def __init__(self, name, data=None, parent=None):
        icon = QtGui.QIcon(QtGui.QPixmap(':/MajorVersion.png'))
        super(MajorVersionNode, self).__init__(name,
                                               data=data,
                                               parent=parent,
                                               icon=icon,
                                               selectable=False,
                                               editable=False)
        self.typeInfo = 'majorversion'


class MinorVersionNode(VersionNode):
    def __init__(self, name, user, desc, data=None, parent=None):
        icon = QtGui.QIcon(QtGui.QPixmap(':/MinorVersion.png'))
        super(MinorVersionNode, self).__init__(name,
                                               data=data,
                                               parent=parent,
                                               icon=icon,
                                               selectable=True,
                                               editable=False)
        self._user = user
        self._desc = desc
        self.typeInfo = 'minorversion'

    def user(self):
        return self._user

    def description(self):
        return self._desc


def getVersions(path):
    versions_1 = [
        ('v001.001', 'john', 'description', 'mb'),
        ('v002.001', 'davidc', 'description', 'mb'),
        ('v002.002', 'davidc', 'description', 'mb'),
        ('v002.003', 'davidc', 'description', 'mb'),
        ('v002.004', 'john', 'description', 'mb'),
        ('v003.001', 'bob', 'description', 'mb'),
    ]
    versions_2 = [
        ('v001.001', 'davidc', 'description', 'mb'),
    ]
    versions_3 = [
        ('v001.001', 'davidc', 'description', 'mb'),
        ('v002.001', 'davidc', 'description', 'mb'),
        ('v003.001', 'davidc', 'description', 'mb'),
        ('v004.001', 'davidc', 'description', 'mb'),
        ('v005.001', 'davidc', 'description', 'mb'),
        ('v006.001', 'davidc', 'description', 'mb'),
        ('v007.001', 'davidc', 'description', 'mb'),
        ('v008.001', 'davidc', 'description', 'mb'),
        ('v009.001', 'davidc', 'description', 'mb'),
        ('v010.001', 'davidc', 'description', 'mb'),
        ('v011.001', 'davidc', 'description', 'mb'),
        ('v012.001', 'john', 'description', 'mb'),
    ]
    versions_4 = [
        ('v001.001', 'bob', 'description', 'mb'),
        ('v001.002', 'bob', 'description', 'mb'),
        ('v001.003', 'bob', 'description', 'mb'),
        ('v001.004', 'bob', 'description', 'mb'),
        ('v001.005', 'bob', 'description', 'mb'),
        ('v001.006', 'bob', 'description', 'mb'),
        ('v001.007', 'bob', 'description', 'mb'),
        ('v001.008', 'bob', 'description', 'mb'),
        ('v001.009', 'bob', 'description', 'mb'),
        ('v001.010', 'bob', 'description', 'mb'),
        ('v002.001', 'davidc', 'description', 'mb'),
        ('v002.002', 'davidc', 'description', 'mb'),
        ('v002.003', 'davidc', 'description', 'mb'),
        ('v002.004', 'davidc', 'description', 'mb'),
        ('v002.005', 'davidc', 'description', 'mb'),
        ('v002.006', 'davidc', 'description', 'mb'),
        ('v002.007', 'davidc', 'description', 'mb'),
        ('v002.008', 'davidc', 'description', 'mb'),
        ('v002.009', 'davidc', 'description', 'mb'),
        ('v002.010', 'davidc', 'description', 'mb'),
        ('v002.011', 'davidc', 'description', 'mb'),
        ('v002.012', 'davidc', 'description', 'mb'),
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
        file_ext = version[3]
        data = {
            'major': major_ver,
            'minor': minor_ver,
            'version': ver,
            'user': user,
            'description': desc,
            'ext': file_ext,
        }

        # Create Major Version
        if major_ver in major_versions:
            majorNode = major_versions[major_ver]
        else:
            majorNode = MajorVersionNode(major_ver,
                                         parent=rootNode,
                                         data=data)  # major_ver

        # Create Minor Version
        if ver in minor_versions:
            minorNode = minor_versions[major_ver]
        else:
            minorNode = MinorVersionNode(minor_ver, user, desc,
                                         parent=majorNode,
                                         data=data)  # ver

        major_versions[major_ver] = majorNode
        minor_versions[ver] = minorNode
    return rootNode


class VersionModel(nodes.ItemModel):
    def __init__(self, root, font=None):
        super(VersionModel, self).__init__(root, font=font)
        self._column_names = {
            0: 'Version',
            1: 'User',
            2: 'Description',
        }
        self._node_attr_key = {
            'Version': 'name',
            'User': 'user',
            'Description': 'description',
        }


class SortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super(SortFilterProxyModel, self).__init__()
        self._user = ''

    def user(self):
        return self._user

    def setUser(self, value):
        self._user = value
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        result = False
        srcModel = self.sourceModel()
        column = self.filterKeyColumn()
        if column < 0:
            column = 0
        index = srcModel.index(sourceRow, column, sourceParent)
        node = index.internalPointer()
        filterUser = self.user()
        nodeUser = node.data().get('user')
        if filterUser is None or len(filterUser) == 0:
            result = True
        elif nodeUser == filterUser:
            result = True
        return result


class VersionSelector(QtWidgets.QWidget, ui_versionSelector.Ui_Form):
    setTag = QtCore.Signal(str, str)

    def __init__(self, parent,
                 withTypeFilter=False,
                 withFileFormatFilter=True):
        super(VersionSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')
        self._path = ''

        # Hide unneeded UI elements.
        if withTypeFilter is False:
            self.typeLabel.hide()
            self.typeComboBox.hide()
        if withFileFormatFilter is False:
            self.fileFormatLabel.hide()
            self.fileFormatComboBox.hide()

        rootNode = nodes.Node('root', data=self._path)
        self.versionModel = VersionModel(rootNode, font=self.font)

        self.versionFilterModel = SortFilterProxyModel()
        self.versionFilterModel.setSourceModel(self.versionModel)
        self.versionFilterModel.setDynamicSortFilter(True)
        self.versionFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)

        self.treeView.setModel(self.versionFilterModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(0, QtCore.Qt.DescendingOrder)
        self.treeView.expandAll()

        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.currentChanged.connect(self.currentChangedFunc)

    def getFileFormats(self):
        return [
            ('.ma', 'Maya ASCII (*.ma)'),
            ('.mb', 'Maya Binary (*.mb)')
        ]

    @QtCore.Slot(str)
    def userChanged(self, value):
        self.versionFilterModel.setUser(value)
        self.treeView.expandAll()

    @QtCore.Slot(str)
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
        if 'minor' in data:
            self.setTag.emit('minor', data['minor'])
        if 'major' in data:
            self.setTag.emit('major', data['major'])
        if 'ext' in data:
            self.setTag.emit('ext', data['ext'])

