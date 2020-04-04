class cust:
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def deposit(self,damt):
        self.cbal=self.cbal+damt
    def withdrawl(self,wamt):
        self.cbal=self.cbal-wamt
        #self.display()
    def display(self):
        print(self.cbal)


cust1=cust('swapnil','chitoda','303556',20000)
print(cust1)
cust1.deposit(10000)
cust1.withdrawl(5000)
cust1.display()

