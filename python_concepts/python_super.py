from objprint import op


class Animal:
    def __init__(this, age):
        this.age = age
        this.name = None

    def func(this, name):
        print(this.age, name)
        this.name = name

class Person(Animal):
    def __init__(self, age, name):
        super(Person, self).__init__(age)
        self.name = name


class Male(Person):
    def __init__(self, age, name):
        super(Male, self).__init__(age, name)
        self.gender = "male"

    def test1(self):
        if self.name == "adam":
            print(123)
        else:
            print(234)

    @staticmethod
    def f(x):
        print(x)

if __name__ == "__main__":

    m = Male(23, "adam")
    print(Male.__name__, Male.__bases__, Male.__dict__)
    # m = Person(23, "adam")
    # print(m.name)
    # op(m)
    # o = Animal(12)
    # print(o.name)
    # Animal.func(o, 'nihao')
    # print(o.name)
