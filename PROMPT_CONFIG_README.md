# 🎯 YAML-Based Prompt Configuration System

This document explains how to use the new YAML-based prompt configuration system for the Multi-Agent Strategy Consulting Team.

## 🚀 Overview

The system now abstracts all agent prompts into a centralized YAML configuration file (`agent_prompts.yaml`) and uses a `PromptManager` class to load and manage these prompts. This makes the system more maintainable, configurable, and easier to customize.

## 📁 Files

- **`agent_prompts.yaml`** - Main configuration file containing all prompts
- **`prompt_manager.py`** - Python class to load and manage prompts
- **`test_prompt_manager.py`** - Test script to verify functionality

## 🔧 Configuration Structure

### **Global Configuration**
```yaml
global:
  model: "gpt-5"                    # AI model to use
  max_completion_tokens: 4000       # Default token limit
  default_max_tokens: 5000          # Default for longer outputs
```

### **System Instructions**
```yaml
system_instructions:
  general:
    - "You are a top-tier strategy consulting professional"
    - "Provide analysis in professional consulting format"
    # ... more general instructions
  
  analysis_framework:
    - "Structure your analysis with clear headings"
    - "Include executive summary for key insights"
    # ... more framework instructions
```

### **Agent-Specific Prompts**
```yaml
agents:
  business_model_analyst:
    system_prompt: "You are an expert business model analyst..."
    user_prompt_template: |
      You are an expert business model analyst...
      Company: {company_name}
      Analysis Parameters: {analysis_parameters}
      # ... rest of prompt template
```

### **Token Limits**
```yaml
token_limits:
  business_model_analyst: 4000
  strategy_storyteller: 5000
  # ... token limits for each agent
```

## 🐍 Using the Prompt Manager

### **Basic Usage**
```python
from prompt_manager import PromptManager

# Initialize prompt manager
manager = PromptManager("agent_prompts.yaml")

# Get agent prompt configuration
agent_prompt = manager.get_agent_prompt("business_model_analyst")

# Get enhanced system prompt (includes global instructions)
system_prompt = manager.get_enhanced_system_prompt("business_model_analyst")

# Format user prompt with parameters
user_prompt = manager.format_user_prompt(
    "business_model_analyst",
    company_name="Apple Inc.",
    analysis_parameters='{"focus": "competitive strategy"}',
    dependency_outputs_section="Previous analysis results..."
)
```

### **Convenience Functions**
```python
from prompt_manager import get_agent_prompt, format_agent_prompt

# Quick access to agent prompts
agent_prompt = get_agent_prompt("market_researcher")

# Quick prompt formatting
formatted_prompt = format_agent_prompt(
    "competitive_analyst",
    company_name="Tesla",
    analysis_parameters='{"scope": "EV market"}'
)
```

## 🔄 Updating Prompts

### **1. Edit the YAML File**
```yaml
agents:
  business_model_analyst:
    system_prompt: "Your updated system prompt here..."
    user_prompt_template: |
      Your updated user prompt template here...
      Company: {company_name}
      # ... rest of template
```

### **2. Reload Configuration**
```python
manager = PromptManager()
manager.reload_config()  # Reloads from file
```

## 📝 Prompt Template Variables

The following variables can be used in prompt templates:

- **`{company_name}`** - Name of the company being analyzed
- **`{analysis_parameters}`** - JSON string of analysis parameters
- **`{dependency_outputs_section}`** - Outputs from dependent agents
- **`{agent_list}`** - List of agent names (for strategy storyteller and senior partner)

## 🧪 Testing

### **Test the Prompt Manager**
```bash
source venv/bin/activate
python test_prompt_manager.py
```

### **Test YAML Configuration**
```bash
# The test script also validates the YAML structure
python test_prompt_manager.py
```

## 🎨 Customization Examples

### **Add New Agent Instructions**
```yaml
system_instructions:
  general:
    - "You are a top-tier strategy consulting professional"
    - "Focus on practical, implementable recommendations"
    - "Use data-driven insights and strategic thinking"
    # Add your custom instruction here
    - "Always consider sustainability and ESG factors"
```

### **Modify Agent Prompts**
```yaml
agents:
  business_model_analyst:
    system_prompt: "You are an expert business model analyst with deep expertise in business model innovation, revenue models, value chain analysis, and sustainability."
    
    user_prompt_template: |
      You are an expert business model analyst specializing in defining and analyzing business models.
      
      Company: {company_name}
      Analysis Parameters: {analysis_parameters}
      
      {dependency_outputs_section}
      
      Please provide a comprehensive business model analysis including:
      
      1. **Business Model Canvas Components:**
         - Value Proposition
         - Customer Segments
         # ... existing content ...
      
      6. **Sustainability and ESG Considerations:**
         - Environmental impact assessment
         - Social responsibility factors
         - Governance considerations
      
      Provide your analysis in professional consulting format with clear sections, insights, and actionable recommendations.
```

### **Adjust Token Limits**
```yaml
token_limits:
  business_model_analyst: 5000      # Increased for more detailed analysis
  market_researcher: 4500           # Custom limit
  competitive_analyst: 4000         # Default limit
```

## 🔍 Validation

The prompt manager automatically validates:

- ✅ Required sections exist
- ✅ All required agents are configured
- ✅ Each agent has system_prompt and user_prompt_template
- ✅ YAML syntax is correct
- ✅ Token limits are specified

## 🚨 Error Handling

### **Common Issues**
1. **Missing YAML file**: `FileNotFoundError: Configuration file not found`
2. **Invalid YAML**: `Invalid YAML configuration: [error details]`
3. **Missing sections**: `Missing required section: [section_name]`
4. **Missing agents**: `Missing required agent: [agent_name]`

### **Debugging**
```python
try:
    manager = PromptManager()
except Exception as e:
    print(f"Error: {e}")
    # Check YAML syntax and structure
```

## 📚 Integration with Main System

To integrate this with the main consulting agent system:

1. **Import the prompt manager** in your agent classes
2. **Replace hardcoded prompts** with prompt manager calls
3. **Use formatted prompts** for API calls
4. **Update token limits** dynamically from configuration

## 🎯 Benefits

- **🔧 Maintainable**: All prompts in one place
- **⚙️ Configurable**: Easy to modify without code changes
- **🧪 Testable**: Prompts can be validated independently
- **📝 Versionable**: YAML files can be version controlled
- **🔄 Dynamic**: Prompts can be updated without restarting
- **🎨 Customizable**: Easy to add new instructions or modify existing ones

## 🚀 Next Steps

1. **Test the current setup**: Run `test_prompt_manager.py`
2. **Customize prompts**: Edit `agent_prompts.yaml` as needed
3. **Integrate with agents**: Update main agent code to use prompt manager
4. **Add new agents**: Extend YAML configuration for new agent types
5. **Create prompt templates**: Build reusable prompt patterns

---

**Happy Prompt Engineering! 🎯🤖**
