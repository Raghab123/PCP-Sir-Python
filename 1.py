import math

# DSA & Python Exam Practice Code (Q1 - Q14)


# -----------------------------
# Q1: List operations (manual way)
# -----------------------------
n = int(input("Enter how many numbers: "))
numbers = []
print("Enter the numbers:")
for i in range(n):
    num = int(input())
    numbers.append(num)

# a. Max and Min (without using built in functions)
max_num = numbers[0]
min_num = numbers[0]
for i in range(1, n):
    if numbers[i] > max_num:
        max_num = numbers[i]
    if numbers[i] < min_num:
        min_num = numbers[i]
print("Maximum:", max_num)
print("Minimum:", min_num)


# Max and min using built in function:
max_num = max(numbers)
min_num = min(numbers)

# b. Sort (ascending)
for i in range(n):
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Sorted list:", numbers)

# Using built in function:
numbers.sort()
print(f"The sorted number using built in function is : {numbers}")
# numbers.sort() doesn't return anything, it sorts the list in place. So we have to print the list after sorting.


# c. Remove duplicates

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f'The list without duplicates without using built in function is {unique_numbers}')

# Using built in functions:
l = set(numbers)
print(f'The list without duplicates is {list(l)}')
# -----------------------------

