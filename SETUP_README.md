# 🐍 Python Environment Setup Guide

This guide will help you set up the Python virtual environment and install all necessary dependencies for the Multi-Agent Strategy Consulting Team project.

## 🚀 Quick Start

### 1. **Activate the Virtual Environment**
```bash
# Option 1: Use the activation script
./activate_env.sh

# Option 2: Manual activation
source venv/bin/activate
```

### 2. **Run the Setup Script**
```bash
python setup_project.py
```

### 3. **Set Your OpenAI API Key**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 4. **Test the Installation**
```bash
python test_multi_agent.py
```

## 📋 Prerequisites

- **Python 3.7+** (You have Python 3.13.7 ✅)
- **pip** (Python package installer)
- **OpenAI API key** with sufficient credits

## 🔧 Detailed Setup Steps

### **Step 1: Verify Python Installation**
```bash
python3 --version
# Should show: Python 3.13.7
```

### **Step 2: Create Virtual Environment**
```bash
# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Verify activation (you should see (venv) in your prompt)
which python
# Should show: ./venv/bin/python
```

### **Step 3: Install Dependencies**
```bash
# Upgrade pip first
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

### **Step 4: Verify Installation**
```bash
# Test if OpenAI library is installed
python -c "import openai; print(f'OpenAI {openai.__version__} installed successfully')"

# Test if other packages are available
python -c "import requests, rich, pydantic; print('All packages installed successfully')"
```

## 📦 Package Details

The following packages are installed:

| Package | Version | Purpose |
|---------|---------|---------|
| `openai` | ≥1.0.0 | OpenAI API client for GPT-5 access |
| `requests` | ≥2.31.0 | HTTP library for API calls |
| `rich` | ≥13.0.0 | Beautiful terminal output and progress bars |
| `python-dotenv` | ≥1.0.0 | Environment variable management |
| `pydantic` | ≥2.0.0 | Data validation and settings management |

## 🔑 OpenAI API Configuration

### **Option 1: Environment Variable (Recommended)**
```bash
export OPENAI_API_KEY="sk-your-actual-api-key-here"
```

### **Option 2: .env File**
```bash
# Copy the example file
cp env_example.txt .env

# Edit .env and add your API key
nano .env
```

### **Option 3: Command Line Parameter**
```bash
python strategy_consulting_agent.py --company "Apple" --brief "Analyze strategy" --api-key "your-key"
```

## 🧪 Testing Your Setup

### **Test 1: Basic Import Test**
```bash
python -c "
from strategy_consulting_agent import ConsultingTeam, AgentRole
print('✅ All modules imported successfully!')
"
```

### **Test 2: Run Test Suite**
```bash
python test_multi_agent.py
```

### **Test 3: Run Example Usage**
```bash
python example_usage.py
```

### **Test 4: Test Main Script**
```bash
python strategy_consulting_agent.py --help
```

## 📁 Project Structure

After setup, your project will have:

```
consulting-agents/
├── venv/                           # Python virtual environment
├── requirements.txt                 # Python dependencies
├── setup_project.py                 # Setup verification script
├── activate_env.sh                  # Environment activation script
├── env_example.txt                  # Environment variables template
├── strategy_consulting_agent.py     # Main consulting system
├── example_usage.py                 # Usage examples
├── test_multi_agent.py             # Test suite
├── consulting_projects/             # Generated consulting reports
├── example_projects/                # Example project outputs
└── logs/                           # System logs
```

## 🚨 Troubleshooting

### **Issue: "command not found: python"**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Or use python3 explicitly
python3 --version
```

### **Issue: "ModuleNotFoundError: No module named 'openai'"**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### **Issue: "OpenAI API key is required"**
```bash
# Set your API key
export OPENAI_API_KEY="your-actual-key"

# Or create a .env file
cp env_example.txt .env
# Edit .env and add your key
```

### **Issue: Permission Denied on Scripts**
```bash
# Make scripts executable
chmod +x activate_env.sh
chmod +x setup_project.py
```

## 🔄 Daily Usage

### **Start Working**
```bash
# Activate environment
source venv/bin/activate

# Run your consulting analysis
python strategy_consulting_agent.py --company "Tesla" --brief "Analyze EV strategy"
```

### **Stop Working**
```bash
# Deactivate virtual environment
deactivate
```

## 📚 Next Steps

After successful setup:

1. **Read the main README.md** for usage instructions
2. **Try the example usage** with `python example_usage.py`
3. **Run a test analysis** with a real company
4. **Explore the generated reports** in the `consulting_projects/` directory

## 🆘 Getting Help

If you encounter issues:

1. **Check the troubleshooting section above**
2. **Verify your Python version** is 3.7+
3. **Ensure you're in the virtual environment** (venv)
4. **Check your OpenAI API key** is set correctly
5. **Review the error messages** for specific guidance

## 🎯 Success Indicators

You'll know everything is working when:

- ✅ Virtual environment activates without errors
- ✅ All packages install successfully
- ✅ `python test_multi_agent.py` runs without errors
- ✅ `python strategy_consulting_agent.py --help` shows help
- ✅ You can import the main modules without errors

---

**Happy Consulting! 🤖📊**
