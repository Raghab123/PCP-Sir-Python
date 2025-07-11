"""
    Create a program that reads a sentence from the user and stores each word as an element of a list. Then count the frequency of each word using only lists.
"""



sentence = "My name is Raghab Basnet. Raghab Basnet i.e. me am currently checking the validity of this code. I am Daredevil."

words = sentence.split(" ")
# List banaunxa
uniq_words = set(words)
print(uniq_words)
d = {}

for word in uniq_words:
    d[word] = words.count(word)

print(d)
