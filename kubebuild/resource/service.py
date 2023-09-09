from rich import print as rprint
import yaml
import typer
from kubebuild.error.validation import InputValidator


class Service:
    def __init__(self, file_name, name, namespace, port, target_port):
        self.file_name = file_name
        self.name = name
        self.namespace = namespace
        self.port = port
        self.target_port = target_port

    def create_yaml(self):
        service_data = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {"name": self.name, "namespace": self.namespace},
            "spec": {
                "type": "NodePort",
                "ports": [
                    {
                        "name": f"{self.name}-port",
                        "port": self.port,
                        "targetPort": self.target_port,
                    }
                ],
            },
        }

        with open(f"{self.file_name}.yaml", "w") as yaml_file:
            yaml.dump(service_data, yaml_file, default_flow_style=False)
            rprint(f"[green]Created Service YAML file: {self.file_name}.yaml[/green]")


class ServiceUserInput(InputValidator):
    def service_input(self):
        file_name = typer.prompt("Enter the file name for the Service YAML:")
        name = typer.prompt("Enter the name for the Service:")
        namespace = typer.prompt("Enter the namespace:")
        while True:
            port = typer.prompt("Enter the port for the Service:")
            if self.is_integer(port):
                break
            else:
                rprint("[red]Port must be an integer. Please try again.[/red]")

        while True:
            target_port = typer.prompt("Enter the target port for the Service:")
            if self.is_integer(target_port):
                break
            else:
                rprint("[red]Target port must be an integer. Please try again.[/red]")

        return file_name, name, namespace, port, target_port
