Merge two dictionaries while summing values for common keys.
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {"as":12, "while":25 , "abc":9}
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)

