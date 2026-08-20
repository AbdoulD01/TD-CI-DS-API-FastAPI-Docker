name: CI - FastAPI

on:
  pull_request:
    branches:
      - main

  push:
    branches:
      - main
      - dev

  workflow_dispatch:

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-24.04

    steps:
      # Récupérer le code
      - name: Checkout code
        uses: actions/checkout@v4

      # Configurer Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      # Installer les dépendances
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip list

      # Lancer les tests
      - name: Run tests
        run: |
          export PYTHONPATH=$(pwd)
          python -m pytest --maxfail=1 --disable-warnings -q