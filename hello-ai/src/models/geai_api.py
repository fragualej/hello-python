import os
from dotenv import load_dotenv
from pygeai.chat.clients import ChatClient
from pygeai.organization.clients import OrganizationClient

load_dotenv()

def chat(prompt):
    """Basic chat function matching documentation examples"""
    # Get model from env if not specified
    model = os.getenv('GEAI_MODEL')
    # Create client and make request
    client = ChatClient()
    messages = [{"role": "user", "content": prompt}]

    display_assistant_list()
    display_project_list()
    display_project_tokens('7dbedb31-f916-4865-8a14-a70c39d70239')

    response = client.chat_completion(
        model=model,
        messages=messages
    )

    return response

def display_assistant_list():
    """Retrieves and displays the assistant list with summary or full details"""
    client = OrganizationClient()
    assistant_list = client.get_assistant_list(detail="full")  # Can change detail to "summary"
    print(assistant_list)
    return assistant_list

def display_project_list():
    """
    Retrieves and displays the project list with optional filters.
    """
    client = OrganizationClient()
    project_list = client.get_project_list(detail="full", name="ProjectName")  # Change filters as needed
    print(project_list)

def display_project_tokens(project_id: str):
    """
    Retrieves and displays tokens for a specific project.
    """
    client = OrganizationClient()
    tokens = client.get_project_tokens(project_id=project_id)
    print(tokens)

# Backward compatibility
def get_geai_completion(prompt, model=None, max_tokens=500):
    """Backward compatibility function"""
    return chat(prompt, model)