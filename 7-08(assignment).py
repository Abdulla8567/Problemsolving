
while True:
    simple_calc = ["+","-","*","/"]
    print(simple_calc)
    print("Pick the symbol")
    n= input("Enter the symbol: ")
    if n in simple_calc:
        a= int(input("Enter the number: "))
        b= int(input("Enter the number: "))
        if n == "+":
            print(a+b)
        elif n=="-":
            print(a-b)
        elif n=="*":
            print(a*b)
        elif n=="/":
            print("Division is not possible") if b==0 else print(a/b)
    else:
        print("Not a valid symbol")
        break

