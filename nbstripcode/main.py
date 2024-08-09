import argparse
import json
import re

def strip_code_from_notebook(notebook_filepath):
    match = re.match(r"^(.*[\\/])", notebook_filepath)
    notebook_dir = match.group(1) if match else ""

    with open(notebook_filepath, mode="r", encoding="utf-8") as f:
        notebook = json.loads(f.read())

    modified_cells = []
    cells = notebook.get("cells", [])
    for cell in cells:
        if cell.get("cell_type") != "code":
            modified_cells.append(cell)
            continue

        if not cell.get("source"):
            modified_cells.append(cell)
            continue

        cell["source"] = [""]
        modified_cells.append(cell)

    modified_notebook = {
        "cells": modified_cells,
        "metadata": notebook.get("metadata"),
        "nbformat": notebook.get("nbformat"),
        "nbformat_minor": notebook.get("nbformat_minor")
    }

    with open(f"{notebook_dir}modified_notebook.ipynb", "w", encoding="utf-8") as file:
        file.write(json.dumps(modified_notebook))

def main():
    parser = argparse.ArgumentParser(
        description="Remove the code, save the outputs!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("notebook_filepath", type=str, help="Location of notebook to 'clean'")
    args = parser.parse_args()

    strip_code_from_notebook(args.notebook_filepath)

if __name__ == "__main__":
    main()