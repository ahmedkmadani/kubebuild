import typer
import subprocess
from PyInquirer import prompt, Separator
from rich import print as rprint
from kubebuild.resource.deployment import Deployment, DeploymentUserInput
from kubebuild.resource.namespace import Namespace, NamespaceUserInput
from kubebuild.resource.service import Service, ServiceUserInput
from kubebuild.resource.ingress import Ingress, IngressUserInput
from kubebuild.resource.configmap import ConfigMap, ConfigMapUserInput
from kubebuild.resource.secret import Secret, SecretUserInput
from kubebuild.resource.volume import create_volume_yaml
from kubebuild.resource.pvc import create_pvc_yaml
import os
from kubebuild.constant.resource_names import ResourceNames

app = typer.Typer()


@app.command("init")
def init():
    resource_list = [
        {
            "type": "list",
            "name": "resource",
            "message": "Select resource you want to create:",
            "choices": [
                {
                    "name": ResourceNames.NAMESPACE,
                },
                {
                    "name": ResourceNames.DEPLOYMENT,
                },
                {
                    "name": ResourceNames.SERVICE,
                },
                {
                    "name": ResourceNames.INGRESS,
                },
                {
                    "name": ResourceNames.CONFIGMAP,
                },
                {
                    "name": ResourceNames.SECRET,
                },
                # {
                #     "name": "Volume",
                # },
                # {
                #     "name": "Persistent Volume Claim (PVC)",
                # },
                # {
                #     "name": "StatefulSet",
                # },
                # {
                #     "name": "DaemonSet",
                # },
                # {
                #     "name": "CronJob",
                # },
                {
                    "name": "Quit",
                },
            ],
        }
    ]

    selected_resource = prompt(resource_list)["resource"]

    if selected_resource == "Quit":
        rprint("[yellow]Exiting the application.[/yellow]")
        raise typer.Abort()

    if not selected_resource:
        rprint("[yellow]No resource selected. Exiting the application.[/yellow]")
        raise typer.Abort()

    rprint(f"[yellow]Creating Kubernetes {selected_resource} YAML[/yellow]")

    if selected_resource == ResourceNames.NAMESPACE:
        name, file_name = NamespaceUserInput.namespace_input()
        namespace = Namespace(name=name, file_name=file_name)
        namespace.create_yaml()

    if selected_resource == ResourceNames.DEPLOYMENT:
        deployment_input_instance = DeploymentUserInput()
        (
            file_name,
            name,
            namespace,
            image,
            port,
            container_name,
            replicas,
        ) = deployment_input_instance.deployment_input()

        deployment = Deployment(
            file_name=file_name,
            name=name,
            namespace=namespace,
            image=image,
            port=port,
            container_name=container_name,
            replicas=replicas,
        )

        deployment.create_yaml()

    if selected_resource == ResourceNames.SERVICE:
        service_input_instance = ServiceUserInput()

        (
            file_name,
            name,
            namespace,
            port,
            target_port,
        ) = service_input_instance.service_input()
        service = Service(
            file_name=file_name,
            name=name,
            namespace=namespace,
            port=port,
            target_port=target_port,
        )
        service.create_yaml()

    if selected_resource == ResourceNames.INGRESS:
        ingress_input_instance = IngressUserInput()

        (
            file_name,
            name,
            namespace,
            ingress_class_name,
            path,
            path_type,
            service_name,
            backend_port,
        ) = ingress_input_instance.ingress_input()

        ingress = Ingress(
            file_name=file_name,
            name=name,
            namespace=namespace,
            ingress_class_name=ingress_class_name,
            path=path,
            path_type=path_type,
            service_name=service_name,
            backend_port=backend_port,
        )

        ingress.create_yaml()

    if selected_resource == ResourceNames.CONFIGMAP:
        file_name, name, cm_data = ConfigMapUserInput.configMap_input()

        cm = ConfigMap(file_name=file_name, name=name, cm_data=cm_data)

        cm.create_yaml()

    if selected_resource == ResourceNames.SECRET:
        file_name, name, namespace, secret_data = SecretUserInput.secret_input()

        secret = Secret(
            secret_data=secret_data, name=name, namespace=namespace, file_name=file_name
        )

        secret.create_yaml()


@app.command("deploy")
def deploy():
    yaml_files = [f for f in os.listdir() if f.endswith(".yml")]

    if not yaml_files:
        rprint("[red]No YAML files found in the current directory.[/red]")
        return

    rprint("[yellow]Available YAML files:[/yellow]")
    for i, file in enumerate(yaml_files):
        rprint(f"{i + 1}. {file}")

    selected_index = input(
        "Enter the number of the YAML file to deploy (or 'q' to quit): "
    )

    if selected_index == "q":
        return

    try:
        selected_index = int(selected_index)
        if 1 <= selected_index <= len(yaml_files):
            selected_yaml = yaml_files[selected_index - 1]
            subprocess.run(["kubectl", "apply", "-f", selected_yaml], check=True)
            rprint(
                f"[green]Successfully applied {selected_yaml} using kubectl.[/green]"
            )
        else:
            rprint(
                "[red]Invalid input. Please enter a valid number or 'q' to quit.[/red]"
            )
            deploy()
    except ValueError:
        rprint("[red]Invalid input. Please enter a valid number or 'q' to quit.[/red]")
    except subprocess.CalledProcessError as e:
        rprint(f"[red]Error applying {selected_yaml} using kubectl: {e.stderr}[/red]")


@app.command("version")
def show_version():
    rprint(f"KubeBuild: 0.0.1")


@app.command("about")
def show_version():
    rprint(
        f"🚀 [yellow]KubeBuild[/yellow] simplifies Kubernetes YAML creation and deployment, ideal for developers and SREs."
    )


if __name__ == "__main__":
    app()
