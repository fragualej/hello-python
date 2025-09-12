from utils.utils import print_separator
from models.geai_api import get_geai_completion, get_geai_models, get_geai_completion_streaming

def geai_models_demo():
    """Display available GEAI models"""
    print_separator("GEAI AVAILABLE MODELS")
    
    print("🔍 Fetching available models...")
    models = get_geai_models()
    
    if isinstance(models, str) and "Error" in models:
        print(f"❌ {models}")
    else:
        print("✅ Available models:")
        for model in models if isinstance(models, list) else [models]:
            print(f"  - {model}")
    print()

def geai_completion_demo():
    """Demonstrate GEAI text completion"""
    print_separator("GEAI TEXT COMPLETION")
    
    prompt = """
    Write a haiku about artificial intelligence and the future of technology.
    Make it inspiring and optimistic.
    """
    
    print("📝 Prompt:")
    print(prompt.strip())
    print()
    
    print("🤖 GEAI Response:")
    response = get_geai_completion(prompt, model="gpt-4", max_tokens=150)
    print(response)
    print()

def geai_streaming_demo():
    """Demonstrate GEAI streaming response"""
    print_separator("GEAI STREAMING RESPONSE")
    
    prompt = """
    Explain quantum computing in 3 short paragraphs for a general audience.
    """
    
    print("📝 Prompt:")
    print(prompt.strip())
    print()
    
    print("🌊 GEAI Streaming Response:")
    try:
        for chunk in get_geai_completion_streaming(prompt, model="gpt-4", max_tokens=300):
            print(chunk, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"Streaming error: {e}")
    print()

def geai_comparison_demo():
    """Compare different GEAI models on the same task"""
    print_separator("GEAI MODEL COMPARISON")
    
    prompt = """
    Summarize the key benefits of renewable energy in exactly 2 sentences.
    """
    
    print("📝 Prompt:")
    print(prompt.strip())
    print()
    
    models_to_test = ["gpt-4", "gpt-3.5-turbo"]
    
    for model in models_to_test:
        print(f"🤖 Model: {model}")
        response = get_geai_completion(prompt, model=model, max_tokens=100)
        print(response)
        print()

def run_geai_demo():
    """Run all GEAI demonstration functions"""
    print_separator("GEAI INTEGRATION DEMO")
    geai_models_demo()
    geai_completion_demo()
    geai_streaming_demo()
    geai_comparison_demo()
    print_separator("GEAI DEMO COMPLETE")