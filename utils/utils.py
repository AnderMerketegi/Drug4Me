import os
import json
import toml
from glob import glob
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
    # xlsx file
    elif path.endswith(".xlsx"):
        return pd.read_excel(path)


def to_csv(file_path, csv_path):
    try:
        df = read_file(file_path)
        df.to_csv(csv_path, index=False)
        os.remove(file_path)
    except Exception as e:
        print(f"Error: {e}")


def convert_files_to_csv(path):

    accepted_formats = [".tsv", ".xlsx"]
    convertible_files = [file for file in glob(path + "*") if os.path.splitext(file)[-1] in accepted_formats]
    for file in convertible_files:
        to_csv(file, f"{os.path.splitext(file)[0]}.csv")


def create_folder(path: str = ""):

    if not os.path.exists(path):
        os.makedirs(path)