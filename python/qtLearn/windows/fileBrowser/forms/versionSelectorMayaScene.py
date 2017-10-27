"""
Specialisation of the VersionSelector for Maya Scene files.

TODO: Make this UI select Maya files in a specific directory structure:
<maya workspace>/scenes/department/<name>_<version>_<subversion>_<description>.<ext>

"""

import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.windows.fileBrowser.nodes as nodes
import qtLearn.windows.fileBrowser.forms.versionSelector as versionSelector



class MajorVersionNode(versionSelector.VersionNode):
    def __init__(self, name, data=None, parent=None):
        icon = QtGui.QIcon(QtGui.QPixmap(':/MajorVersion.png'))
        super(MajorVersionNode, self).__init__(name,
                                               data=data,
                                               parent=parent,
                                               icon=icon,
                                               selectable=False,
                                               editable=False)
        self.typeInfo = 'majorversion'


class MinorVersionNode(versionSelector.VersionNode):
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


class VersionModelMayaScene(versionSelector.VersionModel):
    def __init__(self, root, font=None):
        super(VersionModelMayaScene, self).__init__(root, font=font)
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


class VersionSelectorMayaScene(versionSelector.VersionSelector):
    def __init__(self, parent):
        super(VersionSelectorMayaScene, self).__init__(parent,
                                                       withTypeFilter=False,
                                                       withFileFormatFilter=True)
        # TODO: Fill out this class and work out how to neatly inherit and
        # control the UI.

