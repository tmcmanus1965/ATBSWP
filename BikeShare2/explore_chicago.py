import pandas as pd

df = pd.read_csv("chicago.csv")
print(df.head(5))  # start by viewing the first few rows of the dataset!
print(df.columns)
print(df.describe())
print(df.info())
# print(df['column_name'].value_counts())
#print(df['User Type'].value_counts())
# print(df['column_name'].unique())
#print(df['Start Station'].unique())

