# Multi-Agent Strategy Consulting Team 🤖

An AI-powered consulting team consisting of specialized agents that work asynchronously to deliver comprehensive strategic analysis. Each agent has specific expertise and can collaborate with others to produce consulting-grade deliverables.

## 🚀 Features

- **Multi-Agent Architecture**: Team of 8 specialized AI agents working asynchronously
- **GPT-5 Powered**: All agents use the latest GPT-5 technology for superior analysis
- **Collaborative Workflow**: Agents can learn from each other's outputs and collaborate
- **Structured Output**: Each agent saves work in markdown files with metadata in JSON
- **Phase-Based Execution**: Intelligent dependency management and parallel processing
- **Professional Quality**: Consulting-grade strategic analysis and deliverables
- **Comprehensive Coverage**: Business model, market research, competitive analysis, financial analysis, risk assessment, implementation planning, strategy narrative, and senior partner review

## 🤖 The Consulting Team

### **Core Analysis Agents (Phase 1)**
1. **Business Model Analyst** - Analyzes and defines business models, revenue streams, and value chains
2. **Market Researcher** - Researches TAM, market dynamics, and competitive landscape
3. **Competitive Analyst** - Analyzes competitive positioning and strategic advantages

### **Specialized Analysis Agents (Phase 2)**
4. **Financial Analyst** - Assesses financial performance and strategic financial options
5. **Risk Assessor** - Evaluates strategic and operational risks with mitigation strategies

### **Implementation & Synthesis Agents (Phase 3-4)**
6. **Implementation Specialist** - Creates implementation roadmaps and execution strategies
7. **Strategy Storyteller** - Weaves insights into compelling strategic narratives

### **Quality Assurance (Phase 5)**
8. **Senior Partner** - Reviews all work and provides strategic synthesis and guidance

## 📋 Prerequisites

- Python 3.7 or higher
- OpenAI API key with access to GPT-5
- Sufficient OpenAI API credits
- Asyncio support (included in Python 3.7+)

## 🛠️ Installation

1. **Clone or download the script files:**
   ```bash
   # Make sure you're in the ruby directory
   ls -la
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   ```bash
   # Option 1: Set environment variable
   export OPENAI_API_KEY="your-api-key-here"
   
   # Option 2: Use the --api-key parameter when running the script
   ```

## 🚀 Usage

### Basic Usage

```bash
python strategy_consulting_agent.py \
  --company "Apple Inc." \
  --brief "Analyze Apple's competitive strategy in the smartphone market and provide recommendations for maintaining market leadership"
```

### Advanced Usage

```bash
python strategy_consulting_agent.py \
  --company "Tesla" \
  --brief "Evaluate Tesla's strategic position in the electric vehicle market, including competitive advantages, market opportunities, and strategic risks" \
  --output-dir "./custom_projects" \
  --api-key "your-api-key"
```

### Command Line Options

- `--company, -c`: Company name to analyze (required)
- `--brief, -b`: Analysis brief describing what to analyze (required)
- `--output-dir, -o`: Output directory for project files (default: ./consulting_projects)
- `--api-key`: OpenAI API key (optional if environment variable is set)

## 🔄 Agent Workflow

The consulting team operates in phases with intelligent dependency management:

### **Phase 1: Core Analysis (Parallel Execution)**
- Business Model Analyst
- Market Researcher  
- Competitive Analyst

### **Phase 2: Specialized Analysis (Depends on Phase 1)**
- Financial Analyst
- Risk Assessor

### **Phase 3: Implementation Planning (Depends on Phase 2)**
- Implementation Specialist

### **Phase 4: Strategy Synthesis (Depends on all previous phases)**
- Strategy Storyteller

### **Phase 5: Senior Partner Review (Depends on all outputs)**
- Senior Partner

## 📁 Output Structure

Each project creates a structured directory with:

```
consulting_projects/
└── Company_Name/
    ├── agent_outputs/
    │   ├── business_model_analyst/
    │   │   ├── business_model_analyst_20241215_143022.md
    │   │   └── business_model_analyst_20241215_143022_metadata.json
    │   ├── market_researcher/
    │   ├── competitive_analyst/
    │   ├── financial_analyst/
    │   ├── risk_assessor/
    │   ├── implementation_specialist/
    │   ├── strategy_storyteller/
    │   └── senior_partner/
    └── final_strategic_report_Company_Name.md
