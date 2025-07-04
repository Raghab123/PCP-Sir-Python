# Write a python program to remove all duplicates from a list and print the unique elements.

l = ['a','a','a','b','c','d','d','e','e','f']
print(l)
k = set(l)
# set le duplicate values lai remove garxa
print(k)
m = print(list(k))


# second method

uniq = []
for i in l:
    if i not in uniq:
        uniq.append(i)

print(uniq)

# Count method:

unique = []

for i in l:
    if (unique.count(i)!=1):
        unique.append(i)

print(unique)


# Create a tuple of 10 integers. WAP to display the maximum and minimum numbers from the tuple.


l = []
import random
for i in range (10):
    l.append(random.randint(1,100))

print(l)

t = tuple(l)
print(f'Max value is: {max(t)}')
print(f'Min value is : {min(t)}')


l.sort()
print(l[-1])
print(l[0])


l.sort(reverse = True)
print(l[0])
print(l[-1])



# 3. Create a new list with only even numbers from the list

# l = list(range(20))
# print(l)


# l = []

# for i in range(10):
#     x = int(input("Number: "))
#     l.append(x)

# even_list=[]

# for i in l: 
#     if (i%2==0):
#         even_list.append(i)
    
# print(even_list)

# 4. Wap to count each string in a dictionary ish

s = input("Enter a sample string: ")

d = {}

for i in s:
    if i not in d.keys():
        d[i] = s.count(i)


# if i not in d.values(): le tesko index 
print(d)

# method 2

s = "abdlkajsflk;ajsd;fajkfka"

u_s = set(s)

d = {}

for i in u_s:
    d[i]= s.count(i)
print(d)


# Create a set of prime numbers less than 50. Write a program to check whether a given number exists in the set or not.

prime = []

for num in range (1,51):
    count = 0
    for i in range (1,num+1):
        if (num%i == 0):
            count +=1
        if (count == 2):
            prime.append(num)

# Prime number is divisible by 1 and itself only so count 2. Count needs to be reset after each iteration so count = 0

"""Given two lists, write a program to find their intersection using sets."""


l1 = set([10,20,30,40])

l2 = set([80,90,10,20,100])

print(l1 | l2)
print(l1 & l2)

"""Write a Python program to merge two dictionaries and sum the values of common keys."""

l1 = set([10,20,30,40,50])
l2 =  set([80,90,100,50,40])

print(l1|l2)

d1 = {'a':10,'b':20,'c':30}
d2 = {'a':20,'b':30,'d':40,'e':50}

for k,v in d1.items():
    if k in d2.keys():
        d2[k] = d2[k]+v
    else:
        d2[k]=  v
        
print(d2)


"""Given a list of names, write a program to count how many times each name
appears using a dictionary."""

names = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'd']

d = {}

for name in names:
    if name not in d.keys():
        d[name] = names.count(name)

print(d)


"""Write a Python program to remove elements from a list that are also present
in another list."""

l1 = set([10,20,30,40])
l2 = set([80,90,200,100,70])

print(l1-l2)


# Alt method

for i in l2:
    if i in l1:
        l1.remove(i)

print(l1)


""""""

prices = {}

for i in range (5):
    name = input("Enter name of fruit:")
    cost = input("Enter the price:")
    prices[name] = cost

print(prices)

name = input("Enter the fruit name to search: ")
print(prices[name])



