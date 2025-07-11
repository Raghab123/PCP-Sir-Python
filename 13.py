"""
Write a program that reads a text and counts the frequency of each character (excluding spaces and special characters) using a dictionary
"""

text = input("Enter some text: ")

# Create an empty dictionary to store character frequencies
char_count = {}

for char in text:
    if char.isalpha():  # Only include alphabet letters (a-z, A-Z)
        char = char.lower()  # Optional: convert to lowercase to count 'A' and 'a' as same
        if char in char_count:
            char_count[char] += 1
            # [char] here is a key in the dictionary and not an index
        else:
            char_count[char] = 1

print("Character Frequencies:")
for char, count in char_count.items():
    print(f"{char}: {count}")

