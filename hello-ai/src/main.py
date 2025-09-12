import sys
import os
sys.path.append(os.path.dirname(__file__))

from agents.guidelines import run_guidelines_examples
from agents.summarizing import run_summarizing_examples
from agents.inferring import run_inferring_examples
from agents.geai_demo import run_geai_demo
from utils.model_manager import model_manager

def main():
    """Main function with model availability check"""

    print("🚀 Starting AI Demo")
    print(f"📡 Testing {model_manager.provider.upper()} availability...")

    # Ping the model to check availability
    if not model_manager.ping_model():
        print()
        print("💡 Suggestion: Update MODEL_PROVIDER in your .env file")
        print("   - For Claude: MODEL_PROVIDER=\"claude\"")
        print("   - For GEAI: MODEL_PROVIDER=\"geai\"")
        print()
        return

    print(f"🤖 Using {model_manager.provider.upper()} provider")
    print()

    # Run prompting guidelines examples
    run_guidelines_examples()

    # Run GEAI-specific demonstrations (only if GEAI is selected)
    if model_manager.provider == "geai":
        run_geai_demo()

    # Run summarizing examples
    # run_summarizing_examples()

    # run_inferring_examples()

if __name__ == "__main__":
    main()