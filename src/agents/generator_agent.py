from pydantic_ai import Agent
from src.tools.llm_testcase_generator import generate_testcases_llm

class GeneratorAgent(Agent[str,str]):

    def run(self, requirement: str):
        return generate_testcases_llm(requirement)