#  Lambda functions 


example = lambda a, b, c, d : a + b - c * d

print(example(2,3,5,6 ))

example = 50 #lambda function changed to new re assignment


function1 = lambda a : a**2

function2 = lambda : "Hi Good morning"


# Higher order function 

# there are three higher order functions 
#   1.Map 2.Filter 3.Reduce

# map() → Transform each element

# filter() → Select elements by condition

# reduce() → Combine all elements into one value


# map -  Transform each element

# map(function,iterable)

def square(x):
    return x**2

print(list(range(1,9)))

print(list(map(square,[3,4,6,7,11,-32])))


# Balayya's code 

print(list(map(lambda x :x**3,[3,4,6,7,11,-32])))


# Filter - Select elements by condition

# filter(function,iterable)


print(list(filter(lambda x:x%2==0,[1,3,5,8,9,10,15,17])))

print(list(filter(lambda x:x>7,[1,3,5,8,9,10,15,17])))

print(list(filter(lambda x:x%5==0 or x%3==0,[1,3,5,8,9,10,15,17])))


# reduce - Combine all elements into one value

from functools import reduce

print(reduce(lambda x,y :x+y,[1,2,5,7,11,-10]))

print(reduce(lambda x,y :x*y,[1,2,5,7,11,-10]))

list1 = ['string1','string2','string3']
print(reduce(lambda x,y :x+y,list1))

print(reduce(lambda x,y :x if x>y else y,[1,2,5,7,11,-10]))

print(reduce(lambda x,y :x if x<y else y,[1,2,5,7,11,-10]))


def check_even_odd(x):
    if x%2==0:
        return True
    return False

print(check_even_odd(10))





