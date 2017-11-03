"""

Usage:
>>> import qtLearn.windows.assetBrowser.assetBrowserWindow
>>> qtLearn.windows.assetBrowser.assetBrowserWindow.main()
"""

import sys
from functools import partial

import Qt.QtWidgets as QtWidgets

import qtLearn.uiUtils as uiUtils
import qtLearn.widgets.nodesMayaWidget as nodesMayaWidget
import qtLearn.windows.assetBrowser.forms.ui_assetActions as ui_assetActions
import qtLearn.windows.assetBrowser.forms.ui_assetCart as ui_assetCart
import qtLearn.windows.assetBrowser.forms.ui_assetInfoView as ui_assetInfoView
import qtLearn.windows.assetBrowser.forms.ui_assetListView as ui_assetListView
import qtLearn.windows.assetBrowser.forms.ui_assetDependenciesView as ui_assetDependenciesView
import qtLearn.windows.assetBrowser.forms.ui_assetIncomingView as ui_assetIncomingView
import qtLearn.windows.assetBrowser.forms.ui_assetOutgoingView as ui_assetOutgoingView
import qtLearn.windows.assetBrowser.forms.ui_keyvalueView as ui_keyvalueView
import qtLearn.windows.assetBrowser.forms.ui_searchBar as ui_searchBar
import qtLearn.windows.assetBrowser.forms.ui_searchCustomField as ui_searchCustomField
import qtLearn.windows.assetBrowser.forms.ui_searchTagFinder as ui_searchTagFinder
import qtLearn.windows.assetBrowser.forms.ui_shotView as ui_shotView
import qtLearn.windows.assetBrowser.forms.ui_tagView as ui_tagView
import qtLearn.windows.assetBrowser.ui_assetBrowser as ui_assetBrowser


class AssetListView(QtWidgets.QWidget, ui_assetListView.Ui_Form):
    def __init__(self):
        super(AssetListView, self).__init__()
        self.setupUi(self)


class SearchBar(QtWidgets.QWidget, ui_searchBar.Ui_Form):
    def __init__(self):
        super(SearchBar, self).__init__()
        self.setupUi(self)


class SearchTagFinder(QtWidgets.QWidget, ui_searchTagFinder.Ui_Form):
    def __init__(self):
        super(SearchTagFinder, self).__init__()
        self.setupUi(self)


class SearchCustomField(QtWidgets.QWidget, ui_searchCustomField.Ui_Form):
    def __init__(self):
        super(SearchCustomField, self).__init__()
        self.setupUi(self)


class AssetActions(QtWidgets.QWidget, ui_assetActions.Ui_Form):
    def __init__(self):
        super(AssetActions, self).__init__()
        self.setupUi(self)


class AssetCart(QtWidgets.QWidget, ui_assetCart.Ui_Form):
    def __init__(self):
        super(AssetCart, self).__init__()
        self.setupUi(self)


class AssetInfoView(QtWidgets.QWidget, ui_assetInfoView.Ui_Form):
    def __init__(self):
        super(AssetInfoView, self).__init__()
        self.setupUi(self)


class ShotView(QtWidgets.QWidget, ui_shotView.Ui_Form):
    def __init__(self):
        super(ShotView, self).__init__()
        self.setupUi(self)


class AssetDependenciesView(QtWidgets.QWidget, ui_assetDependenciesView.Ui_Form):
    def __init__(self):
        super(AssetDependenciesView, self).__init__()
        self.setupUi(self)


class AssetIncomingView(QtWidgets.QWidget, ui_assetIncomingView.Ui_Form):
    def __init__(self):
        super(AssetIncomingView, self).__init__()
        self.setupUi(self)


class AssetOutgoingView(QtWidgets.QWidget, ui_assetOutgoingView.Ui_Form):
    def __init__(self):
        super(AssetOutgoingView, self).__init__()
        self.setupUi(self)


class TagView(QtWidgets.QWidget, ui_tagView.Ui_Form):
    def __init__(self):
        super(TagView, self).__init__()
        self.setupUi(self)


class KeyvalueView(QtWidgets.QWidget, ui_keyvalueView.Ui_Form):
    def __init__(self):
        super(KeyvalueView, self).__init__()
        self.setupUi(self)


class AssetBrowserLayout(QtWidgets.QWidget, ui_assetBrowser.Ui_Form):
    def __init__(self, parent):
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
        
        self.assetDependenciesViewForm = AssetDependenciesView()
        self.assetDependenciesViewLayout.addWidget(self.assetDependenciesViewForm)
        
        # self.assetIncomingViewForm = AssetIncomingView()
        # self.assetIncomingViewLayout.addWidget(self.assetIncomingViewForm)

        # self.assetOutgoingViewForm = AssetOutgoingView()
        # self.assetOutgoingViewLayout.addWidget(self.assetOutgoingViewForm)

        self.tagViewForm = TagView()
        self.tagViewLayout.addWidget(self.tagViewForm)

        self.keyvalueViewForm = KeyvalueView()
        self.keyvalueViewLayout.addWidget(self.keyvalueViewForm)


baseModule, BaseWindow = uiUtils.getBaseWindow()


