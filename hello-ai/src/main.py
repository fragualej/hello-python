import sys
import os
sys.path.append(os.path.dirname(__file__))

from agents.guidelines import run_guidelines_examples
from agents.summarizing import run_summarizing_examples
from agents.inferring import run_inferring_examples

if __name__ == "__main__":
    # Principles of prompting
    # Principle 1: Write clear and specific instructions
    # Run prompting guidelines examples
    run_guidelines_examples()

    # Principle 2: Give the model time to "think"
        # Tactic 1: Specify the steps required to complete a task
        # Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion

    # Run summarizing examples
    # run_summarizing_examples()

    # run_inferring_examples()