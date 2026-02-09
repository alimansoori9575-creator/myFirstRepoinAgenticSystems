###         Part 2 – Add Two Numbers          ###

# code without input

def add(a, b):
    sum = a + b
    return sum

total = add(3, 5)
print(total)

# code with input

def add(a, b):
    sum = a + b
    return sum
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
total = add(a, b)
print(f"The sum of {a} and {b} is: {total}")