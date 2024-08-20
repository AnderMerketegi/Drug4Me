from langchain_experimental.agents.agent_toolkits import create_csv_agent
from agents.agent import Agent


class CSVAgent(Agent):

    def __init__(self, file_path: str = "data/PharmGKB/files/clinical_annotations.csv"):

        super().__init__()
        self.agent = create_csv_agent(self.llm, file_path, verbose=True, allow_dangerous_code=True, pipon_bad_lines='warn')

    def execute(self, query: dict | str):
        return self.agent.invoke(f"{self.guidelines}\n{query}")
