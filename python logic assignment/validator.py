### Secure Transaction Validator ###

# without input function

balance = 5000  
withdrawal = 3000  
verified = True

if withdrawal <= balance and verified:
    print("withdrawal successful")
else:
    print("withdrawal denied")

# with input function

balance = 5000
withdrawal = int(input("Enter withdrawal amount: "))
verified = bool(input("Is the transaction verified? (True / False): "))

if withdrawal <= balance and verified:
    print("withdrawal successful")  
else:
    print("withdrawal denied")
    