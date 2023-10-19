Print even numbers from 1 to N using a for loop.
n = int (input("Enter value of n"))
for i in range (0,n+1):
    if i%2==0:
        print(i)
