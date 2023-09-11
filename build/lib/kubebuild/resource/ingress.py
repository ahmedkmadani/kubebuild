from rich import print as rprint
import yaml
import typer
from kubebuild.error.validation import InputValidator


class Ingress:
    def __init__(
        self,
        file_name,
        name,
        namespace,
        ingress_class_name,
        path,
        path_type,
        service_name,
        backend_port,
    ):
        self.file_name = file_name
        self.name = name
        self.namespace = namespace
        self.ingress_class_name = ingress_class_name
        self.path = path
        self.path_type = path_type
        self.service_name = service_name
        self.backend_port = backend_port

    def create_yaml(self):
        ingress_data = {
            "apiVersion": "networking.k8s.io/v1",
            "kind": "Ingress",
            "metadata": {"name": self.name, "namespace": self.namespace},
            "spec": {
                "ingressClassName": self.ingress_class_name,
                "rules": [
                    {
                        "http": {
                            "paths": [
                                {
                                    "path": self.path,
                                    "pathType": self.path_type,
                                    "backend": {
                                        "service": {
                                            "name": self.service_name,
                                            "port": {"number": int(self.backend_port)},
                                        }
                                    },
                                }
                            ]
                        }
                    }
                ],
            },
        }

        with open(f"{self.file_name}.yml", "w") as yaml_file:
            yaml.dump(ingress_data, yaml_file, default_flow_style=False)
            rprint(f"[green]Created Ingress YAML file: {self.file_name}.yaml[/green]")


class IngressUserInput(InputValidator):
    def ingress_input(self):
        file_name = typer.prompt("Enter the file name for the Ingress YAML:")
        name = typer.prompt("Enter the name for the Ingress:")
        namespace = typer.prompt("Enter the namespace:")
        ingress_class_name = typer.prompt("Enter the Ingress Class Name:")
        path = typer.prompt("Enter the path for the Ingress:")
        path_type = typer.prompt(
            "Enter the path type (Prefix/Exact):", default="Prefix"
        ).lower()
        service_name = typer.prompt("Enter the backend service name:")
        while True:
            backend_port = typer.prompt("Enter the backend service port:")
            if self.is_integer(backend_port):
                break
            else:
                rprint("[red]Backend port must be an integer. Please try again.[/red]")

        return (
            file_name,
            name,
            namespace,
            ingress_class_name,
            path,
            path_type,
            service_name,
            backend_port,
        )
