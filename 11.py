"""
Given a list of numbers with duplicates, use a set to remove the duplicates. Then, convert it back to a sorted list and display the result.
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
l = list(set(l))
l.sort()
print("Sorted list without duplicates:", l)
