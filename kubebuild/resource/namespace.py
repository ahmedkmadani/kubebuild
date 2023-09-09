from rich import print as rprint
import yaml
import typer


class Namespace:
    def __init__(self, name, file_name):
        self.name = name
        self.file_name = file_name

    def create_yaml(self):
        """
        func to create namespace yml file
        """
        namespace_data = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {"name": self.name},
        }

        with open(f"{self.file_name}.yml", "w") as yaml_file:
            yaml.dump(namespace_data, yaml_file, default_flow_style=False)
            rprint(f"[green]Created Namespace YAML file: {self.file_name}.yml[/green]")


class NamespaceUserInput:
    def namespace_input():
        file_name = typer.prompt("Enter the file name for the Namespace YAML:")
        name = typer.prompt("Enter the name for the Namespace:")

        return file_name, name
