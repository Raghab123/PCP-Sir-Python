

# Q2: Merge lists and remove common elements 

# Without library function
import random
l1 = []
l2 = []
l = []
for i in range (10):
    l1.append(random.randint(1,100))
    l2.append(random.randint(1,100))

merge = l1+l2

for i in merge:
    if i not in l1 or i not in l2:
        l.append(i)

print(f'The merged list is {l}')


# With library function
l1 = set(l1)
l2 = set(l2)
merge = l1.union(l2)
print(f"The merged list is {list(merge)}")

common = l1.intersection(l2)
print(common)
print(f'The common list is {list}')
print(f'The merged list without common is {list(merge-common)}')