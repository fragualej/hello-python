from .shared.base_template import create_prompt_template, get_prompt

# Single Review Summary Template
SINGLE_REVIEW_PRIMING = "Your task is to generate a short summary of a product review from an ecommerce site."
SINGLE_REVIEW_QUESTION = "Summarize the review below, delimited by triple backticks, in at most $max_words words."
SINGLE_REVIEW_DECORATOR = "Review: ```$review_content```"

SINGLE_REVIEW_TEMPLATE = create_prompt_template(
    SINGLE_REVIEW_PRIMING,
    SINGLE_REVIEW_QUESTION, 
    SINGLE_REVIEW_DECORATOR
)

def get_review_summary_prompt(review_content, max_words=30):
    """Generate review summary prompt"""
    return get_prompt(
        SINGLE_REVIEW_TEMPLATE,
        review_content=review_content.strip(),
        max_words=max_words
    )