#!/usr/bin/env python3
"""
Example usage of the Multi-Agent Strategy Consulting Team.
This script demonstrates how to use the consulting team programmatically.
"""

import os
import asyncio
from pathlib import Path
from strategy_consulting_agent import ConsultingTeam

async def main():
    """Example of using the Multi-Agent Consulting Team programmatically."""
    
    print("🚀 Multi-Agent Strategy Consulting Team - Example Usage")
    print("=" * 70)
    
    # Example 1: Basic consulting engagement
    print("\n📋 EXAMPLE 1: Basic Consulting Engagement")
    print("-" * 50)
    
    try:
        # Get API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("⚠️  Skipping Example 1: OPENAI_API_KEY not set")
            print("   Set with: export OPENAI_API_KEY='your-api-key-here'")
        else:
            # Initialize consulting team
            company_name = "Netflix"
            project_dir = Path("./example_projects") / company_name.replace(' ', '_')
            
            print(f"🤖 Initializing consulting team for {company_name}...")
            team = ConsultingTeam(api_key, company_name, project_dir)
            
            # Define engagement parameters
            parameters = {
                "analysis_brief": "Analyze Netflix's strategy in the streaming wars, including competitive positioning, content strategy, and recommendations for maintaining market leadership",
                "engagement_type": "comprehensive_strategic_analysis",
                "analysis_depth": "executive_level",
                "deliverables": ["business_model_analysis", "market_research", "competitive_analysis", 
                               "financial_analysis", "risk_assessment", "implementation_plan", 
                               "strategy_narrative", "senior_partner_review"]
            }
            
            print("📊 Starting consulting engagement...")
            results = await team.execute_consulting_engagement(parameters)
            
            print("✅ Consulting engagement completed successfully!")
            print(f"📋 Final report: {results['final_report']}")
            print(f"📁 All outputs saved to: {project_dir}")
            
    except Exception as e:
        print(f"❌ Error in Example 1: {e}")
    
    # Example 2: Custom project with specific focus
    print("\n📋 EXAMPLE 2: Custom Project with Specific Focus")
    print("-" * 50)
    
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            company_name = "Tesla"
            project_dir = Path("./example_projects") / company_name.replace(' ', '_')
            
            print(f"🤖 Initializing consulting team for {company_name}...")
            team = ConsultingTeam(api_key, company_name, project_dir)
            
            # Custom parameters for Tesla analysis
            parameters = {
                "analysis_brief": "Evaluate Tesla's strategic position in the electric vehicle market, including competitive advantages, market opportunities, and strategic risks. Focus on innovation strategy and market expansion.",
                "engagement_type": "innovation_strategy_analysis",
                "analysis_depth": "detailed_technical",
                "deliverables": ["business_model_analysis", "market_research", "competitive_analysis", 
                               "risk_assessment", "strategy_narrative", "senior_partner_review"],
                "focus_areas": ["innovation_strategy", "market_expansion", "competitive_positioning"],
                "industry_context": "automotive_electric_vehicles"
            }
            
            print("📊 Starting Tesla innovation strategy analysis...")
            results = await team.execute_consulting_engagement(parameters)
            
            print("✅ Tesla analysis completed successfully!")
            print(f"📋 Final report: {results['final_report']}")
            
        else:
            print("⚠️  Skipping Example 2: OPENAI_API_KEY not set")
            
    except Exception as e:
        print(f"❌ Error in Example 2: {e}")
    
    # Example 3: Batch analysis of multiple companies
    print("\n📋 EXAMPLE 3: Batch Analysis of Multiple Companies")
    print("-" * 50)
    
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            companies_to_analyze = [
                {
                    "name": "Amazon",
                    "brief": "Analyze Amazon's diversification strategy across e-commerce, cloud computing, and other business segments. Focus on ecosystem strategy and competitive moats.",
                    "focus": "ecosystem_strategy"
                },
                {
                    "name": "Microsoft",
                    "brief": "Evaluate Microsoft's enterprise software strategy and cloud transformation approach. Focus on enterprise positioning and cloud strategy.",
                    "focus": "enterprise_cloud_strategy"
                }
            ]
            
            print("🔄 Starting batch analysis of multiple companies...")
            
            for company_data in companies_to_analyze:
                print(f"\n📊 Analyzing {company_data['name']}...")
                
                project_dir = Path("./example_projects") / company_data['name'].replace(' ', '_')
                team = ConsultingTeam(api_key, company_data['name'], project_dir)
                
                parameters = {
                    "analysis_brief": company_data['brief'],
                    "engagement_type": "focused_strategic_analysis",
                    "analysis_depth": "executive_level",
                    "deliverables": ["business_model_analysis", "market_research", "competitive_analysis", 
                                   "strategy_narrative", "senior_partner_review"],
                    "focus_areas": [company_data['focus']]
                }
                
                results = await team.execute_consulting_engagement(parameters)
                print(f"✅ {company_data['name']} analysis completed!")
                print(f"   📋 Report: {results['final_report']}")
            
            print("\n🎉 Batch analysis completed successfully!")
            
        else:
            print("⚠️  Skipping Example 3: OPENAI_API_KEY not set")
            
    except Exception as e:
        print(f"❌ Error in Example 3: {e}")

