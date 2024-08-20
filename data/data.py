from utils.utils import read_file
import toml


class Data:

    def __init__(self):
        self.properties = read_file("data/data.toml")
