from create import list_creator

def maximum():
    m=list_creator()
    maxim = m[0]
    for number in m:
        if number>maxim:
            maxim=number
    print(f'your list as following:{maxim}')
    print('largest number in list is: ',maxim)
    return maxim



#print(maximum())
#print(minimum())