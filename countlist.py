Count the occurrences of each word in a list of sentences
from collections import Counter

words = ['hello', 'goodbye', 'howdy', 'hello', 'hello', 'hi', 'bye']

word_counts = Counter(words)

print(f'"hello" appears {word_counts["hello"]} ')
print(f'"howdy" appears {word_counts["howdy"]}')
