# Palindromic Bus Ticket
# In a small town, bus tickets have a unique pattern — if the ticket number reads the same forwards and backwards, it is considered a “lucky” ticket.
# Given a ticket number as a string, write a program to:
# - Reverse the number
# - Check if it is a palindrome
# If it is, print "Lucky Ticket", otherwise print "Not Lucky".

def check_palindrome(str1):
    if str1 == str1[::-1]:  #examples : wow , madam ,level ,radar , racecar , ciciv , defined ..etc
        return "Lucky Ticket"
    else:
        return "Not Lucky"
    
str1=input("Enter the string: ")
print(check_palindrome(str1))

# Sum of Magic Squares

# A wizard is teaching you a math spell to calculate the *magic sum* of square numbers.
# Given a number n, you must find the sum of the squares of all numbers from 1 to n.
# For example, if n = 3, the result is 1² + 2² + 3² = 14.

def square_of_all_numbers(n):
    sum = 0
    for i in range(1,n+1):
        square=i**2
        sum = sum+square

    print(sum)
        
square_of_all_numbers(3)

# Treasure Hunt Guessing Game
# You are on a treasure island, and the treasure is buried at a specific location marked by a secret number between 1 and 100.
# Write a program that keeps asking the player to guess the number until they find it.
# After each wrong guess, display "Try Again!", and when they guess correctly, display "Treasure Found!".
# Input Format
# Multiple integer guesses entered one per line until the correct number is guessed.
# Output Format
# "Try Again!" for each wrong guess, and "Treasure Found!" when correct.
# Constraints
# Secret number is between 1 and 100.

while True: 
    Guess = int(input("Enter the number:"))

    Tresaure_numbers = [50]

    if Guess not in Tresaure_numbers:
        print("Try again!")

    elif Guess in Tresaure_numbers:
        print("Treasure Found")
        break

    # Perfect Square Festival
# In a city fair, there is a game where you win a prize if your chosen number is a *perfect square*.
# Write a program to display all perfect square numbers between 1 and 500 so players can see which numbers will win.
# Input Format
# No input required.
# Output Format
# All perfect squares between 1 and 500 separated by spaces.
# Constraints
# Numbers between 1 and 500.
# Sample Test Cases
# Output:
# 1 4 9 16 25 36 49 64 81 100 ... 484


def perfect_squares(n):
     for i in range(1,n):
      if i**2<500:
        print(i**2, end = " ")

perfect_squares(500)


# Cube Challenge
# In a video game, your character collects cubes of different sizes.
# Given a number n, print the cube of every number from 1 to n so the player knows the sizes of cubes they can collect.
# Input Format
# A single integer n.
# Output Format
# The cubes of numbers from 1 to n, each on a new line.


def cube_collector(n2):
    for i in range(1,n2):
       print(i**3)

cube_collector(10)