"""
Defines a combo box that contains a list of possible words and are
auto-completed to these names.

Based from:
https://stackoverflow.com/questions/4827207/how-do-i-filter-the-pyqt-qcombobox-items-based-on-the-text-input

Usage:
>>> import Qt.QtGui as QtGui
>>> model = QtGui.QStandardItemModel()
>>> words = ['cat', 'dog', 'fox', 'wolf', 'tiger', 'lion']
>>> for i, word in enumerate(words):
>>>     item = QtGui.QStandardItem(word)
>>>     model.setItem(i, 0, item)
>>> combo = ComboBoxCompleter()
>>> combo.setModel(model)
>>> combo.setModelColumn(0)
"""

import sys
from Qt import QtCore
from Qt import QtGui


class ComboBoxCompleter(QtGui.QComboBox):
    def __init__(self, parent=None):
        super(ComboBoxCompleter, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setEditable(True)
        self.completer = QtGui.QCompleter(self)

        # always show all completions
        self.completer.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        self.pFilterModel = QtGui.QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)

        self.completer.setPopup(self.view())

        self.setCompleter(self.completer)

        self.lineEdit().textEdited[unicode].connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.setTextIfCompleterIsClicked)

    def setModel(self, model):
        super(ComboBoxCompleter, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ComboBoxCompleter, self).setModelColumn(column)

    def view(self):
        return self.completer.popup()

    def index(self):
        return self.currentIndex()

    def setTextIfCompleterIsClicked(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
