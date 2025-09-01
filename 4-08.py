#keyword arbitrary arguments

# def connect_to_db(**kargs):
#     print(kargs)
#     print(type(kargs))

# connect_to_db(db_location='localhost:3300',db_pool=234,db_password='2345',db_port='3366')


#Return statement

# def add(num1,num2):
#     print(num1+num2)

# def add2(num1,num2):
#     return num1 + num2

# add(1,2)

# result = add2(4,5)
# print(result)

# def multiply(a,b):
#     print(a*b)
#     return a*b

# r1 = multiply(2,5)
# print(r1)


# 
def check_ur_knowledgee(num1):
    for i in range(1,num1):
        print(i)
        if i==9:
            return 
    return 55

print(check_ur_knowledgee(22))
