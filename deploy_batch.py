from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    BatchEndpoint,
    BatchDeployment,
    Model,
    Environment,
    CodeConfiguration
)
from azure.identity import DefaultAzureCredential

# Conectar ao workspace
credential = DefaultAzureCredential()
ml_client = MLClient.from_config(credential=credential)

# --- DEFINIÇÃO DO BATCH ENDPOINT ---
endpoint_name = "endpoint-roas-batch"
endpoint = BatchEndpoint(
    name=endpoint_name,
    description="Endpoint em lote para prever o ROAS de campanhas de marketing."
)
# Criando o endpoint
ml_client.batch_endpoints.begin_create_or_update(endpoint).result()

# --- DEFINIÇÃO DA IMPLANTAÇÃO EM LOTE ---
model = ml_client.models.get(name="modelo-roas-dp100", label='latest')

env = Environment(
    name="roas-batch-deployment-env",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu22.04",
    conda_file="./environment/training_env.yml"
)
# Configuração da implantação
deployment = BatchDeployment(
    name="roas-batch-deployment",
    description="Implantação que prevê ROAS em lote.",
    endpoint_name=endpoint_name,
    model=model,
    environment=env,
    code_configuration=CodeConfiguration(
        code="./deployment",
        scoring_script="batch_score.py",
    ),
    # Definindo o cluster para o job
    compute="cluster-cpu-dp100",
    instance_count=1,
    mini_batch_size=1,
)
# Criando a implantação
ml_client.batch_deployments.begin_create_or_update(deployment).result()

print(f"Implantação em lote concluída. Endpoint '{endpoint_name}' está pronto para ser invocado.")