"""
Create a dictionary to store student names as keys and their scores in three subjects as values (in a list). Write functions to:
a. Display the average marks of each student
b. Find the topper
c. Update the marks of a student
"""

students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 82],
    "Charlie": [92, 95, 94]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(f"{name}'s average marks: {average:.2f}")


topper = ""
highest_total = 0

for name, marks in students.items():
    total = sum(marks)
    if total > highest_total:
        highest_total = total
        topper = name

print(f"\nTopper is {topper} with total marks: {highest_total}")

name = input("Enter student name to update marks: ")
if name in students:
    print(f"Current marks for {name}: {students[name]}")
    new_marks = input("Enter 3 new marks separated by space: ").split()
    if len(new_marks) == 3:
        students[name] = [int(m) for m in new_marks]
        print(f"Marks updated for {name}.")
    else:
        print("Invalid number of marks entered.")
else:
    print("Student not found.")