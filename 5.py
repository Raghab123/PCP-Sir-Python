"""
    Write a Python function that accepts a list and returns a new list containing only the elements at even indexes and those that are prime numbers.
"""

l = [2,3,4,5,6,7,8,9]
even_indices = range(0,len(l),2)
print(even_indices)

for index in even_indices:
    count = 0
    for i in range(1,l[index]+1):
        if (l[index]%i==0):
            count +=1
    if count==2:
        print(f"{l[index]} is prime")

