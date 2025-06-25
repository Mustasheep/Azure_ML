import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# MUDANÇA 1: Importando a métrica correta
from sklearn.metrics import mean_absolute_error
import mlflow
import os

# --- RECEBER PARAMETROS ---
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, help="Caminho para dados de entrada")
args = parser.parse_args()

# Inicia o registro com MLflow
mlflow.start_run()

# --- LER OS DADOS ---
print("Lendo os dados...")
df = pd.read_csv(args.input_data, encoding='latin-1')

# --- PREPARAR DADOS ---
target_column = 'ROAS'
features = ['Gasto (R$)', 'Alcance', 'Impressões', 'Cliques no Link']

X = df[features]
y = df[target_column]

# Dividir em treino e teste
# MUDANÇA 2: Corrigindo o nome da variável para y_test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- TREINAR MODELO ---
print("Treinando o modelo de Regressão Linear...")
model = LinearRegression()
model.fit(X_train, y_train)

# --- AVALIAR O MODELO ---
preds = model.predict(X_test)
# MUDANÇA 3: Calculando a métrica correta com a variável correta
mae = mean_absolute_error(y_test, preds)
print(f"Avaliação completa. Mean Absolute Error (MAE): {mae}")

# --- REGISTRAR MÉTRICA COM MLFLOW ---
mlflow.log_metric("mae", mae)
print("Métrica 'mae' registrada no MLflow.")

# Finaliza o registro com MLflow
mlflow.end_run()