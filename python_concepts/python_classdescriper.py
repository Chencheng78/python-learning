class FuncDescr:
    def __get__(self, *args):
        def f(self, data):
            print(self.name)
            print(data)
        return f


class A:
    f = FuncDescr()


def f(self, data):
    print(self.name)
    print(data)

class Name:
    def __get__(self, obj, objtype):
        return 'Peter'


class B:
    # def __init__(self):
    name = Name()

if __name__ == "__main__":
    o = B()
    print(o.name)
    n = Name()
    print(n)
    # o = A()
    # o.name = 'alice'
    # o.f = f
    # o.f('data')