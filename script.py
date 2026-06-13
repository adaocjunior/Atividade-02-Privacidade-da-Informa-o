import pandas as pd
import numpy as np

# Carregamento do dataset
df = pd.read_csv('insurance.csv')

print("\n===== DATASET ORIGINAL =====")
print(df.head())


# ==================================================
# Generalização de idade
# ==================================================

df["age_group"] = pd.cut(
    df["age"],
    bins=[0,29,44,64],
    labels=["18-29","30-44","45-64"]
)

print("\n===== GENERALIZAÇÃO DE IDADE =====")
print(df[["age","age_group"]].head())


# ==================================================
# Generalização de BMI
# ==================================================

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

print("\n===== GENERALIZAÇÃO DE BMI =====")
print(df[["bmi","bmi_group"]].head())


# ==================================================
# Generalização de Região
# ==================================================

mapa = {
    "northeast": "Norte",
    "northwest": "Norte",
    "southeast": "Sul",
    "southwest": "Sul"
}

df["region_group"] = df["region"].map(mapa)

print("\n===== GENERALIZAÇÃO DE REGIÃO =====")
print(df[["region","region_group"]].head())


# ==================================================
# Avaliação de risco
# ==================================================

print("\n===== AVALIAÇÃO DE RISCO =====")

risco = df.groupby(
    ["sex", "age_group", "smoker"]
).size()

print(risco)


# ==================================================
# Anonimização por Perturbação
# ==================================================

np.random.seed(42)

noise = np.random.laplace(
    loc=0,
    scale=500,
    size=len(df)
)

df["charges_noise"] = df["charges"] + noise

print("\n===== CHARGES COM RUÍDO =====")
print(df[["charges","charges_noise"]].head())


# ==================================================
# Comparação das Estatísticas
# ==================================================

print("\n===== COMPARAÇÃO DAS ESTATÍSTICAS =====")

print("\nMédia Original")
print(df["charges"].mean())

print("\nDesvio Padrão Original")
print(df["charges"].std())

print("\nMédia Anonimizada")
print(df["charges_noise"].mean())

print("\nDesvio Padrão Anonimizado")
print(df["charges_noise"].std())