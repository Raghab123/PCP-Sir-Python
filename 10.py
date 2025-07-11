"""
Write a Python function that accepts a sentence and returns a set of all unique vowels used.
"""

sentence = input("Enter a sentence: ")
vowels = ['a', 'e', 'i', 'o', 'u']
unique_vowels = set()

for char in sentence.lower():
    if char in vowels:
        unique_vowels.add(char)

print("Unique vowels used:", unique_vowels)
