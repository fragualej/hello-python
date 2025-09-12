from utils_dir.utils import print_separator
from models.claude_api import get_completion

def run_sentiment_demo():
    lamp_review = """
    Needed a nice lamp for my bedroom, and this one had 
    additional storage and not too high of a price point. 
    Got it fast.  The string to our lamp broke during the 
    transit and the company happily sent over a new one. 
    Came within a few days as well. It was easy to put 
    together.  I had a missing part, so I contacted their 
    support and they very quickly got me the missing piece! 
    Lumina seems to me to be a great company that cares 
    about their customers and products!!
    """

    print_separator("Sentiment (positive/negative)")
    prompt = f"""
    What is the sentiment of the following product review, 
    which is delimited with triple backticks?

    Review text: '''{lamp_review}'''
    """
    response = get_completion(prompt)
    print(response)

def run_inferring_examples():
    print_separator("INFERRING")
    run_sentiment_demo()

    