from utils_dir.utils import print_separator
from api.claude_api import get_completion

def text_summarization_demo():
    """Demonstrate text summarization using clear instructions"""
    print_separator("TEXT SUMMARIZATION")
    text = f"""
    You should express what you want a model to do by 
    providing instructions that are as clear and 
    specific as you can possibly make them. 
    This will guide the model towards the desired output, 
    and reduce the chances of receiving irrelevant 
    or incorrect responses. Don't confuse writing a 
    clear prompt with writing a short prompt. 
    In many cases, longer prompts provide more clarity 
    and context for the model, which can lead to 
    more detailed and relevant outputs.
    """
    prompt = f"""
    Summarize the text delimited by triple backticks 
    into a single sentence.
    ```{text}```
    """
    response = get_completion(prompt)
    print(response)

def json_generation_demo():
    """Demonstrate structured output generation"""
    print_separator("JSON GENERATION")
    prompt = f"""
    Generate a list of three made-up book titles along 
    with their authors and genres. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre.
    """
    response = get_completion(prompt)
    print(response)

def instruction_detection_demo():
    """Demonstrate instruction detection in different texts"""
    print_separator("INSTRUCTION DETECTION - TEA MAKING")
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
    then simply write "No steps provided."

    ```{text_1}``` 
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

def run_guidelines_examples():
    """Run all prompting guidelines examples"""
    text_summarization_demo()
    json_generation_demo()
    instruction_detection_demo()