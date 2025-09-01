# give user input infinite times until it becomes negative the loops runs 

# while True:
#     n= int(input('enter the number:'))
#     if n>0:
#         print(n,"Try again")
#     elif n<=0:
#         print("Loop stopped")
#         break

# Method 2

# ip_num =float(input("Enter the number: "))

# while ip_num>0:
#     ip_num =float(input("Enter the number: "))


# reverse a number and sum of number and count the number 

num1 = 12345
sum = 0
count = 0

while num1>0:  
    rem = num1 % 10
    print(rem,end="")
    num1 = num1 // 10
    count +=1
    sum = sum + rem
print()
print(sum)
print(count)
print(num1)

