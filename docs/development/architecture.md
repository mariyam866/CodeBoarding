```mermaid
graph LR
    Orchestration_Workflow["Orchestration & Workflow"]
    Static_Code_Analyzer["Static Code Analyzer"]
    AI_Analysis_Engine["AI Analysis Engine"]
    Analysis_Persistence["Analysis Persistence"]
    Output_Generator["Output Generator"]
    Orchestration_Workflow -- "invokes analysis on" --> Static_Code_Analyzer
    Static_Code_Analyzer -- "returns raw graph data to" --> Orchestration_Workflow
    Orchestration_Workflow -- "consults and saves analysis to" --> Analysis_Persistence
    Analysis_Persistence -- "provides cached analysis to" --> Orchestration_Workflow
    Orchestration_Workflow -- "invokes with graph data" --> AI_Analysis_Engine
    AI_Analysis_Engine -- "returns high-level model to" --> Orchestration_Workflow
    Orchestration_Workflow -- "sends model for rendering to" --> Output_Generator
    click Orchestration_Workflow href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestration_Workflow.md" "Details"
    click Static_Code_Analyzer href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Static_Code_Analyzer.md" "Details"
    click AI_Analysis_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/AI_Analysis_Engine.md" "Details"
    click Output_Generator href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Output_Generator.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

Abstract Components Overview

### Orchestration & Workflow [[Expand]](./Orchestration_Workflow.md)
The central coordinator that manages the end-to-end analysis pipeline. It initiates static analysis, triggers the AI engine, coordinates with the persistence layer for caching and differential checks, and sends the final, validated results to the output generator.


**Related Classes/Methods**:

- `local_app.py`
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py" target="_blank" rel="noopener noreferrer">`github_action.py`</a>


### Static Code Analyzer [[Expand]](./Static_Code_Analyzer.md)
Responsible for the initial, non-AI parsing of the source code. It uses AST-based techniques to build foundational data structures like call graphs and structure graphs, transforming raw code into a structured format that the AI engine can interpret.


**Related Classes/Methods**:

- `static_analyzer/pylint_analyze/call_graph_builder.py`
- `static_analyzer/pylint_analyze/structure_graph_builder.py`
- `static_analyzer/pylint_graph_transform.py`


### AI Analysis Engine [[Expand]](./AI_Analysis_Engine.md)
The cognitive core of the system. It is a multi-agent framework that interprets the data from the static analyzer. It uses a collection of specialized agents (e.g., Planner, Abstraction, Diff Analyzer) to collaboratively identify architectural patterns, understand component roles, and build a comprehensive model of the codebase.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/agent.py" target="_blank" rel="noopener noreferrer">`agents/agent.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/planner_agent.py" target="_blank" rel="noopener noreferrer">`agents/planner_agent.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/abstraction_agent.py" target="_blank" rel="noopener noreferrer">`agents/abstraction_agent.py`</a>
- `agents/diff_analyzer.py`


### Analysis Persistence
Handles the serialization and deserialization of the analysis model to a storable format (JSON). This enables the caching of results, which is critical for performance and for supporting efficient incremental analysis by providing a baseline for comparison.


**Related Classes/Methods**:

- `diagram_analysis/analysis_json.py`


### Output Generator [[Expand]](./Output_Generator.md)
The final stage in the pipeline. It consumes the rich, structured analysis model produced by the AI Engine and renders it into various human-readable formats, such as Markdown, HTML, and Sphinx documentation. Recent changes indicate a streamlining or simplification of its output capabilities.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/markdown.py" target="_blank" rel="noopener noreferrer">`output_generators/markdown.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/html.py" target="_blank" rel="noopener noreferrer">`output_generators/html.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/sphinx.py" target="_blank" rel="noopener noreferrer">`output_generators/sphinx.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/mdx.py" target="_blank" rel="noopener noreferrer">`output_generators/mdx.py`</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    CodeBoardingAgent["CodeBoardingAgent"]
    LLM_Provider_Interface["LLM Provider Interface"]
    PlannerAgent["PlannerAgent"]
    AbstractionAgent["AbstractionAgent"]
    DiffAnalyzerAgent["DiffAnalyzerAgent"]
    CodeBoardingAgent -- "uses" --> LLM_Provider_Interface
    CodeBoardingAgent -- "orchestrates" --> PlannerAgent
    CodeBoardingAgent -- "orchestrates" --> AbstractionAgent
    CodeBoardingAgent -- "orchestrates" --> DiffAnalyzerAgent
    LLM_Provider_Interface -- "is used by" --> CodeBoardingAgent
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The AI Analysis Engine subsystem is the cognitive core of the system, responsible for interpreting static analysis data through a multi-agent framework. It leverages specialized agents to identify architectural patterns, understand component roles, and build a comprehensive codebase model.

