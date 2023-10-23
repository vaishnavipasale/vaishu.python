Print a pattern of stars in a diamond shape.
num_rows = 5
for i in range(1, num_rows + 1):
    for j in range(num_rows - i):
        print(" ", end="")
      for j in range(2 * i - 1):
        print("*", end="")
print()
for i in range(num_rows - 1, 0, -1):
   for j in range(num_rows - i):
        print(" ", end="")
     for j in range(2 * i - 1):
        print("*", end="")
print()

