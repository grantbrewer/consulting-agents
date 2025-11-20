#!/usr/bin/env python3
"""
Multi-Agent Strategy Consulting System
A team of specialized AI agents that work asynchronously to deliver comprehensive strategic analysis.
Each agent has specific expertise and can collaborate with others to produce consulting-grade deliverables.
"""

import os
import json
import asyncio
import argparse
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path
import openai
from enum import Enum

class AgentRole(Enum):
    """Enumeration of agent roles in the consulting team."""
    BUSINESS_MODEL_ANALYST = "business_model_analyst"
    MARKET_RESEARCHER = "market_researcher"
    STRATEGY_STORYTELLER = "strategy_storyteller"
    SENIOR_PARTNER = "senior_partner"
    COMPETITIVE_ANALYST = "competitive_analyst"
    FINANCIAL_ANALYST = "financial_analyst"
    RISK_ASSESSOR = "risk_assessor"
    IMPLEMENTATION_SPECIALIST = "implementation_specialist"

@dataclass
class AgentOutput:
    """Data structure for agent outputs."""
    agent_role: str
    company_name: str
    output_content: str
    timestamp: str
    parameters_used: Dict[str, Any]
    dependencies: List[str]
    status: str
    file_path: str

class BaseAgent:
    """Base class for all consulting agents."""
    
    def __init__(self, role: AgentRole, api_key: str, company_name: str, project_dir: Path):
        self.role = role
        self.api_key = api_key
        self.company_name = company_name
        self.project_dir = project_dir
        self.client = openai.OpenAI(api_key=api_key)
        self.output_dir = project_dir / "agent_outputs" / role.value
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: Optional[List[str]] = None) -> AgentOutput:
        """Execute the agent's analysis. To be implemented by subclasses.
        
        Args:
            parameters: Dictionary of parameters for the analysis
            dependencies: Optional list of dependency agent roles
            
        Returns:
            AgentOutput: The output of the agent's analysis
            
        Raises:
            NotImplementedError: This method must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement execute()")
        
    def save_output(self, output: AgentOutput) -> str:
        """Save agent output to markdown file and metadata to JSON."""
        # Save markdown content
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.role.value}_{timestamp}.md"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(output.output_content)
        
        # Save metadata
        metadata = asdict(output)
        metadata['file_path'] = str(filepath)
        metadata_file = self.output_dir / f"{self.role.value}_{timestamp}_metadata.json"
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        return str(filepath)
    
    def load_dependency_outputs(self, dependencies: List[str]) -> List[str]:
        """Load outputs from dependent agents."""
        outputs = []
        for dep in dependencies:
            dep_dir = self.project_dir / "agent_outputs" / dep
            if dep_dir.exists():
                # Find the most recent markdown file for this dependency
                md_files = list(dep_dir.glob("*.md"))
                if md_files:
                    latest_file = max(md_files, key=lambda x: x.stat().st_mtime)
                    try:
                        with open(latest_file, 'r', encoding='utf-8') as f:
                            outputs.append(f.read())
                    except IOError as e:
                        print(f"Warning: Could not read dependency file {latest_file}: {e}")
        return outputs

class BusinessModelAnalyst(BaseAgent):
    """Agent specialized in analyzing and defining business models."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.BUSINESS_MODEL_ANALYST, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Analyze and define the business model of the organization."""
        
        # Load any dependency outputs
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        # Use prompt manager for prompts
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        
        # Get agent prompt configuration
        agent_prompt = prompt_manager.get_agent_prompt("business_model_analyst")
        system_prompt = prompt_manager.get_enhanced_system_prompt("business_model_analyst")
        
        # Format user prompt with parameters
        user_prompt = prompt_manager.format_user_prompt(
            "business_model_analyst",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f'Dependency Outputs: {chr(10).join(dependency_outputs)}' if dependency_outputs else ''
        )
        
        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("business_model_analyst")
        )
        
        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        
        return output

