"""Here Extracting actions and conditions for reqirements"""

def parse_requirements(requirement: str) -> dict:

    requirement = requirement.lower()

    actions = []
    conditions = []

    if "login" in requirement:
        actions.append("login")

    if "invalid" in requirement or "wrong" in requirement:
        conditions.append("invalid input")

    if "empty" in requirement or "blank" in requirement:
        conditions.append("empty fields")

    return {
        "actions": actions,
        "conditions": conditions
    }

# Here Converting raw text → structured meaning