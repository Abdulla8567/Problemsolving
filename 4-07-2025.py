# 3.Given text = 'hello', what is text[0]? 
# a.What will be the output of text[4]? 
# b.What does text[-1] give?

text = 'hello'
print(text[0])
#output : h
print(text[4])
#output : o
print(text[-1])
#output : 0

#4.If name = 'Ajay', what is the value of name[0] + name[3]? 
    # What happens if you try name[10]?
    # output  = error message : string index out of range 

name = 'Ajay'
value = name[0] + name[3]
print(value)
#output : Ay

#  5.Given s = 'Python', what is s[0:2]? 
 # a.What does s[5:1] return?
# 6.Predict the output for string s =  'Python' . If the code is print(s[2: -1 :2])
s = 'Python'
print(s[0:2])
#output : Py
print(s[5:1])
# output : empty space as output 
print(s[2:-1:2])
# out put : to beacuse it starts from 2 nd add +2 so its 4 so ythe valuer is "0" nd end up the at -1

# 7. Write code to print the last 3 letters of 'elephant'.

letter = 'elephant'
print(letter[5:])
#output : ant

# 8.How to get only the middle 3 letters from 'Science'?

letter2 = 'Science'
print(letter2[2:5])
# output = ien

