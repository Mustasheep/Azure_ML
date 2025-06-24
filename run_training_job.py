# Importações do SDK do Azure ML
from azure.ai.ml import MLClient, Input, command
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure.identity import DefaultAzureCredential

# Conectar ao workspace
credential = DefaultAzureCredential()
ml_client = MLClient.from_config(credential=credential)

# Deifnir a entrada de dados
data_asset = ml_client.data.get(name="meta_ads_data", version="2")
job_input = Input(type=AssetTypes.URI_FILE, path=data_asset.id)

# Definir o comando que será executado
job_command = command(
    code="./src",
    command="python train.py --input_data ${{inputs.ads_data}}",
    inputs={
        "ads_data": job_input
    },

    # Ambiente de software
    environment="AzureML-sklearn-1.1-ubuntu22.04",
    compute="cluster-cpu-dp100",

    # Interface do Azure
    display_name="Treinamento_Regressao_ROAS",
    experiment_name="experimentos_roas"
)

print("Submetendo o trabalho ao Azure Machine Learning...")
retuned_job = ml_client.jobs.create_or_update(job_command)

print(f"Trabalho submetido. Acompanhe em: {retuned_job.studio_url}")