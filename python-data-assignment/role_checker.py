###     Employee Role Checker (Tuples + Sets)    ###
employee = (101, "Alice", "IT")
roles = {'admin', 'viewer', 'editer'}

print("Employee ID:", employee[0])
print("Employee Name:", employee[1])
print("Employee Department:", employee[2])

if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")

