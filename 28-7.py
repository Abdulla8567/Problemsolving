# #class 1 roll 1
# #class 1 roll 2
# #class 1 roll 3
# #class 1 roll 4

# count=0
# for class_no in range(1,11):
#     for roll_no in range(1,31):
#         count +=1
#         print("Class ",class_no,'roll',roll_no)
# print(count)


# #  print 1 to 20 tables using nested loop
# for i in range(1,21):
#     for s in range(1,21):
#        print(i,'X',s,'=',i*s)


#  only to print even class numbers 
# for class_no in range(1,11):
#    if class_no%2==0:
#       for roll_no in range(1,31):
#          print("class",class_no,"roll",roll_no)

# for class_no in range(1,11):
#    for roll_no in range(1,31):
#       if class_no %3==0 and roll_no%7==0:
#          print("class",class_no,"roll",roll_no)

for class_no in range(1,11):
    roll_no = 1
    while roll_no<31:
        print("class",class_no,"roll",roll_no)
        roll_no+=1



