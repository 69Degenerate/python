q=[]
n=int(input('no of items: '))
t=0
for i in range(1,n+1):
    print('price of item',i)
    item=int(input())
    q.append(item)
    t+=item
print('total',t)