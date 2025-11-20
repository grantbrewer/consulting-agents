#!/bin/bash
# Script to activate the Python virtual environment for the Consulting Agents project

echo "🐍 Activating Python virtual environment for Consulting Agents..."
echo "📁 Project directory: $(pwd)"
echo "🔧 Python version: $(python3 --version)"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment 'venv' not found!"
    echo "   Run: python3 -m venv venv"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Verify activation
if [ "$VIRTUAL_ENV" != "" ]; then
    echo "✅ Virtual environment activated successfully!"
    echo "🐍 Python: $(which python)"
    echo "📦 Pip: $(which pip)"
    echo "🔑 OpenAI: $(python -c 'import openai; print(f"OpenAI {openai.__version__}")' 2>/dev/null || echo "OpenAI not installed")"
    echo ""
    echo "💡 To deactivate, run: deactivate"
    echo "💡 To install dependencies: pip install -r requirements.txt"
    echo "💡 To run tests: python test_multi_agent.py"
    echo ""
    echo "🚀 Ready to use the Consulting Agents system!"
else
    echo "❌ Failed to activate virtual environment"
    exit 1
fi
