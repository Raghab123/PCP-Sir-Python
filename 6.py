"""
    6. Write a program to create a tuple of n numbers, then find:
    a. The average of the numbers
    b. The median
    c. The mode (without using libraries)
"""


l = (2, 3, 4, 5, 6, 7, 8, 9, 9 , 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# Finding average
average = sum(l)/len(l)
print(f"Average: {average:.2f}")

# Finding median:
sorted_list = sorted(l)
n = len(sorted_list)

if n % 2 == 0:
    median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
else:
    median = sorted_list[n//2]
print(f"Median: {median}")

# Finding mode:
mode_count = {}
for number in l:
    if number in mode_count:
        mode_count[number] += 1
    else:
        mode_count[number] = 1

print(mode_count)

max_count = 0
for num, count in mode_count.items():
    if count > max_count:
        max_count = count
        mode = num

print(f"Mode: {mode}")
