"""
https://stackoverflow.com/questions/4827207/how-do-i-filter-the-pyqt-qcombobox-items-based-on-the-text-input
"""
import sys
from Qt import QtCore
from Qt import QtGui


class ExtendedCombo(QtGui.QComboBox):
    def __init__(self, parent=None):
        super(ExtendedCombo, self).__init__(parent)

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
        super(ExtendedCombo, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedCombo, self).setModelColumn(column)

    def view(self):
        return self.completer.popup()

    def index(self):
        return self.currentIndex()

    def setTextIfCompleterIsClicked(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)


def main(argv):
    app = QtGui.QApplication(argv)

    model = QtGui.QStandardItemModel()

    words = ['hola', 'adios', 'hello', 'good bye']
    for i, word in enumerate(words):
        item = QtGui.QStandardItem(word)
        model.setItem(i, 0, item)

    combo = ExtendedCombo()
    combo.setModel(model)
    combo.setModelColumn(0)

    combo.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
