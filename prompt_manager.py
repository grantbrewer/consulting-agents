#!/usr/bin/env python3
"""
Prompt Manager for Multi-Agent Strategy Consulting Team
Loads and manages prompts from YAML configuration files
"""

import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass

@dataclass
class AgentPrompt:
    """Data structure for agent prompts."""
    system_prompt: str
    user_prompt_template: str
    token_limit: int

class PromptManager:
    """Manages prompts and system instructions for all consulting agents."""
    
    def __init__(self, config_file: str = "agent_prompts.yaml"):
        """Initialize the prompt manager with a configuration file."""
        self.config_file = Path(config_file)
        self.config = self._load_config()
        self._validate_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load the YAML configuration file."""
        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            return config
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML configuration: {e}")
    
    def _validate_config(self):
        """Validate the configuration structure."""
        required_sections = ['global', 'system_instructions', 'agents', 'token_limits']
        for section in required_sections:
            if section not in self.config:
                raise ValueError(f"Missing required section: {section}")
        
        required_agents = [
            'business_model_analyst', 'market_researcher', 'competitive_analyst',
            'financial_analyst', 'risk_assessor', 'implementation_specialist',
            'strategy_storyteller', 'senior_partner'
        ]
        
        for agent in required_agents:
            if agent not in self.config['agents']:
                raise ValueError(f"Missing required agent: {agent}")
            
            agent_config = self.config['agents'][agent]
            if 'system_prompt' not in agent_config:
                raise ValueError(f"Missing system_prompt for agent: {agent}")
            if 'user_prompt_template' not in agent_config:
                raise ValueError(f"Missing user_prompt_template for agent: {agent}")
    
    def get_global_config(self) -> Dict[str, Any]:
        """Get global configuration settings."""
        return self.config.get('global', {})
    
    def get_system_instructions(self) -> Dict[str, List[str]]:
        """Get system instructions for all agents."""
        return self.config.get('system_instructions', {})
    
    def get_agent_prompt(self, agent_name: str) -> AgentPrompt:
        """Get the prompt configuration for a specific agent."""
        if agent_name not in self.config['agents']:
            raise ValueError(f"Unknown agent: {agent_name}")
        
        agent_config = self.config['agents'][agent_name]
        token_limit = self.config['token_limits'].get(agent_name, 4000)
        
        return AgentPrompt(
            system_prompt=agent_config['system_prompt'],
            user_prompt_template=agent_config['user_prompt_template'],
            token_limit=token_limit
        )
    
    def format_user_prompt(self, agent_name: str, **kwargs) -> str:
        """Format the user prompt template with provided parameters."""
        agent_prompt = self.get_agent_prompt(agent_name)
        
        # Get the template
        template = agent_prompt.user_prompt_template
        
        # Format template variables
        formatted_prompt = template.format(**kwargs)
        
        return formatted_prompt
    
    def get_model_name(self) -> str:
        """Get the AI model name from global config."""
        return self.config['global'].get('model', 'gpt-5')
    
    def get_default_token_limit(self) -> int:
        """Get the default token limit from global config."""
        return self.config['global'].get('max_completion_tokens', 4000)
    
    def get_agent_token_limit(self, agent_name: str) -> int:
        """Get the token limit for a specific agent."""
        return self.config['token_limits'].get(agent_name, self.get_default_token_limit())
    
    def get_enhanced_system_prompt(self, agent_name: str) -> str:
        """Get an enhanced system prompt with global instructions."""
        agent_prompt = self.get_agent_prompt(agent_name)
        system_instructions = self.get_system_instructions()
        
        # Build enhanced system prompt
        enhanced_prompt = agent_prompt.system_prompt + "\n\n"
        
        # Add general instructions
        if 'general' in system_instructions:
            enhanced_prompt += "General Instructions:\n"
            for instruction in system_instructions['general']:
                enhanced_prompt += f"- {instruction}\n"
            enhanced_prompt += "\n"
        
        # Add analysis framework
        if 'analysis_framework' in system_instructions:
            enhanced_prompt += "Analysis Framework:\n"
            for framework in system_instructions['analysis_framework']:
                enhanced_prompt += f"- {framework}\n"
        
        return enhanced_prompt
    
    def list_available_agents(self) -> List[str]:
        """List all available agent names."""
        return list(self.config['agents'].keys())
    
    def get_agent_summary(self) -> Dict[str, Dict[str, Any]]:
        """Get a summary of all agents and their configurations."""
        summary = {}
        for agent_name in self.list_available_agents():
            agent_config = self.config['agents'][agent_name]
            summary[agent_name] = {
                'system_prompt_length': len(agent_config['system_prompt']),
                'user_prompt_length': len(agent_config['user_prompt_template']),
                'token_limit': self.get_agent_token_limit(agent_name)
            }
        return summary
    
    def reload_config(self):
        """Reload the configuration from file."""
        self.config = self._load_config()
        self._validate_config()

# Convenience functions for easy access
def get_prompt_manager(config_file: str = "agent_prompts.yaml") -> PromptManager:
    """Get a prompt manager instance."""
    return PromptManager(config_file)

def get_agent_prompt(agent_name: str, config_file: str = "agent_prompts.yaml") -> AgentPrompt:
    """Get prompt configuration for a specific agent."""
    manager = PromptManager(config_file)
    return manager.get_agent_prompt(agent_name)

def format_agent_prompt(agent_name: str, config_file: str = "agent_prompts.yaml", **kwargs) -> str:
    """Format user prompt for a specific agent."""
    manager = PromptManager(config_file)
    return manager.format_user_prompt(agent_name, **kwargs)