class MarketResearcher(BaseAgent):
    """Agent specialized in market research and TAM analysis."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.MARKET_RESEARCHER, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Research the total addressable market and market dynamics."""
        
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        # Use prompt manager for prompts
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        
        # Get agent prompt configuration
        agent_prompt = prompt_manager.get_agent_prompt("market_researcher")
        system_prompt = prompt_manager.get_enhanced_system_prompt("market_researcher")
        
        # Format user prompt with parameters
        user_prompt = prompt_manager.format_user_prompt(
            "market_researcher",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f'Dependency Outputs: {chr(10).join(dependency_outputs)}' if dependency_outputs else ''
        )
        
        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("market_researcher")
        )
        
        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        
        return output

class CompetitiveAnalyst(BaseAgent):
    """Agent specialized in competitive analysis and positioning."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.COMPETITIVE_ANALYST, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Analyze competitive landscape and positioning."""
        
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        system_prompt = prompt_manager.get_enhanced_system_prompt("competitive_analyst")
        user_prompt = prompt_manager.format_user_prompt(
            "competitive_analyst",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f'Dependency Outputs: {chr(10).join(dependency_outputs)}' if dependency_outputs else ''
        )

        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("competitive_analyst")
        )

        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        return output

class FinancialAnalyst(BaseAgent):
    """Agent specialized in financial analysis and performance assessment."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.FINANCIAL_ANALYST, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Analyze financial performance and health."""
        
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        system_prompt = prompt_manager.get_enhanced_system_prompt("financial_analyst")
        user_prompt = prompt_manager.format_user_prompt(
            "financial_analyst",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f'Dependency Outputs: {chr(10).join(dependency_outputs)}' if dependency_outputs else ''
        )

        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("financial_analyst")
        )

        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        return output

class RiskAssessor(BaseAgent):
    """Agent specialized in risk assessment and mitigation strategies."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.RISK_ASSESSOR, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Assess strategic and operational risks."""
        
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        system_prompt = prompt_manager.get_enhanced_system_prompt("risk_assessor")
        user_prompt = prompt_manager.format_user_prompt(
            "risk_assessor",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f'Dependency Outputs: {chr(10).join(dependency_outputs)}' if dependency_outputs else ''
        )

        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("risk_assessor")
        )

        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        return output

class StrategyStoryteller(BaseAgent):
    """Agent specialized in creating compelling strategy narratives."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.STRATEGY_STORYTELLER, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Create a compelling strategy storyline based on all agent outputs."""
        
        # This agent depends on outputs from all other analysis agents
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        system_prompt = prompt_manager.get_enhanced_system_prompt("strategy_storyteller")
        user_prompt = prompt_manager.format_user_prompt(
            "strategy_storyteller",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f"Dependencies: {', '.join(dependencies or [])}\n\n{chr(10).join(dependency_outputs)}" if dependency_outputs else ''
        )

        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("strategy_storyteller")
        )
        
        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        
        return output

class ImplementationSpecialist(BaseAgent):
    """Agent specialized in implementation planning and execution strategy."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.IMPLEMENTATION_SPECIALIST, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Create implementation roadmap and execution strategy."""
        
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        system_prompt = prompt_manager.get_enhanced_system_prompt("implementation_specialist")
        user_prompt = prompt_manager.format_user_prompt(
            "implementation_specialist",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f'Dependency Outputs: {chr(10).join(dependency_outputs)}' if dependency_outputs else ''
        )

        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("implementation_specialist")
        )

        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        return output

