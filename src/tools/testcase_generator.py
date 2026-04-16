from typing import List
from pydantic import BaseModel

class TestCase(BaseModel):
    id:str
    description:str
    steps:list[str]
    expected_result:str

def generate_testcase(parsed_data: dict) -> List[TestCase]:

    cases = []
    # what users can does
    actions = parsed_data["actions"]
    # edge casess
    conditions = parsed_data["conditions"]

    if "login" in actions:

        cases.append(TestCase(
            id="TC01",
            description="Valid login",
            steps=[
                "Enter valid username",
                "Enter valid password",
                "Click login"
            ],
            expected_result="Login successful"
        ))

        if "invalid input" in conditions:
            cases.append(TestCase(
                id="TC02",
                description="Invalid login",
                steps=[
                    "Enter wrong username",
                    "Enter wrong password",
                    "Click login"
                ],
                expected_result="Error message displayed"
            ))

        if "empty fields" in conditions:
            cases.append(TestCase(
                id="TC03",
                description="Empty fields login",
                steps=[
                    "Leave username blank",
                    "Leave password blank",
                    "Click login"
                ],
                expected_result="Validation error"
            ))

    return cases

# Converting structured data - > testcases

"""
parser - > understands
Generator - > creates output
"""