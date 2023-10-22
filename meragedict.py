Merge two dictionaries and handle duplicate keys by concatenating values into lists
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict3 = {**dict1, **dict2}

print(dict3)
