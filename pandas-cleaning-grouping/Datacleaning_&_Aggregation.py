###         Question:AI-Style Employee Data Cleaning & Aggregation Pipeline         ###

import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print(df)
# Detecting missing value
print(df.isnull())

# counting missing value
print(df.isnull().sum())

# Filling missing value
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Removing unusful column
df = df.drop(columns=['Temporary_Notes'])

# Renaming Salary
df = df.rename(columns={"Salary": "Annual_Salary"})

# Groupby Department
Summary = df.groupby('Department').agg({
    "Annual_Salary": "mean",
    'Employee': "count"
})
print(Summary)
