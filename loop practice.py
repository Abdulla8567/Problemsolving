# li = ["abdulla","basheer","kiran"]
# for i in li:
#     print(i)

# for index in range(len(li)):
#     print(li[index])

# # the range(len[li]) generates the indicies from 0 to the length of the list minus 1.

# d = {
#     1 : "abddulla",
#     2 : "basheer",
#     3 : "kiran",
#     4 : "sabeer"
# }

# for s in d:
#     print(s,":",d[s])

# n = 10

# for i in range (0,n):
#     print(i)


# # nested for loop 

# for i in range(1,5):
#     for j in range (i):
#         print(i,end="")
#     print()


# for i in range(1,5):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()



# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(65+j),end="")
#     print()

# i = 1
# while i<5:
#     j=0
#     while j<i:
#         print(chr(64+i),end="")
#         j=j+1
#     print()
#     i=i+1


# for i in range(1,5):
#     for j in range(i):
#         print(chr(64+i),end="")
#     print()
 
# pattern problem
# i = 1
# while i <5:
#     j=0
#     while j<i:
#         print(chr(97+j-32),end="")
#         j=j+1
#     print()
#     i=i+1


# Print 1 to N using a loop.

# using for & while

# n=21
# for i in range(n):
#     print(i)

# i = 1

# while i<n:
#     print(i)
#     i+=1


# Print Even Numbers from 1 to N.

# for i in range(n):
#     if i%2==0:
#         print(i)

# n8 = 20

# i8 = 1

# while i8<=n8:
#     i8+=1
#     if i8%2==0:
#         print(i8)
        

# Print Sum of First N Natural Numbers.

# n=10
# i=1
# sum = 0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)
# sum = 0
# for i2 in range(n):
#     i2=i2+1
#     sum=sum+i2
# print(sum)

# for factorial using for loop 

# abdul = 1
# for i3 in range(n):
#     i3 = i3+1
#     abdul = abdul*i3
# print(abdul)

# i4 = 1

# while i<=n:
#     abdul*=i4
#     i4+=1
# print(abdul)

# # Print the Table of a Given Number (e.g., 5 × 1 = 5 … 5 × 10 = 50).

# n = int(input("Enter the number:"))

# for i in range(1,21):
#     print(n,"X",i,"=",n*i)

# i = 1

# while i<20:
#     i+=1
    # print(n,"X",i,"=",n*i)

# Count the Number of Digits in a number using a loop.

# abdul_1=int(input("Enter the number:"))
# count = 0
# for i in str(abdul_1): # here we used conversion type str
#     count = count + 1 
# print("Number of digits is",count)

# n = int(input("Enter the number:"))

# count = 0

# while n>0:
#      n=n//10
#      count=count+1
# print("Number of digits is :",count)


# to count side by side numbers 

# n = int(input("enter the number:"))

# sum = 0

# for i in str(n):
#     digit = n%10
#     sum = sum + digit # same for product just sum =1 & sum*digit
#     n=n//10
# print()


#fibanoic series 

n = int(input("Enter the n value:"))

a = 0 
b = 1

for i in range(n):
    print(a,end=" ")
    a,b = b ,a+b