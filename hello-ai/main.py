import os
from dotenv import load_dotenv
import anthropic

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
    # Example for learning prompting
    text_1 = """
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

    text_2 = f"""
    The sun is shining brightly today, and the birds are
    singing. It's a beautiful day to go for a \ 
    walk in the park. The flowers are blooming, and the \ 
    trees are swaying gently in the breeze. People \ 
    are out and about, enjoying the lovely weather. \ 
    Some are having picnics, while others are playing \ 
    games or simply relaxing on the grass. It's a \ 
    perfect day to spend time outdoors and appreciate the \ 
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

    ```{text_1}```
    """
    
    # print("Prompt:")
    # print(prompt)
    # print("\n" + "="*50 + "\n")
    
    response = get_completion(prompt)
    print("AI Response:")
    print(response)