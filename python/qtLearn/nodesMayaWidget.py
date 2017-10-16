"""

Usage:
>>> import qtLearn.nodesMayaWidget
>>> reload(qtLearn.nodesMayaWidget)
>>> widget = qtLearn.nodesMayaWidget.NodesMayaWidget()
"""

import Qt
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.widgets.ui_nodesList
reload(qtLearn.widgets.ui_nodesList)


class NodeListViewModel(QtCore.QAbstractListModel):
    def __init__(self, nodeUUIDs=None, *args, **kwargs):
        super(NodeListViewModel, self).__init__(*args, **kwargs)
        if nodeUUIDs is None:
            nodeUUIDs = []
        self.__nodeUUIDs = nodeUUIDs
        self.setNodeUUIDs(nodeUUIDs)

    def getNodeUUIDs(self):
        nodes = self.__nodeUUIDs
        print 'getNodeUUIDs:', nodes
        return nodes

    def setNodeUUIDs(self, value):
        print 'setNodeUUIDs:', value
        self.__nodeUUIDs = value
        # self.modelReset()

    def rowCount(self, parent):
        # return len(self.__nodeUUIDs)
        nodes = self.getNodeUUIDs()
        # return len(nodes)
        print 'rowCount', len(nodes), nodes
        return len(nodes)

    def data(self, index, role):
        result = None
        # Qt.DecorationRole
        # Qt.ToolTipRole
        if role == Qt.DisplayRole:
            row = index.row()
            nodes = self.getNodeUUIDs()
            node = nodes[row]
            # node = self.__nodeUUIDs[row]
            import maya.cmds
            result = maya.cmds.ls(node, long=True) or []
            result = str(result[0])
            print 'result', row, result
            return result

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return 'Palette'
            else:
                return 'Color'
        pass


class NodesMayaWidget(QtWidgets.QWidget, qtLearn.widgets.ui_nodesList.Ui_Widget):
    def __init__(self, *args, **kwargs):
        super(NodesMayaWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.listViewModel = NodeListViewModel()
        # self.listView.setModel(self.listViewModel)
        self.getSelectionButton.clicked.connect(self.getNodes)
        self.clearButton.clicked.connect(self.clearView)

    def getNodes(self):
        import maya.cmds
        print 'getNodes'
        nodes = maya.cmds.ls(sl=True, uuid=True) or []
        sep = ', '
        text = '['
        for node in nodes:
            print 'getNodes node:', node
            value = maya.cmds.ls(node, long=True) or []
            text += str(value[0]) + sep
        text = text.rpartition(sep)[0] + ']'
        # self.listViewModel.setNodeUUIDs(nodes)
        print 'getNodes nodes:', self.listViewModel.getNodeUUIDs()
        # self.listViewModel.emit()
        # startIndex = QModelIndex()
        # self.listViewModel.dataChanged.emit()
        # self.listViewModel.modelReset()
        return text

    def clearView(self):
        print 'clearView'
        nodes = []
        # self.listViewModel.setNodeUUIDs(nodes)
        # self.listViewModel.modelReset()
        return

    def getNodeStrings(self):
        # value = self.listViewModel.getNodeUUIDs()
        value = self.getNodes()
        print 'get string:', value
        return value
