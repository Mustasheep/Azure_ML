import os
import json
import pandas as pd
import mlflow
import joblib

# Chamada de inicialização
def init():
    global model
    model_path = os.getenv("AZUREML_MODEL_DIR", "modelo_regressao_roas/model.pkl")
    model = joblib.load(model_path)
    print(f"Modelo carregado de {model_path}")

# Chamada de predição
def run(raw_data):
    try:
        print(f"Recebida solicitação de dados: {raw_data}")
        data = json.loads(raw_data)['data']

        df = pd.DataFrame(data, columns=[
            'gasto', 'alcance', 'impressoes', 'cliques_no_link'])
        
        result = model.predict(df)
        print(f"Predição gerada: {result.tolist()}")
        return result.tolist()
    
    except Exception as e:
        error = str(e)
        print(f"Erro na execução: {error}")
        return error