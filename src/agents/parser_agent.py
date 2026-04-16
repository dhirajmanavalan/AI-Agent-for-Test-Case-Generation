from pydantic import BaseModel
from pydantic_ai import Agent
from src.tools.requirement_parser import parse_requirements

class RequirementInput(BaseModel):
    requirement: str

class ParserAgent(Agent[RequirementInput, dict]):

    def run(self, input: RequirementInput):
        return parse_requirements(input.requirement)