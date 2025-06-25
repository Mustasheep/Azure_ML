# Azure_ML

## Estrutura

```
meu-projeto-dp100/
│
├── data/
│   ├── sample.csv            # Uma pequena amostra dos dados para testes rápidos
│   └── README.md             # Explicação de onde obter os dados
│
├── deployment/
│   └── score.py              # Script para prever novas entradas
|
├── environment/
│   └── training_env.yml      # Definição do ambiente Conda para treinamento no Azure ML
│
├──  src/
│   ├── train.py              # Script principal de treinamento do modelo
│   └── utils.py              # Funções auxiliares usadas por outros scripts
|
├── .gitignore          
├── LICENSE  
├── README.md       
├── deploy_model.py           # Script para implantar o modelo
├── requirements.txt          # Dependências Python para o ambiente local
└── run_training_job.py       # Script para implantar o modelo
```
