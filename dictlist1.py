Count the frequency of elements in a list using a dictionary.
list = ['a','b','a','c','d','c','c']
frequency = {}
for item in list:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
   print( {key, value})
