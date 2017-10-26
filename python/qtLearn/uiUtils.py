"""

"""

import sys

import Qt # __version__, __binding__, __qt_version__, __binding_version__
import Qt.QtCore as QtCore
import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets


def getHostApplication():
    result = None
    appName = QtWidgets.QApplication.applicationName()
    if appName is None or len(appName) == 0:
        result = 'standalone'
    elif 'maya' in str(appName).lower():
        result = 'maya'
    elif 'nuke' in str(appName).lower():
        result = 'nuke'
    elif 'houdini' in str(appName).lower():
        result = 'houdini'
    else:
        print('Warning: Unknown application name, %r' % appName)
        result = appName
    return result


def getMayaMainWindow():
    from shiboken import wrapInstance
    from maya import OpenMayaUI as omui
    windowPtr = omui.MQtUtil.mainWindow()
    window = wrapInstance(long(windowPtr), QtWidgets.QWidget)
    return window


def getParent():
    host = getHostApplication()
    print('getParent host:', host)

    # try running outside of maya
    app = None
    parent = None
    if host == 'standalone':
        app = QtWidgets.QApplication(sys.argv)
        parent = None
    elif host == 'maya':
        parent = getMayaMainWindow()
    else:
        assert False
    return app, parent


def getBaseWindow():
    BaseWindow = None
    baseModule = None
    host = getHostApplication()
    print(host)
    if host == 'standalone':
        import qtLearn.baseStandaloneWindow as baseModule
        # reload(baseModule)
        BaseWindow = baseModule.BaseStandaloneWindow
    elif host == 'maya':
        import qtLearn.baseMayaWindow as baseModule
        # reload(baseModule)
        BaseWindow = baseModule.BaseMayaWindow
    else:
        print('Warning: Unknown application host, %r' % host)
    return baseModule, BaseWindow


def getFont(name=None):
    font = QtGui.QFont()
    name = name.lower()
    if 'normal' in name:
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
    elif 'small' in name:
        font.setPointSize(6)
    elif 'mediumlarge' in name:
        font.setPointSize(10)
    elif 'large' in name:
        font.setPointSize(12)

    if 'monospace' in name:
        font.setStyleHint(QtGui.QFont.Monospace)

    if 'bold' in name:
        font.setBold(True)

    if 'italic' in name:
        font.setItalic(True)
    return font
