Calculate the LCM and GCD of two numbers
num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
tnum1 = num1
tnum2 = num2
while num1 % num2 !=0:
    r = num1 % num2
    num1= num2
    num2= r
gcd = num2
print(f"gcd is {gcd}")
lcm = (tnum1 * tnum2)// gcd
print(f"lcm is {lcm}"
