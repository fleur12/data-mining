# PRACTICAL 2: Data Integration and Data Transformation for Data Mining

import pandas as pd
import numpy as np

# Sample Datasets
data1 = {
   'ID': [1, 2, 3, 4],
   'Name': ['Alice', 'Bob', 'Charlie', 'David'],
   'Age': [25, 30, 35, 40]
}
data2 = {
   'ID': [3, 4, 5, 6],
   'Gender': ['F', 'M', 'M', 'F'],
   'Salary': [70000, 80000, 50000, 60000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Tight Coupling (Inner Join)
tight_coupling = pd.merge(df1, df2, on='ID', how='inner')
print("Tight Coupling Result:\n", tight_coupling)

# Loose Coupling (Outer Join)
loose_coupling = pd.merge(df1, df2, on='ID', how='outer')
print("\nLoose Coupling Result:\n", loose_coupling)

# Smoothing (Moving Average for Age)
loose_coupling['Smoothed_Age'] = loose_coupling['Age'].rolling(window=2, min_periods=1).mean()
print("\nSmoothing:\n", loose_coupling[['ID', 'Age', 'Smoothed_Age']])

# Aggregation (Salary by Gender)
aggregation = loose_coupling.groupby('Gender')['Salary'].sum().reset_index()
print("\nAggregation:\n", aggregation)

# Discretization (Age Bins)
bins = [0, 20, 30, 40, 50]
labels = ['Teen', 'Young Adult', 'Adult', 'Senior']
loose_coupling['Age_Group'] = pd.cut(loose_coupling['Age'], bins=bins, labels=labels)
print("\nDiscretization:\n", loose_coupling[['ID', 'Age', 'Age_Group']])

# Attribute Construction (Age-Salary Ratio)
loose_coupling['Age_Salary_Ratio'] = loose_coupling['Age'] / loose_coupling['Salary']
print("\nAttribute Construction:\n", loose_coupling[['ID', 'Age', 'Salary', 'Age_Salary_Ratio']])
