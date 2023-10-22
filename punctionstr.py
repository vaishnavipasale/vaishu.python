Remove all punctuation from a string.

test = "Gfg, is best : for ! Geeks ;"
 

print(f"The original string is : {test}")
 

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 

for ele in test:
    if ele in punc:
        test = test.replace(ele, "")
 

print(f"The string after punctuation filter : {test}")
