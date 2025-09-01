# # # # What is an f-string?
# # # # An f-string is a formatted string literal. It's a way to embed variables and expressions directly inside a string using {} — all prefixed by the letter f.
# # # # f"some text {expression_or_variable} more text"
# # # #  Example:
# # # name = "Abdul"
# # # age = 22
# # # weight = 55
# # # print(f"My name is {name} and I am {age} years old. and my weight is {weight}")
# # # a = 5
# # # b = 3
# # # print(f"{a} + {b} = {a + b}")
# # # print(f"{a} - {b} = {a - b}")

# # # #CONDITIONAL STATEMENTS

# # # # if statment

# # # n1=10
# # # if n1%5 == 0:
# # #     print(f'{n1} is divisible by 5')

# # #     # num greater than 40 & divisible by 7 or not if divisible by 7 given power that num

# # n = int(input("please enter the input:"))
# # if n>40 and n%7==0 :
# #     print(f'{n} is divisble by 7',n**2)
# # if n<40 and n%7!=0 :
# #     print(f'{n} is not divisble by 7')

# #     #take a list take num check that num present in list or not 

# # list1 = [5,8,99,100,55,22,33]
# # n2 = int(input("enter the number:"))
# # if n2 in list1:
# #     print(f'{n2} is present in the {list1}')
# # if n2 not in list1:
# #     print(f'{n2} is not in {list1}')

# # #else statement

# # num1 = 32
# # if num1%2==0 :
# #     print(f'{num1} is even')
# # else:
# #     print(f'{num1} is a odd number')

# # age = int(input('please enter the age:'))
# # if age>=18:
# #     print("He is eligible to vote")
# # else:
# #     print("He is not eligible for vote")

# # elif = we have more  one condition or more task

# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# c = int(input("enter the number:"))

# if a>b and a>c:
#     print("a is greater than b & c")
# elif b>a and b>c:
#     print("b is greater than a & c")
# else :
#     print("c is greater than a & b")

# calculator task 

# a = 4
# b = 6
# n = int(input("Enter the number:"))
# if n ==1:
#     print(f'{a}+{b}={a+b}')
# elif n==2:
#     print(f'{a}-{b} = {a-b}')
# else:
#     print("That number  is not available")

#given number is positive or negative 

# n = int(input("Please enter the number:"))
# if n>0:
#     print("Given number is positive")
# else:
#     if n==0:
#         print("Zero")
#     else:
#         print("Negative")


# n = int(input("Enter the number"))
# if n>0:
#     print("Given number is positive")
# else:
#     if(n==0):
#         print("Zero")
#     else:
#         if(n==-1):
#             print("-1")
#         else:
#             print("negative")

# n=int(input("Enter the number:"))
# if n>0:
#     print("positive")
# elif n==0:
#     print("zero")
# elif n==-1:
#     print("-1")
# else:
#     print("negative")

num1 =float(input("Enter the number:"))
num2 =float(input("Enter the number:"))
symbol=input("enter the symbol:")

if symbol== "+":
    print(f"{num1+num2}")
elif symbol=="-":
    print(f'{num1-num2}')
elif symbol=="/":
    if num2!=0: #to avoid zero division error use if condition 
        print(f'{num1/num2}')
    else:
        print("Zero division error ,pakkaki elli aduko ma")
else:
    print("symbol is not available")