import os
import pandas as pd
import mlflow
import traceback

# Chamada uma vez no início do trabalho
def init():
    global model
    global model_input_names

    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "modelo_regressao_roas")
    
    print(f"Carregando modelo de: {model_path}")
    model = mlflow.pyfunc.load_model(model_path)
    
    model_input_names = model.metadata.get_input_schema().input_names()
    print(f"Modelo carregado. Entradas esperadas: {model_input_names}")

# Processa um mini-lote de arquivos
def run(mini_batch):
    print(f"Iniciando processamento do mini-lote: {mini_batch}")
    results = []

    for file_path in mini_batch:
        try:
            print(f"Processando arquivo: {file_path}")
            df = pd.read_csv(file_path, encoding='latin-1')
            
            X = df[model_input_names]
            
            print(f"Dados de entrada para o modelo (primeiras linhas):\n{X.head()}")
            
            # Previsões
            predictions = model.predict(X)
            
            df['previsao_roas'] = predictions
            
            results.append(df)
            print(f"Arquivo {file_path} processado com sucesso.")

        except Exception as e:
            print(f"Erro ao processar o arquivo {file_path}. Erro: {e}")
            print(traceback.format_exc())

    if results:
        return pd.concat(results)
    else:
        return None