#!/usr/bin/env python3
"""
Test script to verify the Multi-Agent Strategy Consulting Team installation.
This script checks if all dependencies are available and the main module can be imported.
"""

import sys
import importlib

def test_imports():
    """Test if all required modules can be imported."""
    print("🧪 Testing Multi-Agent Strategy Consulting Team Installation...")
    print("=" * 70)
    
    # Test Python version
    python_version = sys.version_info
    print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    else:
        print("✅ Python version is compatible")
    
    # Test required packages
    required_packages = [
        ("openai", "OpenAI API client"),
        ("pathlib", "Path handling"),
        ("json", "JSON processing"),
        ("argparse", "Command line argument parsing"),
        ("datetime", "Date and time handling"),
        ("asyncio", "Asynchronous programming support"),
        ("dataclasses", "Data class support"),
        ("enum", "Enumeration support")
    ]
    
    all_packages_available = True
    
    for package_name, description in required_packages:
        try:
            importlib.import_module(package_name)
            print(f"✅ {package_name} - {description}")
        except ImportError as e:
            print(f"❌ {package_name} - {description}: {e}")
            all_packages_available = False
    
    # Test main module import
    try:
        from strategy_consulting_agent import (
            AgentRole, AgentOutput, BaseAgent, BusinessModelAnalyst,
            MarketResearcher, CompetitiveAnalyst, FinancialAnalyst,
            RiskAssessor, StrategyStoryteller, ImplementationSpecialist,
            SeniorPartner, ConsultingTeam
        )
        print("✅ strategy_consulting_agent module imported successfully")
        print("✅ All agent classes are available")
    except ImportError as e:
        print(f"❌ Failed to import strategy_consulting_agent: {e}")
        all_packages_available = False
    
    return all_packages_available

def test_agent_classes():
    """Test that all agent classes have the required methods."""
    print("\n🔧 Testing Agent Class Functionality...")
    print("=" * 70)
    
    try:
        from strategy_consulting_agent import (
            AgentRole, BaseAgent, BusinessModelAnalyst, MarketResearcher,
            CompetitiveAnalyst, FinancialAnalyst, RiskAssessor,
            StrategyStoryteller, ImplementationSpecialist, SeniorPartner
        )
        
        # Test agent roles enum
        print("📋 Testing Agent Roles:")
        for role in AgentRole:
            print(f"   ✅ {role.value}")
        
        # Test agent classes
        agent_classes = [
            (BusinessModelAnalyst, "Business Model Analyst"),
            (MarketResearcher, "Market Researcher"),
            (CompetitiveAnalyst, "Competitive Analyst"),
            (FinancialAnalyst, "Financial Analyst"),
            (RiskAssessor, "Risk Assessor"),
            (StrategyStoryteller, "Strategy Storyteller"),
            (ImplementationSpecialist, "Implementation Specialist"),
            (SeniorPartner, "Senior Partner")
        ]
        
        print("\n🤖 Testing Agent Classes:")
        for agent_class, name in agent_classes:
            # Check if class inherits from BaseAgent
            if issubclass(agent_class, BaseAgent):
                print(f"   ✅ {name}: Inherits from BaseAgent")
            else:
                print(f"   ❌ {name}: Does not inherit from BaseAgent")
                return False
            
            # Check if class has required methods
            if hasattr(agent_class, 'execute'):
                print(f"      ✅ Has execute method")
            else:
                print(f"      ❌ Missing execute method")
                return False
                
            if hasattr(agent_class, 'save_output'):
                print(f"      ✅ Has save_output method")
            else:
                print(f"      ❌ Missing save_output method")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing agent classes: {e}")
        return False

def test_consulting_team():
    """Test the ConsultingTeam class."""
    print("\n👥 Testing Consulting Team...")
    print("=" * 70)
    
    try:
        from strategy_consulting_agent import ConsultingTeam
        
        # Test class attributes
        if hasattr(ConsultingTeam, 'execute_consulting_engagement'):
            print("✅ execute_consulting_engagement method available")
        else:
            print("❌ execute_consulting_engagement method not found")
            return False
            
        if hasattr(ConsultingTeam, '_get_agent_dependencies'):
            print("✅ _get_agent_dependencies method available")
        else:
            print("❌ _get_agent_dependencies method not found")
            return False
            
        if hasattr(ConsultingTeam, '_execute_agent_with_dependencies'):
            print("✅ _execute_agent_with_dependencies method available")
        else:
            print("❌ _execute_agent_with_dependencies method not found")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing consulting team: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality without making API calls."""
    print("\n🔧 Testing Basic Functionality...")
    print("=" * 70)
    
    try:
        from strategy_consulting_agent import ConsultingTeam
        
        # Test class attributes
        if hasattr(ConsultingTeam, 'execute_consulting_engagement'):
            print("✅ execute_consulting_engagement method available")
        else:
            print("❌ execute_consulting_engagement method not found")
            return False
            
        # Check if class has the expected structure
        try:
            # Create a minimal instance to test attributes
            from pathlib import Path
            temp_dir = Path("./temp_test")
            temp_dir.mkdir(exist_ok=True)
            
            team = ConsultingTeam("test_key", "Test Company", temp_dir)
            
            if hasattr(team, 'agents'):
                print("✅ agents attribute available")
            else:
                print("❌ agents attribute not found")
                return False
                
            if hasattr(team, 'execution_order'):
                print("✅ execution_order attribute available")
            else:
                print("❌ execution_order attribute not found")
                return False
            
            # Clean up
            import shutil
            shutil.rmtree(temp_dir)
            
        except Exception as e:
            print(f"❌ Error testing ConsultingTeam instance: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing basic functionality: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Multi-Agent Strategy Consulting Team - Installation Test")
    print("=" * 70)
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test agent classes
        classes_ok = test_agent_classes()
        
        if classes_ok:
            # Test consulting team
            team_ok = test_consulting_team()
            
            if team_ok:
                # Test basic functionality
                functionality_ok = test_basic_functionality()
                
                if functionality_ok:
                    print("\n" + "=" * 70)
                    print("🎉 All tests passed! The Multi-Agent Consulting Team is ready to use.")
                    print("\nNext steps:")
                    print("1. Set your OpenAI API key: export OPENAI_API_KEY='your-key-here'")
                    print("2. Run the main script: python strategy_consulting_agent.py --help")
                    print("3. Try an example: python example_usage.py")
                    print("4. Test with a real company: python strategy_consulting_agent.py --company 'Apple' --brief 'Analyze Apple\\'s strategy'")
                else:
                    print("\n⚠️  Basic functionality tests failed.")
            else:
                print("\n⚠️  Consulting team tests failed.")
        else:
            print("\n⚠️  Agent class tests failed.")
    else:
        print("\n❌ Import tests failed. Please install missing dependencies:")
        print("pip install -r requirements.txt")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
