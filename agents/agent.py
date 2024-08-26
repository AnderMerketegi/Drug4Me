import os
from dotenv import load_dotenv
from utils.utils import read_file
from langchain_groq import ChatGroq

from abc import ABC, abstractmethod


load_dotenv()


class Agent:

    def __init__(self):

        self.temperature = 0
        self.model = "llama3-70b-8192"
        self.llm = ChatGroq(temperature=self.temperature, model=self.model, api_key=os.environ["GROK_API_KEY"])
        self.guidelines = read_file("agents/prompts/guidelines.txt")

    @abstractmethod
    def execute(self, prompt: dict | str):
        pass
