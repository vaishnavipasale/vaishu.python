Print a pattern of stars in the shape of a right-angled triangle.

rows = int(input("please enter the row"))
for i in range (1 , rows+1):
    for j in range(1 , i+1):
        print("*" , end = "")
    print()
