c#!/usr/bin/env python3
"""
Debug script to test the API call and see what's happening with the agents.
"""

import os
import json
from prompt_manager import PromptManager

def test_api_call():
    """Test a simple API call to see if it works."""
    print("🧪 Testing OpenAI API Call...")
    print("=" * 50)
    
    try:
        # Get API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ OPENAI_API_KEY not set")
            return False
        
        print(f"✅ API key found: {api_key[:8]}...")
        
        # Test prompt manager
        prompt_manager = PromptManager()
        print("✅ Prompt manager initialized")
        
        # Get prompts
        system_prompt = prompt_manager.get_enhanced_system_prompt("business_model_analyst")
        user_prompt = prompt_manager.format_user_prompt(
            "business_model_analyst",
            company_name="Test Company",
            analysis_parameters='{"test": "value"}',
            dependency_outputs_section="No dependencies"
        )
        
        print(f"✅ System prompt length: {len(system_prompt)}")
        print(f"✅ User prompt length: {len(user_prompt)}")
        
        # Test OpenAI client
        import openai
        client = openai.OpenAI(api_key=api_key)
        print("✅ OpenAI client created")
        
        # Make API call
        print("📡 Making API call...")
        response = client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("business_model_analyst")
        )
        
        print("✅ API call successful!")
        print(f"📝 Response content length: {len(response.choices[0].message.content)}")
        print(f"📝 First 200 chars: {response.choices[0].message.content[:200]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function."""
    print("🚀 OpenAI API Debug Test")
    print("=" * 60)
    
    success = test_api_call()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 API test successful! The issue might be elsewhere.")
    else:
        print("❌ API test failed. Check the error above.")
    print("=" * 60)

if __name__ == "__main__":
    main()
