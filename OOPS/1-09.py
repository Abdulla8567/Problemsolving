# OOPS 

#code maintainability
# Data security, Code exposure
# code reuse

# class and object 
# class => class is a blueprint of an object
# object - Real world entity 
# Behaviour and Data => Methods

class Calculator:
    def add(self,a,b):
        print(a+b)

    def sub(self,a,b):
        print(a-b)

    # def mul(self):
    #     print("Dummy")

    def mul(self,a,b):
        print(a*b)

    def div(self,a,b):
        if b!=0:
            print(a/b)
            print(a%b)
        else:
            print("Zero division error")
    
    def describe(self):
        print(self.id,self.manfac_date)

clc1 = Calculator()
clc2 = Calculator()
clc3 = Calculator()
clc4 = Calculator()

# add(2,3,5)

clc1.add(2,3)
# clc2.add(4,5)
# clc3.add(9,11)
clc1.sub(20,10)
clc1.mul(9,6)
clc1.div(6,2)
clc1.div(6,0)
# adding variables - 2 ways => 1.Manual way 2.Constructor

clc1.id = 45
clc1.manfac_date = "01-sep"
clc1.describe()
# clc1.mul()
# clc3.describe()

# def self ?
# # self is a reference to the current object (instance) of the class.

# 🔹 Points to remember:

# It is used inside class methods to access instance variables and methods of that object.

# self is passed automatically when you call a method on an object, you don’t need to pass it manually.

# You can use any name instead of self, but by convention, we always use self.

