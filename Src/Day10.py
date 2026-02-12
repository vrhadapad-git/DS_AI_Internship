#Task 1


import pandas as pd
df = pd.read_csv("sample_orders.csv")
print(df.head())
print(df.isna().sum())
print(df.fillna(0))
print( df["quantity"].fillna(df["quantity"].median()))
print(df.duplicated().sum())
print(df.drop_duplicates())

#Task 2
print(df.dtypes)
print(df["price"].astype(str))
df["price"]=df["price"].str.replace("$","" ,regex=False)
df["price"]=df["price"].astype(float)
df["date"]=pd.to_datetime(df["date"])
df.dtypes

#Task 3
print(df["product"].str.strip())
print(df["product"].str.lower())
print(df["product"].unique().sum())

