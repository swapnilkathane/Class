class x:
    a=1000
    b=2000
    def display(self):
        print(x.a)
        print(x.b)
    def modify(self):
        x.a=3000
        x.b=4000

X1=x()
X1.display()
X1.modify()
X1.display()
X2=x()
X2.display()
