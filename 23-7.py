# to extract the values

s = {10,20,30,10,90}
for n in s:
    print(n)

# to print dict keys and values

n1 = {
    1 :"abdul",
    2 : "kiran",
    3 : "basheer",
    "subject":"python"
}

for key in n1:
    print(key,n1[key])
for key in n1.items():
    print(key)

# reverse a string 
s = "string"
for n1 in s[::-1]:
    print(n1,end=",")

count = 0  
for i in s:
    count=count+1
print(count)

# count vowels 

variable1 = "AbdullaBasheerKiran"
count=0
for i in variable1:
    if i in "a,e,i,o,u,A,E,I,O,U":
        count=count+1
    if i in "a,e,i,o,u":
        print(i)
print(count)

# even numbers  and numbers print and count 

list1 = [22,44,77,88,99,58,38]
even_count = 0
odd_count=0
for i in list1:
    if i%2 == 0:
        even_count+=1
        print(i, "is even")
    elif i%2!=0:
        odd_count+=1
        print(i,"is odd")
print(even_count," is even")
print(odd_count," is odd")

# upper character or lower without inbuilt functions 


s1 = 'A'

for i in s1:
    if 'A'<=i<='Z':
        print('it is uppercase')
    else:
        print("it is lower case")

print(ord(s1))
print(chr(122))

#  ascii values = american standard code international information 
#  
# "A" TO "Z"  => 65 TO 90
# "a" ro "z"  => 97 to 122
# 0 to 9 => 48 to 57 
#0-47 ,58 to 64,91 to 96,123-127 = special characters 

#  Methods 

# ord(),char()

# print(ord("B"))
#print(char(122))

