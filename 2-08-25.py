# def simple_calc(a=20,b=10):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     if b!=0:
#         print(a/b)
#         print(a%b)
#         print(a//b)
#     else:
#         ("Divisible is not posible")

# #Positional arguments

# simple_calc(10,20)

# #keyword arguments

# simple_calc(a=20,b = 0)

# #Default arguments

# simple_calc(10)# here a = 20 & b is taken as default argumets
# simple_calc()

# Arbitrary arguments 

def add(a,*b):
    print(a+sum(b))
    print(a)
    print(b)

add(3,55,89,78)
add(2,4,4,5,5,5,5,6,6,6,6,5,5,4,4,4)