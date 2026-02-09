###         Part 3 – Even or Odd Checker          ###

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = even_or_odd(number)
print(f"The number is {result}.")
