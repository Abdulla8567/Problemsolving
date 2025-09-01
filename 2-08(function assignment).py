# Write a function that takes two numbers and prints their sum.

def sum(n1,n2):
    return n1+n2

print(sum(2,3))

# Write a function that prints the square of a number

def square_of_number(n):
    return n**2

print(square_of_number(2))

# Write a function to check if a number is even or odd and print the result.

def check_even_odd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
    
print(check_even_odd(5))
print(check_even_odd(8))


# Write a function that prints the factorial of a number.
def fact(n,sum):
    for i in range(1,n):
        sum=sum*i
    return sum
    
print(fact(5,1))

# Write a function to find the maximum of three numbers and print it.

def check_greater(num1,num2,num3):
    return "num1" if num1>num2>num3 else "All are equal" if num1==num2==num3 else "num2" if num2>num1>num3 else "num3"

print(check_greater(2,5,6))


# Write a function to count and print the number of vowels in a string.

def count_vowels():
    n = input("Enter the string: ").lower()
    count = 0
    for i in n:
        if i in ['a','e','i','o','u']:
            count=count+1
    print(count)

count_vowels()


# Write a function that takes a list and prints the sum of all elements.

def list_sum():
    list1=[2,3,4,5,6,55]
    sum1 = 0

    for i in list1:
        sum1 = sum1 + i
    return sum1

print(list_sum())

# Write a function to reverse a string and print it.

def reverse_string():
    str1=input("Enter the string:")
    return str1[::-1]

print(reverse_string())

# Write a function that checks if a string is a palindrome and prints the result.

def check_palindrome():
    n4 = input("Enter the string1: ")

    if n4 == n4[::-1]:
            print(n4 , "Is Palindrome")
    else:
            print("Not a palindrome")


check_palindrome()
        
# Write a function that takes a list and prints only the even numbers.

def list_even_number():
       list2 = [2,4,5,9,66,44,88,33,36]
       for i in list2:
              if i%2==0:
                    print(i)

list_even_number()

# Write a function that prints the length of a string without using the len() function.


def length_of_string():
     n3 = input("Enter the string3: ")
     count = 0
     for i in str(n3):
          count=count +1

     print(count)
length_of_string()


# Write a function that accepts any number of arguments and prints their average.


def check_average(a,*b):
     total = a+sum(b)
     count = 1+len(b)
     average = total/count

     print(average)

check_average(1,2,3,5,6,55)
