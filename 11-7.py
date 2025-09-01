#From int to all type conversions
n1 = 123
print(int(n1))  #123


n2 = 123
print(float(n2))  #123.0


n3 = 123
print(str(n3)+"sai")  #123sai


n = 123
print(bool(n))  #True


#From float to all conversions
n4 = 10.5
print(int(n4))  #10


n5 = 10.5
print(float(n5))  #10.5


n6 = 10.5
print(str(n6))  #10.5


n7 = 10.5
print(bool(n7))  #true


# from str to all types
nam1 = "123"
print(int(nam1))  #123 #if numeric 



nam2 = "123"
print(float(nam2))  #123.0


nam3 = "sai"
print(str(nam3))  #sai


nam4 = "sai"
print(bool(nam4))  #True


# from bool to all types


b1 = True
print(int(b1))  #(True=1, False=0)


b2 = True
print(float(b2)) #1.0


b3 = True
print(str(b3)) #True


b4 = True
print(bool(b4))  #True

#covert positive int to binary
bin(13)        # Output: '0b1101'
format(13, 'b')  # Output: '1101' (without '0b')


#convert binary to positive int


#manual method
#1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13


#python method
int('1101', 2)   # Output: 13