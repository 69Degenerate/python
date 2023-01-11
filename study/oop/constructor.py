class demo:
    s=1
    d=2
    def de(self):
       return self.d+self.s

class nonparameterizedconstr():
    def __init__(self):
        pass
    name="name"
    def demo2(self):
        print("first construst")
    def de(self):
        self.demo2()
obj=nonparameterizedconstr()

class parameterizedconstr():
    no1=0
    no2=0
    def __init__(self,n1,n2):
        self.no1=n1
        self.no2=n2
    def display(self):
        print('no1=',self.no1,'\nno2=',self.sno2)
obj=parameterizedconstr(1,2)
obj.display()


