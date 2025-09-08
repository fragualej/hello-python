# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python AI project that uses Hugging Face Transformers for local AI text generation. The codebase consists of:
- `main.py`: Interactive chat application using GPT-2 model locally
- `.env`: Environment variables file (optional for HF tokens)
- `venv/`: Python virtual environment with dependencies

## Development Setup

### Environment Setup
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies (if needed)
pip install transformers huggingface_hub numpy regex safetensors tokenizers python-dotenv
```

### Environment Variables
No API key required for basic usage. Optional `.env` variables:
- `HF_TOKEN`: Hugging Face token for private models (optional)

### Running the Application
```bash
# Activate virtual environment first
source venv/bin/activate

# Run the interactive chat application
python main.py
```

The first run will download the GPT-2 model (~500MB) automatically.

## Dependencies

Install all dependencies with:
```bash
pip install -r requirements.txt
```

Core packages:
- `transformers` (4.56.0) - Hugging Face transformers library
- `anthropic` (0.66.0) - Claude API client
- `huggingface_hub` - Model hub integration
- `python-dotenv` - Environment variable management
- `torch` - PyTorch for local models
- Supporting packages: `numpy`, `regex`, `safetensors`, `tokenizers`

## Python Version

Python 3.12.3 is used for this project.