import os
import time
import zipfile
import requests
from glob import glob
from io import BytesIO
from data.dataset import Dataset
from utils.utils import convert_files_to_csv


class EMA(Dataset):

    def __init__(self):

        super().__init__()
        self.properties = self.properties["ema"]
        self.data_path = self.properties["data_path"]
