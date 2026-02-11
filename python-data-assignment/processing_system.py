###     Part 4: User Data Processing System     ###
users = [
    {"name": "Alice", "scores" : [80, 85, 82, 87], "roles" : {"admin", "editor"}},
    {"name": "Bob", "scores" : [79, 67, 90, 84], "roles" : {"visiter", "editor"}},
    {"name": "Jack", "scores" : [64, 83, 94, 87], "roles" : {"editor"}}
    ]

def avg(scores):
    total = 0
    count = 0
    for score in scores:
        total = total + score
        count = count + 1
    average = total/count
    return average

def has_access(roles):
    if "admin" in roles:
        return True
    else:
        return False
    
def main():
    for user in users:
        name = user["name"]
        scores = user['scores']
        roles = user['roles']

        avg_score = avg(scores)
        admin_access = has_access(roles) 

        print("Name:", name)
        print("Average score:", avg_score)
        print("Admin access:", admin_access)

main()