### CodeBoardingAgent
The central orchestrator of the AI analysis workflow. It manages analysis requests, initializes LLMs, invokes them with prompts, and processes their responses. It acts as the primary coordinator for all specialized agents within the engine.


**Related Classes/Methods**:

- `agents.agent`


### LLM Provider Interface
Provides an abstraction layer for interacting with various Large Language Model providers (e.g., OpenAI, Anthropic, Google Gemini, AWS Bedrock). It handles API calls, model selection, and standardizes response retrieval, decoupling the core logic from specific LLM vendor implementations.


**Related Classes/Methods**:

- `llm_providers.interface` (1:1)


### PlannerAgent
A specialized AI agent focused on strategic planning within the analysis workflow. It determines the sequence of steps and sub-tasks required to achieve a given analysis objective, guiding the overall process.


**Related Classes/Methods**:

- `agents.planner_agent`


### AbstractionAgent
A specialized AI agent responsible for identifying and generating higher-level abstractions from raw code data. This includes summarizing code sections, identifying design patterns, and distilling complex details into more manageable concepts.


**Related Classes/Methods**:

- `agents.abstraction_agent`


### DiffAnalyzerAgent
A specialized AI agent dedicated to analyzing differences between code versions or states. It identifies changes, assesses their impact, and provides insights into how modifications affect architectural patterns or component roles.


**Related Classes/Methods**:

- `agents.diff_analyzer`




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    api_layer["api_layer"]
    orchestration_workflow["orchestration_workflow"]
    static_analysis_module["static_analysis_module"]
    ai_analysis_engine["ai_analysis_engine"]
    data_persistence["data_persistence"]
    output_generation["output_generation"]
    integrations["integrations"]
    configuration["configuration"]
    api_layer -- "initiates analysis requests" --> orchestration_workflow
    orchestration_workflow -- "returns processed results" --> api_layer
    orchestration_workflow -- "invokes" --> static_analysis_module
    orchestration_workflow -- "submits static analysis results to" --> ai_analysis_engine
    orchestration_workflow -- "stores results in" --> data_persistence
    data_persistence -- "provides cached data to" --> orchestration_workflow
    orchestration_workflow -- "provides processed data to" --> output_generation
    integrations -- "provides raw source code to" --> orchestration_workflow
    configuration -- "provides settings to" --> api_layer
    configuration -- "provides settings to" --> orchestration_workflow
    configuration -- "provides settings to" --> static_analysis_module
    configuration -- "provides settings to" --> ai_analysis_engine
    configuration -- "provides settings to" --> data_persistence
    configuration -- "provides settings to" --> output_generation
    configuration -- "provides settings to" --> integrations
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The `Orchestration & Workflow` component is central to the system, coordinating the entire analysis pipeline. Its interactions with other components are crucial for the system's functionality.

### api_layer
The primary interface for external communication, responsible for receiving analysis requests via HTTP and returning the final processed results. It acts as the system's public-facing entry point.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py#L1-L1" target="_blank" rel="noopener noreferrer">`local_app` (1:1)</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py#L1-L1" target="_blank" rel="noopener noreferrer">`github_action` (1:1)</a>


### orchestration_workflow
The central coordinator that manages the end-to-end analysis pipeline. It initiates static analysis, triggers the AI engine, coordinates with the persistence layer for caching and differential checks, and sends the final, validated results to the output generator.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py#L1-L1" target="_blank" rel="noopener noreferrer">`local_app` (1:1)</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py#L1-L1" target="_blank" rel="noopener noreferrer">`github_action` (1:1)</a>


### static_analysis_module
Responsible for parsing source code, building abstract syntax trees (ASTs), control flow graphs (CFGs), and extracting raw code metadata. It provides the foundational data for subsequent analysis steps.


**Related Classes/Methods**:

- `astroid` (1:1)
- `python-call-graph` (1:1)
- `networkx` (1:1)


### ai_analysis_engine
Encapsulates all interactions with Large Language Models (LLMs), including prompt engineering, multi-provider support (OpenAI, Anthropic, Google Gemini, AWS Bedrock), and processing LLM responses to derive high-level insights and recommendations.


**Related Classes/Methods**:

- `LangChain` (1:1)
- `LangGraph` (1:1)
- `OpenAI` (1:1)
- `Anthropic` (1:1)
- `Google Gemini` (1:1)
- `AWS Bedrock` (1:1)


### data_persistence
Manages data storage and retrieval for analysis results, intermediate data, and caching mechanisms. It abstracts the underlying database (e.g., DuckDB via SQLAlchemy) to provide a consistent data access layer.


**Related Classes/Methods**:

- `SQLAlchemy` (1:1)
- `DuckDB` (1:1)


