import pandas as pd

df = pd.read_csv(r"C:\Users\91917\Desktop\Module_1\myFirstRepoinAgenticSystems\python data assignment_pandas\employee2.csv")
head = df.head()
tail = df.tail()
info = df.info()
desc = df.describe()
age = df['Age']
name_and_salary = df[['Name', 'Salary']]
filter = df[df['Salary'] > 40000]

print("First 5 raws are:\n", head)
print("Last 5 raws are;\n", tail)
print("Dataset Info:\n", info)
print("Dataset Description:\n", desc)
print("Age column:\n", age)
print("Name and Salary columns:\n", name_and_salary)
print("Filtered rows based on a numerical condition(Salary > 40000):\n", filter)

