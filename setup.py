from setuptools import setup, find_packages

# Open the README.md file and convert it to reST format
with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="kubebuild",
    version="1.1.0",
    description='Kubebuild - Kubernetes YAML Generator and Deployment Tool',
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify that the description is in Markdown format
    author="Ahmed K. Madani",
    author_email="ahmedk.madani@outlook.com",
    url="https://github.com/ahmedkmadani/kubebuild.git",
    packages=find_packages(),
    install_requires=[
        "typer",
        "PyInquirer",
        "PyYAML",
        "rich",
    ],
    entry_points={
        'console_scripts': [
            'kubebuild = kubebuild.app:app',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
