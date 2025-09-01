# arm strong numbers 

num1 = int(input('Enter the number:'))

temp = num1 

sum = 0

while temp>0:

    rem = temp % 10

    sum = sum+rem**len(str(num1))

    temp=temp // 10

print(num1,"=",sum)

if sum == num1:
    print("Armstrong number")

else:
    print("Not a armstrong number")


#  in function and find the armstrong number in range of 200 to 400


def check_armstrong(num2):

    temp1 = num2

    sum1 = 0

    while temp1 > 0 :

        rem1 = temp1 % 10 

        sum1 = sum1 + rem1 ** len(str(num2))

        temp1 = temp1 // 10


    if sum1 == num2:

        return True
    
    else:

        return False
    
ip1 = int(input('Enter the number:'))

ip2 = int(input('Enter the number:'))

for i in range(ip1 ,ip2+1):

    res = check_armstrong(i)

    if res == True: 
        print(i)

