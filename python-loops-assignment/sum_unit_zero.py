###            6: Sum Unit Zero         ###

total = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total = num + total
print("Total:", total)