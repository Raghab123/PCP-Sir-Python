"""
Create a set of random numbers. Add more numbers until the set has 10 unique elements. Also, remove the smallest and largest element.
"""

import random
# 🔹 Create a set of random numbers
random_numbers = set()
while len(random_numbers) < 10:
    random_numbers.add(random.randint(1, 100))
print("Random numbers:", random_numbers)

# 🔹 Remove the smallest and largest elements
random_numbers.remove(min(random_numbers))
random_numbers.remove(max(random_numbers))
print(f"After removing smallest and largest: {random_numbers}")