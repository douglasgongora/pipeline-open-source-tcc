from airflow.providers.docker.operators.docker import DockerOperator
from airflow.decorators import dag
from airflow.utils.dates import days_ago
from datetime import datetime


@dag(
    schedule_interval="*/5 * * * *",
    start_date=days_ago(1),
    catchup=False,
    tags=["tcc_project"],
)
def dag_etl_pipeline_tcc():
    container_name = (
        f"run_docker_python_access-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    )

    docker_task = DockerOperator(
        task_id="run_docker_python_access",
        image="tcc_projeto",
        docker_url="tcp://docker-proxy:2375",
        network_mode="tcc",
        command="python3 orchestrator.py",
        container_name=container_name,
        auto_remove=True,
    )

    docker_task


dag = dag_etl_pipeline_tcc()




from airflow.providers.docker.operators.docker import DockerOperator
from airflow.decorators import dag
from airflow.utils.dates import days_ago
from datetime import datetime
from airflow.providers.docker.types import DockerMount

@dag(
    schedule_interval="*/5 * * * *",
    start_date=days_ago(1),
    catchup=False,
    tags=["tcc_project"],
)
def dag_etl_pipeline_tcc():
    container_name = (
        f"run_docker_python_access-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    )

    docker_task = DockerOperator(
        task_id="run_docker_python_access",
        image="tcc_projeto",
        docker_url="tcp://docker-proxy:2375",
        network_mode="tcc",
        command="python3 orchestrator.py",
        container_name=container_name,
        auto_remove=True,
        mount_tmp_dir=False,  # Desativa montagem do tmp
        mounts=[
            DockerMount(
                source="/home/douglas/docker/tcc_project",  # Caminho no host
                target="/src",  # Caminho no container
                type="bind"  # Tipo de montagem
            ),
        ],
    )

    docker_task

dag = dag_etl_pipeline_tcc()



