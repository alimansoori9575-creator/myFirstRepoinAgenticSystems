###        Question: AI Data Query and Ranking System         ###
import pandas as pd

df = pd.read_csv("students.csv")

names = df['Name']
score_and_grade = df[["Score","Category"]]
first_three_1 = df.iloc[0:3]
df.index = ['a','b','c','d','e','f','g','h']
last_three = df.loc["f":'h']
filter_1 = df[df['Score'] > 85]
filter_2 = df[(df['Score'] > 85) & (df['Passed'] == True)]
sort_1 = filter_1.sort_values('Score', ascending=False)
sort_2 = filter_2.sort_values('Score', ascending=False)

combination = (
    df[(df['Passed'] == True) & (df["Category"] == "A+")]
    .sort_values('Score', ascending=False)
    )

print("Names of all students:")
print(names)
print("\nScores and Grades of all students:")
print(score_and_grade)
print("\nFirst three students:")
print(first_three_1)
print("\nLast three students:")
print(last_three)
print("\nStudents with Score > 85:")
print(filter_1)
print("\nStudents with Score > 85 and Passed:")
print(filter_2)
print("\nStudents with Score > 85 (sorted):")
print(sort_1)
print("\nStudents with Score > 85 and Passed (sorted):")
print(sort_2)
print("\nStudents who passed and have an A+ grade (sorted):")
print(combination)  