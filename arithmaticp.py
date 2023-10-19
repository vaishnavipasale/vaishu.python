Calculate the nth term of an arithmetic progression
a = int(input("Enter the value of a:"))
d = int(input("Enter the difference:"))
n= int(input("Enter number of term:"))
b = 1
print("ap series as follow")
while(b<=n):
    tm = a + (b-1)*d
    print(tm)
    b = b+1
sum = ((n / 2) * (2 * a + (n - 1)*d))
print(f"sum of arethmatic progressive is {sum}")
