#Functions 
# it is a block of coden, which gets executed whenever you call it

# def cal_volume(r):
#     print('Calculating volume of a sphere')
#     print((4/3)*3.14*(r**3))
#     print('Calculated volume')

# print("Someother operations")
# cal_volume(10)
# print('operation 2')
# cal_volume(25)
# cal_volume(35)
# cal_volume(5)

# def simple_calc(a,b):
#   print(a+b)
#   print(a-b)
#   print(a*b)
#   if b!=0:
#      print(a/b)
#      print(a%b)
#      print(a//b)
#   else:
#      print("Divisible not posible")


# simple_calc(10,20)
# simple_calc(20,0)
# simple_calc(63,55)
# simple_calc(90,100)

# def table(n):
#     for i in range(1,21):
#         print(n,"X",i,"=",n*i)
# table(17)
# table(20)
# table(18)

# def sum_natural(n):
#     sum = 0
#     for i in range(n):
#         i = i +1
#         sum = sum +i
#     print(sum)

# sum_natural(10)
# sum_natural(11)


# def product_natural(n):
#     sum = 1
#     for i in range(n):
#         i = i +1
#         sum = sum *i
#     print(sum)

# product_natural(10)
# product_natural(11)


def factorial(n):
    fact = 1
    for i in range(n):
        i = i +1
        fact = fact*i
    print(fact)

factorial(5)
factorial(6)
factorial(10)