import pandas as pd
pd.set_option('display.max_columns', None)   # show all columns
pd.set_option('display.max_rows', None)      # show all rows
pd.set_option('display.width', None)         # no line wrapping
pd.set_option('display.max_colwidth', None)  # full content in each cell
path="dataset_eda/train.csv"
df=pd.read_csv(path)
print(df.head())
print(df.tail())
print(df.info())
print(df.columns.values)
print(df.describe())
print(df.isnull().sum())
print(f"passengers under age of 10 is {(df["Age"]<10).sum()}")
print(f"survive: {(df["Survived"]==0).sum()}")
print(df[["Pclass","Survived"]].value_counts().reset_index().sort_values("Pclass"))
print(df[["Pclass","Survived"]].groupby("Pclass").mean().reset_index().sort_values("Survived" ))


# df.drop(columns="")

# loc,apply,fillna