### output_generation
Transforms processed analysis data into various user-consumable output formats, particularly interactive diagrams (e.g., Mermaid.js, pygraphviz, pydot) and other visualizations.


**Related Classes/Methods**:

- `pygraphviz` (1:1)
- `pydot` (1:1)
- `Mermaid.js` (1:1)


### integrations
Handles specific logic related to external services, such as cloning repositories from GitHub (using GitPython, Dulwich) and potential integrations with other platforms (VS Code, MCP Server).


**Related Classes/Methods**:

- `GitPython` (1:1)
- `Dulwich` (1:1)


### configuration
Centralizes application settings, environment variable loading, and credential management, ensuring consistent and secure configuration across all components of the system.


**Related Classes/Methods**:

- `config_module` (1:1)




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    API_Layer["API Layer"]
    Orchestration_Workflow["Orchestration Workflow"]
    Static_Analysis_Module["Static Analysis Module"]
    AI_Analysis_Engine["AI Analysis Engine"]
    Data_Persistence["Data Persistence"]
    Output_Generator["Output Generator"]
    Integrations["Integrations"]
    Configuration["Configuration"]
    API_Layer -- "sends to" --> Orchestration_Workflow
    Orchestration_Workflow -- "sends to" --> Static_Analysis_Module
    Orchestration_Workflow -- "sends to" --> AI_Analysis_Engine
    Orchestration_Workflow -- "sends to" --> Output_Generator
    Static_Analysis_Module -- "sends to" --> Orchestration_Workflow
    AI_Analysis_Engine -- "sends to" --> Orchestration_Workflow
    Orchestration_Workflow -- "sends to" --> Data_Persistence
    AI_Analysis_Engine -- "sends to" --> Data_Persistence
    Data_Persistence -- "sends to" --> Orchestration_Workflow
    Data_Persistence -- "sends to" --> AI_Analysis_Engine
    Orchestration_Workflow -- "sends to" --> Integrations
    Configuration -- "provides to" --> API_Layer
    Configuration -- "provides to" --> Orchestration_Workflow
    Configuration -- "provides to" --> Static_Analysis_Module
    Configuration -- "provides to" --> AI_Analysis_Engine
    Configuration -- "provides to" --> Data_Persistence
    Configuration -- "provides to" --> Output_Generator
    Configuration -- "provides to" --> Integrations
    click Orchestration_Workflow href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestration_Workflow.md" "Details"
    click AI_Analysis_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/AI_Analysis_Engine.md" "Details"
    click Output_Generator href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Output_Generator.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

One paragraph explaining the functionality which is represented by this graph. What the main flow is and what is its purpose.

### API Layer
This component serves as the external interface for the application, built using FastAPI. It defines all public endpoints, handles incoming HTTP requests, validates request/response models, and orchestrates the initial interaction with the `Orchestration Workflow`. It ensures secure and structured communication with clients.


**Related Classes/Methods**:

- `local_app.py`


### Orchestration Workflow [[Expand]](./Orchestration_Workflow.md)
The `Orchestration Workflow` is the central coordinator of the analysis pipeline. Leveraging frameworks like LangChain/LangGraph, it manages the overall flow of operations, sequencing calls between the `Static Analysis Module`, `AI Analysis Engine`, and `Output Generation` components. It ensures data is correctly passed between stages and handles the overall execution logic.


**Related Classes/Methods**:

- `local_app.py`
- `demo.py`


### Static Analysis Module
This component is responsible for the initial, language-agnostic processing of source code. It parses code, builds Abstract Syntax Trees (ASTs), generates Control Flow Graphs (CFGs), and extracts raw code metadata. It acts as the foundational data provider for subsequent AI-driven analysis.


**Related Classes/Methods**:

- `agents/tools/read_cfg.py`
- `agents/tools/read_source.py`


### AI Analysis Engine [[Expand]](./AI_Analysis_Engine.md)
The `AI Analysis Engine` encapsulates all interactions with Large Language Models (LLMs) from various providers (OpenAI, Anthropic, Google Gemini, AWS Bedrock). It handles prompt engineering, manages multi-provider support, processes LLM responses, and transforms raw static analysis data into rich, structured analysis models using AI capabilities.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/agent.py#L1-L1" target="_blank" rel="noopener noreferrer">`agents/agent.py` (1:1)</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/meta_agent.py#L1-L1" target="_blank" rel="noopener noreferrer">`agents/meta_agent.py` (1:1)</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/planner_agent.py#L1-L1" target="_blank" rel="noopener noreferrer">`agents/planner_agent.py` (1:1)</a>


