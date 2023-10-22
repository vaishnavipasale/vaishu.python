Find the length of the longest word in a list of words.
def longestLength(words):
    res=max(words,key=len)
    print("The word with the longest length is:", res,  " and length is ", len(res))
list1 = ["swara" , "sakshi", "sneha" , "vaishnavi"]
print(longestLength(list1))
