# # chr1 = input("Enter the character:")
# # for i in chr1:
# #     if 'A'<=i<="Z":
# #         print("it is upper case")
# #     elif "a"<=i<="z":
# #         print("it is lower case")

# # #print either upper or lower case after then print its opposite case 

# # n=input("Enter the character:")
# # for s in n:
# #     if 'A'<=s<='Z':
# #         abdul = chr(ord(s)+32)
# #         print(abdul)
# #     elif 'a'<=s<='z':
# #         abdul = chr(ord(s)-32)
# #         print(abdul)




# n=input("Enter the character:")
# for s in n:
#     if 'A'<=s<='Z':
#         abdul = chr(ord(s)+1)
#         print(abdul)
#     elif 'a'<=s<='z':
#         abdul = chr(ord(s)-1)
#         print(abdul)

# print upper to lower nd lower to upper
# n = "PYThon"

# for i in n:
#     if "A"<=i<="Z":
#         abdul = chr(ord(i)+32)
#         print(abdul)

# for i in n:
#     if "a"<=i<="z":
#         abdul = chr(ord(i)-32)
#         print(abdul)


#  count the upper or lower values 
# count = 0
# n = "PYThon"
# for i in n:
#     if "A"<=i<="Z":
#         count+=1
# print("there are", count ,"upper values ")


n = int(input("Enter the number:"))
i = 1
fact = 1
while i<=n:
    fact=fact*i
    i = i+1
print(fact)
 
