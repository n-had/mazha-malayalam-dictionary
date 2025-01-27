<img src="src/assets/ma.ico" width="64" alt="Mazha Logo" />

# മഴ - Mazha Malayalam Dictionary

An offline English-to-Malayalam and Malayalam-to-Malayalam dictionary for desktop.

It is based on the [Olam](https://olam.in) open-source dictionary and built using Qt for Python.

## Features
- Simple, user-friendly interface
- Light and dark themes
- Copy definitions to clipboard with one click

[Download](https://github.com/n-had/mazha-malayalam-dictionary/releases)

> **Note**: The application is currently in the alpha stage and is supported only on Windows.

## Installation
### It is recommended to use a virtual environment to manage dependencies:
```shell
python -m venv venv
```
### Activate the virtual environment

On Windows
```shell
venv\Scripts\activate
```


### Install the required dependencies:
```shell
pip install -r requirements.txt
```
### Run the application:
```shell
python src/main.py
```
### To compile the application into an executable file:
```shell
pyinstaller Mazha.spec
```