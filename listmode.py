find the mode of list.
C = [10, 30, "Hello", 30, 10, "Hello", 30, 10]
print("Mode of List C is % s" % (max(set(C), key=C.count)))
