"""
Allows users to pick a specific version of a file / asset.
"""

import random

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiModels
import qtLearn.nodes as nodes
import qtLearn.paths as paths
import qtLearn.uiUtils as uiUtils
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
            icon = ':/Version.png'
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
        icon = ':/MajorVersion.png'
        super(MajorVersionNode, self).__init__(name,
                                               data=data,
                                               parent=parent,
                                               icon=icon,
                                               selectable=False,
                                               editable=False)
        self.typeInfo = 'majorversion'


class MinorVersionNode(VersionNode):
    def __init__(self, name, user, desc, data=None, parent=None):
        icon = ':/MinorVersion.png'
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

    def fileFormat(self):
        return self._data['ext']


class VersionModel(qtLearn.uiModels.ItemModel):
    def __init__(self, root, font=None):
        super(VersionModel, self).__init__(root, font=font)
        self._column_names = {
            0: 'Version',
            # 1: 'Format',
            1: 'User',
            2: 'Description',
        }
        self._node_attr_key = {
            'Version': 'name',
            # 'Format': 'fileFormat',
            'User': 'user',
            'Description': 'description',
        }


class VersionSelector(QtWidgets.QWidget, ui_versionSelector.Ui_Form):
    signalSetTagStart = QtCore.Signal()
    signalSetTag = QtCore.Signal(str, str)
    signalSetTagEnd = QtCore.Signal()

    def __init__(self, parent,
                 withFileFormatFilter=True,
                 fileFormatFilterTagName=None,
                 fileFormatFilterNodeType=None,
                 pathFormat=None):
        super(VersionSelector, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.font = uiUtils.getFont('monospace')
        self._data = {}
        self._path = ''
        self.__internalRemap = {}

        self._pathFormat = pathFormat
        if pathFormat is None:
            self._pathFormat = '/projects/{project}/{sequence}/{shot}/{department}/{task}/{name}_{major}.{minor}.{ext}'

        # File Format Filter
        self.fileFormatModel = None
        self._fileFormatFilterTagName = None
        self._fileFormatFilterNodeType = None
        if withFileFormatFilter is True:
            filterData = self.__getFileFormatNames()
            self.fileFormatModel = QtCore.QStringListModel(filterData)
            self.fileFormatComboBox.setModel(self.fileFormatModel)
            if fileFormatFilterTagName is not None:
                if isinstance(fileFormatFilterTagName, str):
                    self._fileFormatFilterTagName = fileFormatFilterTagName
                else:
                    raise ValueError
            if fileFormatFilterNodeType is not None:
                if isinstance(fileFormatFilterNodeType, str):
                    self._fileFormatFilterNodeType = fileFormatFilterNodeType
                else:
                    raise ValueError
        else:
            self.fileFormatLabel.hide()
            self.fileFormatComboBox.hide()

        rootNode = nodes.Node('root', data=self._path)
        self.versionModel = VersionModel(rootNode, font=self.font)

        self.versionFilterModel = qtLearn.uiModels.SortFilterProxyModel()
        self.versionFilterModel.setSourceModel(self.versionModel)
        self.versionFilterModel.setDynamicSortFilter(True)
        self.versionFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.versionFilterModel.setFilterTagName(self._fileFormatFilterTagName)
        self.versionFilterModel.setFilterTagNodeType(self._fileFormatFilterNodeType)

        self.treeView.setModel(self.versionFilterModel)
        self.treeView.setSortingEnabled(True)
        self.treeView.sortByColumn(0, QtCore.Qt.DescendingOrder)
        self.treeView.expandAll()

        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.currentChanged.connect(self.slotCurrentChanged)

        self.fileFormatComboBox.currentIndexChanged.connect(self.slotFileFormatFilterChanged)
        # self.fileFormatComboBox.currentIndexChanged.connect(self.slotSetFilterTagValue)

    ############################################################################

    def __getFileFormatNames(self):
        data = self.getFileFormatsData()
        names = map(lambda x: x[1], data)
        # names = list(names)
        # print('getFileFormatNames:', names)
        return names

    def __getFileFormatExtensions(self):
        data = self.getFileFormatsData()
        exts = map(lambda x: x[0], data)
        # exts = list(exts)
        # print('getFileFormatExtensions:', exts)
        return exts

    def data(self):
        if self._data is None:
            return {}
        return self._data.copy()

    def setData(self, value):
        self._data = value

    def getDataValue(self, key, default=None):
        return self._data.get(key, default)

    def setDataValue(self, key, value):
        self._data[key] = value

    def getFileFormatFilterTagName(self):
        return self._fileFormatFilterTagName

    def getFileFormatFilterTagNodeType(self):
        return self._fileFormatFilterNodeType

    ############################################################################

    def getFileFormatsData(self):
        return [
            # (None, '<all file formats>'),
            # ('.ma', 'Maya ASCII (*.ma)'),
            # ('.mb', 'Maya Binary (*.mb)')
            (None, '<all file formats>'),
            ('.ma', 'ma'),
            ('.mb', 'mb')
        ]

    def getVersionNodes(self):
        # TODO: Use 'path' to look up versions rather than hard-coding test data.
        tags = self.data()
        pth = paths.Path(tags, format=self._pathFormat)
        path = pth.getPath()
        # print('VersionSelector getVersionNodes path:', path)
        rootNode = self.__internalRemap.get(path)
        if rootNode is not None:
            return rootNode

        exts = ['mb', 'ma']

        versions_1 = [
            ('v001.001', 'john', 'description', random.choice(exts)),
            ('v002.001', 'davidc', 'description', random.choice(exts)),
            ('v002.002', 'davidc', 'description', random.choice(exts)),
            ('v002.003', 'davidc', 'description', random.choice(exts)),
            ('v002.004', 'john', 'description', random.choice(exts)),
            ('v003.001', 'bob', 'description', random.choice(exts)),
        ]
        versions_2 = [
            ('v001.001', 'davidc', 'description', random.choice(exts)),
        ]
        versions_3 = [
            ('v001.001', 'davidc', 'description', random.choice(exts)),
            ('v002.001', 'davidc', 'description', random.choice(exts)),
            ('v003.001', 'davidc', 'description', random.choice(exts)),
            ('v004.001', 'davidc', 'description', random.choice(exts)),
            ('v005.001', 'davidc', 'description', random.choice(exts)),
            ('v006.001', 'davidc', 'description', random.choice(exts)),
            ('v007.001', 'davidc', 'description', random.choice(exts)),
            ('v008.001', 'davidc', 'description', random.choice(exts)),
            ('v009.001', 'davidc', 'description', random.choice(exts)),
            ('v010.001', 'davidc', 'description', random.choice(exts)),
            ('v011.001', 'davidc', 'description', random.choice(exts)),
            ('v012.001', 'john', 'description', random.choice(exts)),
        ]
        versions_4 = [
            ('v001.001', 'bob', 'description', random.choice(exts)),
            ('v001.002', 'bob', 'description', random.choice(exts)),
            ('v001.003', 'bob', 'description', random.choice(exts)),
            ('v001.004', 'bob', 'description', random.choice(exts)),
            ('v001.005', 'bob', 'description', random.choice(exts)),
            ('v001.006', 'bob', 'description', random.choice(exts)),
            ('v001.007', 'bob', 'description', random.choice(exts)),
            ('v001.008', 'bob', 'description', random.choice(exts)),
            ('v001.009', 'bob', 'description', random.choice(exts)),
            ('v001.010', 'bob', 'description', random.choice(exts)),
            ('v002.001', 'davidc', 'description', random.choice(exts)),
            ('v002.002', 'davidc', 'description', random.choice(exts)),
            ('v002.003', 'davidc', 'description', random.choice(exts)),
            ('v002.004', 'davidc', 'description', random.choice(exts)),
            ('v002.005', 'davidc', 'description', random.choice(exts)),
            ('v002.006', 'davidc', 'description', random.choice(exts)),
            ('v002.007', 'davidc', 'description', random.choice(exts)),
            ('v002.008', 'davidc', 'description', random.choice(exts)),
            ('v002.009', 'davidc', 'description', random.choice(exts)),
            ('v002.010', 'davidc', 'description', random.choice(exts)),
            ('v002.011', 'davidc', 'description', random.choice(exts)),
            ('v002.012', 'davidc', 'description', random.choice(exts)),
        ]
        versions = [versions_1, versions_2, versions_3, versions_4]
        versions = random.choice(versions)

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
                                             data=data)

            # Create Minor Version
            if ver in minor_versions:
                minorNode = minor_versions[major_ver]
            else:
                minorNode = MinorVersionNode(minor_ver, user, desc,
                                             parent=majorNode,
                                             data=data)

            major_versions[major_ver] = majorNode
            minor_versions[ver] = minorNode

        self.__internalRemap[path] = rootNode
        return rootNode

    ############################################################################

    @QtCore.Slot(int)
    def slotFileFormatFilterChanged(self, index):
        text = self.fileFormatComboBox.currentText()
        text = text.lower()
        if not text.isalpha():
            text = None
        # print('VersionSelector slotFileFormatFilterChanged', text)
        self.versionFilterModel.setFilterTagValue(text)
        self.treeView.expandAll()

    @QtCore.Slot(str)
    def slotSetUserFilterValue(self, value):
        # print('VersionSelector slotSetFilterTagValue', value)
        self.versionFilterModel.setFilterTagValue(value)
        self.treeView.expandAll()

    @QtCore.Slot(dict)
    def slotSetPathData(self, tags):
        # print('VersionSelector slotSetPathData tags:', tags)
        if not isinstance(tags, dict):
            return
        allowedTagKeys = [
            'project', 'sequence', 'shot',
            'name', 'task', 'department'
        ]
        for key in tags.keys():
            if key in allowedTagKeys:
                self._data[key] = tags.get(key)
            else:
                if key in self._data:
                    self._data.pop(key)
        # print('VersionSelector slotSetPathData changed:', self._data)
        rootNode = self.getVersionNodes()
        self.versionModel.setRootNode(rootNode)
        self.treeView.expandAll()
        return

    @QtCore.Slot(QtCore.QModelIndex, QtCore.QModelIndex)
    def slotCurrentChanged(self, index, prevIndex):
        # print('VersionSelector currentChanged START')

        if not index.isValid():
            return
        index_map = self.versionFilterModel.mapToSource(index)
        node = index_map.internalPointer()
        if node is None:
            return
        nodeData = node.data()
        if nodeData is None:
            return

        # Emit tag signals
        self.signalSetTagStart.emit()
        # print('VersionSelector currentChanged keys', nodeData.keys())
        for key in nodeData.keys():
            value = nodeData.get(key)
            # print('VersionSelector currentChanged value', key, newValue)
            self.setDataValue(key, nodeData[key])
            self.signalSetTag.emit(key, value)
        self.signalSetTagEnd.emit()

        # print('VersionSelector currentChanged END', repr(nodeData))
        return
