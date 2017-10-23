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
import qtLearn.windows.assetBrowser.forms.ui_assetIncomingView as ui_assetIncomingView
import qtLearn.windows.assetBrowser.forms.ui_assetInfoView as ui_assetInfoView
import qtLearn.windows.assetBrowser.forms.ui_assetListView as ui_assetListView
import qtLearn.windows.assetBrowser.forms.ui_assetOutgoingView as ui_assetOutgoingView
import qtLearn.windows.assetBrowser.forms.ui_keyvalueView as ui_keyvalueView
import qtLearn.windows.assetBrowser.forms.ui_searchBar as ui_searchBar
import qtLearn.windows.assetBrowser.forms.ui_searchCustomField as ui_searchCustomField
import qtLearn.windows.assetBrowser.forms.ui_searchTagFinder as ui_searchTagFinder
import qtLearn.windows.assetBrowser.forms.ui_shotView as ui_shotView
import qtLearn.windows.assetBrowser.forms.ui_tagView as ui_tagView
import qtLearn.windows.assetBrowser.ui_assetBrowser as ui_assetBrowser

# reload(uiUtils)
# reload(nodesMayaWidget)
# reload(ui_assetBrowser)
# reload(ui_assetListView)
# reload(ui_searchBar)
# reload(ui_searchTagFinder)
# reload(ui_searchCustomField)

# reload(ui_assetActions)
# reload(ui_assetCart)
# reload(ui_assetInfoView)
# reload(ui_shotView)
# reload(ui_assetIncomingView)
# reload(ui_assetOutgoingView)
# reload(ui_keyvalueView)
# reload(ui_tagView)


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


baseModule, BaseWindow = uiUtils.getBaseWindow()


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
        file_menu = QtWidgets.QMenu('File', menubar)

        # New Search
        newSearchAction = QtWidgets.QAction('New Search', file_menu)
        newSearchAction.setShortcut('Ctrl+N')
        newSearchAction.setStatusTip('Start a new Asset search')
        newSearchAction.triggered.connect(partial(self.newSearchCallback))

        # Save Search
        saveSearchAction = QtWidgets.QAction('Save Search', file_menu)
        saveSearchAction.setShortcut('Ctrl+S')
        saveSearchAction.setStatusTip('Save an Asset search')
        saveSearchAction.triggered.connect(partial(self.saveSearchCallback))

        file_menu.addAction(newSearchAction)
        file_menu.addAction(saveSearchAction)
        menubar.addMenu(file_menu)

    def newSearchCallback(self):
        print('new search callback')

    def saveSearchCallback(self):
        print('save search callback')


ui = None


def main(show=True, widthHeight=(1100, 1000)):
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
        pos = ui.pos()
        ui.setGeometry(pos.x(), pos.y(), widthHeight[0], widthHeight[1])

    # Enter Qt application main loop
    if app is not None:
        sys.exit(app.exec_())
    return ui

