import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlProject"


list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/mlProject/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
]