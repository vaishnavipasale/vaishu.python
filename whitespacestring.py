.Remove all whitespace from a string.
sample= "  This  is  a Sample String   "

sample = ''.join(sample.split())
print(f" {sample}")
