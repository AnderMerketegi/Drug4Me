import os
import time
from glob import glob
import pandas as pd
import requests
import zipfile
from io import BytesIO
from data.data import Data
from sqlalchemy import create_engine
from utils.utils import read_file, tsv_to_csv
from langchain_community.utilities import SQLDatabase


class PharmGKB(Data):

    def __init__(self):

        super().__init__()
        self.properties = self.properties["pharmgkb"]

    def download(self, convert_to_csv=True):

        # Skip download if files exist
        if len(glob(self.properties["data_path"] + "*sv")) > 0:
            print("-- Skipping data download --\n")
            return

        # Make request
        response = requests.get(self.properties["download_path"])
        response.raise_for_status()
        # Get content and unzip file
        if response.status_code == 200:
            zip_file = zipfile.ZipFile(BytesIO(response.content))
            zip_file.extractall(self.properties["data_path"])

            time.sleep(3)

            # Convert tsv files to csv format
            if convert_to_csv:
                csv_files = glob(f"{self.properties["data_path"]}*.tsv")
                [tsv_to_csv(file, f"{os.path.splitext(file)[0]}.csv") for file in csv_files]
            return

    def tsv_to_db(self):

        data = read_file(os.path.join(self.properties["data_path"], "clinical_ann_alleles.tsv"))

        try:
            engine = create_engine("sqlite:///data/PharmGKB/files/pharmgkb.db")
            data.to_sql("pharmagkb", engine, index=False)
        except ValueError:
            print("Database already exists.")