### Data Persistence
This component provides an abstraction layer for all data storage and retrieval operations. It manages the persistence of analysis results, intermediate data, and caching mechanisms. It abstracts the underlying database technology (e.g., DuckDB via SQLAlchemy), ensuring other components do not need direct database knowledge.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/duckdb_crud.py#L1-L1" target="_blank" rel="noopener noreferrer">`duckdb_crud.py` (1:1)</a>


### Output Generator [[Expand]](./Output_Generator.md)
The `Output Generator` component serves as the final stage in the project's analysis pipeline. Its primary responsibility is to consume the rich, structured analysis models, which are typically produced by the `AI Analysis Engine` and coordinated by the `Orchestration Workflow`. It then transforms these models into various human-readable and machine-consumable formats, including Markdown, HTML, Sphinx documentation, and MDX. A key emphasis of this component is the generation of interactive diagrams, such as those using Mermaid.js, to enhance visualization of the analysis results. Recent architectural adjustments indicate a streamlining or simplification of its output capabilities, focusing on efficient and targeted rendering. This component is crucial for making complex code analysis results accessible and actionable for users.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/html.py#L1-L1" target="_blank" rel="noopener noreferrer">`output_generators/html.py` (1:1)</a>
- `diagram_analysis/diagram_generator.py`


### Integrations
This component is dedicated to managing interactions with external services. This includes specific logic for cloning repositories from platforms like GitHub using `GitPython` or `Dulwich`, and potentially other integrations with tools like VS Code or an MCP Server. It isolates external API complexities from core business logic.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py#L1-L1" target="_blank" rel="noopener noreferrer">`github_action.py` (1:1)</a>
- `repo_utils.py` (1:1)


### Configuration
The `Configuration` component centralizes all application settings, environment variable loading, and credential management. It provides a consistent and secure way for other components to access necessary parameters without hardcoding, facilitating easy deployment and environment-specific adjustments.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/logging_config.py#L1-L1" target="_blank" rel="noopener noreferrer">`logging_config.py` (1:1)</a>
- `local_app.py`




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    Static_Code_Analyzer["Static Code Analyzer"]
    orchestration_workflow["orchestration_workflow"]
    ai_analysis_engine["ai_analysis_engine"]
    data_persistence["data_persistence"]
    integrations["integrations"]
    orchestration_workflow -- "sends raw code or analysis requests to" --> Static_Code_Analyzer
    Static_Code_Analyzer -- "provides structured code data and initial analysis results back to" --> orchestration_workflow
    Static_Code_Analyzer -- "provides structured code data to" --> ai_analysis_engine
    Static_Code_Analyzer -- "provides extracted code metadata and generated graphs to" --> data_persistence
    Static_Code_Analyzer -- "utilizes" --> integrations
    click Static_Code_Analyzer href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Static_Code_Analyzer.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

One paragraph explaining the functionality which is represented by this graph. What the main flow is and what is its purpose.

### Static Code Analyzer [[Expand]](./Static_Code_Analyzer.md)
The Static Code Analyzer component is responsible for the initial, non-AI parsing of source code. It leverages Abstract Syntax Tree (AST)-based techniques to build foundational data structures such as ASTs, Call Graphs, and Structure Graphs. Its primary role is to transform raw code into a structured, machine-readable format, extracting essential code metadata that can then be interpreted and further processed by the AI analysis engine. This component is fundamental as it provides the structured input necessary for all subsequent AI-driven analysis.


**Related Classes/Methods**:

- `static_analyzer/pylint_analyze/call_graph_builder.py`
- `static_analyzer/pylint_analyze/structure_graph_builder.py`


### orchestration_workflow
This component acts as the central coordinator for the code analysis process. It is responsible for receiving raw code or analysis requests, initiating the static analysis process, and managing the flow of data between different analysis stages. It orchestrates the interaction with the `Static Code Analyzer` and potentially other downstream components, ensuring that the analysis pipeline executes correctly.


**Related Classes/Methods**: _None_

### ai_analysis_engine
The `AI Analysis Engine` component is responsible for performing advanced, AI-driven analysis on the structured code data provided by the `Static Code Analyzer`. It leverages machine learning models and algorithms to identify complex patterns, potential vulnerabilities, or areas for optimization that go beyond traditional static analysis.


**Related Classes/Methods**: _None_

### data_persistence
The `Data Persistence` component is responsible for securely storing and retrieving all generated analysis artifacts, including extracted code metadata, Abstract Syntax Trees (ASTs), Call Graphs, and Structure Graphs. It ensures the long-term availability and integrity of the analysis results for historical tracking, reporting, and further processing.


**Related Classes/Methods**: _None_

### integrations
The `Integrations` component provides a standardized interface for interacting with external systems, tools, or services. It handles the communication protocols and data formats required to exchange information with external platforms, such as version control systems, CI/CD pipelines, or reporting dashboards, enabling the seamless flow of code and analysis results.


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)

