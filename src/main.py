from agents.testcase_agent import TestCaseAgent, RequirementInput

agent = TestCaseAgent()

req = RequirementInput(
    requirement="What is India"
)

print("FIRST RUN")
result1 = agent.run(req)
print(result1)

print("\nSECOND RUN")
result2 = agent.run(req)
print(result2)