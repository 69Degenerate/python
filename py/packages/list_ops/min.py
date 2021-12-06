def minimum():
    m=list_creator()
    minm = m[0]
    for number in m:
        if number>minm:
            minm=number
    print(f'your list as following:{m}')
    print('largest number in list is: ',minm)
    return minm