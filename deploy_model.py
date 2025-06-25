from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
    CodeConfiguration
)
from azure.identity import DefaultAzureCredential

# Conectar ao workspace
credential = DefaultAzureCredential()
ml_client = MLClient.from_config(credential=credential)

# -- DEFINIÇÃO DO ENDPOINT --
endpoint_name = "endpoint-roas-pred"
endpoint = ManagedOnlineEndpoint(
    name=endpoint_name,
    description="Endpoint para predição de ROAS em campanhas de marketing",
    auth_mode="key"
)
# Criar o endpoint
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# -- DEFINIÇÃO DA IMPLANTAÇÃO --
model = ml_client.models.get(name="modelo-roas-dp100", version="latest")

env = Environment(
    name="roas-deployment-env",
    description="Ambiente para a implantação do modelo de ROAS",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu22.04",
    conda_file="./environment/training_env.yml"
)
# Configuração da implantação
blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=endpoint_name,
    model=model,
    environment=env,
    code_configuration=CodeConfiguration(
        code="./deployment",
        scoring_script="score.py"
    ),
    instance_type="Standard_DS2_v2",
    instance_count=1
)

# Criar a implantação
ml_client.online_deployments.begin_create_or_update(blue_deployment).result()

endpoint.traffic = {"blue": 100}  # Direcionar 100% do tráfego para a implantação "blue"
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

print(f"Implantação '{blue_deployment.name}' criada com sucesso no endpoint '{endpoint_name}'.")