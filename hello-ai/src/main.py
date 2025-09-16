import sys
import os
sys.path.append(os.path.dirname(__file__))

from agents.guidelines import run_guidelines_examples
from agents.summarizing import run_summarizing_examples
from agents.inferring import run_inferring_examples
from utils.model_manager import get_chat_response

def main():
    """Main function with model availability check"""

    import os
    provider = os.getenv("MODEL_PROVIDER", "claude").upper()

    print("Starting AI Demo")
    print(f"Using {provider} provider")
    print()

    # Test basic chat functionality
    print("Testing basic chat...")
    response = get_chat_response("Hello, can you introduce yourself?")
    print(f"Response: {response}")
    print()

    # Run prompting guidelines examples
    run_guidelines_examples()

    # Run summarizing examples
    # run_summarizing_examples()

    # run_inferring_examples()

if __name__ == "__main__":
    main()