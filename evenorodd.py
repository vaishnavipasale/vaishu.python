Calculate the sum of all even numbers between 1 and N.
n = int (input("Enter a numbers"))
sum=0
print(n)
for i in range (0,n+1):
    if i%2==0:
        print(f"even number is {i}")
        sum=sum+i
print(f"sum of n number is {sum}")
