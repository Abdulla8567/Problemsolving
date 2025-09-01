# JUMP statements

#Break statement = instantly break the loop

# for i in range(1,100):
#     if i<=50:
#         print(i)

# for i  in range(1,100):
#     print(i)
#     if i==50:
#         break

# for i in range(9999):
#     print(i)
#     if i==8 or i>-55 :
#         break
#     print(i)
#     print(i)

# continue statement = it only skips given condition 


# for i in range(1,25):
    # print(i)
    # print(i)
    # continue
    # print(i)

# for i in range(1,25):
#     continue

# for i in range(1,32):
#     if i < i *(-1):
#         continue
#     print(i**2)

# for class_no in range(1,11):
#     if class_no==5:
#         break
#     for roll_no in range(1,11):
#         if roll_no == 5:
#             break # it will break at roll no 5 only for 2nd loop 
#         print(class_no,roll_no)

# for class_no in range(1,11):
#     if class_no==5:
#         continue
#     for roll_no in range(1,11):
#         print(class_no,roll_no)

for class_no in range(1,11):
    for roll_no in range(1,31):
        if class_no>5 or roll_no<16:
            break
            print(class_no,roll_no)  

#pass statement 



