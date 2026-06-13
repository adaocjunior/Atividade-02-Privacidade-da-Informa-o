import pandas as pd
import numpy as np

df = pd.read_csv('insurance.csv')

df.head()

#Generalização de idade
df["age_group"] = pd.cut(
    df["age"],
    bins=[0,29,44,64],
    labels=["18-29","30-44","45-64"]
)

df[["age","age_group"]].head()

#Generalização de BMI
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

#Generalização de Região
mapa = {
    "northeast":"Norte",
    "northwest":"Norte",
    "southeast":"Sul",
    "southwest":"Sul"
}

df["region_group"] = df["region"].map(mapa)

df[["region","region_group"]].head()

#Avaliação de risco
df.groupby(
    ["sex","age_group","smoker"]
).size()

#Perturbação dos Charges
np.random.seed(42)

noise = np.random.laplace(
    loc=0,
    scale=500,
    size=len(df)
)

df["charges_noise"] = df["charges"] + noise

df[["charges","charges_noise"]].head()

#Comparação das estatisticas
print("Média Original")
print(df["charges"].mean())

print("Desvio Original")
print(df["charges"].std())

print("Média Anonimizada")
print(df["charges_noise"].mean())

print("Desvio Anonimizado")
print(df["charges_noise"].std())