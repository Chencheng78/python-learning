from objprint import op


class Animal:
    def __init__(self, age):
        self.age = age


class Person(Animal):
    def __init__(self, age, name):
        super(Person, self).__init__(age)
        self.name = name


class Male(Person):
    def __init__(self, age, name):
        super(Male, self).__init__(age, name)
        self.gender = "male"


m = Male(23, "adam")
# m = Person(23, "adam")
op(m)