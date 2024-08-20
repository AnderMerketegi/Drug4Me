import os
import json
import toml
import pandas as pd


def read_file(path: str):

    # toml file
    if path.endswith(".toml"):
        with open(path, "r") as f:
            return toml.load(f)
    # csv and tsv file
    elif path.endswith(".tsv") or path.endswith(".csv"):
        return pd.read_csv(path, sep=f"{'\t' if path.endswith('.tsv') else ','}", on_bad_lines='warn')
    # txt file
    elif path.endswith(".txt"):
        with open(path, "r") as f:
            return f.read()


def tsv_to_csv(tsv_path, csv_path):

    try:
        df = pd.read_csv(tsv_path, sep='\t')
        df.to_csv(csv_path, index=False)
        os.remove(tsv_path)
    except Exception as e:
        print(f"Error: {e}")
