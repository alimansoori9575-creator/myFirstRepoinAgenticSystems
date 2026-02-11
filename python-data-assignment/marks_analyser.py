###   Part 1: Student Marks Analyzer (Lists + Slicing)    ###

student_marks = [78, 85, 90, 65, 72,88, 92, 80]
print("The full list of student marks: ", student_marks)
First_3_marks = student_marks[0:3]
Last_3_marks = student_marks[5:8] 
print("First 3 marks: ", First_3_marks)
print("Last 3 marks: ", Last_3_marks)
print("Highest: ", max(student_marks))
print("Lowest: ", min(student_marks))
print("Average: ", sum(student_marks) / len(student_marks))