# KubeBuild - Kubernetes YAML Generator and Deployment Tool

KubeBuild is a command-line tool designed to simplify the process of creating Kubernetes YAML files for various Kubernetes resources and deploying them into your Kubernetes clusters. It's a valuable tool for both developers and Site Reliability Engineers (SREs).

## Installation  🛠️

You can install KubeBuild via pip:

```bash
pip install kubebuild
```

### Usage 📋

### KubeBuild init  🚀

The init command helps you create Kubernetes YAML files for different resources interactively. It supports the following resources:

- Namespace
- Deployment
- Service
- Ingress
- ConfigMap
- Secret

Example:

```bash
kubebuild init
```

### KubeBuild deploy  🚢

The deploy command allows you to deploy previously generated Kubernetes YAML files into your Kubernetes cluster. It lists available YAML files in the current directory and lets you choose which one to deploy.

Example:

```bash
kubebuild deploy
```

### KubeBuild version 📌
The version command displays the current version of KubeBuild.

Example:

```bash
kubebuild version
```

### Feedback and Contributions 🤝
KubeBuild is an open-source project, and we welcome contributions and feedback from the community. Feel free to report issues, suggest improvements, or contribute to the project on GitHub: KubeBuild GitHub Repository.

Happy Kubernetes resource management with KubeBuild! 🎉
