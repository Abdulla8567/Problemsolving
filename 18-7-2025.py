# 300>=4 rupees 
# 200=3 rupees 
#100>= 2 rupees 
# 0to 100= 0

n= float(input("Enter the units:"))
if n>=300:
    print("one unit per charge is 4 rupees and total bill is",n*4)
else:
    if n>=200:
        print("one unit per charge is 3 rupees and total bill is:",n*3)
    else:
        if n>=100:
            print("one unit per charge is 2 rupees and total bill is",n*2)
        else:
            if n>=0 and n<100:
                print("one unit per charge is zero(0) rupees and total bills is",n*0)


# leap year code 

#year should be divisible by 4 

year = int(input("Enter the year:"))
# 1.
# if (year%4==0 and year % 100!=0) or  year%400==0:
#     print("leap year")
# else :
#     print("Not a leap year")

if year%400==0:
    print("leap")
else:
    if year%100!=0 and year%4==0:
        print('leap')
    else:
        print("Nlot a leap year")

#2
# if (year%400==0) or (year%100!=0 and year%4==0):
#     print('Leap year')
# else:
#     print("Not a leap year")


