from mistralai.client import Mistral
from src.utils.config import MISTRAL_API_KEY

client = Mistral(api_key=MISTRAL_API_KEY)

def generate_testcases_llm(requirement : str):

    prompt = f"""
    You are a QA expert.

    Generate test cases for the following requirement:
    {requirement}

    Format:
    - ID
    - Description
    - Steps
    - Expected Result
    """

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role":"user", "content": prompt
            }
        ]
    )
    return response.choices[0].message.content