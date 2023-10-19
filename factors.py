.Find the prime factors of a number
def factors(x):
    print("the factores of" , x )
    for i in range (1, x+1):
        if x % i ==0:
            print(i)
num = 14
factors(num)
