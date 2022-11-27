from view.screens.first import Ui_MainWindow
from view.screens.edit import Ui_EditWindow
from view.screens.delete import Ui_DeleteWindow


import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class View:
    def __init__(self, c, m):
        self.model = m
        self.controller = c

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()

        self.MainScreen = Ui_MainWindow(self.controller, self.model)
        self.EditScreen = Ui_EditWindow(self.controller, self.model)
        self.DeleteScreen = Ui_DeleteWindow(self.controller, self.model)

    def show_start(self):
        self.MainScreen.show()
        self.EditScreen.hide()
        self.DeleteScreen.hide()
        sys.exit(self.app.exec_())

    def show_edit(self):
        self.MainScreen.hide()
        self.EditScreen.show()

    def show_delete(self):
        self.MainScreen.hide()
        self.DeleteScreen.show()
