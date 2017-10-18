"""

Usage:
>>> import qtLearn.windows.assetBrowser.assetBrowserWindow
>>> reload(qtLearn.windows.assetBrowser.assetBrowserWindow)
>>> qtLearn.windows.assetBrowser.assetBrowserWindow.main()
"""

import sys
from functools import partial

import Qt.QtGui as QtGui

import qtLearn.uiUtils
import qtLearn.widgets.nodesMayaWidget
import qtLearn.windows.assetBrowser.forms.ui_assetActions
import qtLearn.windows.assetBrowser.forms.ui_assetCart
import qtLearn.windows.assetBrowser.forms.ui_assetIncomingView
import qtLearn.windows.assetBrowser.forms.ui_assetInfoView
import qtLearn.windows.assetBrowser.forms.ui_assetListView
import qtLearn.windows.assetBrowser.forms.ui_assetOutgoingView
import qtLearn.windows.assetBrowser.forms.ui_keyvalueView
import qtLearn.windows.assetBrowser.forms.ui_searchBar
import qtLearn.windows.assetBrowser.forms.ui_searchCustomField
import qtLearn.windows.assetBrowser.forms.ui_searchTagFinder
import qtLearn.windows.assetBrowser.forms.ui_shotView
import qtLearn.windows.assetBrowser.forms.ui_tagView
import qtLearn.windows.assetBrowser.ui_assetBrowser

reload(qtLearn.uiUtils)
reload(qtLearn.widgets.nodesMayaWidget)
reload(qtLearn.windows.assetBrowser.ui_assetBrowser)
reload(qtLearn.windows.assetBrowser.forms.ui_assetListView)
reload(qtLearn.windows.assetBrowser.forms.ui_searchBar)
reload(qtLearn.windows.assetBrowser.forms.ui_searchTagFinder)
reload(qtLearn.windows.assetBrowser.forms.ui_searchCustomField)

reload(qtLearn.windows.assetBrowser.forms.ui_assetActions)
reload(qtLearn.windows.assetBrowser.forms.ui_assetCart)
reload(qtLearn.windows.assetBrowser.forms.ui_assetInfoView)
reload(qtLearn.windows.assetBrowser.forms.ui_shotView)
reload(qtLearn.windows.assetBrowser.forms.ui_assetIncomingView)
reload(qtLearn.windows.assetBrowser.forms.ui_assetOutgoingView)
reload(qtLearn.windows.assetBrowser.forms.ui_keyvalueView)
reload(qtLearn.windows.assetBrowser.forms.ui_tagView)


class AssetListView(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_assetListView.Ui_Form):
    def __init__(self):
        super(AssetListView, self).__init__()
        self.setupUi(self)


class SearchBar(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_searchBar.Ui_Form):
    def __init__(self):
        super(SearchBar, self).__init__()
        self.setupUi(self)


class SearchTagFinder(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_searchTagFinder.Ui_Form):
    def __init__(self):
        super(SearchTagFinder, self).__init__()
        self.setupUi(self)


class SearchCustomField(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_searchCustomField.Ui_Form):
    def __init__(self):
        super(SearchCustomField, self).__init__()
        self.setupUi(self)


class AssetActions(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_assetActions.Ui_Form):
    def __init__(self):
        super(AssetActions, self).__init__()
        self.setupUi(self)


class AssetCart(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_assetCart.Ui_Form):
    def __init__(self):
        super(AssetCart, self).__init__()
        self.setupUi(self)


class AssetInfoView(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_assetInfoView.Ui_Form):
    def __init__(self):
        super(AssetInfoView, self).__init__()
        self.setupUi(self)


class ShotView(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_shotView.Ui_Form):
    def __init__(self):
        super(ShotView, self).__init__()
        self.setupUi(self)


class AssetIncomingView(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_assetIncomingView.Ui_Form):
    def __init__(self):
        super(AssetIncomingView, self).__init__()
        self.setupUi(self)


class AssetOutgoingView(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_assetOutgoingView.Ui_Form):
    def __init__(self):
        super(AssetOutgoingView, self).__init__()
        self.setupUi(self)


class TagView(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_tagView.Ui_Form):
    def __init__(self):
        super(TagView, self).__init__()
        self.setupUi(self)


