import pandas as pd

df = pd.read_csv('insurance.csv')

df.head()

#Classificando idade de forma generica
df["age_group"] = pd.cut(
    df["age"],
    bins=[0,29,44,64],
    labels=["18-29","30-44","45-64"]
)

df[["age","age_group"]].head()

print(df[["age","age_group"]].head())