.Combine two dictionaries, preserving the original keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5}


dict1.update(dict2)


print(dict1)
