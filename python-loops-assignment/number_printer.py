###         1: Number Printer           ###

# first way to do it

for i in range(0, int(input("Enter a number: ")) + 1):
    print(i)

# second way to do it

num = int(input("Enter a number: "))   
for i in range(num + 1):
    print(i)