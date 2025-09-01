# def check_prime(num4):
#     if num4<=1:
#         return "Not a prime number"
    
#     for i in range(2,int(num4**0.5)+1):
#         if num4%i==0:
#             return "Not a prime number"
        
#     return "Prime number"

# print(check_prime(3))


# square , cube , exit 

while True:
    square_cube_exit = ["square","cube"]
    print(square_cube_exit)
    n = input("choose the option:")
    if n in square_cube_exit:
        a=int(input("Enter the number"))

        if n=="square":
            print(a**2)
        elif n=="cube":
            print(a**3)

    else:
        print("Exit")
        break
   
        