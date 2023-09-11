import yaml
from rich import print as rprint
import typer


class ConfigMap:
    def __init__(self, file_name, name, cm_data) -> None:
        self.file_name = file_name
        self.name = name
        self.cm_data = cm_data

    def create_yaml(self):
        configmap_data = {
            "apiVersion": "v1",
            "kind": "ConfigMap",
            "metadata": {"name": self.name},
            "data": self.cm_data,
        }

        with open(f"{self.file_name}.yml", "w") as yaml_file:
            yaml.dump(configmap_data, yaml_file, default_flow_style=False)
            rprint(f"[green]Created ConfigMap YAML file: {self.file_name}.yaml[/green]")


class ConfigMapUserInput:
    @staticmethod
    def configMap_input():
        file_name = typer.prompt("Enter the file name for the ConfigMap YAML:")
        name = typer.prompt("Enter the name for the ConfigMap:")

        cm_data = {}

        while True:
            key = typer.prompt(
                "Enter a key for the ConfigMap (or press Enter to save):"
            )
            if not key:
                break

            value = typer.prompt("Enter the value for the key:")
            cm_data[key] = value

            add_more = typer.confirm("Do you want to add more data?", default=False)
            if not add_more:
                break
        return file_name, name, cm_data
