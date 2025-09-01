
# 1.Add an integer and float. What is the result’s type?
n1 = 123
n2 = 10.0
print(n1+n2)
#output -> 133.0(float)


#2.	Create a string and access its:
#  1.	First character
#  2.	Last character
#  3.	A substring from index 2 to 5

name = "srinivaas"
print(name[0]) #s
print(name[8]) #s
print(name[2:5]) #ini
print(name[-1:4:-2]) #sa


# 3.Concatenate two strings and print the result.
n = "123"
na = "sai"
print(n+na) #123sai

#4.	Define list. What are the difference between List and Tuple.
# list -> List is a sequence and ordered elements.
#      -> list a heteroginous ,mutable elements
# diff list and tuple
# -> list is ordered,mutable
# -> tuple is ordered,immutable


#5.	Write a programme to print a list in reverse order.
list1 = [1,5,6,"sai"]
print(list1[::-1]) #['sai', 6, 5, 1]

#6.	Create a tuple of 4 elements. Print the first and last element.
tup = (1,"sai",2,3)
print(tup[0]) #1
print(tup[-1]) #3

#7.	Try changing a value in a tuple. What happens?
#tup2 = (1,2,3)
#tup2[1] = 9
#print(tup2) #TypeError: 'tuple' object does not support item assignment because tuple is immutable

#8.	Create a dictionary of 3 students with their marks. Print the dictionary.
d1 = {
    "srinu" : 800,
    "sai" : 700,
    "abdul" : 500
}

print(d1)  #{'srinu': 800, 'sai': 700, 'abdul': 500}


#9.	Access the marks of one student using their name.
print(d1["sai"])

#10.Update the marks of an existing student.
d1["sai"] = 900
print(d1)  #{'srinu': 800, 'sai': 900, 'abdul': 500}


#11.Can I access a key using a value in a dictionary.
# print(d1["srinu"]) # no we can't access


# Can I have duplicate values and keys in a dictionary? What happens if I wanted try to duplicate key in a dictionary? 
# d1 = {
#     "srinu" : 800,
#     "sai" : 700,
#     "abdul" : 500,
#     "sai" :700
# }
# print(d1)  
# we can duplicate values only we can't duplicate keys

#13.Print all multiples of 17 using range. Numbers should start from -34 and end below 400.


print(list(range(-34,400,17)))
