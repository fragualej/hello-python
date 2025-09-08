import os
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv()

def get_completion(prompt):
    """Generate text using Claude API"""
    try:
        client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"Claude API Error: {str(e)}"