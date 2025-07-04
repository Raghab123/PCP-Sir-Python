import random

# Create a list of lottery numbers
lottery_numbers = list(range(1, 11))  # Numbers 1 to 10

print("Welcome to the Simple Lottery Game!")
print(f"Lottery numbers: {lottery_numbers}\n")

# Without replacement version
print("1. Without Replacement (unique numbers):")
drawn_without = random.sample(lottery_numbers, 3)  # Draw 3 unique numbers
print(f"Drawn numbers: {drawn_without}")
print(f"Your prize: ${sum(drawn_without)}\n")

# With replacement version
print("2. With Replacement (possible duplicates):")
drawn_with = [random.choice(lottery_numbers) for _ in range(3)]  # Draw 3 numbers (could repeat)
print(f"Drawn numbers: {drawn_with}")
print(f"Your prize: ${sum(drawn_with)}")