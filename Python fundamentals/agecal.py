###     Section 1: user age Calculater      ###

# First way to calculate age
birth_year = int(input("Enter your birth year: "))
current_year = 2026 
age = current_year - birth_year
print("your age is", age)

# Second way to calculate age
birth_year = input("Enter your birth year: ")
current_year = input("Enter the current year: ")
age = int(current_year) - int(birth_year)
print("you are", age, "years old")
print(f"you are {age} years old")