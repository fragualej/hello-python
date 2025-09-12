import os
import argparse
from dotenv import load_dotenv
from models.claude_api import get_completion
from models.geai_api import get_geai_completion

# Load environment variables
load_dotenv()

class ModelSelector:
    """Utility class for selecting and managing AI models"""
    
    SUPPORTED_PROVIDERS = ["claude", "geai", "both"]
    CLAUDE_MODELS = ["claude-3-haiku-20240307", "claude-3-sonnet-20240229", "claude-3-opus-20240229"]
    GEAI_MODELS = ["gpt-4", "gpt-3.5-turbo", "claude-3-haiku", "claude-3-sonnet"]
    
    def __init__(self):
        self.provider = os.getenv("DEFAULT_MODEL_PROVIDER", "claude")
        self.claude_model = os.getenv("DEFAULT_CLAUDE_MODEL", "claude-3-haiku-20240307")
        self.geai_model = os.getenv("DEFAULT_GEAI_MODEL", "gpt-4")
    
    def set_provider(self, provider):
        """Set the model provider"""
        if provider in self.SUPPORTED_PROVIDERS:
            self.provider = provider
            print(f"✅ Model provider set to: {provider}")
        else:
            print(f"❌ Unsupported provider: {provider}")
            print(f"Supported providers: {', '.join(self.SUPPORTED_PROVIDERS)}")
    
    def set_claude_model(self, model):
        """Set the Claude model"""
        if model in self.CLAUDE_MODELS:
            self.claude_model = model
            print(f"✅ Claude model set to: {model}")
        else:
            print(f"❌ Unsupported Claude model: {model}")
            print(f"Supported Claude models: {', '.join(self.CLAUDE_MODELS)}")
    
    def set_geai_model(self, model):
        """Set the GEAI model"""
        if model in self.GEAI_MODELS:
            self.geai_model = model
            print(f"✅ GEAI model set to: {model}")
        else:
            print(f"❌ Unsupported GEAI model: {model}")
            print(f"Supported GEAI models: {', '.join(self.GEAI_MODELS)}")
    
    def get_completion(self, prompt, max_tokens=500):
        """Get completion using the selected provider and model"""
        if self.provider == "claude":
            return self._get_claude_completion(prompt, max_tokens)
        elif self.provider == "geai":
            return self._get_geai_completion(prompt, max_tokens)
        elif self.provider == "both":
            return self._get_both_completions(prompt, max_tokens)
        else:
            return f"Error: Unknown provider '{self.provider}'"
    
    def _get_claude_completion(self, prompt, max_tokens):
        """Get Claude completion"""
        try:
            # Update the Claude API to use the selected model
            return get_completion(prompt)  # Note: Claude API uses fixed model for now
        except Exception as e:
            return f"Claude Error: {str(e)}"
    
    def _get_geai_completion(self, prompt, max_tokens):
        """Get GEAI completion"""
        try:
            return get_geai_completion(prompt, model=self.geai_model, max_tokens=max_tokens)
        except Exception as e:
            return f"GEAI Error: {str(e)}"
    
    def _get_both_completions(self, prompt, max_tokens):
        """Get completions from both providers"""
        claude_response = self._get_claude_completion(prompt, max_tokens)
        geai_response = self._get_geai_completion(prompt, max_tokens)
        
        return {
            "claude": claude_response,
            "geai": geai_response
        }
    
    def print_current_config(self):
        """Print current model configuration"""
        print("🤖 Current Model Configuration:")
        print(f"  Provider: {self.provider}")
        print(f"  Claude Model: {self.claude_model}")
        print(f"  GEAI Model: {self.geai_model}")
        print()
    
    def print_available_models(self):
        """Print all available models"""
        print("📋 Available Models:")
        print(f"  Providers: {', '.join(self.SUPPORTED_PROVIDERS)}")
        print(f"  Claude Models: {', '.join(self.CLAUDE_MODELS)}")
        print(f"  GEAI Models: {', '.join(self.GEAI_MODELS)}")
        print()

def parse_model_args():
    """Parse command-line arguments for model selection"""
    parser = argparse.ArgumentParser(description="AI Model Selection")
    parser.add_argument("--provider", "-p", choices=ModelSelector.SUPPORTED_PROVIDERS,
                       help="Model provider (claude, geai, both)")
    parser.add_argument("--claude-model", "-c", choices=ModelSelector.CLAUDE_MODELS,
                       help="Claude model to use")
    parser.add_argument("--geai-model", "-g", choices=ModelSelector.GEAI_MODELS,
                       help="GEAI model to use")
    parser.add_argument("--list-models", "-l", action="store_true",
                       help="List available models")
    parser.add_argument("--config", action="store_true",
                       help="Show current configuration")
    
    return parser.parse_known_args()  # Use parse_known_args to allow other arguments

# Global model selector instance
model_selector = ModelSelector()

def get_model_completion(prompt, max_tokens=500):
    """Global function to get completion using current model configuration"""
    return model_selector.get_completion(prompt, max_tokens)

def set_model_provider(provider):
    """Global function to set model provider"""
    model_selector.set_provider(provider)

def print_model_info():
    """Global function to print model information"""
    model_selector.print_current_config()
    model_selector.print_available_models()