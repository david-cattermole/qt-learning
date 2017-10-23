"""


Some help came from:
https://stackoverflow.com/questions/21964061/qt-qlineedit-error-popup-balloon-message
"""

import sys

import Qt.QtCore as QtCore
import Qt.QtWidgets as QtWidgets


class SuggestionListWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SuggestionListWidget, self).__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.listWidget = QtWidgets.QListWidget()
        self.button = QtWidgets.QPushButton("Button")

        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.button)

    # def moveEvent(self, event):
    #     print('moveEvent:', event, event.pos(), event.oldPos())
    #     super(SuggestionListWidget, self).moveEvent(event)


class WidgetErrorChecking(SuggestionListWidget):
    def __init__(self, parent, widget):
        super(WidgetErrorChecking, self).__init__(parent)

        self.widget = widget

        self.hide()

        if isinstance(widget, QtWidgets.QLineEdit):
            widget.textEdited.connect(self.showSuggestions)

    def showSuggestions(self):
        """
        Show the widget.
        """
        message = "suggestions..."
        # self.setText(message)
        self.adjustSize()
        self.update()
        self.show()

        self.move(self.widget.mapTo(self.parentWidget(),
                                    self.widget.rect().bottomLeft()))

    # def checkWidgetValue(self, value):
    #     if not value:
    #         return
    #
    #     try:
    #         value = float(value)
    #     except ValueError:
    #         value = 0.0
    #
    #     if 0.0 > value:
    #         self.showMessage('Needs to be greater then 0.0')
    #     elif value > 100:
    #         self.showMessage('Needs to be less then 100.0')
    #     else:
    #         self.hide()
    #
    # def showMessage(self, message = None):
    #     """
    #     Show the widget.
    #     """
    #     self.setText(message)
    #     self.adjustSize()
    #     self.update()
    #     self.show()
    #
    #     self.move(self.widget.mapTo(self.parentWidget(),
    #                                 self.widget.rect().bottomLeft()))


class LineEditSuggestion(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super(LineEditSuggestion, self).__init__(parent)
        # self.listWidget = QtWidgets.QListWidget()
        self.listWidget = SuggestionListWidget(parent)
        self.listWidget.hide()

        self.textEdited.connect(self.showSuggestions)
        # self.editingFinished.connect(self.hideSuggestions)
        self.returnPressed.connect(self.hideSuggestions)

    def focusInEvent(self, event):
        print('focusInEvent:', event)
        if event.reason() == QtCore.Qt.MouseFocusReason:
            # print('The mouse triggered the event')
            self.showSuggestions()
        super(LineEditSuggestion, self).focusInEvent(event)

    def focusOutEvent(self, event):
        print('focusOutEvent:', event)
        if event.reason() == QtCore.Qt.MouseFocusReason:
            # print('The mouse triggered the event')
            self.hideSuggestions()
        super(LineEditSuggestion, self).focusInEvent(event)

    def showSuggestions(self):
        print('showSuggestions')
        self.listWidget.adjustSize()
        p = self.mapFromGlobal(-self.rect().bottomLeft())
        self.listWidget.move(-p)
        self.listWidget.update()
        self.listWidget.show()
        return

    def hideSuggestions(self):
        print('hideSuggestions')
        if self.listWidget is not None:
            self.listWidget.hide()
        return


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QHBoxLayout(self)

        self.button = QtWidgets.QPushButton(self)
        self.layout.addWidget(self.button)

        self.lineEdit = LineEditSuggestion(self)
        self.layout.addWidget(self.lineEdit)

        # self.lineEditSuggestion = WidgetErrorChecking(self, self.lineEdit)

        # self.lineEdit.cursorPositionChanged.connect(self.popup)

    # def popup(self, index_before, index_after):
    #     # cursorPositionChanged(int, int)
    #     print('i1:', index_before, 'i2:', index_after)
    #     # self.listWidget = QtWidgets.QListWidget(self)


def main(argv):
    app = QtWidgets.QApplication(argv)

    ui = Window()
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
