# #while loop

# i=5
# while i < 8:
#     print("Hello Brother")
#     i+=1

# is_vishnu_alive = True

# while is_vishnu_alive==True:
#     print("salarodu is still fighting")
#     is_vishnu_alive = False

# #print natural number 1 to 10 using while loop

# n = 40
# i = 0

# while i<=n:
#     print(i)
#     i+=1

# #print 17th table 

# n1 = 17
# i = 1
# while i<=20:
#     print(n1,'X',i,'=',n1*i)
#     i = i+1

# n2 = 18
# i = 1
# while i<=20:
#     print(n2,'x',i,'=',n2*i)
#     i+=1

# n3 = 19 
# i = 1

# while i in range(1,21):
#      print(n3,'x',i,'=',n3*i)
#      i = i+1

# # Write a program to check if a given number is positive,negative, or zero.



# while True:
#     num= int(input("Enter the number:"))
    
#     if num ==0:
#         print("loop stopped")
#         break
#     elif num>0:
#             print("positive")
#     else:
#          print("negative")

# # for loop

# i. Print all numbers from 1 to 100 using a for loop

for i in range(1,101):
     if i>=0 and i<=100:
          print(i)


# Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
sum = 0
num = int(input("Enter the number:"))
for i in range(num +1):
    sum = sum + i
print(sum)    

