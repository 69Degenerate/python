print('***arithmatic oparation using class***')
q=int(input('1st digit:'))
w=int(input('2nd digit:'))
class Mth():
    def add(self):
        print(q+w,'Addition')
    def sub(self):
        print(q-w,'Substraction')
    def mul(self):
        print(q*w,"Multiplication")


m=Mth()
m.add()
m.sub()
m.mul()