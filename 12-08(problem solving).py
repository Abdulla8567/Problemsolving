
# Fibanoccic series => Print first n fib numbers

# 0 1 1 2 3 5 8 13 

# n=10

# n1,n2 = 0,1

# for i in range(0,n):
#     print(n1)

#     new_num1 = n1+n2
#     n1 = n2
#     n2 = new_num1

# # using  function 

# def check_fib(n,num1,num2):

#     for i in range(0,n):
#         print(num1)
#         new_num = num1+num2
#         num1 = num2
#         num2 = new_num


# check_fib(10,0,1)

#  Armstrong number =>

# 153 = 1**3 + 5**3 + 3**3 = 153

#1634 = 1**4 + 6 **4 + 3**4 + 4**4 = 1634

# armstrong_num = 153

# sum = 0

# temp = armstrong_num

# while temp>0:

#     rem = temp % 10

#     sum = sum + rem**len(str(armstrong_num))

#     temp = temp // 10

# print(sum)

# if sum == armstrong_num:
#     print("Armstrong number")
# else:
#     print("Not armstrong number")




# armstrong_num = 153

# temp = armstrong_num

# sum = 0

# for i in str(armstrong_num+1):

#     rem = temp %10

#     sum = sum + rem ** len(str(armstrong_num))

#     temp = temp//10

# print(sum)

# if sum == armstrong_num:
#     print("Armstrong number")
# else:
#     print("Not a armstrong number")



#to check prime from 200 to 400 

# def check_prime(num1):
#     if num1<=1:
#         return False
#     for i in range(2,num1):
#         if num1%i==0:
         

#           return False
#     return True

# input1=int(input("Enter the number:"))
# input2=int(input("Enter the number:"))

# for i in range(input1,input2+1):
#     res=check_prime(i)

#     if res:
#         print(i)
    

# def check_prime():
#     count=0
#     num1=int(input("enter a number:"))
#     for i in range(1,num1+1):
#         if num1%i==0:
#             count=count+1
#             print(i)
        
#     if count ==2:
#         print("prime number")
#     else:
#         print("not prime number")


# check_prime()

# num1 = int(input("Enter the number:"))

# flag = True

# count=0
# if num1<=1:
#     print("not a prime number")
# else:

#     for i in range(2,num1):
#         if num1%i==0:
#             flag=False
#             count=count+1
#             print("Not a prime number")

#     if flag == True: 
#         print("Prime number")



#to check armstrong number from 200 to 400 

def check_armstrong(num1):
    temp = num1

    sum = 0 

    while temp>0:
        rem = temp%10
        sum = sum + rem ** len(str(num1))
        temp = temp//10

    if sum == num1:
        return True

    else:
        return False

i1 = int(input("Enter the number: "))
i2 = int(input("Enter the number: "))

for i in range(i1,i2+1):
    res = check_armstrong(i)
    if res==True:
        print(i)
        



















