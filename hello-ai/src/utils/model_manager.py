import os
from dotenv import load_dotenv
from models.claude_api import get_completion
from models.geai_api import chat

load_dotenv()

def get_chat_response(prompt):
    provider = os.getenv("MODEL_PROVIDER", "claude").lower()

    if provider == "claude":
        return get_completion(prompt)
    elif provider == "geai":
        return chat(prompt)
    else:
        return f"Error: Unknown provider '{provider}'"