async def demonstrate_agent_collaboration():
    """Demonstrate how agents can collaborate and learn from each other."""
    
    print("\n📋 EXAMPLE 4: Agent Collaboration Demonstration")
    print("-" * 50)
    
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("⚠️  Skipping Example 4: OPENAI_API_KEY not set")
            return
        
        company_name = "Spotify"
        project_dir = Path("./example_projects") / company_name.replace(' ', '_')
        
        print(f"🤖 Demonstrating agent collaboration for {company_name}...")
        team = ConsultingTeam(api_key, company_name, project_dir)
        
        # Show how agents work in phases with dependencies
        print("\n📋 Agent Execution Phases:")
        print("Phase 1: Core Analysis (Business Model, Market Research, Competitive Analysis)")
        print("Phase 2: Specialized Analysis (Financial Analysis, Risk Assessment)")
        print("Phase 3: Implementation Planning")
        print("Phase 4: Strategy Synthesis")
        print("Phase 5: Senior Partner Review")
        
        parameters = {
            "analysis_brief": "Analyze Spotify's business model strategy, including freemium approach, content licensing, and strategic partnerships. Focus on subscription model innovation and market expansion.",
            "engagement_type": "business_model_innovation_analysis",
            "analysis_depth": "detailed_strategic",
            "deliverables": ["business_model_analysis", "market_research", "competitive_analysis", 
                           "financial_analysis", "risk_assessment", "implementation_plan", 
                           "strategy_narrative", "senior_partner_review"]
        }
        
        print("\n📊 Starting collaborative analysis...")
        results = await team.execute_consulting_engagement(parameters)
        
        print("✅ Collaborative analysis completed!")
        print(f"📋 Final report: {results['final_report']}")
        
        # Show agent outputs and collaboration
        print("\n📁 Agent Collaboration Results:")
        for role, result in results['agent_results'].items():
            if isinstance(result, dict) and result.get("status") == "completed":
                print(f"   ✅ {role}: Completed with dependencies")
            else:
                print(f"   ❌ {role}: Failed or incomplete")
        
    except Exception as e:
        print(f"❌ Error in Example 4: {e}")

if __name__ == "__main__":
    print("Make sure you have set the OPENAI_API_KEY environment variable")
    print("export OPENAI_API_KEY='your-api-key-here'")
    print()
    
    # Run examples
    asyncio.run(main())
    
    # Demonstrate agent collaboration
    asyncio.run(demonstrate_agent_collaboration())
    
    print("\n" + "=" * 70)
    print("Example usage completed!")
    print("Check the generated project directories for detailed analysis results.")
    print("Each agent saves their work in markdown files with metadata in JSON.")
    print("=" * 70)
