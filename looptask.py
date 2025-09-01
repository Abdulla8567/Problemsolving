# 1.WAP take a list add the that number
n = float(input('Enter the number:'))
list1 = [1,22,33,66,99]
for  i in list1:
    print(f'{i}+{n}={i+n}')

# 2.WAP take a list find even number

list2 = [1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if i%2==0:
        print(i)

# 3. WAP PRINT COUNT THE EVEN ODD NUMBERS 1 TO 10
    

count_even = 0
count_odd = 0
for i in range(1,11):
    if i%2==0:
         count_even=count_even+1
    elif i%2!=0:
        count_odd+=1
print("There are ",count_even,"even numbers")
print("There are ",count_odd,"odd numbers")

    
# 4.SUM OF DIGITS OF A NUMBER EXAMPLE 12322 OUTPUT=10

n = 12322
sum = 0
for i in str(n):
    digit = n%10
    sum = sum+digit
    n=n//10
print(sum)

# 5.PRODUCT OF DIGITS OF A NUMBER EXAMPLE 123 OUTPUT=6

n = 12322
sum = 1
for i in str(n):
    digit = n%10
    sum = sum*digit
    n=n//10
print(sum)
