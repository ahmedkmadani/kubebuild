import yaml
from rich import print as rprint


def create_pvc_yaml(file_name, name):
    pvc_data = {
        "apiVersion": "v1",
        "kind": "PersistentVolumeClaim",
        "metadata": {"name": name},
    }

    with open(f"{file_name}.yaml", "w") as yaml_file:
        yaml.dump(pvc_data, yaml_file, default_flow_style=False)
        rprint(f"[green]Created PVC YAML file: {file_name}.yaml[/green]")
