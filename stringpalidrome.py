.Check if a string is a palindrome.
def isPalindrome(string):
    if string==string[::-1]:
        print("Yes")
    else:
        print("No")

s1 = input("Enter the string")
print(s1,":",isPalindrome(s1))
