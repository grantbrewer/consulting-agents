#!/usr/bin/env python3
"""
Test script for the Prompt Manager
Verifies that prompts can be loaded and formatted correctly
"""

import sys
from pathlib import Path

def test_prompt_manager():
    """Test the prompt manager functionality."""
    print("🧪 Testing Prompt Manager...")
    print("=" * 50)
    
    try:
        from prompt_manager import PromptManager, get_prompt_manager
        
        # Test basic initialization
        print("✅ Prompt manager imported successfully")
        
        # Create prompt manager instance
        manager = PromptManager()
        print("✅ Prompt manager initialized successfully")
        
        # Test global configuration
        global_config = manager.get_global_config()
        print(f"✅ Global config loaded: {global_config}")
        
        # Test system instructions
        system_instructions = manager.get_system_instructions()
        print(f"✅ System instructions loaded: {len(system_instructions)} sections")
        
        # Test agent listing
        agents = manager.list_available_agents()
        print(f"✅ Available agents: {len(agents)} agents")
        for agent in agents:
            print(f"   - {agent}")
        
        # Test agent prompt retrieval
        test_agent = "business_model_analyst"
        agent_prompt = manager.get_agent_prompt(test_agent)
        print(f"✅ Agent prompt for {test_agent} loaded")
        print(f"   System prompt length: {len(agent_prompt.system_prompt)}")
        print(f"   User prompt template length: {len(agent_prompt.user_prompt_template)}")
        print(f"   Token limit: {agent_prompt.token_limit}")
        
        # Test enhanced system prompt
        enhanced_prompt = manager.get_enhanced_system_prompt(test_agent)
        print(f"✅ Enhanced system prompt created: {len(enhanced_prompt)} characters")
        
        # Test prompt formatting
        formatted_prompt = manager.format_user_prompt(
            test_agent,
            company_name="Test Company",
            analysis_parameters='{"test": "value"}',
            dependency_outputs_section="No dependencies"
        )
        print(f"✅ User prompt formatted successfully: {len(formatted_prompt)} characters")
        
        # Test model name
        model_name = manager.get_model_name()
        print(f"✅ Model name: {model_name}")
        
        # Test token limits
        token_limit = manager.get_agent_token_limit(test_agent)
        print(f"✅ Token limit for {test_agent}: {token_limit}")
        
        # Test agent summary
        summary = manager.get_agent_summary()
        print(f"✅ Agent summary generated for {len(summary)} agents")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing prompt manager: {e}")
        return False

def test_yaml_loading():
    """Test YAML configuration loading."""
    print("\n📋 Testing YAML Configuration...")
    print("=" * 50)
    
    try:
        import yaml
        
        # Test YAML file loading
        with open("agent_prompts.yaml", 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        print("✅ YAML file loaded successfully")
        
        # Test required sections
        required_sections = ['global', 'system_instructions', 'agents', 'token_limits']
        for section in required_sections:
            if section in config:
                print(f"✅ Section '{section}' found")
            else:
                print(f"❌ Section '{section}' missing")
                return False
        
        # Test agents
        agents = config['agents']
        required_agents = [
            'business_model_analyst', 'market_researcher', 'competitive_analyst',
            'financial_analyst', 'risk_assessor', 'implementation_specialist',
            'strategy_storyteller', 'senior_partner'
        ]
        
        for agent in required_agents:
            if agent in agents:
                agent_config = agents[agent]
                if 'system_prompt' in agent_config and 'user_prompt_template' in agent_config:
                    print(f"✅ Agent '{agent}' configured correctly")
                else:
                    print(f"❌ Agent '{agent}' missing required fields")
                    return False
            else:
                print(f"❌ Agent '{agent}' not found")
                return False
        
        # Test global config
        global_config = config['global']
        if 'model' in global_config and global_config['model'] == 'gpt-5':
            print("✅ Global config: GPT-5 model configured")
        else:
            print("❌ Global config: GPT-5 model not configured")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing YAML configuration: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Prompt Manager Test Suite")
    print("=" * 60)
    
    # Test YAML loading
    yaml_ok = test_yaml_loading()
    
    if yaml_ok:
        # Test prompt manager
        manager_ok = test_prompt_manager()
        
        print("\n" + "=" * 60)
        if manager_ok:
            print("🎉 All tests passed! The Prompt Manager is working correctly.")
            print("\nNext steps:")
            print("1. Update the main consulting agent code to use the prompt manager")
            print("2. Test with a real consulting engagement")
            print("3. Customize prompts in agent_prompts.yaml as needed")
        else:
            print("⚠️  Some prompt manager tests failed.")
    else:
        print("\n❌ YAML configuration tests failed.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
