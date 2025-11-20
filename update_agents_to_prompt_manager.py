#!/usr/bin/env python3
"""
Script to update all agent classes to use the prompt manager instead of hardcoded prompts.
This will systematically replace the old prompt system with the new YAML-based system.
"""

import re
from pathlib import Path

def update_agent_class(agent_name: str, class_content: str) -> str:
    """Update a single agent class to use the prompt manager."""
    
    # Remove the old hardcoded prompt
    prompt_pattern = r'prompt = f""".*?"""'
    class_content = re.sub(prompt_pattern, '', class_content, flags=re.DOTALL)
    
    # Find the response creation section and update it
    response_pattern = r'response = self\.client\.chat\.completions\.create\(\s*model="gpt-5",\s*messages=\[\s*{"role": "system", "content": "[^"]*"},\s*{"role": "user", "content": prompt}\s*\],\s*max_completion_tokens=\d+\s*\)'
    
    replacement = f'''        # Use prompt manager for prompts
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        
        # Get agent prompt configuration
        agent_prompt = prompt_manager.get_agent_prompt("{agent_name}")
        system_prompt = prompt_manager.get_enhanced_system_prompt("{agent_name}")
        
        # Format user prompt with parameters
        user_prompt = prompt_manager.format_user_prompt(
            "{agent_name}",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f'Dependency Outputs: {{chr(10).join(dependency_outputs)}}' if dependency_outputs else ''
        )
        
        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {{"role": "system", "content": system_prompt}},
                {{"role": "user", "content": user_prompt}}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("{agent_name}")
        )'''
    
    class_content = re.sub(response_pattern, replacement, class_content, flags=re.DOTALL)
    
    return class_content

def update_strategy_consulting_agent():
    """Update the main strategy consulting agent file."""
    
    file_path = Path("strategy_consulting_agent.py")
    
    if not file_path.exists():
        print("❌ strategy_consulting_agent.py not found")
        return False
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # List of agents to update
    agents = [
        "business_model_analyst",
        "market_researcher", 
        "competitive_analyst",
        "financial_analyst",
        "risk_assessor",
        "implementation_specialist",
        "strategy_storyteller",
        "senior_partner"
    ]
    
    # Update each agent class
    for agent in agents:
        print(f"🔄 Updating {agent}...")
        
        # Find the class definition
        class_pattern = rf'class {agent.replace("_", "").title()}\(BaseAgent\):.*?async def execute\(.*?return output'
        class_match = re.search(class_pattern, content, flags=re.DOTALL)
        
        if class_match:
            old_class_content = class_match.group(0)
            new_class_content = update_agent_class(agent, old_class_content)
            content = content.replace(old_class_content, new_class_content)
            print(f"   ✅ {agent} updated successfully")
        else:
            print(f"   ⚠️  {agent} class not found or already updated")
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ All agent classes updated successfully!")
    return True

def main():
    """Main function to update the agent classes."""
    print("🚀 Updating Agent Classes to Use Prompt Manager")
    print("=" * 60)
    
    try:
        success = update_strategy_consulting_agent()
        
        if success:
            print("\n🎉 Update completed successfully!")
            print("\nNext steps:")
            print("1. Test the updated system: python test_prompt_manager.py")
            print("2. Run a test engagement: python example_usage.py")
            print("3. Verify that agents now produce content")
        else:
            print("\n❌ Update failed. Check the error messages above.")
            
    except Exception as e:
        print(f"\n❌ Error during update: {e}")
        return False
    
    print("=" * 60)
    return True

if __name__ == "__main__":
    main()