class AssetBrowserWindow(BaseWindow):
    def __init__(self, parent=None, name=None, title=None):
        super(AssetBrowserWindow, self).__init__(parent, name=name)
        self.setupUi(self)
        self.addSubForm(AssetBrowserLayout)
        # self.parent = parent

        if title is None:
            title = 'Asset Browser'
        self.setWindowTitle(title)

        # Menu Bar
        self.addMenuBarContents(self.menubar)
        self.menubar.show()

        # Hide irrelevant stuff
        self.baseHideProgressBar()
        self.baseHideStandardButtons()

    def addMenuBarContents(self, menubar):
        # Search Menu
        search_menu = QtWidgets.QMenu('Search', menubar)

        # New Search
        newSearchAction = QtWidgets.QAction('New Search', search_menu)
        newSearchAction.setShortcut('Ctrl+N')
        newSearchAction.setStatusTip('Start a new Asset search')
        newSearchAction.triggered.connect(partial(self.newSearchCallback))

        # Save Search
        saveSearchAction = QtWidgets.QAction('Save Search', search_menu)
        saveSearchAction.setShortcut('Ctrl+S')
        saveSearchAction.setStatusTip('Save an Asset search')
        saveSearchAction.triggered.connect(partial(self.saveSearchCallback))

        # Search Mode Menu
        search_mode_menu = QtWidgets.QMenu('Search Mode', search_menu)

        modeBasicAction = QtWidgets.QAction('Basic', search_mode_menu)
        modeBasicAction.setStatusTip('Use simple search text')
        modeBasicAction.setCheckable(True)
        modeBasicAction.setChecked(True)

        modeTagAction = QtWidgets.QAction('Tag Finder', search_mode_menu)
        modeTagAction.setStatusTip('Use tag browsing')
        modeTagAction.setCheckable(True)
        modeTagAction.setChecked(False)

        modeFieldAction = QtWidgets.QAction('Search Condtions', search_mode_menu)
        modeFieldAction.setStatusTip('Use custom Search condtions on database fields')
        modeFieldAction.setCheckable(True)
        modeFieldAction.setChecked(False)

        searchModeActionGroup = QtWidgets.QActionGroup(search_menu)
        searchModeActionGroup.addAction(modeBasicAction)
        searchModeActionGroup.addAction(modeTagAction)
        searchModeActionGroup.addAction(modeFieldAction)

        search_mode_menu.addAction(modeBasicAction)
        search_mode_menu.addAction(modeTagAction)
        search_mode_menu.addAction(modeFieldAction)

        search_menu.addAction(newSearchAction)
        search_menu.addAction(saveSearchAction)
        search_menu.addSeparator()
        search_menu.addMenu(search_mode_menu)
        menubar.addMenu(search_menu)

        # View Menu
        view_menu = QtWidgets.QMenu('View', menubar)

        assetViewListAction = QtWidgets.QAction('List Asset View', view_menu)
        assetViewListAction.setCheckable(True)
        assetViewListAction.setChecked(True)
        assetViewGridAction = QtWidgets.QAction('Grid Asset View', view_menu)
        assetViewGridAction.setCheckable(True)

        assetViewActionGroup = QtWidgets.QActionGroup(view_menu)
        assetViewActionGroup.addAction(assetViewGridAction)
        assetViewActionGroup.addAction(assetViewListAction)

        view_menu.addAction(assetViewListAction)
        view_menu.addAction(assetViewGridAction)
        menubar.addMenu(view_menu)

        # Version Menu
        version_menu = QtWidgets.QMenu('Versions', menubar)

        approvedVersionAction = QtWidgets.QAction('Approved Versions', version_menu)
        approvedVersionAction.setCheckable(True)
        approvedVersionAction.setChecked(True)
        latestVersionAction = QtWidgets.QAction('Latest Version', version_menu)
        latestVersionAction.setCheckable(True)
        deletedVersionAction = QtWidgets.QAction('Deleted Versions', version_menu)
        deletedVersionAction.setCheckable(True)
        customVersionAction = QtWidgets.QAction('Custom Versions', version_menu)
        customVersionAction.setCheckable(True)

        assetVersionActionGroup = QtWidgets.QActionGroup(version_menu)
        assetVersionActionGroup.addAction(approvedVersionAction)
        assetVersionActionGroup.addAction(latestVersionAction)
        assetVersionActionGroup.addAction(deletedVersionAction)
        assetVersionActionGroup.addAction(customVersionAction)

        version_menu.addAction(approvedVersionAction)
        version_menu.addAction(latestVersionAction)
        version_menu.addAction(deletedVersionAction)
        version_menu.addAction(customVersionAction)
        menubar.addMenu(version_menu)
        
        # Window Menu
        window_menu = QtWidgets.QMenu('Window', menubar)

        assetCartAction = QtWidgets.QAction('Asset Cart', window_menu)
        assetCartAction.setStatusTip('Show or hide the asset cart')
        assetCartAction.setCheckable(True)
        assetCartAction.setChecked(True)

        assetInfoAction = QtWidgets.QAction('Asset Info', window_menu)
        assetInfoAction.setStatusTip('Show or hide the asset info')
        assetInfoAction.setCheckable(True)
        assetInfoAction.setChecked(True)

        window_menu.addAction(assetCartAction)
        window_menu.addAction(assetInfoAction)
        menubar.addMenu(window_menu)

    def newSearchCallback(self):
        print('new search callback')

    def saveSearchCallback(self):
        print('save search callback')


ui = None


def main(show=True, widthHeight=(1400, 600)):
    global ui
    print('ui:', ui)

    name = 'AssetBrowserWindow'
    app, parent = uiUtils.getParent()

    if ui is not None:
        ui.close()
    ui = AssetBrowserWindow(parent=parent, name=name)
    if not ui:
        return ui
    if show:
        ui.show()

    if widthHeight:
        uiUtils.setWindowWidthHeight(ui, widthHeight)

    # Enter Qt application main loop
    if app is not None:
        sys.exit(app.exec_())
    return ui

