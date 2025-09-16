import os
from dotenv import load_dotenv
from pygeai.chat.clients import ChatClient

load_dotenv()

def chat(prompt, model=None):
    """Basic chat function matching documentation examples"""
    # Get model from env if not specified
    if model is None:
        model = os.getenv('GEAI_MODEL', 'gpt-4-turbo')

    # Create client and make request
    client = ChatClient()
    messages = [{"role": "user", "content": prompt}]

    response = client.chat_completion(
        model=model,
        messages=messages
    )

    return response

def display_assistant_list():
    """Retrieves and displays the assistant list with summary or full details"""
    try:
        from pygeai.organization.clients import OrganizationClient

        client = OrganizationClient()
        assistant_list = client.get_assistant_list(detail="full")  # Can change detail to "summary"
        print(assistant_list)
        return assistant_list
    except Exception as e:
        print(f"Error getting assistant list: {str(e)}")
        return f"Error: {str(e)}"

# Backward compatibility
def get_geai_completion(prompt, model=None, max_tokens=500):
    """Backward compatibility function"""
    return chat(prompt, model)