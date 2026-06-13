# Atividade 02 – Técnicas de Privacidade

## Descrição

Este projeto foi desenvolvido para a disciplina de Privacidade da Informação e tem como objetivo aplicar técnicas de de-identificação e anonimização em um dataset de clientes, reduzindo os riscos de reidentificação e preservando a utilidade dos dados para análises estatísticas.

O dataset utilizado foi o `insurance.csv`.

## Objetivos

* Classificar atributos em:

  * Identificadores diretos;
  * Quase-identificadores;
  * Atributos sensíveis;
  * Atributos não sensíveis.
* Aplicar técnicas de de-identificação.
* Avaliar riscos de reidentificação.
* Aplicar anonimização por perturbação.
* Comparar estatísticas antes e depois da anonimização.

## Tecnologias Utilizadas

* Python 3
* Pandas
* NumPy
* Visual Studio Code

## Observação

Embora o enunciado da atividade mencione a utilização do Google Colab, o desenvolvimento foi realizado utilizando o Visual Studio Code (VS Code) por conveniência. As bibliotecas utilizadas são compatíveis com ambos os ambientes e produzem os mesmos resultados.

## Instalação

Instale as dependências necessárias:

```bash
pip install pandas numpy
```

## Execução

Execute o script:

```bash
python script.py
```

## Técnicas Aplicadas

### Generalização

Foram realizadas as seguintes generalizações:

* Idade → Faixas etárias

  * 18–29
  * 30–44
  * 45–64

* BMI → Categorias

  * Baixo Peso
  * Normal
  * Sobrepeso
  * Obesidade

* Região → Agrupamento geográfico

  * Norte
  * Sul

### Avaliação de Risco

Foi realizada uma análise utilizando a combinação dos atributos:

* Sexo
* Faixa etária
* Condição de fumante

para identificar possíveis riscos de reidentificação.

### Anonimização por Perturbação

Foi aplicado ruído aleatório utilizando distribuição de Laplace sobre o atributo `charges`, gerando uma nova coluna chamada `charges_noise`.

## Resultados Esperados

O script apresenta:

* Dataset original;
* Generalização da idade;
* Generalização do BMI;
* Generalização da região;
* Avaliação de risco de reidentificação;
* Comparação entre valores originais e anonimizados;
* Média e desvio padrão antes e depois da anonimização.

## Autor

Adão Junior

Pontifícia Universidade Católica do Paraná – PUCPR

Disciplina: Privacidade da Informação
