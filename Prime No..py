from math import sqrt

n= int(input("Enter any number"))
flag_prime= True
if n % 2==0:
    print("Not prime")
else:
    for i in range (3,int(sqrt(n)) +1):
        if n % i==0:
            flag_prime= False
            break
    if flag_prime:
        print("It is prime")
    else:
        print("It is not prime")