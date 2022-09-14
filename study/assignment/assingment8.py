v = bool(input('''
does buyer have high income
(type any key for yes or leav empty for no): '''))
x = bool(input('''
does buyer have good credits
(type any key for yes or leav empty for no): '''))
z = bool(input('''
does buyer have any criminal record
(type any key for yes or leav empty for no): '''))

if v and x and z:
     print('''****
     we don't have money for criminals
     ***''')
if v and x and not z:
    print('''****
    you can have loan and also my doughter,
    Heck you can just fuck me instead :)****
    ''')
if v and not x and not z:
    print('no loan for brok ass shit like you')

if x and not v and not z:
    print('no loan for brok ass shit like you')