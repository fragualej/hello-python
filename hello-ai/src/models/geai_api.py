"""
Simple GEAI API implementation
"""

import os
from dotenv import load_dotenv
from pygeai.chat.clients import ChatClient

load_dotenv()

def get_geai_completion(prompt, model=None, max_tokens=500):
    """Generate text using GEAI ChatClient"""
    # Get configuration
    api_key = os.getenv('GEAI_API_KEY')
    base_url = os.getenv('GEAI_API_BASE_URL')
    project_id = os.getenv('GEAI_PROJECT_ID')

    if not api_key:
        return "Error: GEAI_API_KEY not found"

    if model is None:
        model = os.getenv('GEAI_MODEL', 'saia:assistant:PromptTestAgent')

    # Create client and make request
    client = ChatClient()
    response = client.chat_completion(
        model=model,
        messages={"role": "user", "content": prompt},
        max_tokens=max_tokens
    )

    # Return response
    if isinstance(response, dict):
        if 'error' in response:
            return f"Error: {response['error']['message']}"
        if 'choices' in response and response['choices']:
            return response['choices'][0]['message']['content']
        return str(response)

    if hasattr(response, 'choices') and response.choices:
        return response.choices[0].message.content

    return str(response)

def get_geai_completion_streaming(prompt, model=None, max_tokens=500):
    """Generate streaming text using GEAI ChatClient"""
    # Get configuration
    api_key = os.getenv('GEAI_API_KEY')
    base_url = os.getenv('GEAI_API_BASE_URL')
    project_id = os.getenv('GEAI_PROJECT_ID')

    if not api_key:
        yield "Error: GEAI_API_KEY not found"
        return

    if model is None:
        model = os.getenv('GEAI_MODEL', 'saia:assistant:PromptTestAgent')

    # Create client and make streaming request
    client = ChatClient()
    stream = client.chat_completion(
        model=model,
        messages={"role": "user", "content": prompt},
        max_tokens=max_tokens,
        stream=True
    )

    # Yield chunks
    for chunk in stream:
        if hasattr(chunk, 'choices') and chunk.choices:
            content = chunk.choices[0].delta.content
            if content:
                yield content
        elif isinstance(chunk, dict) and 'choices' in chunk:
            content = chunk['choices'][0].get('delta', {}).get('content')
            if content:
                yield content