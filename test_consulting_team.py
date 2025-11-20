#!/usr/bin/env python3
"""
Test script to debug the ConsultingTeam execution flow.
"""

import os
import asyncio
from pathlib import Path
from strategy_consulting_agent import ConsultingTeam

async def test_consulting_team():
    """Test the consulting team execution flow."""
    print("🧪 Testing Consulting Team Execution Flow...")
    print("=" * 60)
    
    try:
        # Get API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ OPENAI_API_KEY not set")
            return False
        
        print("✅ API key found")
        
        # Create test directory
        test_dir = Path("./test_team_debug")
        test_dir.mkdir(exist_ok=True)
        
        # Create consulting team
        print("🤖 Creating Consulting Team...")
        team = ConsultingTeam(api_key, "Test Company", test_dir)
        print("✅ Consulting team created successfully")
        
        # Test parameters
        parameters = {
            "analysis_brief": "Test analysis brief for consulting team",
            "engagement_type": "test",
            "analysis_depth": "test"
        }
        
        print("📝 Testing team execution...")
        print(f"   Company: {team.company_name}")
        print(f"   Parameters: {parameters}")
        
        # Execute team
        results = await team.execute_consulting_engagement(parameters)
        print("✅ Team execution completed")
        
        # Check results
        print(f"   Status: {results.get('status', 'unknown')}")
        print(f"   Agent results count: {len(results.get('agent_results', {}))}")
        
        # Check individual agent results
        for role, result in results.get('agent_results', {}).items():
            if isinstance(result, dict):
                print(f"   {role}: {result.get('status', 'unknown')}")
                if 'output_content' in result:
                    print(f"      Content length: {len(result['output_content'])}")
            else:
                print(f"   {role}: {type(result).__name__}")
        
        # Check final report
        final_report = results.get('final_report', '')
        if final_report:
            print(f"   Final report: {final_report}")
            if Path(final_report).exists():
                with open(final_report, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f"      Report content length: {len(content)}")
        
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
    print("🚀 Consulting Team Debug Test")
    print("=" * 60)
    
    success = asyncio.run(test_consulting_team())
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 Consulting team test completed!")
    else:
        print("❌ Consulting team test failed.")
    print("=" * 60)

if __name__ == "__main__":
    main()
