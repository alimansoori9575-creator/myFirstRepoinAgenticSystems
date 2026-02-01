###         Access Control System          ###

# First program with input function

age = int(input("Enter your age: "))
has_id = bool(input("Do you have ID? (True / False): "))
if age >= 18 and has_id:
    print("Entery allowed")
else:
    print("Entry Denied")

# Second program without input function

age = 20
has_id = True
if age >= 18 and has_id:
    print("Entery allowed")
else:
    print("Entry Denied")   
