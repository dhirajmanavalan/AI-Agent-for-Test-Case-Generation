from src.tools.requirement_parser import parse_requirements

def test_parser():
    result = parse_requirements("User login with empty fields")

    assert "login" in result["actions"]
    assert "empty fields" in result["conditions"]

# Check: Parser correctly understands input