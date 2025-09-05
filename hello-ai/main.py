import os
from dotenv import load_dotenv
import anthropic
from utils import print_separator

# Load environment variables
load_dotenv()

def get_completion(prompt):
    """Get completion from Claude API"""
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


if __name__ == "__main__":
    # Principles  of prompting
    # Principle 1: Write clear and specific instructions
    # Tactic 1: Use delimiters to clearly indicate distinct parts of the input
        # * Triple quotes: """ or '''
        # * Triple backticks: ```
        # * Angle brackets: < >
        # * HTML tags: <tag> </tag>

    print_separator("TEXT SUMMARIZATION")
    text = f"""
    You should express what you want a model to do by \
    providing instructions that are as clear and \
    specific as you can possibly make them. \
    This will guide the model towards the desired output, \
    and reduce the chances of receiving irrelevant \
    or incorrect responses. Don't confuse writing a \
    clear prompt with writing a short prompt. \
    In many cases, longer prompts provide more clarity \
    and context for the model, which can lead to \
    more detailed and relevant outputs.
    """
    prompt = f"""
    Summarize the text delimited by triple backticks \
    into a single sentence.
    ```{text}```
    """
    response = get_completion(prompt)
    print(response)

    print_separator("JSON GENERATION")
    # Tactic 2: Ask for structured output
    prompt = f"""
    Generate a list of three made-up book titles along \
    with their authors and genres. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre.
    """
    response = get_completion(prompt)
    print(response)

    print_separator("INSTRUCTION DETECTION - TEA MAKING")
    # Tactic 3: Ask the model to check whether conditions are met
    text_1 = f"""
    Making a cup of tea is easy! First, you need to get some
    water boiling. While that's happening, 
    grab a cup and put a tea bag in it. Once the water is 
    hot enough, just pour it over the tea bag. 
    Let it sit for a bit so the tea can steep. After a 
    few minutes, take out the tea bag. If you 
    like, you can add some sugar or milk to taste.
    And that's it! You've got yourself a delicious
    cup of tea to enjoy.
    """
    prompt = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions,
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions,
    then simply write \"No steps provided.\"

    \"\"\"{text_1}\"\"\"
    """
    response = get_completion(prompt)
    print(response)

    print_separator("INSTRUCTION DETECTION - NATURE DESCRIPTION")
    text_2 = f"""
    The sun is shining brightly today, and the birds are
    singing. It's a beautiful day to go for a
    walk in the park. The flowers are blooming, and the
    trees are swaying gently in the breeze. People
    are out and about, enjoying the lovely weather.
    Some are having picnics, while others are playing
    games or simply relaxing on the grass. It's a
    perfect day to spend time outdoors and appreciate the
    beauty of nature.
    """
    
    prompt = f"""
    You will be provided with text delimited by triple quotes. 
    If it contains a sequence of instructions, 
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, 
    then simply write "No steps provided."

    ```{text_2}```
    """
    response = get_completion(prompt)
    print(response)


    # Tactic 4: "Few-shot" prompting

    # Principle 2: Give the model time to "think"
        # Tactic 1: Specify the steps required to complete a task
        # Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion