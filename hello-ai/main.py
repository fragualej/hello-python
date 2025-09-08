from guidelines import run_guidelines_examples
from summarizing import run_summarizing_examples
from inferring import run_inferring_examples    

if __name__ == "__main__":
    # Principles of prompting
    # Principle 1: Write clear and specific instructions
    # Tactic 1: Use delimiters to clearly indicate distinct parts of the input
        # * Triple quotes: """ or '''
        # * Triple backticks: ```
        # * Angle brackets: < >
        # * HTML tags: <tag> </tag>

    # Run prompting guidelines examples
    #run_guidelines_examples()
    
    # Run summarizing examples
    #run_summarizing_examples()

    # Tactic 4: "Few-shot" prompting

    # Principle 2: Give the model time to "think"
        # Tactic 1: Specify the steps required to complete a task
        # Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion
    run_inferring_examples()