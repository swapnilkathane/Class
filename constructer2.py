class X:
    def __init__(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
    def modify(self):
        self.a=self.a+100
        self.b=self.b+200
X1=X()
X1.display()
X1.modify()
X1.display()
X2=X()

