print('***price of a house is 1M.***')

x = bool(input('''Do you have good credits
(type any word for yes or no is default): '''))

if x:
    print('you have to pay ',1000000/10,'as downpayment')
else:
    print('you have to pay ',1000000/20,'as downpayment')
