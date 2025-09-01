
# # # # # # # # # n8 = 20

# # # # # # # # # i8 = 1

# # # # # # # # # while i8<=n8:
# # # # # # # # #     i8+=1
# # # # # # # # #     if i8%2==0:
# # # # # # # # #         print(i8)
        


# # # # # # # # # # Print the Table of a Given Number (e.g., 5 × 1 = 5 … 5 × 10 = 50).

# # # # # # # # # n = int(input("Enter the number:"))

# # # # # # # # # for i in range(1,21):
# # # # # # # # #     print(n,"X",i,"=",n*i)

# # # # # # # # # i = 1

# # # # # # # # # while i<20:
# # # # # # # # #     i+=1
# # # # # # # # #     print(n,"X",i,"=",n*i)

# # # # # # # # # Count the Number of Digits in a number using a loop.

# # # # # # # # # abdul_1=int(input("Enter the number:"))
# # # # # # # # # count = 0
# # # # # # # # # for i in str(abdul_1): # here we used conversion type str
# # # # # # # # #     count = count + 1 
# # # # # # # # # print("Number of digits is",count)


# # # # # # # # n = int(input("Enter the number:"))

# # # # # # # # count = 0

# # # # # # # # while n>0:
# # # # # # # #      n=n//10
# # # # # # # #      count=count+1
# # # # # # # # print("Number of digits is :",count)

# # # # # # # count_even = 0
# # # # # # # count_odd = 0
# # # # # # # for i in range(1,11):
# # # # # # #    if i%2==0:
# # # # # # #       count_even+=1
# # # # # # # print(count_even)

# # # # # # n = 12322
# # # # # # sum = 0
# # # # # # for i in str(n):
# # # # # #     digit = n%10
# # # # # #     sum = sum+digit
# # # # # #     n=n//10
# # # # # # print(sum)

# # # # # # n=int(input("Enter the number:"))

# # # # # # sum = 0
# # # # # # i=1

# # # # # # while n>0:
# # # # # #     digit = n%10
# # # # # #     sum = sum +digit
# # # # # #     n=n//10
# # # # # # print(sum)

# # # # # # n=int(input("Enter the number:"))

# # # # # # sum = 1
# # # # # # i=1

# # # # # # while n>0:
# # # # # #     digit = n%10
# # # # # #     sum = sum *digit
# # # # # #     n=n//10
# # # # # # print(sum)

# # # # # # for i in range(1,25):
# # # # # #     continue

# # # # # # n=int(input("Enter the value:"))

# # # # # # for i in range(n):
# # # # # #     i=i+1
# # # # # #     if i%2==0:
# # # # # #         print(i,'even')

# # # # # # n = int(input("Enter the value:"))

# # # # # # if n % 2 == 0:
# # # # # #     print("Even")
# # # # # # else:
# # # # # #     print("Odd")

# # # # # # def check_palindrome():
# # # # # #     n4 = input("Enter the string1: ")

# # # # # #     if n4 == n4[::-1]:
# # # # # #             print(n4 , "Is Palindrome")
# # # # # #     else:
# # # # # #             print("Not a palindrome")


# # # # # # check_palindrome()
        

# # # # # # # Write a function that takes a list and prints only the even numbers.

# # # # # # def list_even_number():
# # # # # #        list2 = [2,4,5,9,66,44,88,33,36]
# # # # # #        for i in list2:
# # # # # #               if i%2==0:
# # # # # #                     print(i)

# # # # # # list_even_number()


# # # # # def length_of_string():
# # # # #      n3 = input("Enter the string3: ")
# # # # #      count = 0
# # # # #      for i in str(n3):
# # # # #           count=count +1

# # # # #      print(count)
# # # # # length_of_string()

# # # # # def check_average(a,*b):
# # # # #      total = a+sum(b)
# # # # #      count=1+len(b)
# # # # #      average = total/count
# # # # #      print(average)

# # # # # check_average(1,2,3,5,6)

# # # # def check_average(a,*b):
# # # #      total = a+sum(b)
# # # #      count = 1+len(b)
# # # #      average = total/count

# # # #      print(average)

# # # # check_average(1,2,3,5,6)

# # # def valid_triangle(s1,s2,s3):


# # #      if (s1+s2>s3) and (s2+s3>s1) and (s3+s1>s2):
# # #           return "Valid triangle"
# # #      else:
# # #           return "not a valid trianlge"
     
# # # valid_triangle(3,4,5)

# # # d1 = {
# # #     "srinu" : 800,
# # #     "sai" : 700,
# # #     "abdul" : 500
# # # }

# # # print(d1["abdul"])


# # # n=int(input("Enter the number: "))

# # # for i in range(1,n+1):
# # #     if n%i==0:
# # #         print(i)


# # def square_of_all_numbers(n):
# #     sum = 0
# #     for i in range(1,n+1):
# #         square = i**2
# #         sum = sum+square
        
# #     print(sum)
   
        
# # square_of_all_numbers(3)
# # square_of_all_numbers(5)

# # # Treasure Hunt Guessing Game
# # # You are on a treasure island, and the treasure is buried at a specific location marked by a secret number between 1 and 100.
# # # Write a program that keeps asking the player to guess the number until they find it.
# # # After each wrong guess, display "Try Again!", and when they guess correctly, display "Treasure Found!".
# # # Input Format
# # # Multiple integer guesses entered one per line until the correct number is guessed.
# # # Output Format
# # # "Try Again!" for each wrong guess, and "Treasure Found!" when correct.
# # # Constraints
# # # Secret number is between 1 and 100.

# # while True: 
# #     Guess = int(input("Enter the number:"))

# #     Tresaure_numbers = [50]

# #     if Guess not in Tresaure_numbers:
# #         print("Try again!")

# #     elif Guess in Tresaure_numbers:
# #         print("Treasure Found")
# #         break

        
# # def perfect_squares(n):
# #      for i in range(1,n):
# #       if i**2<500:
# #         print(i**2, end = " ")

# # perfect_squares(500)

# def cube_collector(n):
#     for i in range(1,n):
#         print(i**3,end=" ")

# cube_collector(10)

n2 = 153
sum = 0
temp = n2
no_of_digits = len(str(n2))
while n2>0:
    rem = temp % 10
    sum = sum + rem**no_of_digits
    temp = temp // 10

print(sum)

if sum == n2:
    print("Armstrong number")
else:
    print("Not Armstrong number")

  