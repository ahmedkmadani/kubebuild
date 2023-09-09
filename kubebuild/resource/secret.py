import yaml
from rich import print as rprint
import typer


class Secret:
    def __init__(self, file_name, name, secret_data, namespace) -> None:
        self.file_name = file_name
        self.name = name
        self.secret_data = secret_data
        self.namespace = namespace

    def create_yaml(self):
        secret_data = {
            "apiVersion": "v1",
            "kind": "Secret",
            "metadata": {"name": self.name, "namespace": self.namespace},
            "data": self.secret_data,  # Add the secret data here
        }

        with open(f"{self.file_name}.yaml", "w") as yaml_file:
            yaml.dump(secret_data, yaml_file, default_flow_style=False)
            rprint(f"[green]Created Secret YAML file: {self.file_name}.yaml[/green]")


class SecretUserInput:
    @staticmethod
    def secret_input():
        file_name = typer.prompt("Enter the file name for the Secret YAML:")
        name = typer.prompt("Enter the name for the Secret:")
        namespace = typer.prompt("Enter the namespace for the Secret:")

        secret_data = {}

        while True:
            key = typer.prompt(
                "Enter a key for the Secret data (or press Enter to save):"
            )
            if not key:
                break

            value = typer.prompt(f"Enter the value for the key '{key}':")
            secret_data[key] = value

            add_more = typer.confirm(
                "Do you want to add more Secret data?", default=False
            )
            if not add_more:
                break

        return file_name, name, namespace, secret_data
