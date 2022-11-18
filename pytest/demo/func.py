class calc:
    def add(x,y):
        return x+y

    def sub(x,y):
        return x-y

    def mul(x,y):
        return x*y
    
def test_add():
    assert calc.add(1,1)==2
def test_sub():
    assert calc.sub(3,2)==1
def test_mul():
    assert calc.mul(1,1)==1
    
print('run test')