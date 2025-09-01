cmp1 = 2+3j
cmp2 = -4j
print(cmp1 + cmp2) # floor division // nd modulo % are not supported operands 

#list topic  =  ordered and hetrogenous elements nd Mutuable 

list1 = [1,2,4,5.5,'str1',[1,55,72,[99]],3+4j,[5,6]]
print(list1)
print(len(list1))
print(list1[-2])
print(list1[5][2])
print(list1[-3][-1])
print(list1[-3][-1][0])
print(list1[5:7])
print(list1[::-1])
print(list1[99:222])
list1[3] = 7.51
print(list1)

#Tuple topic = ordered  nd hetrogenous nd Immutable 

tup1 = (1,2,3,5,1,7.6,'string1')
tup1 = (5,6,7,8)

# String = sequence of characters enclosed with quotes 

# range topic 

print(range(0,10))
print(list(range(0,10))) # using conversion we can change one to another data type 
print(list(range(10,10)))
print(list(range(10,0)))
print(list(range(10,0,-1)))
print(list(range(10,0,-2)))

# odd number first 25 

print(list(range(1,51,2)))

# even numbers first 25 number
print(list(range(0,51,2)))

#13 table 

print(list(range(13,200,13)))

# 3 nd 5 mutliple to 300

print(list(range(15,300,15)))

#dic =>  dictionary is collection of keys nd value pairs  nd mutuable nd ordered

dict1 = {}
set1 = {}
print(type(dict1))
print(type(set1))

dict2 = {
    1 : "Mahesh Babu",
    2 : '',
    3 : 'Dhanush',
    '4': 'Rajendra Prasad',
    5 :'Mohan babu',
    6 : 'Surya',
'7': 'Surya',
    2 : 'Sradha kapoor'
}
print(dict2[3])
#print(dict2['Surya'])key error
#print(dict2['3'])key error 