class SeniorPartner(BaseAgent):
    """Senior partner agent that reviews and synthesizes all work."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        super().__init__(AgentRole.SENIOR_PARTNER, api_key, company_name, project_dir)
        
    async def execute(self, parameters: Dict[str, Any], dependencies: List[str] = None) -> AgentOutput:
        """Review and synthesize all agent outputs as a senior partner."""
        
        # This agent depends on outputs from all other agents
        dependency_outputs = self.load_dependency_outputs(dependencies or [])
        
        from prompt_manager import PromptManager
        prompt_manager = PromptManager()
        system_prompt = prompt_manager.get_enhanced_system_prompt("senior_partner")
        user_prompt = prompt_manager.format_user_prompt(
            "senior_partner",
            company_name=self.company_name,
            analysis_parameters=json.dumps(parameters, indent=2),
            dependency_outputs_section=f"Dependencies: {', '.join(dependencies or [])}\n\n{chr(10).join(dependency_outputs)}" if dependency_outputs else ''
        )

        response = self.client.chat.completions.create(
            model=prompt_manager.get_model_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=prompt_manager.get_agent_token_limit("senior_partner")
        )

        output = AgentOutput(
            agent_role=self.role.value,
            company_name=self.company_name,
            output_content=response.choices[0].message.content,
            timestamp=datetime.now().isoformat(),
            parameters_used=parameters,
            dependencies=dependencies or [],
            status="completed",
            file_path=""
        )
        return output

class ConsultingTeam:
    """Manages the team of consulting agents and orchestrates their collaboration."""
    
    def __init__(self, api_key: str, company_name: str, project_dir: Path):
        self.api_key = api_key
        self.company_name = company_name
        self.project_dir = project_dir
        self.project_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize all agents
        self.agents = {
            AgentRole.BUSINESS_MODEL_ANALYST: BusinessModelAnalyst(api_key, company_name, project_dir),
            AgentRole.MARKET_RESEARCHER: MarketResearcher(api_key, company_name, project_dir),
            AgentRole.COMPETITIVE_ANALYST: CompetitiveAnalyst(api_key, company_name, project_dir),
            AgentRole.FINANCIAL_ANALYST: FinancialAnalyst(api_key, company_name, project_dir),
            AgentRole.RISK_ASSESSOR: RiskAssessor(api_key, company_name, project_dir),
            AgentRole.IMPLEMENTATION_SPECIALIST: ImplementationSpecialist(api_key, company_name, project_dir),
            AgentRole.STRATEGY_STORYTELLER: StrategyStoryteller(api_key, company_name, project_dir),
            AgentRole.SENIOR_PARTNER: SeniorPartner(api_key, company_name, project_dir)
        }
        
        # Define execution dependencies
        self.execution_order = [
            # Phase 1: Core analysis (can run in parallel)
            [AgentRole.BUSINESS_MODEL_ANALYST, AgentRole.MARKET_RESEARCHER, AgentRole.COMPETITIVE_ANALYST],
            # Phase 2: Specialized analysis (depends on Phase 1)
            [AgentRole.FINANCIAL_ANALYST, AgentRole.RISK_ASSESSOR],
            # Phase 3: Implementation planning (depends on Phase 2)
            [AgentRole.IMPLEMENTATION_SPECIALIST],
            # Phase 4: Strategy synthesis (depends on all previous phases)
            [AgentRole.STRATEGY_STORYTELLER],
            # Phase 5: Senior partner review (depends on all outputs)
            [AgentRole.SENIOR_PARTNER]
        ]
        
    async def execute_consulting_engagement(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the complete consulting engagement with all agents."""
        
        print(f"🚀 Starting consulting engagement for {self.company_name}")
        print("=" * 60)
        
        results = {}
        
        # Execute agents in phases
        for phase_num, phase_agents in enumerate(self.execution_order, 1):
            print(f"\n📋 Phase {phase_num}: Executing {len(phase_agents)} agents")
            print("-" * 40)
            
            # Execute agents in this phase (can run in parallel)
            phase_tasks = []
            for agent_role in phase_agents:
                # Determine dependencies for this agent
                dependencies = self._get_agent_dependencies(agent_role)
                task = self._execute_agent_with_dependencies(agent_role, parameters, dependencies)
                phase_tasks.append(task)
            
            # Wait for all agents in this phase to complete
            phase_results = await asyncio.gather(*phase_tasks, return_exceptions=True)
            
            # Process results
            for agent_role, result in zip(phase_agents, phase_results):
                if isinstance(result, Exception):
                    print(f"❌ {agent_role.value} failed: {result}")
                    results[agent_role.value] = {"status": "error", "error": str(result)}
                else:
                    print(f"✅ {agent_role.value} completed successfully")
                    results[agent_role.value] = result
                    
                    # Save output
                    filepath = self.agents[agent_role].save_output(result)
                    print(f"   📁 Output saved to: {filepath}")
        
        # Generate final report
        final_report = await self._generate_final_report(results, parameters)
        
        return {
            "company_name": self.company_name,
            "engagement_parameters": parameters,
            "agent_results": results,
            "final_report": final_report,
            "timestamp": datetime.now().isoformat(),
            "status": "completed"
        }
    
    def _get_agent_dependencies(self, agent_role: AgentRole) -> List[str]:
        """Get the list of agent roles that this agent depends on."""
        if agent_role == AgentRole.STRATEGY_STORYTELLER:
            # Depends on all analysis agents
            return [role.value for role in [AgentRole.BUSINESS_MODEL_ANALYST, AgentRole.MARKET_RESEARCHER, 
                                          AgentRole.COMPETITIVE_ANALYST, AgentRole.FINANCIAL_ANALYST, 
                                          AgentRole.RISK_ASSESSOR, AgentRole.IMPLEMENTATION_SPECIALIST]]
        elif agent_role == AgentRole.SENIOR_PARTNER:
            # Depends on all agents
            return [role.value for role in self.agents.keys() if role != AgentRole.SENIOR_PARTNER]
        elif agent_role in [AgentRole.FINANCIAL_ANALYST, AgentRole.RISK_ASSESSOR]:
            # Depends on core analysis agents
            return [role.value for role in [AgentRole.BUSINESS_MODEL_ANALYST, AgentRole.MARKET_RESEARCHER, 
                                          AgentRole.COMPETITIVE_ANALYST]]
        elif agent_role == AgentRole.IMPLEMENTATION_SPECIALIST:
            # Depends on analysis and risk assessment
            return [role.value for role in [AgentRole.BUSINESS_MODEL_ANALYST, AgentRole.MARKET_RESEARCHER, 
                                          AgentRole.COMPETITIVE_ANALYST, AgentRole.FINANCIAL_ANALYST, 
                                          AgentRole.RISK_ASSESSOR]]
        else:
            # No dependencies for core analysis agents
            return []
    
    async def _execute_agent_with_dependencies(self, agent_role: AgentRole, parameters: Dict[str, Any], dependencies: List[str]) -> AgentOutput:
        """Execute an agent with its dependencies."""
        agent = self.agents[agent_role]
        return await agent.execute(parameters, dependencies)
    
    async def _generate_final_report(self, results: Dict[str, Any], parameters: Dict[str, Any]) -> str:
        """Generate a final comprehensive report."""
        
        # Load all agent outputs
        all_outputs = []
        for role, result in results.items():
            # Handle both AgentOutput objects and dictionaries
            if hasattr(result, 'status') and result.status == "completed":
                # AgentOutput object
                if hasattr(result, 'output_content') and result.output_content:
                    all_outputs.append(f"## {role.replace('_', ' ').title()}\n\n{result.output_content}\n\n")
                else:
                    # Fallback to reading from file
                    agent_dir = self.project_dir / "agent_outputs" / role
                    if agent_dir.exists():
                        md_files = list(agent_dir.glob("*.md"))
                        if md_files:
                            latest_file = max(md_files, key=lambda x: x.stat().st_mtime)
                            with open(latest_file, 'r', encoding='utf-8') as f:
                                all_outputs.append(f"## {role.replace('_', ' ').title()}\n\n{f.read()}\n\n")
            elif isinstance(result, dict) and result.get("status") == "completed":
                # Dictionary result (for error cases)
                agent_dir = self.project_dir / "agent_outputs" / role
                if agent_dir.exists():
                    md_files = list(agent_dir.glob("*.md"))
                    if md_files:
                        latest_file = max(md_files, key=lambda x: x.stat().st_mtime)
                        with open(latest_file, 'r', encoding='utf-8') as f:
                            all_outputs.append(f"## {role.replace('_', ' ').title()}\n\n{f.read()}\n\n")
        
        # Create final report
        final_report_content = f"""# Strategic Analysis Report: {self.company_name}

**Generated:** {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
**Analysis Parameters:** {json.dumps(parameters, indent=2)}

## Executive Summary

This comprehensive strategic analysis was conducted by an AI-powered consulting team consisting of specialized agents, each focusing on different aspects of strategic analysis.

## Detailed Analysis

{chr(10).join(all_outputs)}

## Conclusion

This analysis represents the collaborative work of multiple specialized AI agents, each bringing deep expertise in their respective domains. The findings provide a comprehensive strategic assessment with actionable recommendations for {self.company_name}.

---
*Report generated by AI Consulting Team using GPT-5 technology*
"""
        
        # Save final report
        final_report_path = self.project_dir / f"final_strategic_report_{self.company_name.replace(' ', '_')}.md"
        with open(final_report_path, 'w', encoding='utf-8') as f:
            f.write(final_report_content)
        
        return str(final_report_path)

