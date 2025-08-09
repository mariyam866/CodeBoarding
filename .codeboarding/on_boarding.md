```mermaid
graph LR
    API_Service["API Service"]
    Orchestrator["Orchestrator"]
    Static_Analyzer["Static Analyzer"]
    AI_Interpretation_Engine["AI Interpretation Engine"]
    Output_Generator["Output Generator"]
    API_Service -- "Invokes" --> Orchestrator
    Orchestrator -- "Invokes" --> Static_Analyzer
    Orchestrator -- "Invokes" --> AI_Interpretation_Engine
    Orchestrator -- "Invokes" --> Output_Generator
    Output_Generator -- "Returns final report to" --> Orchestrator
    Orchestrator -- "Returns final report to" --> API_Service
    click API_Service href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/API_Service.md" "Details"
    click Orchestrator href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestrator.md" "Details"
    click Static_Analyzer href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Static_Analyzer.md" "Details"
    click AI_Interpretation_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/AI_Interpretation_Engine.md" "Details"
    click Output_Generator href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Output_Generator.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The system's main flow begins with the `API Service` receiving external requests, which then invokes the `Orchestrator`. The `Orchestrator` acts as the central coordinator, first initiating the `Static Analyzer` to perform code analysis and build foundational data structures. Subsequently, it passes this data to the `AI Interpretation Engine`, a suite of specialized AI agents that interpret the analysis and generate architectural insights. Finally, the `Orchestrator` directs the `Output Generator` to convert these insights into human-readable formats, with the final report being returned back through the `Orchestrator` to the `API Service`.

### API Service [[Expand]](./API_Service.md)
Serves as the primary entry point for all external interactions. It exposes the system's capabilities, handling incoming requests and returning the final generated analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py" target="_blank" rel="noopener noreferrer">`local_app.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py" target="_blank" rel="noopener noreferrer">`github_action.py`</a>


### Orchestrator [[Expand]](./Orchestrator.md)
Acts as the central coordinator of the analysis pipeline. It manages the sequence of operations, directing the flow of data between the various components to ensure the end-to-end process runs smoothly.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/meta_agent.py" target="_blank" rel="noopener noreferrer">`agents/meta_agent.py`</a>


### Static Analyzer [[Expand]](./Static_Analyzer.md)
Performs language-aware static analysis of the source code. It builds foundational data structures, including call graphs and package dependencies, which form the basis for the AI interpretation.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/scanner.py" target="_blank" rel="noopener noreferrer">`static_analyzer/scanner.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/lsp_client/" target="_blank" rel="noopener noreferrer">`static_analyzer/lsp_client/`</a>


### AI Interpretation Engine [[Expand]](./AI_Interpretation_Engine.md)
A suite of specialized AI agents responsible for interpreting the static analysis data. It uses a planner, abstraction, and validator agents, along with a toolkit for reading code artifacts, to generate high-level architectural insights. The core agent functionality, likely defined in `agents/agent.py`, has been updated to enhance or refine the capabilities shared by the specialized agents.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/planner_agent.py" target="_blank" rel="noopener noreferrer">`agents/planner_agent.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/abstraction_agent.py" target="_blank" rel="noopener noreferrer">`agents/abstraction_agent.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/validator_agent.py" target="_blank" rel="noopener noreferrer">`agents/validator_agent.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/tools/" target="_blank" rel="noopener noreferrer">`agents/tools/`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/agent.py" target="_blank" rel="noopener noreferrer">`agents/agent.py`</a>


### Output Generator [[Expand]](./Output_Generator.md)
Responsible for converting the final, validated analysis from the AI engine into human-readable formats. It serializes the analysis data and renders it as diagrams and text.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/html.py" target="_blank" rel="noopener noreferrer">`output_generators/html.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/markdown.py" target="_blank" rel="noopener noreferrer">`output_generators/markdown.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`diagram_analysis/diagram_generator.py`</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
