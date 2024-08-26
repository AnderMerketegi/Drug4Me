import os
import time
from glob import glob
import pandas as pd
import requests
import zipfile
from io import BytesIO
from data.dataset import Dataset
from sqlalchemy import create_engine
from utils.utils import read_file, convert_files_to_csv
from langchain_community.utilities import SQLDatabase


class PharmGKB(Dataset):

    def __init__(self):

        super().__init__()
        self.properties = self.properties["pharmgkb"]
        self.data_path = self.properties["data_path"]

    def tsv_to_db(self):

        data = read_file(os.path.join(self.properties["data_path"], "clinical_ann_alleles.tsv"))

        try:
            engine = create_engine("sqlite:///data/PharmGKB/files/pharmgkb.db")
            data.to_sql("pharmagkb", engine, index=False)
        except ValueError:
            print("Database already exists.")
