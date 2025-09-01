# Functions - scopes 
# Python uses the LEGB rule to determine variable scope
# Local scope - inside the current function
# Enclosed scope - variables from any outer function
# Global scope - variables defined at the top level of the module
# Built-in scope -names from Python’s built-in scope (like len, print)

 

#  local scope - inside the current function

def first_function():
    temp = "Good morning"

    def second_function():
        print("output is Nested function")
    second_function()

    print(temp)

first_function()


#Enclosed scope -variables from any outer function

def abdulla():

    new = "Good evening"

    def kiran():
        new = "Good afternoon" 
        print(new)
    
    kiran()

    print(new)

abdulla()


# Built-in scope -names from Python’s built-in scope (like len, print)

print(len("Hi"))

# local and global shadowing differences 

num1 = 25

def test_function():

    num1 = 40
    print(num1) #Local function

test_function()

print(num1) #Global function






