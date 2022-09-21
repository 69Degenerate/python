#string specific functions

first = input('name:')
#len is general purpose methodes to count to no of characters
print(len(first))

#string specific functions are called as methodes
print(first.upper())     #method to convert string in upper case

#methode to find positiion of character
m = input('type the character you wanna find: ')
print(first.find(m))

#method to replace sting
n = input('type the word you wanna replace: ')
p = input('type the word you wanna put threre: ')
print(first.replace(n,p))

#methhod to check if given string is present or not
a = input('type the word you wanna check: ')
print(a in first)
