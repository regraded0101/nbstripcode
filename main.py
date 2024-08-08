import argparse
import json
import re

parser = argparse.ArgumentParser(
    description="Remove the code, save the outputs!",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("notebook_filepath", type=str, help="Location of notebook to 'clean'")
args = vars(parser.parse_args())


path = args["notebook_filepath"]
match = re.match(r"^(.*[\\/])", path)
notebook_dir = match.group(1) if match else ""

with open(args["notebook_filepath"], mode="r", encoding="utf-8") as f:
    notebook = json.loads(f.read())

metadata = notebook.get("metadata")
nbformat = notebook.get("nbformat")
nbformat_minor = notebook.get("nbformat_minor")

modified_cells = []
cells = notebook.get("cells")
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
    "metadata": metadata,
    "nbformat": nbformat,
    "nbformat_minor": nbformat_minor
}

print(notebook_dir)
with open(f"{notebook_dir}modified_notebook.ipynb", "w") as file:
    file.write(json.dumps(modified_notebook))