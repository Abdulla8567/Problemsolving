# 1.What is a data type in Python?

# Data : Data is collection of information

# Datatype : structure in which your data is organized (or)
             # A data type in Python defines the type of value a variable can hold and what operations can be performed on it.

# 2. List all the data types that we have in Python?

# Data Type	 Example	               Description

# int	     10	                   Whole numbers
# float	     10.5	               Decimal numbers
# complex	 3 + 4j	               Complex numbers (real + imaginary)
# str	     "Hello"	           Text(string)
# bool	     True, False	       Boolean values
# list	     [1, 2, 3]	           Ordered, changeable collection
# tuple	     (1, 2, 3)	           Ordered, unchangeable collection
#range 
# dict	     {"a": 1}	           Key-value pairs
# set	     {1, 2, 3}	           Unordered collection with no duplicates

# 3. What is the difference between mutable and immutable data types?

# 🔹 Mutable Data Type:
# A mutable data type is a type whose values can be changed after the object is created without changing its identity (memory address).

# Example types :	list, dict, set, bytearray

my_list = [1, 2, 3]
my_list[0] = 99
print(my_list)   # Output: [99, 2, 3]

# 🔹 Immutable Data Type:
# An immutable data type is a type whose values cannot be changed after the object is created. Any modification creates a new object.

# Example types	: int, float, str, tuple, bool, complex

my_str = "hello"
my_str = my_str + " world"
print(my_str)   # Output: "hello world"

# 4.What is the difference between int, float, and complex?

# | Feature        | `int`           | `float`               | `complex`                             |
# | -------------- | --------------- | --------------------- | ------------------------------------- |
# | **Definition** | Whole numbers   | Decimal numbers       | Numbers with real and imaginary parts |
# | **Syntax**     | `x = 5`         | `x = 5.0`             | `x = 5 + 2j`                          |
# | **Contains**   | Only real part  | Only real part        | Real + Imaginary parts                |
# | **Example**    | `10`, `-3`, `0` | `3.14`, `-2.5`, `0.0` | `2 + 3j`, `-1 - 4j`                   |
# | **Data type**  | `int`           | `float`               | `complex`                             |


# 5. Which data type is used to represent text in Python?

# The data type used to represent text in Python is the    str (string) type. 

message = "Hello, world!"
print(type(message))  # Output: <class 'str'>

# 6.What is the output of type(521) and type("521")?
print(type(521))
print(type("521"))

# 7.What is the difference between list, tuple, and set?

#         List

# List = Ordered collection of hetregenous elements .

# Mutuable (can change, add, or remove elements)

# Allow duplicates 

# Supports indexing and slicing 

# Example: [1, 2, 2, 3]

#        Tuple

# Ordered collection of items

# Immutable (cannot change elements once created)

# Allows duplicates

# Supports indexing and slicing

# Example: (1, 2, 2, 3)

#         Set

# Unordered collection of items

# Mutable (can add or remove elements)

# Does not allow duplicates (automatically removes duplicates)

# Does not support indexing or slicing

# Useful for membership testing and unique elements

# Example: {1, 2, 2, 3} stored as {1, 2, 3}


# 8.How is a dictionary different from a list?

# A dictionary is a collection of key-value pairs, while a list is an ordered collection of values indexed by position.

# 9. What is the default data type of a number with a decimal point?

# Any number written with a decimal point is treated as a floating-point number by default

# 10.Declare variables of type int, float, string, and complex.

a = 10
b = 21.1
c = 2+3j
d = "abdul"
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 11.Take any 3 datatypes examples and check type of each variable using the type() function.

abdul = [1,2,3,9,5]
kiran = (3,2,5,8,7)
mahesh = { 1 : "hari",2 : "sameer",3 : "prasad"}

print(type(abdul))
print(type(kiran))
print(type(mahesh))

# 13. What is the output of:
#     1.x = [1, 2, 3]
#     2.y = (1, 2, 3)
#     3.z = {1, 2, 3}


x = [1, 2, 3]
y = (1, 2, 3)
z = {1, 2, 3}
print(x)
print(y)
print(z)
print(type(x), type(y), type(z))


# 14.Can you change a value in a tuple once it is defined? Why or why not?

# No, you cannot change a value in a tuple once it is defined because a tuple is immutable in Python. This means that after creating a tuple, its elements cannot be modified, added, or removed. Any attempt to change a tuple’s content will raise a TypeError.

# 15.Is reassignment possible for immutable datatypes?

# Explanation:
# Immutable data types (like int, float, str, tuple) cannot have their content changed after creation.

# But you can reassign a variable to a new object/value of the same or different type.

x = 5           # x points to an integer object 5
x = 10          # x now points to a new integer object 10 (reassignment)

y = "hello"
y = "world"     # y points to a new string object "world"



