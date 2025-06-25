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
│   ├── batch_score.py        # Script para prever lotes de dados
│   └── score.py              # Script para prever novas entradas em tempo real
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
├── deploy_batch.py           # Implantação que prevê ROAS em lote    
├── deploy_model.py           # Implantação que prevê ROAS em tempo real
├── invoke_batch_endpoint.py  # Invoca o endpoint para iniciar o trabalho em lote
├── requirements.txt          
└── run_training_job.py       # Script para implantar o modelo
```
