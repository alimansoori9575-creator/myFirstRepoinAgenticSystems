###       Part 4 – Modular Student Evaluation System        ###

def greeting():
    name = input("Enter your name: ")
    return "Hello, " + name + "!"

def subjects():
    no_of_subjects = int(input("Enter the number of subjects: "))
    return no_of_subjects

def grades(count):
    marks = []
    for i in range(count):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    return marks

def average_score(marks):
    return sum(marks) / len(marks)
    
def main():
    print(greeting())
    count = subjects()
    marks = grades(count)
    print("Subjects:", len(marks))
    print("Total Marks:", sum(marks))
    print("Average Score:", average_score(marks))
    print("Result:", "Pass" if average_score(marks) >= 50 else "Fail")

main()