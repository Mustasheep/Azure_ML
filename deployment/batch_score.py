import os
import pandas as pd
import mlflow
import joblib
import glob

# Chamada para inicializar
def init():
    global model
    
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "modelo_regressao_roas")

    print(f"Carregando modelo de: {model_path}...")
    model = mlflow.pyfunc.load_model(model_path)
    print("Modelo carregado.")

def run(mini_batch):
    print(f"Iniciando processamento do mini-lote: {mini_batch}...")
    results = []

    for file_path in mini_batch:
        df = pd.read_csv(file_path, encoding='latin-1')

        features = ['gasto', 'alcance', 'impressoes', 'cliques_no_link']
        X = df[features]

        # Aplicando previsões
        predictions = model.predict(X)
        df['previsao_roas'] = predictions

        results.append(df)
    
    return pd.concat(results)