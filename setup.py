from setuptools import setup, find_packages

setup(
    name="kubebuild",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "typer==0.9.0",
        "PyInquirer==1.0.3",
        "PyYAML==6.0.1",
        "rich==13.5.2",
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
