###         2: Password Retry System            ###

real_password = "admin123"
password = ""
while password != real_password:
    password = input("Enter your password: ")
    if password == real_password:
        print("Access granted.")
    else:
        print("Incorrect password. Please try again.")