```

## 💡 Example Analysis Briefs

### Business Model Innovation
```
"Analyze the company's business model innovation strategy, including revenue model evolution, value proposition development, and business model transformation opportunities"
```

### Market Entry Strategy
```
"Evaluate the company's readiness for entering the European market, including competitive landscape assessment, market entry strategies, and risk mitigation approaches"
```

### Digital Transformation
```
"Assess the company's digital transformation strategy, including current digital capabilities, transformation roadmap, and strategic recommendations for digital leadership"
```

### Competitive Positioning
```
"Analyze the company's competitive positioning in its core market, identify competitive advantages, and provide strategic recommendations for strengthening market position"
```

## 🔧 Programmatic Usage

```python
import asyncio
from strategy_consulting_agent import ConsultingTeam

async def run_consulting_engagement():
    team = ConsultingTeam(api_key, "Company Name", project_dir)
    
    parameters = {
        "analysis_brief": "Your analysis brief here",
        "engagement_type": "comprehensive_strategic_analysis",
        "analysis_depth": "executive_level"
    }
    
    results = await team.execute_consulting_engagement(parameters)
    return results

# Run the engagement
results = asyncio.run(run_consulting_engagement())
```

## 📊 Agent Collaboration Features

- **Dependency Management**: Agents automatically wait for required inputs
- **Parallel Execution**: Independent agents run simultaneously for efficiency
- **Knowledge Sharing**: Agents can access and learn from each other's outputs
- **Quality Assurance**: Senior Partner reviews all work for consistency and quality
- **Iterative Improvement**: Agents can request additional work from others

## 🎯 Use Cases

- **Strategic Planning**: Comprehensive strategic analysis for business planning
- **Market Entry**: Market research and competitive analysis for new markets
- **Business Model Innovation**: Analysis and optimization of business models
- **Competitive Intelligence**: Deep competitive analysis and positioning
- **Risk Assessment**: Comprehensive risk analysis and mitigation strategies
- **Implementation Planning**: Strategic implementation roadmaps and execution plans
- **Executive Presentations**: Professional strategy narratives and presentations
- **Consulting Engagements**: Full-service strategic consulting support

## 🚀 Performance Features

- **Asynchronous Execution**: Non-blocking agent execution for optimal performance
- **Parallel Processing**: Multiple agents work simultaneously when possible
- **Intelligent Caching**: Agents reuse outputs to avoid redundant work
- **Progress Tracking**: Real-time progress updates and status monitoring
- **Error Handling**: Graceful handling of agent failures with fallback options

## 🔍 Monitoring and Debugging

- **Real-time Progress**: Live updates on agent execution status
- **Detailed Logging**: Comprehensive logging of all agent activities
- **Output Validation**: Automatic validation of agent outputs
- **Dependency Tracking**: Clear visibility into agent dependencies and execution order
- **Performance Metrics**: Execution time and resource usage tracking

## 🛡️ Security and Best Practices

- **API Key Management**: Secure handling of OpenAI API keys
- **Output Isolation**: Each project runs in isolated directories
- **Error Handling**: Comprehensive error handling and recovery
- **Resource Management**: Efficient resource usage and cleanup
- **Audit Trail**: Complete audit trail of all agent activities and outputs

## 🔮 Future Enhancements

The system is designed for extensibility and can be enhanced with:

- **Additional Agent Types**: New specialized agents for specific industries or analysis types
- **Custom Workflows**: Configurable execution workflows and dependencies
- **Integration APIs**: REST APIs for external system integration
- **Advanced Analytics**: Machine learning-based insights and recommendations
- **Multi-Modal Outputs**: Support for presentations, visualizations, and interactive reports
- **Real-time Collaboration**: Live collaboration features for human-AI teams

## 📚 Example Projects

Run the example script to see the system in action:

```bash
python example_usage.py
```

This demonstrates:
- Basic consulting engagements
- Custom project configurations
- Batch analysis of multiple companies
- Agent collaboration workflows

## 🆘 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your OpenAI API key is set correctly
2. **Rate Limits**: If you hit rate limits, the system will handle retries automatically
3. **Token Limits**: For very long analyses, agents may need to break work into smaller chunks
4. **API Credits**: Ensure you have sufficient OpenAI API credits for all agents

### Error Messages

- `OpenAI API key is required`: Set the OPENAI_API_KEY environment variable or use --api-key
- `Agent execution failed`: Check your API key, credits, and network connectivity
- `Dependency not met`: Ensure all required agents have completed successfully

## 📄 License

This system is provided as-is for educational and business use. Please ensure compliance with OpenAI's terms of service and your organization's policies.

## 🤝 Contributing

Feel free to enhance the system with additional features such as:
- New specialized agent types
- Enhanced collaboration mechanisms
- Additional output formats
- Integration with external data sources
- Custom analysis templates
- Advanced workflow management

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your OpenAI API key and credits
3. Ensure you're using the latest version of the system
4. Check that all dependencies are properly installed
5. Review the agent output logs for detailed error information
