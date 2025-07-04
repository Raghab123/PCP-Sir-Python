# WAP to check whether a number is prime or not

num = int(input("Enter a number: "))
if (num % 2 ==0):
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')


# WAP to print all the even numbers between 1 and 100 using a loop

print("The even number are: ")
for i in range (2,100):
    if (i%2==0):
        print(i)
    else:
        continue

# WAP that reads a number and prints the factorial of that number using a while loop

num = int(input("Enter a number : "))
n = num
fact = 1

while (num>0):
    fact *= num
    # fact = fact * num 
    num -= 1

print(f'The factorial of {n} is {fact}')

# WAP to print the multiplication table of a given number using a for loop

num = int(input("Enter a number whose multiplcation number you want : "))

print(f"The multiplication number of {num} is : ")
for i in range (1,11):
    print(f"{num} * {i} = {num*i} ")

# WAP to find the largest and the smallest number in a list entered by the user

l = []
import random
for i in range (10):
    l.append(random.randint(1,100))

l.sort()
print(l)
print(f'The min value is {l[0]}')
print(f'The max value is {l[-1]}')


# WAP that accepts 10 integers from the user and counts how many are positive, negative and zero.

l = []
for i in range(10):
    entry = int(input("Enter an integer : "))
    l.append(entry)

zero = 0
positive = 0
negative = 0
for j in l:
    if (j==0):
        zero += 1
    elif (j%2>0):
        positive += 1
    else:
        negative += 1 
print(f"The total numbers of zero are {zero}")
print(f'The total number of positive integer are : {positive}')
print(f'The total number of negative integers are : {negative}')

print()
print()
print()

# WAP to generate the Fibonacci sequence upto n terms.

# Each number is the sum of the two numbers before it.

n = int(input("Enter how many Fibonacci numbers to print: "))

a, b = 0,1

for i in range (n):
    print(a, end = " ")
    temp_a = b
    temp_b = a + b

    a = temp_a
    b = temp_b


print()
print()
print()

# Write a program that reads a number and prints whether it is a palindrome or not.

n = int(input("Enter a number : "))

string = str(n)
# Converts the number into string

reversed_string = string[::-1]

if string == reversed_string:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")



# Write a program that finds all numbers between 100 and 999 where the sum of the cubes of the digits equals the number itself (Armstrong numbers).


for num in range(100, 1000):
    # Extract digits
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    # Calculate sum of cubes of digits
    sum_cubes = hundreds**3 + tens**3 + units**3
    
    # Check if Armstrong
    if num == sum_cubes:
        print(num)

# Write a menu-driven program to perform arithmetic operations (+, -, *, /) based on user choice using conditional statements.

print("=== Simple Calculator ===")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user choice
choice = int(input("Enter your choice (1-4): "))

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation based on choice
if choice == 1:
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")

