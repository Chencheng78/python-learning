class M(type):
    def __new__(cls, name, bases, dict):
        print(name, bases, dict)
        return type.__new__(cls, name, bases, dict)

class A(metaclass=M):
    pass