"""
Write a program to input two sets of student roll numbers: one who play cricket and another who play football. Find:
a. Students who play both sports
b. Students who play only one sport
c. Students who play neither (given a master list of all students)
"""

"""
🧠 Set operations used:
Operation	            Symbol	                Meaning
Intersection	        &	                    Common in both sets
Union	                |	                    All elements in either set
Symmetric difference	^	                    Elements in only one set
Difference	            -	                    Elements in A but not in B
"""


# 🔹 Input master list
master = set(input("Enter all student roll numbers (space-separated): ").split())

# 🔹 Input sports sets
cricket = set(input("Enter roll numbers of students who play cricket: ").split())
football = set(input("Enter roll numbers of students who play football: ").split())

# a. Students who play both sports (intersection)
both = cricket & football
print("\n(a) Students who play both cricket and football:", both)

# b. Students who play only one sport (symmetric difference)
only_one = cricket ^ football
print("(b) Students who play only one sport:", only_one)

# c. Students who play neither (master - (cricket U football))
neither = master - (cricket | football)
print("(c) Students who play neither sport:", neither)

