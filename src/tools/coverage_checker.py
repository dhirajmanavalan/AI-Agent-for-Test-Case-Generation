def validate_testcases(testcases: list):
    unique_cases = []

    # Duplicates can be removed using seen...
    seen_description = set()

    for tc in testcases:
        desc = tc.description.strip().lower()

        if desc not in seen_description:
            unique_cases.append(tc)
            seen_description.add(desc)

    description = [tc.description.lower() for tc in unique_cases]

    # Coverage checker
    has_valid = any("valid login" in d for d in description)
    has_invalid = any("invalid login" in d for d in description)

    if not has_valid:
        print("Warning: Missing valid test case")

    if not has_invalid:
        print("Warning: Missing invalid test case")

    return unique_cases