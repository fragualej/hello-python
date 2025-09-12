import os
from dotenv import load_dotenv
from pygeai.core.base.session import get_session
from pygeai.chat.clients import ChatClient
from pygeai.core.common.exceptions import GEAIException

# Load environment variables
load_dotenv()

def get_geai_completion(prompt, model="gpt-4", max_tokens=500):
    """Generate text using GEAI API"""
    try:
        # Create chat client (no session needed - it uses configured credentials)
        chat_client = ChatClient()
        
        # Generate completion
        messages = [{"role": "user", "content": prompt}]
        response = chat_client.chat_completion(
            model=model,
            messages=messages,
            max_tokens=max_tokens
        )
        
        # Extract content from response
        if hasattr(response, 'choices') and response.choices:
            return response.choices[0].message.content
        elif isinstance(response, dict):
            return response.get("content", "No response content")
        else:
            return str(response)
    except GEAIException as e:
        return f"GEAI API Error: {str(e)}"
    except Exception as e:
        return f"GEAI Unexpected Error: {str(e)}"

def get_geai_models():
    """Get available GEAI models"""
    try:
        chat_client = ChatClient()
        # For now return common models - actual model list API might differ
        return ["gpt-4", "gpt-3.5-turbo", "claude-3-haiku", "claude-3-sonnet"]
    except Exception as e:
        return f"Error getting models: {str(e)}"

def get_geai_completion_streaming(prompt, model="gpt-4", max_tokens=500):
    """Generate text using GEAI API with streaming"""
    try:
        chat_client = ChatClient()
        
        # Use streaming completion
        messages = [{"role": "user", "content": prompt}]
        response = chat_client.chat_completion(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            stream=True
        )
        
        # Stream the response
        for chunk in response:
            if hasattr(chunk, 'choices') and chunk.choices:
                content = chunk.choices[0].delta.content
                if content:
                    yield content
    except Exception as e:
        yield f"GEAI Streaming Error: {str(e)}"