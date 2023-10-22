Find the common elements between the two dictionaries.

a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"c": 3, "d": 4, "e": 5, "f": 6}
 
for key in a:
    if key in b:
        print(key, end=" ")
