import os
from dotenv import load_dotenv
from models.claude_api import get_completion
from models.geai_api import get_geai_completion

load_dotenv()

class ModelManager:
    def __init__(self):
        self.provider = os.getenv("MODEL_PROVIDER", "claude").lower()
        self.available = False
        
    def ping_model(self):
        """Test if the selected model is available and working"""
        test_prompt = "Say 'OK' if you can hear me."
        
        try:
            if self.provider == "claude":
                response = get_completion(test_prompt)
                if "Error" not in response and len(response) > 0:
                    self.available = True
                    print(f"✅ Claude is available")
                    return True
                else:
                    print(f"❌ Claude error: {response}")
                    return False
                    
            elif self.provider == "geai":
                response = get_geai_completion(test_prompt, max_tokens=10)
                if "Error" not in response and len(response) > 0:
                    self.available = True
                    print(f"✅ GEAI is available")
                    return True
                else:
                    print(f"❌ GEAI error: {response}")
                    return False
            else:
                print(f"❌ Unknown provider: {self.provider}")
                return False
                
        except Exception as e:
            print(f"❌ {self.provider.upper()} connection failed: {str(e)}")
            return False
    
    def get_completion(self, prompt, max_tokens=500):
        """Get completion from the selected provider"""
        if not self.available:
            return f"Error: {self.provider.upper()} is not available. Please check configuration."
            
        if self.provider == "claude":
            return get_completion(prompt)
        elif self.provider == "geai":
            return get_geai_completion(prompt, max_tokens=max_tokens)
        else:
            return f"Error: Unknown provider '{self.provider}'"

# Global instance
model_manager = ModelManager()