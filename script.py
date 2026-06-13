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

#Generalizando BMI
df["bmi_group"] = pd.cut(
    df["bmi"],
    bins=[0,18.5,25,30,100],
    labels=[
        "Baixo Peso",
        "Normal",
        "Sobrepeso",
        "Obesidade"
    ]
)

df[["bmi","bmi_group"]].head()

print(df[["bmi","bmi_group"]].head())