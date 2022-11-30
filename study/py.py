# ----------------------------------------------------------------------------------------------------
# # # inheritance
# # basicaly sharing things of parent class with child classes,these things can consist variables,methods and classes of parent class
# # following are the types of inheritance
# # Single inheritance.
# # Multi-level inheritance.
# # Multiple inheritance.
# # Multipath inheritance.
# # Hierarchical Inheritance.
# # Hybrid Inheritance(combination of all or some of above).

# class mul:
#     def m():
#         print('2*8')
#     def sub(self,n,m):
#         return n-m

# class demo:
#     def add(self,n,m):
#         return n+m

#     def dadd(self):
#         return self.add(1,2)
    
# class newcls(demo):
#     pass

# class new(newcls,mul):
#     pass

# c=demo()
# print(c.dadd())
# n=newcls()
# print(n.dadd)
# nn=new()
# print(nn.dadd())
# mm=new()
# print(mm.sub(1,1))
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# # #  abstraction with python
# # its a process of minimizing code by hiding lenthie or unneccesory code 
# # in this code we writted code in file class
# from classpro import demo
# d= demo()
# print(d.d,' ',d.s,' ',d.de())
# # to use abstraction we import ABC and abstractmethod fropm abc
# # following creates abstract class and method
# from abc import ABC,abstractmethod
# class abstra(ABC):
#     @abstractmethod
#     def abcmethod():
#         pass
# abstract class is a class that constains an abstract method
# abstract class cannot be used to create an object,it's only accesssesible throgh inheritance
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# # # polymorphism:its means multiple forms
# # two different classes with same methods 
# class d:
#     def one(self):
#         print('first function')
#     def sec(self):
#         print('second fun')
# class d2:
#     def one(self):
#         print('first function')
#     def sec(self):
#         print('second fun')
# q=d()
# w=d2()
# q.one()
# w.one()

# # but these methods can also be different with their operetions
# class d:
#     def one(self):
#         print('first function')
#     def sec(self):
#         print('second fun')
# class d2:
#     def one(self):
#         s='first function'
#         return s
#     def sec(self):
#         s='second function'
#         return s
# q=d()
# w=d2()
# print('first class methods')
# q.one()
# q.sec()
# print('\nsecond class methods')
# print(w.one())
# print(w.sec())

# # method overriding
# # method overriding is a condition where child class can have method with same as one in the parent class 
# # these methods may or may not be same in working
# # following is a example of method overriding
# class demo:
#     def one(self):
#         return 'first original method from parent class'
# class demo2(demo):
#     def one(self):
#         return 'same function but with child class'
# class demo3(demo):
#     def one(self):
#         return 'same function but with second child class'
# d=demo()
# d2=demo2()
# d3=demo3()
# print('',d.one(),'\n',d2.one(),'\n',d3.one())
# # method overloading is not possible in python by default
# # method overloading a condition where to methods can have same name but different type and/or number of parameters
# def overloade(no,no1,no2):
#     pass
# def overloead(str1,str2):
#     pass
# # method overriding is only possible in compiler bases languages
# # since python is a interpeter based language ,the second method will overwrite the first method
# ---------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------
# # # encsulation with python
# # encapsulation means wrappind data in a sigle unit
# # its not something that we need to do specificaly, its comes with using classes.like a class consist of methods and variables
# # we dont really need to write any code for this cause its a concept of OOPS
# # in a compiler based languages encapsulate code in byte code we can be executed but cant be readed, and data hiding is one of its advantage
# ---------------------------------------------------------------------------------------------------