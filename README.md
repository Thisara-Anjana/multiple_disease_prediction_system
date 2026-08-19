# Multiple Disease Prediction System

A collection of Jupyter notebooks and supporting files for building and evaluating machine learning models that predict multiple diseases from clinical/medical data. This repository contains data preparation, model training, evaluation, and demonstration notebooks designed for experimentation and reproducible research.

## Table of contents

- [Project overview](#project-overview)
- [Features](#features)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
- [Running the notebooks](#running-the-notebooks)
- [Dataset](#dataset)
- [Modeling & results](#modeling--results)
- [Docker (optional)](#docker-optional)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project overview

This project aims to provide an end-to-end environment for experimenting with multi-disease prediction models. The code is organized as Jupyter notebooks so you can inspect data transformations, model code, training loops, and evaluation steps interactively.

## Features

- Data preprocessing and feature engineering pipelines (in notebooks)
- Multiple model experiments (classical ML and/or deep learning)
- Model evaluation and visualization (confusion matrices, ROC, precision/recall, etc.)
- Reproducible notebooks for training and inference
- Guidance for packaging models into a deployable service

## Repository structure

Note: exact file and folder names may vary. Typical layout:

- *.ipynb* — Jupyter notebooks (preprocessing, training, evaluation, demo)
- data/ — raw and processed datasets (if present)
- models/ — saved model artifacts (if present)
- notebooks/ — optional folder for grouped notebooks
- requirements.txt — Python dependencies (you may generate one)
- Dockerfile — optional container definition
- README.md — this file

Adjust paths above to match your repository layout.

## Getting started

### Prerequisites

- Python 3.8+ recommended
- pip or conda
- Jupyter Notebook or JupyterLab

### Install

1. Clone the repository:
   git clone https://github.com/Thisara-Anjana/multiple_disease_prediction_system.git
   cd multiple_disease_prediction_system

2. Create a virtual environment (recommended):
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows PowerShell

3. Install dependencies:
   - If a requirements.txt exists:
     pip install -r requirements.txt
   - If not, install typical packages used in notebooks:
     pip install jupyterlab numpy pandas scikit-learn matplotlib seaborn

4. (Optional) If you use conda:
   conda create -n mdps python=3.9
   conda activate mdps
   pip install -r requirements.txt

## Running the notebooks

1. Start Jupyter:
   jupyter lab
   or
   jupyter notebook

2. Open the notebooks in the repository and run cells in order. Notebooks are designed to be run top-to-bottom:
   - Data preprocessing / exploration
   - Feature engineering
   - Model training and hyperparameter tuning
   - Evaluation and visualization
   - Inference / demo

If long-running training is included, consider sampling data or using a smaller configuration for quick experiments.

## Dataset

If datasets are included in the `data/` folder, verify license and usage terms before sharing. If large or sensitive datasets are not included, add instructions here describing how to obtain them (links, required credentials, or preprocessing steps).

Example:
- place raw CSV files in `data/raw/`
- run the "data_preparation.ipynb" notebook to produce `data/processed/`

## Modeling & results

Notebooks include experiments with one or more model types (e.g., logistic regression, tree-based models, and neural networks). Evaluation notebooks produce standard metrics (accuracy, precision, recall, F1, ROC-AUC) and visualizations to compare models. See the evaluation notebook for detailed plots and tables.

## Docker (optional)

If this repository includes a Dockerfile, you can build and run a container:

docker build -t mdps .
docker run -p 8888:8888 -v $(pwd):/workspace mdps

Adjust the Dockerfile and run commands to match the repository’s configuration.

## Recommendations / TODOs

- Add a `requirements.txt` (pip freeze > requirements.txt) for reproducible installs.
- Add a brief example notebook that demonstrates end-to-end inference on a small sample.
- If you plan to deploy, include a script or notebook that exports a model and shows how to load it for inference.

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repository.
2. Create a branch for your change.
3. Open a pull request with a clear description of changes.

Please include tests or a reproducible notebook snippet when adding models or data transforms.

## License

Add a license file (e.g., MIT, Apache-2.0) if you want to permit reuse. If unsure, add `LICENSE` with your preferred open-source license.

## Contact

Maintainer: Thisara-Anjana  
Repository: https://github.com/Thisara-Anjana/multiple_disease_prediction_system
