#prime number =

# 2,3,5,7,11,13,17,19,23

#7 => 1 to 7

#Method one to find a prime number

num1 =int(input("Enter a number: "))

count = 0

for i in range(1,num1+1):

     if num1%i==0:
         count+=1
         print(i)

if count==2:
    print("Given number is a prime number",count ,"is having a 2 factors")
else:
    print("Not a prime number")


#Method two to find a prime number

num2 =int(input("Enter a number: "))

if num2<=1:
    print("Not a prime number")
else:

    flag = True

    for i in range(2,num2):
        if num2%i==0:
            flag=False
            print("Not a prime number")
            break
        
    if flag == True: 
        print("Prime number")


#Method 3 using function 

def check_prime(num3):
    if num3<=1:
        return "Not a prime number"
    
    for i in range(2,num3):
        if num3%i==0:
            return "Not a prime number"
        
    return "Prime number"

print(check_prime(3))

#Methof 4 using half of given number

def check_prime(num4):
    if num4<=1:
        return "Not a prime number"
    
    for i in range(2,num4//2+1):
        if num4%i==0:
            return "Not a prime number"
        
    return "Prime number"

print(check_prime(3))

