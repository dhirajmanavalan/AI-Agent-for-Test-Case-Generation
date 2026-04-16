from pydantic_ai import Agent
from src.tools.coverage_checker import validate_testcases
from src.tools.testcase_generator import TestCase

class ValidatorAgent(Agent[list[TestCase], list[TestCase]]):

    def run(self, testcases: list[TestCase]):
        return validate_testcases(testcases)