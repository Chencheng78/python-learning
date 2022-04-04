class A:
    def say(self):
        print("A")


class B:
    def say(self):
        print("B")


class C(A):
    pass


class M(B, C):
    pass


m = M()
print(M.mro())
m.say()