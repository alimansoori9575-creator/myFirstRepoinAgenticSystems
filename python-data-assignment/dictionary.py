###     Part 2: Simple Contact Book (Dictionary)     ###
contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Alice": "9846820456"
}
print(contacts)
name = input("Enter a name: ")
if name in contacts:
    print(contacts[name])
else:
    print("Contact not found")

  

