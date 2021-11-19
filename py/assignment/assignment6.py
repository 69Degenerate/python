#modules are set of prewritten programs
import math
a = input('type the number: ')
b = input('type second number: ')
x = float(a)
y = float(b)
#function for ceiling value of given input
print(math.ceil(x))

#function for floor value of given input
print(math.floor(x))

#Return a float with the magnitude (absolute value) of x but the sign of y. On platforms that support signed zeros
print(math.copysign(x,y))

#for squere of input
print(math.sqrt(x))
