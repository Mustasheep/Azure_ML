# Azure_ML

## Estrutura

```
meu-projeto-dp100/
│
├── .gitignore          # Arquivo para ignorar arquivos desnecessários no Git
├── README.md           # A porta de entrada do seu projeto
├── requirements.txt    # Dependências Python para o ambiente local
│
├── data/
│   ├── sample.csv      # Uma pequena amostra dos dados para testes rápidos
│   └── README.md       # Explicação de onde obter os dados completos
│
├── notebooks/
│   ├── 1-data-exploration.ipynb   # Análise exploratória, visualizações (EDA)
│   └── 2-model-prototyping.ipynb  # Testes rápidos e prototipagem de modelos
│
├── environment/
│   └── training_environment.yml   # Definição do ambiente Conda para treinamento no Azure ML
│
└── src/
    ├── train.py        # Script principal de treinamento do modelo
    ├── evaluate.py     # Script para avaliar o modelo com métricas
    ├── deploy.py       # (Opcional) Script para implantar o modelo
    └── utils.py        # Funções auxiliares usadas por outros scripts
```