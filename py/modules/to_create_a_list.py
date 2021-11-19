def list_creator():
    list=[]
    n=int(input('no of elements: '))
    t=int(input('''
    what type of data you are going to enter
    1.int
    2.string
    3.float
    4.long int
    '''))
    if t==1:
        print('enter the elements:')
        for i in range(0,n):
            elements=int(input())
            list.append(elements)
    if t==2:
        print('enter the elements:')
        for i in range(0,n):
            elements=str(input())
            list.append(elements)
    if t==3:
        print('enter the elements:')
        for i in range(0,n):
            elements=float(input())
            list.append(elements)
    return list





