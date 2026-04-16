from pydantic import BaseModel
from pydantic_ai import Agent

from src.agents.generator_agent import GeneratorAgent
from src.memory.memory_module import MemoryModule

class RequirementInput(BaseModel):
    requirement: str

memory = MemoryModule()

class PlannerAgent(Agent[RequirementInput, str]):

    def __init__(self):
        super().__init__()
        self.generator = GeneratorAgent()

    def run(self, input: RequirementInput) -> str:

        requirement = input.requirement.strip()

        cached = memory.retrieve(requirement)
        if cached:
            print("Using cached result from memory")
            return cached

        print("Generating test cases using LLM...")

        result = self.generator.run(requirement)

        memory.save(requirement, result)

        print("LLM test case generation completed")

        return result









'''
Exexution flow

main.py
   ↓
TestCaseAgent
   ↓
PlannerAgent
   ↓
Memory check
   ↓
GeneratorAgent (LLM call)
   ↓
Mistral API
   ↓
AI generates test cases
   ↓
Memory save
   ↓
Return output
'''





'''
from pydantic import BaseModel
from pydantic_ai import Agent

from src.agents.parser_agent import ParserAgent
from src.agents.generator_agent import GeneratorAgent
from src.agents.validator_agent import ValidatorAgent
from src.memory.memory_module import MemoryModule
from src.tools.testcase_generator import TestCase

class RequirementInput(BaseModel):
    requirement: str

memory = MemoryModule()

class PlannerAgent(Agent[RequirementInput, list[TestCase]]):

    def __init__(self):
        super().__init__()
        self.parser = ParserAgent()
        self.generator = GeneratorAgent()
        self.validator = ValidatorAgent()

    def run(self, input: RequirementInput):
        cached = memory.retrieve(input.requirement)
        if cached:
            print("Using cached result from the memory")
            return cached

        parsed = self.parser.run(input)

        testcases = self.generator.run(parsed)

        validated = self.validator.run(testcases)

        memory.save(input.requirement, validated)

        return validated
'''
