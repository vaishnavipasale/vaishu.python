Write a program to check if a number is a palindrome
num = int (input("Enter a number"))
rev = 0
temp= num
while temp>0:
    rem = temp%10
    rev = rem +(rev*10)
    temp = int(temp/10)
if rev == num:
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")
