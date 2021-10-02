# TP1 IA UQAC

> Pour l'exécution du programme, **aucune librairie n'est nécessaire**. En revanche, pour la modification de celui-ci, il est préférable d'installer les librairies de développement dans un environnement virtuel.

## Prérequis

- Python (3.9 idéalement)
- PIP
## Installation

> /!\ Ce projet nécessite la librairie `virtualenv`. Pour l'installer, exécutez la commande `pip install virtualenv`.

1. Création de l'environment virtuel

```bash
python -m venv venv
```


2. Activer l'environment virtuel

```bash
venv/Scripts/activate      # Windows
. ./venv/Scripts/activate  # Linux
```

3. Installation des dépendances

```bash
pip install -r requirements-dev.txt
```

Et voila !

Il ne reste plus qu'a lancer le fichier `main_thread.py`