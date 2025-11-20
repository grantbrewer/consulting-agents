#!/usr/bin/env python3
"""
Claude Agent SDK Orchestrator for Multi-Agent Strategy Consulting

This orchestrator coordinates 8 specialized consulting agents using the Claude Agent SDK
to deliver comprehensive strategic business analysis.

Usage:
    python orchestrator.py --company "CompanyName" --brief "Strategic analysis brief"
"""

import os
import argparse
from pathlib import Path
from anthropic import Anthropic
from datetime import datetime
import json

class ConsultingOrchestrator:
    """
    Orchestrates multi-agent consulting analysis using Claude's subagent system.

    This class coordinates 8 specialized consulting agents in a phased approach:
    - Phase 1: Business Model, Market, Competitive Analysis (parallel)
    - Phase 2: Financial Analysis, Risk Assessment (parallel, depends on Phase 1)
    - Phase 3: Implementation Planning (depends on Phase 2)
    - Phase 4: Strategic Storytelling (depends on Phase 3)
    - Phase 5: Senior Partner Review (depends on Phase 4)
    """

    def __init__(self, api_key: str, company_name: str, brief: str):
        """
        Initialize the orchestrator.

        Args:
            api_key: Anthropic API key
            company_name: Name of company being analyzed
            brief: Strategic analysis brief/objectives
        """
        self.client = Anthropic(api_key=api_key)
        self.company_name = company_name
        self.brief = brief
        self.project_dir = Path(f"consulting_projects/{company_name}")
        self.project_dir.mkdir(parents=True, exist_ok=True)

        # Track execution metadata
        self.metadata = {
            "company": company_name,
            "brief": brief,
            "start_time": datetime.now().isoformat(),
            "agents_executed": [],
            "status": "in_progress"
        }

    def run_analysis(self) -> dict:
        """
        Execute the complete multi-agent strategic analysis.

        Returns:
            dict: Analysis results and metadata
        """
        print(f"\n{'='*80}")
        print(f"🚀 Multi-Agent Strategy Consulting Analysis")
        print(f"{'='*80}")
        print(f"Company: {self.company_name}")
        print(f"Project Directory: {self.project_dir}")
        print(f"{'='*80}\n")

        # Create the orchestrator prompt
        orchestrator_prompt = self._build_orchestrator_prompt()

        print("📊 Launching Lead Orchestrator Agent (Claude Opus)...\n")

        try:
            # Execute with streaming for real-time progress
            with self.client.messages.stream(
                model="claude-opus-4-20250514",  # Lead orchestrator uses Opus for superior reasoning
                max_tokens=8000,
                messages=[{
                    "role": "user",
                    "content": orchestrator_prompt
                }],
                # Subagents are auto-discovered from .claude/agents/ directory
            ) as stream:
                # Stream output to console for real-time progress
                full_response = ""
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                    full_response += text

            final_message = stream.get_final_message()

            # Update metadata
            self.metadata["end_time"] = datetime.now().isoformat()
            self.metadata["status"] = "completed"
            self.metadata["output_length"] = len(full_response)

            # Save metadata
            self._save_metadata()

            # Save final orchestrator output
            orchestrator_output_path = self.project_dir / "orchestrator_execution_log.md"
            with open(orchestrator_output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Orchestrator Execution Log\n\n")
                f.write(f"**Company:** {self.company_name}\n\n")
                f.write(f"**Brief:** {self.brief}\n\n")
                f.write(f"**Execution Time:** {self.metadata['start_time']} to {self.metadata['end_time']}\n\n")
                f.write(f"---\n\n")
                f.write(full_response)

            print(f"\n\n{'='*80}")
            print(f"✅ Analysis Completed Successfully!")
            print(f"{'='*80}")
            print(f"📁 Results saved to: {self.project_dir}")
            print(f"{'='*80}\n")

            return {
                "status": "completed",
                "company": self.company_name,
                "project_dir": str(self.project_dir),
                "metadata": self.metadata
            }

        except Exception as e:
            print(f"\n\n❌ Error during analysis: {e}\n")
            self.metadata["status"] = "failed"
            self.metadata["error"] = str(e)
            self._save_metadata()
            raise

    def _build_orchestrator_prompt(self) -> str:
        """Build the main orchestrator prompt that coordinates all subagents."""

        prompt = f"""You are the Lead Partner of an elite strategy consulting firm conducting a comprehensive strategic analysis for **{self.company_name}**.

## Client Brief

{self.brief}

## Your Mission

Coordinate a team of 8 specialized consulting agents to deliver a world-class strategic analysis. Each agent has specific expertise and will save their analysis to the project directory.

## Agent Team & Execution Phases

Execute the following phases in order, invoking the appropriate subagents:

### Phase 1: Foundation Analysis (Execute in Parallel)
Invoke these three agents simultaneously to build the analytical foundation:

1. **business-model-analyst**
   - Analyze {self.company_name}'s business model, value proposition, and revenue streams
   - Save output to: `consulting_projects/{self.company_name}/business_model_analysis.md`

2. **market-researcher**
   - Conduct market sizing, TAM analysis, and market dynamics research
   - Save output to: `consulting_projects/{self.company_name}/market_research.md`

3. **competitive-analyst**
   - Analyze competitive landscape, positioning, and strategic advantages
   - Save output to: `consulting_projects/{self.company_name}/competitive_analysis.md`

### Phase 2: Financial & Risk Analysis (Execute in Parallel, after Phase 1)
After Phase 1 completes, invoke these agents:

4. **financial-analyst**
   - Analyze financial performance, unit economics, and strategic financial options
   - Use insights from Phase 1 agents
   - Save output to: `consulting_projects/{self.company_name}/financial_analysis.md`

5. **risk-assessor**
   - Identify and assess strategic, operational, and market risks
   - Use insights from Phase 1 agents
   - Save output to: `consulting_projects/{self.company_name}/risk_assessment.md`

### Phase 3: Implementation Planning (After Phase 2)

6. **implementation-specialist**
   - Create detailed implementation roadmap and execution plan
   - Build on insights from all previous phases
   - Save output to: `consulting_projects/{self.company_name}/implementation_roadmap.md`

### Phase 4: Strategic Narrative (After Phase 3)

7. **strategy-storyteller**
   - Synthesize all analysis into compelling strategic narrative
   - Integrate insights from all 6 previous agents
   - Save output to: `consulting_projects/{self.company_name}/strategic_narrative.md`

### Phase 5: Senior Review (After Phase 4)

8. **senior-partner**
   - Final quality review and senior strategic counsel
   - Review all previous agent outputs
   - Save output to: `consulting_projects/{self.company_name}/senior_partner_review.md`

## Execution Instructions

1. **Invoke agents by name** - Simply refer to them (e.g., "I'll now engage the business-model-analyst...")
2. **Pass context between phases** - Ensure later agents can access insights from earlier phases
3. **Ensure outputs are saved** - Each agent should save to the specified file path
4. **Provide progress updates** - Keep me informed as each phase completes
5. **Synthesize final deliverable** - Create a final strategic report integrating all insights

## Final Deliverable

After all agents complete, create a comprehensive final strategic report:
- Save to: `consulting_projects/{self.company_name}/final_strategic_report_{self.company_name}.md`
- Include: Executive summary, key insights from all agents, integrated recommendations
- Format: Professional consulting deliverable ready for C-suite presentation

Begin the analysis now. Coordinate the team systematically through each phase.
"""
        return prompt

    def _save_metadata(self):
        """Save execution metadata to JSON file."""
        metadata_path = self.project_dir / "execution_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)


def main():
    """Main entry point for the orchestrator."""
    parser = argparse.ArgumentParser(
        description="Multi-Agent Strategy Consulting using Claude Agent SDK"
    )
    parser.add_argument(
        "--company",
        required=True,
        help="Name of the company to analyze"
    )
    parser.add_argument(
        "--brief",
        required=True,
        help="Strategic analysis brief and objectives"
    )
    parser.add_argument(
        "--api-key",
        help="Anthropic API key (or set ANTHROPIC_API_KEY environment variable)"
    )

    args = parser.parse_args()

    # Get API key from argument or environment
    api_key = args.api_key or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY not found!")
        print("   Set it via environment variable or --api-key argument")
        return 1

    # Create and run orchestrator
    orchestrator = ConsultingOrchestrator(
        api_key=api_key,
        company_name=args.company,
        brief=args.brief
    )

    try:
        result = orchestrator.run_analysis()
        print(f"\n✅ Success! Check results at: {result['project_dir']}\n")
        return 0
    except Exception as e:
        print(f"\n❌ Analysis failed: {e}\n")
        return 1


if __name__ == "__main__":
    exit(main())
