# Print all numbers from 1 to 100 using a for loop.

# for i in range(1,101):
#     print(i)

# Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)

# n = int(input("enter the number : "))
# sum = 0
# for i in range(n):
#     i = i+1
#     sum = sum + i
# print(sum)

# Print all even numbers between 1 and 50 using a while loop.

# n = 50

# i =1

# while i<=n:
#     if i%2==0:
#         print(i)
#     i = i+1   

# Write a program to display the multiplication table of a given number. First 20

# for i in range(1,21):
#     for j in range(1,21):
#         print(i,"x",j,"=",i*j)

# Reverse a number using a while loop.
    #   1. Also can we get the sum of all the digits.

# n = int(input("enter the number:"))
# reverse = 0
# total = 0

# using while looop 


# while n!=0:
#     digit = n%10
#     reverse = reverse*10+digit
#     total=total+digit
#     n = n//10
# print("Reversed number is :",reverse)
# print("Sum of the digit is :",total)

# using for loop reverse a number and sum of given numbers 

# for i in str(n):
#     digit = n %10
#     total=total+digit
#     if n!=0:
#         reverse=reverse*10+digit
#     n = n//10
# print(total)
# print(reverse)

# Write a program to count the number of digits in a given number using a while loop.

# n = int(input("enter the number:"))

# count = 0 
# using while loop

# while n>0:
#     count=count+1
#     n = n//10 #it will remove the last digit of the number 
# print("No of digits is :",count)

# using for loop 


# for i in str(n):
#     count=count+1
# print(count)

#Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.

# n = int (input("Enter the number :" ))

# while n>=0:
#     print("Give number is positive",n)
#     n = int (input("Enter the number :" ))
# print("you enterned a non-negative number, loop stopped",n)


# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.

# for i in range(1,101):
#     if i%3==0 or i %5 == 0:
#         print(i)


n = 101
i = 1

while i<n:
    if i % 3 == 0 or i % 5 == 0 :
        print(i)
    i = i + 1