async def main():
    """Main function to run the consulting team."""
    parser = argparse.ArgumentParser(
        description="Multi-Agent Strategy Consulting Team - AI-powered strategic analysis"
    )
    parser.add_argument(
        "--company", "-c", 
        required=True, 
        help="Name of the company to analyze"
    )
    parser.add_argument(
        "--brief", "-b", 
        required=True, 
        help="Analysis brief describing what to analyze"
    )
    parser.add_argument(
        "--output-dir", "-o", 
        default="./consulting_projects",
        help="Output directory for project files (default: ./consulting_projects)"
    )
    parser.add_argument(
        "--api-key", 
        help="OpenAI API key (optional, can use OPENAI_API_KEY env var)"
    )
    
    args = parser.parse_args()
    
    try:
        # Get API key
        api_key = args.api_key or os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass it as a parameter.")
        
        # Create project directory
        project_dir = Path(args.output_dir) / args.company.replace(' ', '_').replace('/', '_')
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize consulting team
        print("🤖 Initializing AI Consulting Team...")
        team = ConsultingTeam(api_key, args.company, project_dir)
        
        # Define engagement parameters
        parameters = {
            "analysis_brief": args.brief,
            "engagement_type": "comprehensive_strategic_analysis",
            "analysis_depth": "executive_level",
            "deliverables": ["business_model_analysis", "market_research", "competitive_analysis", 
                           "financial_analysis", "risk_assessment", "implementation_plan", 
                           "strategy_narrative", "senior_partner_review"]
        }
        
        # Execute consulting engagement
        print(f"📊 Starting comprehensive analysis for: {args.company}")
        print(f"📝 Analysis brief: {args.brief}")
        print(f"📁 Project directory: {project_dir}")
        print("\n" + "="*60)
        
        results = await team.execute_consulting_engagement(parameters)
        
        print("\n" + "="*60)
        print("🎉 Consulting engagement completed successfully!")
        print(f"📋 Final report: {results['final_report']}")
        print(f"📁 All outputs saved to: {project_dir}")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nMake sure you have:")
        print("1. Set the OPENAI_API_KEY environment variable, or")
        print("2. Pass the --api-key parameter")
        print("3. Have sufficient OpenAI API credits")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(asyncio.run(main()))
