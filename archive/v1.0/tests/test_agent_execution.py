#!/usr/bin/env python3
"""
Test script to debug agent execution step by step.
"""

import os
import asyncio
from pathlib import Path
from strategy_consulting_agent import BusinessModelAnalyst

async def test_agent_execution():
    """Test a single agent execution to see what's happening."""
    print("🧪 Testing Agent Execution Step by Step...")
    print("=" * 60)
    
    try:
        # Get API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ OPENAI_API_KEY not set")
            return False
        
        print("✅ API key found")
        
        # Create test directory
        test_dir = Path("./test_agent_debug")
        test_dir.mkdir(exist_ok=True)
        
        # Create agent
        print("🤖 Creating BusinessModelAnalyst agent...")
        agent = BusinessModelAnalyst(api_key, "Test Company", test_dir)
        print("✅ Agent created successfully")
        
        # Test parameters
        parameters = {
            "analysis_brief": "Test analysis brief",
            "engagement_type": "test",
            "analysis_depth": "test"
        }
        
        print("📝 Testing agent execution...")
        print(f"   Company: {agent.company_name}")
        print(f"   Parameters: {parameters}")
        
        # Execute agent
        result = await agent.execute(parameters)
        print("✅ Agent execution completed")
        
        # Check result
        print(f"   Status: {result.status}")
        print(f"   Output content length: {len(result.output_content)}")
        print(f"   Output content preview: {result.output_content[:200]}...")
        
        # Save output
        print("💾 Saving output...")
        filepath = agent.save_output(result)
        print(f"   Output saved to: {filepath}")
        
        # Check if file was created and has content
        if Path(filepath).exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"   File content length: {len(content)}")
            print(f"   File content preview: {content[:200]}...")
        else:
            print("   ❌ File was not created")
        
        # Clean up
        import shutil
        shutil.rmtree(test_dir)
        print("🧹 Test directory cleaned up")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function."""
    print("🚀 Agent Execution Debug Test")
    print("=" * 60)
    
    success = asyncio.run(test_agent_execution())
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 Agent execution test completed!")
    else:
        print("❌ Agent execution test failed.")
    print("=" * 60)

if __name__ == "__main__":
    main()
