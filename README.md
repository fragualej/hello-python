# Hello AI - Python Prompting Course

A Python project for learning AI prompting techniques using Claude AI's API. This repository contains practical examples and exercises for understanding how to craft effective prompts for AI language models.

## Overview

This project demonstrates:
- Basic AI prompting concepts
- Text processing and instruction following  
- API integration with Anthropic's Claude
- Local AI model usage with Hugging Face Transformers
- Practical examples of prompt engineering

## Features

- **Prompt Engineering Examples**: Learn how to structure prompts for better AI responses
- **Text Analysis**: Process and analyze text using AI assistance  
- **API Integration**: Direct connection to Claude's API for real-time responses
- **Local AI Models**: GPT-2 and other Hugging Face models running locally
- **Text Summarization**: Advanced summarization techniques
- **Instruction Detection**: Identify and format step-by-step instructions
- **Learning Exercises**: Hands-on examples for prompt optimization

## Setup

### Prerequisites
- Python 3.12+ 
- Anthropic API key
- Hugging Face account (optional, for private models)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/fragualej/hello-python.git
cd hello-python
```

2. Set up virtual environment:
```bash
cd hello-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```bash
# Anthropic Claude API
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Hugging Face Token (optional, for local models)
HF_TOKEN=your_huggingface_token_here
```

## Usage

### Available Scripts

**Interactive Chat with Local GPT-2:**
```bash
python main.py
```

**Text Summarization Examples:**
```bash
python summarizing.py
```

**Content Analysis and Guidelines:**
```bash
python guidelines.py
```

**Text Inference Examples:**
```bash
python inferring.py
```

The scripts demonstrate:
- How to structure prompts for instruction following
- Text analysis and processing using both local and API models
- Advanced summarization techniques
- Error handling for API calls
- Local AI model integration

## Examples

The project includes examples of:
- **Local AI Chat**: Interactive conversations with GPT-2 model
- **Text Summarization**: Multiple summarization strategies and techniques
- **Instruction Detection**: Identifying and reformatting step-by-step instructions
- **Text Classification**: Analyzing different types of content
- **Content Guidelines**: Moderation and content analysis
- **Prompt Optimization**: Techniques for getting better AI responses

## Learning Objectives

- Understand prompt structure and formatting
- Learn to write clear, specific instructions for AI
- Practice with real API interactions
- Explore different prompting strategies

## Contributing

This is a learning project. Feel free to fork and experiment with your own prompting examples!

## License

This project is for educational purposes.