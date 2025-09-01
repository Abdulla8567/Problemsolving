# n = int(input("Enter the number:"))

# fact =1
# sum = 1

# for i in range(n):
#     i = i+1
#     sum = sum+1
#     fact = fact *i
# print(fact)


# n=int()

# armstrong=370

# original_num = armstrong

# sum = 0

# while original_num>0:
#      rem = original_num % 10
#      sum = sum + rem**len(str(armstrong))
#      original_num=original_num//10

# print(sum)

# if sum == armstrong:
#      print("Armstrong number")
# else:
#      print("Not a armstrong number")


# def check_prime(num1):
#     count=0
#     for i in range(1,num1+1):
#         if num1%i==0:
#             count=count+1
#     if count==2:
#         print("Prime number")
#     else:
#         print("Not a prime number")

# check_prime(5)

# num1 = int(input("Enter the number:"))
# check_prime(num1)


num1 = int(input("Enter the number:"))
if num1<=1:
    print("not a prime number")
else:
    flag=True
    for i in range(2,num1):
        if num1%i==0:
            flag=False
            print("Not a prime number")
    if flag==True:
        print("Prime number")