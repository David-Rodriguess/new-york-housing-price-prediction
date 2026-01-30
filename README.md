# Previsão de Preços de Imóveis em Nova York

## O Problema

Prever preços no mercado imobiliário de Nova York é um desafio devido à grande variância entre imóveis comuns e propriedades de alto padrão.
O objetivo deste projeto é facilitar essa precificação, oferecendo uma estimativa baseada em dados e uma visão geral do mercado imobiliário da cidade.

## Estrutura do Projeto

O projeto foi organizado utilizando dois datasets distintos:

Modelagem (NY_House_Dataset_ML.csv)

Visualização e Análise (NY_House_Dataset_BI.csv)

Essa separação foi feita para evitar vazamento de dados, garantindo que o Power BI seja usado apenas para análise visual e storytelling, sem influenciar o treinamento do modelo.

## Análise Exploratória dos Dados (EDA)

Através da análise exploratória, foi possível identificar:

Distribuição assimétrica dos preços

Forte concentração em faixas intermediárias

Presença de outliers reais, representando imóveis de alto padrão

Essas observações foram fundamentais para a escolha do modelo e para a criação das novas features.

## Feature Engineering

Com base na EDA, senti a necessidade de criar novas variáveis para agregar valor ao dataset e facilitar o aprendizado do modelo.
As principais features criadas foram:

BATH_PER_BED → relação entre banheiros e quartos

BEDS_PER_SQFT → densidade de quartos por área

Essas features ajudam a capturar características estruturais dos imóveis que não são evidentes apenas com valores absolutos.

## Modelagem

Após diversos testes, o modelo final escolhido foi o Gradient Boosting Regressor, utilizando um pipeline completo com:

ColumnTransformer

One-Hot Encoding para variáveis categóricas

Engenharia de atributos

Modelo final integrado ao pipeline

O Gradient Boosting foi escolhido por apresentar o melhor desempenho nos testes, atingindo um R² ≈ 0.79, valor satisfatório para este problema.

O modelo apresenta maior precisão na faixa predominante do dataset e um desempenho inferior nos extremos, comportamento esperado devido à distribuição dos dados.

## API

Foi desenvolvida uma API simples utilizando FastAPI, permitindo a inserção de novos dados para realizar previsões de preço.
O modelo é carregado diretamente via joblib, garantindo que o mesmo pipeline utilizado no treino seja aplicado na inferência.

## Power BI

O Power BI foi utilizado para responder perguntas de negócio de forma visual, como:

Onde estão os imóveis mais caros?

Como os preços se distribuem por localidade?

Qual a dispersão dos preços no mercado?

O dashboard auxilia na compreensão do comportamento dos dados e complementa a análise do modelo.

## Limitações

O modelo apresenta maior erro em imóveis de alto padrão (valores extremos)

Ausência de variáveis espaciais (latitude e longitude)

## Possíveis Evoluções

Algumas melhorias futuras incluem:

Inclusão de features espaciais

Modelos segmentados por faixa de preço

Deploy do modelo em nuvem

Integração direta entre API e Power BI

O projeto possui diversas possibilidades de evolução. 🙂