class KeyvalueView(QtGui.QWidget, qtLearn.windows.assetBrowser.forms.ui_keyvalueView.Ui_Form):
    def __init__(self):
        super(KeyvalueView, self).__init__()
        self.setupUi(self)


class AssetBrowserLayout(QtGui.QWidget, qtLearn.windows.assetBrowser.ui_assetBrowser.Ui_Form):
    def __init__(self):
        super(AssetBrowserLayout, self).__init__()
        self.setupUi(self)

        self.searchBarForm = SearchBar()
        self.searchBarLayout.addWidget(self.searchBarForm)

        self.searchCustomFrame.hide()
        self.searchTagFinderForm = SearchTagFinder()
        # self.searchTagFinderForm.hide()
        self.searchCustomLayout.addWidget(self.searchTagFinderForm)

        self.searchCustomFieldForm = SearchCustomField()
        # self.searchCustomFieldForm.hide()
        self.searchCustomLayout.addWidget(self.searchCustomFieldForm)

        self.assetListViewForm = AssetListView()
        self.assetListViewLayout.addWidget(self.assetListViewForm)

        self.assetActionsForm = AssetActions()
        self.assetActionsLayout.addWidget(self.assetActionsForm)

        self.assetCartForm = AssetCart()
        self.assetCartLayout.addWidget(self.assetCartForm)

        self.assetInfoViewForm = AssetInfoView()
        self.assetInfoViewLayout.addWidget(self.assetInfoViewForm)

        self.shotViewForm = ShotView()
        self.shotViewLayout.addWidget(self.shotViewForm)

        self.assetIncomingViewForm = AssetIncomingView()
        self.assetIncomingViewLayout.addWidget(self.assetIncomingViewForm)
        
        self.assetOutgoingViewForm = AssetOutgoingView()
        self.assetOutgoingViewLayout.addWidget(self.assetOutgoingViewForm)

        self.tagViewForm = TagView()
        self.tagViewLayout.addWidget(self.tagViewForm)

        self.keyvalueViewForm = KeyvalueView()
        self.keyvalueViewLayout.addWidget(self.keyvalueViewForm)


baseModule, BaseWindow = qtLearn.uiUtils.getBaseWindow()


class AssetBrowserWindow(BaseWindow):
    def __init__(self, parent=None, name=None):
        super(AssetBrowserWindow, self).__init__(parent, name=name)
        self.setupUi(self)
        self.addSubForm(AssetBrowserLayout)

        self.setWindowTitle('Asset Browser')

        # Menu Bar
        self.addMenuBarContents(self.menubar)
        self.menubar.show()

        # Hide irrelevant stuff
        self.baseHideProgressBar()
        self.baseHideStandardButtons()

    def addMenuBarContents(self, menubar):
        # File Menu
        file_menu = QtGui.QMenu('File', menubar)

        # New Search
        newSearchAction = QtGui.QAction('New Search', file_menu)
        newSearchAction.setShortcut('Ctrl+N')
        newSearchAction.setStatusTip('Start a new Asset search')
        newSearchAction.triggered.connect(partial(self.newSearchCallback))

        # Save Search
        saveSearchAction = QtGui.QAction('Save Search', file_menu)
        saveSearchAction.setShortcut('Ctrl+S')
        saveSearchAction.setStatusTip('Save an Asset search')
        saveSearchAction.triggered.connect(partial(self.saveSearchCallback))

        file_menu.addAction(newSearchAction)
        file_menu.addAction(saveSearchAction)
        menubar.addMenu(file_menu)

    def newSearchCallback(self):
        print 'new search callback'

    def saveSearchCallback(self):
        print 'save search callback'


ui = None


def main(show=True, widthHeight=(1100, 1000)):
    global ui
    print 'ui:', ui

    name = 'AssetBrowserWindow'
    app, parent = qtLearn.uiUtils.getParent()

    if ui is not None:
        ui.close()
    ui = AssetBrowserWindow(parent=parent, name=name)
    if not ui:
        return ui
    if show:
        ui.show()

    if widthHeight:
        pos = ui.pos()
        ui.setGeometry(pos.x(), pos.y(), widthHeight[0], widthHeight[1])

    # Enter Qt application main loop
    if app is not None:
        sys.exit(app.exec_())
    return ui

