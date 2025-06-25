from azure.ai.ml import MLClient, Input
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure.identity import DefaultAzureCredential

# Conectar ao worskpace
credential = DefaultAzureCredential()
ml_client = MLClient.from_config(credential=credential)

endpoint_name = "endpoint-roas-batch"

# Referenciar ao conjunto de dados
input_data = Input(
    type=AssetTypes.URI_FILE,
    path=f"azureml:dados-batch-input:2"
)

# Invocar o endpoint para iniciar o trabalho em lote
print(f"Invocando o endpoint '{endpoint_name}'...")
batch_job = ml_client.batch_endpoints.invoke(
    endpoint_name=endpoint_name,
    input=input_data,
)

print(f"Trabalho de pontuação em lote iniciado com sucesso.")
print(f"Acompanhe o andamento no Estúdio do Azure ML, na seção 'Trabalhos'.")