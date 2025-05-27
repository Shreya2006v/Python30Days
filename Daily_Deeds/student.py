import json

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {"name": self.name, "grades": self.grades}
