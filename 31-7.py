# 1.(2 marks)
# What will be the output and data type of the following code?

# a = input("Enter value:")
# print(a*2)
# print(type(a))

# output = <class str>

# 2.Convert the string '123.45' into a float, and print its integer part only.

# string_1='123.45'

# float1 = float(string_1)

# int1 = int(float1)

# print(int1) # output = int value = 123

# 3.(2 marks)
# Identify the correct output of this expression:

# result = 10 > 5 and 3 < 1
# print(result)  # output = False

# 4.(4 marks)
# Write a program to take a number from the user and check whether it is:

# o Divisible by 3 and 4 → print “Divisible by both”
# o Only divisible by 3 → print “Divisible by 3”
# o Only divisible by 4 → print “Divisible by 4”
# o Otherwise → print “Not divisible”

# n = int(input("Enter the number:"))

# if n % 3 == 0 and n % 4 == 0:
#     print("Divisible by both")
# elif n%3 == 0:
#     print("Divisible by 3")
# else:
#     if n%4 == 0:
#         print("Divisible by 4")
#     else:
#         print("Not divisible")


# 5.(4 marks)
# Accept two numbers from the user and print whether their sum is even or odd, and whether it is greater than 50 or not.

# a = int(input("Enter value:"))
# b = int(input("Enter Value:"))

# sum = a+b
# print("Sum value is :",sum)
# if sum % 2 == 0 :
#     print("Sum is even")
#     if sum >50:
#         print("Sum is greater than 50")
#     else:
#         print("It is not greater than 50")
# elif sum % 2 != 0:
#     print("Sum is odd")
#     if sum >50:
#         print("Sum is greater than 50")
#     else:
#         print("It is not greater than 50")

# 6.(4 marks)
# Rewrite the following using elif and correct syntax errors:


# x = int(input("Enter number:"))
# if x < 0 :
#     print("Negative")
# elif x == 0:  # changed if to elif 
#     print("Zero")
# else:
#     print("Positive")

# 7.Write a program that asks for a password (input from user).

# If the password is incorrect, print “Try again”, and ask again. Repeat until correct password ("admin123") is entered.
# 1.Hint: You have to use an infinite while loop and break statement.

# while True:
#     password1= input("Enter the password:")
#     if password1 == "admin123":
#         print("Correct password")
#         break
#     else :
#         print("Try again")
    
# 8.Print all odd numbers between 1 to 20 using a loop, but skip 13 and 17 using the continue statement.

# i = 1

# while i <=20:
#     if i%2!=0:
#         if i == 13 or i == 17:
#             i+=1
#             continue
#         print(i)
#     i=i+1
    

# for i in range(1,20):
#     if i%2!=0:
#         if i == 13 or i == 17:
#             continue
#         print(i)

# 9.(4 marks)
# Write a program to find the sum of first n natural numbers. Solve the question in as many ways as you can.
# Example: for 5 input. Answer should be 15.
    

# n = int(input("Enter the number:"))
# sum = 0
# for i in range(n):
#     i = i +1
#     sum=sum+i
# print(sum)



# 10.(4 marks)
# Ask the user to enter a number.
# Print “Buzz” if the number is divisible by 7 or ends with even digit.
# Otherwise, print “Not a Buzz number”.

# n = int(input("Enter the number:"))

# last_digit = n % 10

# if n%7==0 or last_digit%2==0:
#     print("Buzz")
# else :
#     print("Not a Buzz number")


# 11.Explain each step:


# x = 5
# while x > 0: # 5 is greater than zero
#     if x == 3: condition is if x ==3 we have to skip 3 in loop 
#         x -= 1 # 3 = 3-1 = 2 so it will skip 3 and print 2 nd x value is 2 = 2-1 = 1 nd this is the last step because next is 0 nd loop will be stopped
#         continue
#     print(x)
#     x -= 1    #5 4 2  1

# 12.(4 marks)
# Write a program that:
# Takes an integer input
# If it’s a multiple of 4, prints square of the number
# If it’s a multiple of 5, prints cube of the number
# Otherwise, prints the number itself

# n = int(input("Enter the number:"))

# if n%4==0:
#     print(n**2)
# elif n%5==0:
#     print(n**3)
# else:
#     print(n)

# 13.Write a program to count how many alphabets are there in a string input from the user.
# Example input: abc123 → Output: 3

# str1 =input("Enter the input:")

# count = 0

# for i in str1:
#     if ("a"<=i<="z") or ("A"<=i<="Z"):
#         count+=1
# print(count)


# 14.What is the role of the pass statement in Python?
# Use an example of an empty for loop using pass.

    # pass statemment is like null does nothing just pass the statement

# n = ''

# for i in n:
#     pass
# print("Pass")
