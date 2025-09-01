#operators
#operands

#Arthematic Operators -> +, -, *, /, //, **, %
#Assignment Operators -> =, +=, -=, *=
#Relational Operators -> >, <, >=, <=, !=, ==
#Logical Operators -> and, or, not
#bitwise operators -> &, |, ^, ~, <<, >>
#membership operators -> in, not in
#identity Operator ->




#Arthematic operators

#BODMAS RULE 

print(2 + 3 * 5)
print((2+3)*5)

# / , // , % = zero division error 

# a = 10
# b = 0

# if b != 0:
#     print(a / b)
# else:
#     print("Cannot divide by zero")


# num1, num2 = 10, 0
# print(num1/num2) #Zero division error 

# n1 = 10
# n2 = 0

# print(n1%n2)

#ASSIGNMENT OPERATORS 

m1 = 55
print(m1+5)
print(m1) 

database_password_corrected = 2
database_password_corrected = database_password_corrected + 1
print(database_password_corrected)

#Relational operators 

print(3>=3)

print(2 !='2')

print('abc' > 'b')

print('abc'<'abd')

# Membership operators 

print(3 in [1,2,4,5])

print(3 in [1,2,3,4,5])

print(int('3') in [1,2,3,4,5])

print('a' in  'apple')

dict1 = {
    1: '1',
    2: '2',
    3: '3',
    4: '4'
}

print(1 in dict1)

print(11 in list(range(0,10)))

print(int('3') not in [1,2,3,4,5])

print(31 in [1,2,3,4,5,[31,32]])

#logical operators - and , or ,not 

#And 


print(True and False)
print(True and True)
print(False and True)
print(False and False)

#Truthy values: All values except False, None, 0, "", [], {}, set()

#Falsy values: False, None, 0, "", [], {}, set()

print(2 and 3)
print(0 and 3)
print('' and [3])

#1st input True =>output will be same as second input
#!St input is false => o/p will be first input isself

print(2 and 2 ) 

print({2}and '')

print('abdulla' and 'hussain')

print('' and [])

#OR operator

print(True or False )

print(2 or 3)
print(3 or '')
print('' or [])
print('Truth' or 'Dare')

print(0 or 0)
print(85 or 99)

#not operator 

print(not True)
print(not False)

#bitwise operators => & , | , ^ , >> , << , 

print(5 & 7)

print(5 | 7)

print(13 | 22)

print(bin(11))#0b1011
print(oct(11))#0o
print(hex(11))#0x

print(bin(13))
print(bin(22))

#XOR OPERATOR

# | A | B | A ^ B |
# | - | - | ----- |
# | 0 | 0 | 0     |
# | 0 | 1 | 1     |
# | 1 | 0 | 1     |
# | 1 | 1 | 0     |

# 001101
# 010110
# 011011

print(int(0b011011))



