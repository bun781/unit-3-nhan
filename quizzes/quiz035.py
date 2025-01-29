# quiz#035
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self, grade, name, age):
        Person.__init__(name=name, age=age)
        self.grade = grade

    def get_grade(self):
        return f'{Person(self).name}, {Person(self).age} is in grade {self.grade}'
