Check if a list is a subset of another list
list1 = [9, 4, 5, 8, 10]
list2 = [10, 5, 4]
print(f"Original list : {list}")
print(f"Original sub list : {list2}")
flag = 0
if(all(x in list1 for x in list2)):
    flag = 1
    if (flag):
        print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")

