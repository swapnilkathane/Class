class C:
    v = 1234
    def f1(self):
        print("in fun f1 of class c")
    def f2(self):
        print("in fun f2 of class c")
        print(C.v)


x=C()
x.f1()
x.f2()
print(C.v)
