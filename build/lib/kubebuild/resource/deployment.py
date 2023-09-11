import yaml
from rich import print as rprint
import typer
from kubebuild.error.validation import InputValidator


class Deployment:
    def __init__(
        self, name, file_name, namespace, image, port, container_name, replicas
    ):
        self.name = name
        self.file_name = file_name
        self.namespace = namespace
        self.image = image
        self.port = port
        self.container_name = container_name
        self.replicas = replicas

    def create_yaml(self):
        deployment_data = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {"name": self.name, "namespace": self.namespace},
            "spec": {
                "replicas": int(self.replicas),
                "selector": {"matchLabels": {"app": self.name}},
                "template": {
                    "metadata": {"labels": {"app": self.name}},
                    "spec": {
                        "containers": [
                            {
                                "name": self.container_name,
                                "image": self.image,
                                "ports": [{"containerPort": int(self.port)}],
                            }
                        ]
                    },
                },
            },
        }

        with open(f"{self.file_name}.yml", "w") as yaml_file:
            yaml.dump(deployment_data, yaml_file, default_flow_style=False)
            rprint(f"[green]Created Deployment YAML file: {self.file_name}.yml[/green]")


class DeploymentUserInput(InputValidator):
    def deployment_input(self):
        file_name = typer.prompt("Enter the file name for the Deployment YAML:")
        name = typer.prompt("Enter the name for the Deployment YAML:")
        namespace = typer.prompt("Enter the namespace:")
        image = typer.prompt("Enter the container image:")
        while True:
            port = typer.prompt("Enter the container port:")
            if self.is_integer(port):
                break
            else:
                rprint("[red]Port must be an integer. Please try again.[/red]")
        container_name = typer.prompt("Enter the container name:")
        while True:
            replicas = typer.prompt("Enter the number of replicas:")
            if self.is_integer(replicas):
                break
            else:
                rprint("[red]replicas must be an integer. Please try again.[/red]")

        return file_name, name, namespace, image, port, container_name, replicas
