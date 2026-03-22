###         Question – EDA – Iris Dataset           ###

import pandas as pd
import plotly.express as px

df = pd.read_csv('iris_flower_data.csv')
# 1. How you would inspect the dataset structure after loading it.
print(df.shape) # this shows how many rows and columns are there
print(df.columns) # this all the columns and there names

# 2. How you would check column information and missing values.
print(df.info()) # this will show all info we need to know
print(df.isnull().sum()) # This will show us if there any null values
print(df.duplicated().sum()) # This will show is there any Duplicate data

# 3. How you would analyze the distribution of one feature (for example: petal length)
fig = px.histogram(
    df,
    x="petal_length",
    title="Petal length distribution"
)
fig.show()
#  This histogram shows where most values lies and where data skewed, where extreame value exists

# 4. How you would identify possible outliers in the dataset
fig2 = px.box(
    df,
    y="petal_length",
    title="possible outliers in Petal length"
)
fig2.show()
# We will use box plots and scatter plots to identify outliers in the data. 
#           Outliers can significantly affect the performance of machine learning models, 
#           so it's important to identify and handle them appropriately.

# 5. How you would analyze relationships between variables (for example: petal length vs petal width)
corr = df.corr(numeric_only=True)
fig3 = px.imshow(
    corr,
    text_auto=True,
    title="Corelation b\w columns"
)

fig3.show()
# this will help us understand corelation b\w columns 

# 6. What insights you might discover about different species
# THe data is structured and not has missing values and don't has any perticular outliers
