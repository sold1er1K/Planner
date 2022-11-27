from view.view import View
from model.model import Model


class Controller:
    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)

    def start(self):
        self.view.show_start()

    def showDeleteScreen(self):
        self.view.show_delete()

    def showEditScreen(self):
        self.view.show_edit()
