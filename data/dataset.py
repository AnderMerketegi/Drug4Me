from abc import ABC, abstractmethod

from glob import glob
from utils.utils import read_file, create_folder, convert_files_to_csv
from io import BytesIO

import zipfile
import toml
import os
import requests


class Dataset:

    def __init__(self):
        self.properties = read_file("data/data.toml")
        self.data_path = ""

    @abstractmethod
    def download(self, convert: bool = True):
        """Download data"""
        create_folder(self.data_path)
        # Skip download if files already exist
        if len(glob(f"{self.data_path}*")) > 0:
            return
        # Make request
        response = requests.get(self.properties["download_path"])
        response.raise_for_status()
        # Get and save content
        if response.status_code == 200:
            self.save_byte_files(response.content, self.properties["download_path"], self.properties["data_path"])
            # Convert tsv files to csv format
            if convert:
                convert_files_to_csv(self.properties["data_path"])

    def save_byte_files(self, content: bytes, file_path: str, save_path: str):
        """Save bytes files obtained from request"""
        file_ext = os.path.splitext(file_path)[-1]
        # Unzip and extract contents
        if file_ext == ".zip":
            zip_file = zipfile.ZipFile(BytesIO(content))
            zip_file.extractall(save_path)
        else:
            with open(f"{save_path}{self.properties['name']}{file_ext}", "wb") as f:
                f.write(content)
