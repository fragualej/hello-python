from string import Template

def create_prompt_template(priming, question, decorator):
    """
    Create a prompt template using the priming → question → decorator pattern
    
    Args:
        priming (str): Sets context and role
        question (str): Main instruction with $parameters
        decorator (str): Input formatting with $parameters
    
    Returns:
        Template: String template ready for substitution
    """
    template_text = f"""
{priming}

{question}

{decorator}
""".strip()
    
    return Template(template_text)

def get_prompt(template, **kwargs):
    """
    Generate prompt from template with parameters
    
    Args:
        template (Template): The prompt template
        **kwargs: Parameters to substitute in template
    
    Returns:
        str: Formatted prompt ready for AI model
    """
    return template.substitute(**kwargs)