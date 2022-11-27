from enum import Enum


class Model:
    def __init__(self):
        self.Planner = Planner()


class Planner:
    def __init__(self):
        self.tasksList = []


class Task:
    def __init__(self, date, description, group, importance):
        self.date = date
        self.description = description
        self.group = group
        self.importance = importance

    def create_task(self):
        pass

    def delete_task(self):
        pass

    def edit_task(self):
        pass

    def get_task(self):
        pass
