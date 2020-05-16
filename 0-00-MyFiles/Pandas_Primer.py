import pandas as pd
import numpy as np
file = 'F:\\PythonCodes-PlotlyDash\\Plotly-Dashboards-with-Dash\\0-02-Pandas-Crash-Course\\salaries.csv'
df = pd.read_csv(file)
print(df)
print(df['Salary'])
print(df[['Name', 'Salary']])
print(df['Salary'].min())
print(df['Salary'].mean())
ser_of_bool = df['Age'] > 30
print(ser_of_bool)
print(df[ser_of_bool])
print(df['Age'].unique())
print(df['Age'].nunique())
print(df.columns)
print(df.info())
print(df.describe())
print(df.index)

mat = np.arange(0, 50).reshape(5, 10)
print(mat)
df = pd.DataFrame(mat)
print(df)

mat = np.arange(0, 10).reshape(5, 2)
print(mat)
df = pd.DataFrame(mat, columns=["A", "B"])
print(df)
