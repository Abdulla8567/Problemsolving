#loops = for,while
# Adavantages of loops => Time efficiency or space,file size,maintainability

#iterable - list,tuple,dictionary,set,string,range

for i in range(0,11):
    # print('Hi')
    # print('Hello')
    # print('Good morning')
    print(i)
#for even
for i in range(2,11,2):
    print(i)
#another method
for i in range(0,11):
    if i%2==0:
        print('even',i)
#for odd
for i in range(1,11,2):
    print(i)

#list

list1 = [1,55,99,88,66]
for i in list1:
    print(i)

#tuple 

tuple1  = (1,99,77,33,88)
for i in tuple1:
    print(i)

#dictionary

my_dict = {
    "name:" : "Abdul",
    "age:": 21,
    "place:":"India"
}

for key in my_dict:
    print(key,my_dict[key])

#string 

str1 = "Abdul"
for i in str1:
    print(i)

#set

set1 = {1,8,9,6,6888}

for i in set1:
    print(i)


for i in range(1,100):
    if (i>=40 and i<50) or (i>=70 and i<80):
        print(i)

# n=int(input("Enter number"))
# for i in range(1,21):
#     print(n,"X",i,'=',n*i)
n1=int(input("Enter number"))
for i in range(0,340):
    if i in range(1,21):
        print(n1,"X",i,"=",i*n1)