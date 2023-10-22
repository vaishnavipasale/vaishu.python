Convert a list of tuples into a dictionary.
tups = [("sakshi", 10), ("swara", 12), ("sneha", 14),
        ("jay", 20), ("harsh", 25), ("vaishnavi", 30), ("Avir" , 45)]
dictionary = {}
for key, val in tups:
    dictionary.setdefault(key, val)
print(dictionary)
