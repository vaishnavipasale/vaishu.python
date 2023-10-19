Calculate the factorial of a number?
num1 = int (input("Enter a number"))
fact = 1
if num1 <0:
    print("does not find factorial of negative number")
elif num1 ==0:
    print("factorial of 0 is 1")
else:
    for i in range (1, num1+1):
        fact = fact*i
        print(f"factorial of {num1} is {fact}")
