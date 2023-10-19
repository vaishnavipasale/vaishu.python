Write a program to remove duplicates from a list.
xyz = [10, 10 , 45 , 54 , 20 , 12, 23, 1 , 1 , 2 , 2,]
abc = []
print(f"list before remove duplicates elements: {xyz}")
for data in xyz:
    if data not in abc:
        abc.append(data)
print(f" list after removing duplicates elements :{abc}")
