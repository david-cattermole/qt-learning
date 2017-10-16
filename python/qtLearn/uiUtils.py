"""

"""

import sys

# import Qt # __version__, __binding__, __qt_version__, __binding_version__
# import Qt.QtCore as QtCore
# import Qt.QtGui as QtGui
import Qt.QtWidgets as QtWidgets


def getHostApplication():
    result = None
    appName = QtWidgets.QApplication.applicationName()
    if appName is None:
        result = 'standalone'
    elif 'maya' in str(appName).lower():
        result = 'maya'
    elif 'nuke' in str(appName).lower():
        result = 'nuke'
    elif 'houdini' in str(appName).lower():
        result = 'houdini'
    else:
        print 'Warning: Unknown application name, %r' % appName
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
    print 'getParent host:', host

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
    if host == 'standalone':
        import qtLearn.baseStandaloneWindow as baseModule
        reload(baseModule)
        BaseWindow = baseModule.BaseStandaloneWindow
    elif host == 'maya':
        import qtLearn.baseMayaWindow as baseModule
        reload(baseModule)
        BaseWindow = baseModule.BaseMayaWindow
    else:
        print 'Warning: Unknown application host, %r' % host
    return baseModule, BaseWindow
