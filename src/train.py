import argparse
import utils
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import os

# --- RECEBER PARAMETROS ---
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, help="Caminho para dados de entrada")
args = parser.parse_args()

# Inicia o registro com MLflow
mlflow.start_run()

# --- LER E PREPARAR OS DADOS ---
print("Lendo os dados...")
df = pd.read_csv(args.input_data, encoding='latin-1')
utils.renomear_colunas(df)
utils.selecionar_roas(df)

# --- PREPARAR DADOS ---
target_column = 'roas'
features = ['gasto', 'alcance', 'impressoes', 'cliques_no_link']

X = df[features]
y = df[target_column]

# Dividir em treino e teste
X_train, X_test, y_train, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- TREINAR MODELO ---
print("Treinando o modelo de Regressão Linear...")
model = LinearRegression()
model.fit(X_train, y_train)

# --- AVALIAR O MODELO ---
preds = model.predict(X_test)
mae = mean_squared_error(y_teste, preds)
print(f"Avaliação completa. Mean Absolute Error (MAE): {mae}")

# --- REGISTRAR MÉTRICA COM MLFLOW ---
mlflow.log_metric("mae", mae)
print("Métrica 'mae' registrada no MLflow.")

# --- GERAR E REGISTRAR GRÁFICO DE REGRESSÃO ---
print("Gerando e registrando o gráfico de dispersão...")
fig = plt.figure(figsize=(10, 7))
plt.scatter(y_test, preds, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--r', linewidth=2)
plt.xlabel("ROAS Real")
plt.ylabel("ROAS Previsto")
plt.title("ROAS Real vs. Previsto")
plt.grid(True)

mlflow.log_figure(fig, "scatter_real_vs_previsto.png")
print("Gráfico registrado como artefato no MLflow.")

# --- SALVAR E REGISTRAR O MODELO ---
print("Registrando o modelo no workspace...")
mlflow.sklearn.log_model(
    sk_model=model,
    artifact_path="modelo_regressao_roas", 
    registered_model_name="modelo-roas-dp100"
)
print("Modelo registrado com sucesso.")

# Finaliza o registro com MLflow
mlflow.end_run()