
# def check_positive_or_negative_or_zero(n):
#     if n==0:
#         print("Zero")
#         return n,"Zero"
#     elif n>0:
#         print("POsitive")
#         return n,"positive"
#     else:
#         if n<0:
#             print("negative")
#             return n,"negative"


# check_positive_or_negative_or_zero(1)
# check_positive_or_negative_or_zero(-5)
# check_positive_or_negative_or_zero(0) 

# result = check_positive_or_negative_or_zero(25)
# print(result)
    

# def even_or_odd(n):
#     return "even" if n%2==0 else "odd"

# res1 = float(input("enter the number:"))
# print(even_or_odd(res1))

#vote eligible using terinary

# def vote_eligible(n):
#     return "eligible" if n>=18 else "not eligible to vote"

# result = float(input("Enter the number:"))

# print(vote_eligible(result))

# def check_greater(num1,num2):
#     if num1>num2:
#         print("num1 is greater than num2",num1)
#     elif num1 == num2:
#         print("both are equal")
#     else :
#         print("num2 is greater than num1",num2)

# check_greater(10,22)
# check_greater(22,22)
# check_greater(55,10)

# def check_greater(num1,num2,num3):
#     return "num1 is greater than num2&num3" if num1>num2>num3 else "all are equal" if num1==num2==num3 else "num2 is greater than num1&num3" if num2>num1>num3 else "num3 is greater than num2&num1"

# print(check_greater(1,2,3))

# def simple_calc(num1 ,num2 ,op):
#     if op=='+' or op == 'add':  # op in ['add',"+"] using membership operator
#         print(num1+num2)
#     elif op=='-' or op == "sub":
#         print(num1-num2)
#     elif op =='*' or op == "mul":
#         print(num1*num2)
#     elif op=='/' or op == 'div':
#         print(num1/num2) if num2!=0 else print("Division is not possible")
#     else:
#         print("Invalid operator")



    # return num1+num2 if op== '+' else num1-num2 if op == '-' else num1*num2 if op == '*' else "not a valid operation"


# print(simple_calc(1,2,"+"))

# n1=float(input("Enter n1:"))
# n2=float(input("Enter n2:"))
# sym =input("Enter operation").lower()


num1  = int(input("Enter the num:"))
num2  = int(input("Enter the num:"))

print("num2 is greater",num1) if num1>num2 else print("both are equal") if num1==num2 else print("num2 is greater",num2)
