###         3: Score Evaluation Pipeline         ###

scores = [72, 45, 89, 30, 60]

# loop using continue 

for score in scores:
    if score < 50:
        print("Fail")
        continue            
    print("Pass")


print("----------------------------------------------------")

# loop without continue (i prefer this way)

for score in scores:
    if score >= 50:
        print("Pass")
    else:
        print("Fail")