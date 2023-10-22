.Find the first non-repeated character in a string.
str = "PREPINSTA"
flag = 0
for i in range(1):
    flag = 0
    for j in range(1):
        if str[i] == str[j] and i != j:
            flag = 1
            break
    if flag == 0:
        print(f"First non-repeating character is : {str}")
        break

if flag == 1:
    print("No non-repeating character")
