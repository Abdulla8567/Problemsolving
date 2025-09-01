#scopes 

# To change the global variable value within the function 

# num1 = 10

# def first_func():
#     global num1
#     num1 =20
#     def second_func():
#         print(num1)
#     second_func()
#     print(num1)
# first_func()
# print(num1)


#To declare local and globals variables in one function method 

# num1 = 10

# def first_func():
#     num1 =20
#     globals()["num1"] = 50
#     print(num1)
# first_func()
# print(num1)

# To change the local value from the previous function 

num1 = 10

def first_func():
    num1 =20
    def second_fun():
        num1 = 20
        def third_func():
              nonlocal num1
              num1=30
              print(num1)
        third_func()
        print(num1)
    second_fun()
    print(num1)
first_func()
print(num1)

# Lifetime =>
#            lifetime of the global scope variable
#  for example num1 declared in global scope it will be accessible until program end execution.

# scope - area 
# 
# local scope variable accessible within in the function where its runtime will be unaccessible when the function will be called.



#  lambda function - anonymous function on one line 

example_function = lambda a,b:a+b

print(example_function(2,5))