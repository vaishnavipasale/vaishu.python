.Check if a number is a perfect number.
n = 28
sum = 0
for i in range (1 , n):
    if n % i == 0:
        sum = sum + i
        print(sum)
if sum == n:
    print("The number is a perfect number")
else:
    print("The number is a not perfect number")
