from setuptools import setup, find_packages

setup(
    name="emtechstack",
    version="0.0.89",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "black",
        "requests",
        "tabulate",
        "termcolor",
    ],
    entry_points={
        "console_scripts": [
            "emtechstack=emtechstack.cli:cli",
            "e9k=emtechstack.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
