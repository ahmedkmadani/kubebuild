import yaml
from rich import print as rprint


def create_volume_yaml(file_name, name):
    volume_data = {}

    with open(f"{file_name}.yaml", "w") as yaml_file:
        yaml.dump(volume_data, yaml_file, default_flow_style=False)
        rprint(f"[green]Created Volume YAML file: {file_name}.yaml[/green]")
