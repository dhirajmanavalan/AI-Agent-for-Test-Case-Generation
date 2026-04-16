from src.agents.planner_agent import PlannerAgent, RequirementInput

def test_agent():
    agent = PlannerAgent()

    req = RequirementInput(requirement="User login")

    result = agent.run(req)

    assert result is not None
    assert len(result) > 0

# Check: Entire pipeline works