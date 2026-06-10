from pydantic import BaseModel
from pydantic_ai import Agent

from src.agents.planner_agent import PlannerAgent
from src.tools.testcase_generator import TestCase


class RequirementInput(BaseModel):
    requirement: str

class TestCaseAgent(Agent[RequirementInput, list[TestCase]]):
    def __init__(self):
        '''Here initializing parent agent class I am
        -->TestCaseAgent is NOT doing work
        PlannerAgent is doing work
        '''
        super().__init__()
        self.planner = PlannerAgent()

    def run(self, input: RequirementInput):
        return self.planner.run(input)
