#!/usr/bin/env python3
"""
Setup script for the Multi-Agent Strategy Consulting Team project.
This script verifies the environment and sets up necessary configurations.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def check_virtual_environment():
    """Check if we're running in a virtual environment."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
        return True
    else:
        print("⚠️  Not running in virtual environment")
        print("   Consider activating the virtual environment: source venv/bin/activate")
        return False

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        'openai',
        'requests', 
        'rich',
        'python-dotenv',
        'pydantic'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✅ All packages installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install packages: {e}")
            return False
    
    return True

def check_api_key():
    """Check if OpenAI API key is configured."""
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        # Mask the API key for security
        masked_key = api_key[:8] + '*' * (len(api_key) - 12) + api_key[-4:] if len(api_key) > 12 else '***'
        print(f"✅ OpenAI API key is configured: {masked_key}")
        return True
    else:
        print("⚠️  OpenAI API key not found")
        print("   Set it with: export OPENAI_API_KEY='your-api-key-here'")
        print("   Or create a .env file with your API key")
        return False

def create_project_directories():
    """Create necessary project directories."""
    directories = [
        'consulting_projects',
        'example_projects',
        'logs'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")

def test_imports():
    """Test if the main modules can be imported."""
    try:
        from strategy_consulting_agent import ConsultingTeam, AgentRole
        print("✅ Main modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import main modules: {e}")
        return False

def main():
    """Run the setup process."""
    print("🚀 Multi-Agent Strategy Consulting Team - Project Setup")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    print()
    
    # Check virtual environment
    check_virtual_environment()
    
    print()
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Dependency check failed")
        sys.exit(1)
    
    print()
    
    # Check API key
    api_key_configured = check_api_key()
    
    print()
    
    # Create project directories
    create_project_directories()
    
    print()
    
    # Test imports
    if not test_imports():
        print("❌ Import test failed")
        sys.exit(1)
    
    print()
    print("=" * 60)
    print("🎉 Project setup completed successfully!")
    
    if api_key_configured:
        print("\n🚀 You're ready to use the Consulting Agents system!")
        print("   Try running: python example_usage.py")
    else:
        print("\n⚠️  Please configure your OpenAI API key before using the system")
        print("   Set it with: export OPENAI_API_KEY='your-api-key-here'")
    
    print("\n📚 Available commands:")
    print("   python strategy_consulting_agent.py --help")
    print("   python example_usage.py")
    print("   python test_multi_agent.py")
    print("   source venv/bin/activate  # Activate virtual environment")
    print("   deactivate                 # Deactivate virtual environment")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
