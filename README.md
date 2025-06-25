# Projeto de Previsão de ROAS com Azure Machine Learning

## Sumário

Este repositório documenta a criação e implementação de uma solução de Machine Learning de ponta a ponta na plataforma Microsoft Azure. O projeto foi desenvolvido como um exercício prático e demonstração de competências para a **Certificação DP-100: Designing and Implementing a Data Science Solution on Azure**.

O objetivo principal não é oferecer um software para uso direto, mas sim apresentar um portfólio detalhado do ciclo de vida de MLOps, desde a ingestão de dados e treinamento de um modelo de regressão até a sua implantação em ambientes de produção para inferência em tempo real e em lote.

---

## Tecnologias e Serviços Utilizados

* **Plataforma Cloud:** Microsoft Azure
* **Serviço Principal:** Azure Machine Learning Workspace
* **Recursos de Computação:**
    * Azure ML Compute Cluster (para treinamento e inferência em lote)
    * Azure ML Managed Online Endpoint (para inferência em tempo real)
* **Orquestração e Versionamento:**
    * Azure ML SDK v2 para Python
    * MLflow Tracking (para registro de métricas, artefatos e modelos)
* **Linguagem e Bibliotecas:**
    * Python 3.11
    * Scikit-learn (para modelagem de Regressão Linear)
    * Pandas 
    * Matplotlib

---

## Visão Geral do Projeto

O projeto consiste em prever o **Retorno do Investimento em Anúncios (ROAS)** com base em métricas de desempenho de campanhas de marketing. O fluxo de trabalho implementado abrange as seguintes etapas:

1.  **Configuração do Ambiente:** Provisionamento de um Workspace do Azure ML e seus recursos associados (Storage, Key Vault, etc.), além de um Cluster de Computação para execução dos trabalhos.
2.  **Versionamento de Dados:** Os dados de entrada são versionados como Ativos de Dados (Data Assets) no Azure ML para garantir rastreabilidade.
3.  **Treinamento do Modelo:** Um script de treinamento (`train.py`) executa um Trabalho de Comando (Command Job) no Azure. Durante a execução, o script:
    * Lê os dados versionados.
    * Treina um modelo de Regressão Linear.
    * Avalia o modelo usando a métrica Mean Absolute Error (MAE).
    * Registra a métrica, um gráfico de visualização e o modelo treinado usando MLflow.
4.  **Implantação:** O modelo registrado é implantado em dois tipos de pontos de extremidade:
    * **Online Endpoint:** Para previsões instantâneas, ideais para integrações com aplicações.
    * **Batch Endpoint:** Para processar grandes volumes de dados de forma assíncrona.
5.  **Inferência:** Scripts de invocação demonstram como consumir ambos os endpoints para obter previsões.

---

## Estrutura do Repositório

```
meu-projeto-dp100/
│
├── data/                  # Contém amostras de dados e informações sobre o dataset.
├── deployment/            # Scripts de pontuação (scoring) para os endpoints.
│   ├── batch_score.py
│   └── score.py
├── environment/           # Definição do ambiente de software customizado.
│   └── training_env.yml
├── src/                   # Código-fonte principal do projeto.
│   ├── train.py
│   └── utils.py           # (Conceitual) Funções auxiliares.
|
├── .gitignore
├── LICENSE
├── README.md              # Este arquivo.
├── deploy_batch.py        # Orquestra a implantação do Batch Endpoint.
├── deploy_model.py        # Orquestra a implantação do Online Endpoint.
├── invoke_batch_endpoint.py # Inicia um trabalho de inferência em lote.
├── requirements.txt       # Dependências locais para interagir com o SDK.
└── run_training_job.py    # Orquestra o trabalho de treinamento do modelo.
```

---

## Aprendizados e Competências Demonstradas

Este projeto solidificou e demonstra minha proficiência nas seguintes áreas do Azure Machine Learning:

* **Gerenciamento do Ciclo de Vida de ML:** Execução de um projeto completo, desde a concepção até a operacionalização.
* **Uso do Azure ML SDK v2:** Habilidade em interagir com a plataforma Azure de forma programática para automação e reprodutibilidade.
* **Ambientes e Reprodutibilidade:** Capacidade de criar e gerenciar ambientes de software consistentes para garantir que os experimentos sejam reprodutíveis.
* **Versionamento de Ativos:** Experiência com o versionamento de dados e modelos, uma prática central de MLOps.
* **MLflow:** Uso eficaz do MLflow para rastrear métricas, artefatos e registrar modelos, permitindo governança e comparação de experimentos.
* **Implantação e Inferência:** Conhecimento prático na implantação de modelos para consumo em cenários de tempo real e em lote, incluindo a criação de scripts de pontuação.
* **Depuração (Debugging):** Habilidade em diagnosticar e resolver uma variedade de erros de configuração, ambiente, código e dados em um ambiente de nuvem complexo.

---

## Contato

* [LinkedIn](https://www.linkedin.com/in/thiago-mustasheep/)