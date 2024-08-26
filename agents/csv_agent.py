from langchain_experimental.agents.agent_toolkits import create_csv_agent
from agents.agent import Agent


class CSVAgent(Agent):

    def __init__(self, file_path: str = "data/PharmGKB/files/clinical_annotations.csv"):

        super().__init__()
        self.agent = create_csv_agent(self.llm, file_path, verbose=True, allow_dangerous_code=True)

    def set_table(self, table_path: str | list):
        self.agent = create_csv_agent(self.llm, table_path, verbose=True, allow_dangerous_code=True)

    def execute(self, query: dict | str):
        return self.agent.invoke(f"{self.guidelines}\n{query}")
