```mermaid
graph LR
    Orchestration_Engine["Orchestration Engine"]
    MetaAgent["MetaAgent"]
    AbstractionAgent["AbstractionAgent"]
    DetailsAgent["DetailsAgent"]
    PlannerAgent["PlannerAgent"]
    ValidatorAgent["ValidatorAgent"]
    ProjectScanner["ProjectScanner"]
    StaticAnalysisResults["StaticAnalysisResults"]
    Unclassified["Unclassified"]
    Orchestration_Engine -- "orchestrates" --> ProjectScanner
    ProjectScanner -- "produces" --> StaticAnalysisResults
    Orchestration_Engine -- "consumes" --> StaticAnalysisResults
    Orchestration_Engine -- "orchestrates" --> MetaAgent
    Orchestration_Engine -- "exchanges data with" --> MetaAgent
    Orchestration_Engine -- "orchestrates" --> AbstractionAgent
    Orchestration_Engine -- "exchanges data with" --> AbstractionAgent
    Orchestration_Engine -- "orchestrates" --> DetailsAgent
    Orchestration_Engine -- "exchanges data with" --> DetailsAgent
    Orchestration_Engine -- "orchestrates" --> PlannerAgent
    Orchestration_Engine -- "exchanges data with" --> PlannerAgent
    Orchestration_Engine -- "orchestrates" --> ValidatorAgent
    Orchestration_Engine -- "exchanges data with" --> ValidatorAgent
    click Orchestration_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestration_Engine.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The core of the system is the Orchestration Engine, which drives the entire documentation generation process. It begins by engaging the ProjectScanner to gather comprehensive static analysis data from the codebase, now including specialized TypeScript configuration scanning. This collected data is then encapsulated within StaticAnalysisResults, serving as the foundational input for subsequent analysis stages. The Orchestration Engine then orchestrates a series of specialized AI agents (MetaAgent, AbstractionAgent, DetailsAgent, PlannerAgent, ValidatorAgent) to progressively analyze the project, generate architectural abstractions, detail component responsibilities, plan future analysis, and validate the generated documentation, ensuring accuracy and consistency. The system is centered around an Orchestration Engine that manages the entire documentation generation pipeline. It initiates the ProjectScanner to collect static analysis data, including specialized TypeScript configuration scans, which is then stored in StaticAnalysisResults. The Orchestration Engine then coordinates a suite of AI agents—MetaAgent, AbstractionAgent, DetailsAgent, PlannerAgent, and ValidatorAgent—to perform various analysis tasks, generate architectural insights, plan subsequent analysis, and validate the overall output, ensuring a comprehensive and accurate documentation process.

### Orchestration Engine [[Expand]](./Orchestration_Engine.md)
The central control unit that manages the entire documentation generation pipeline, coordinating all analysis and generation stages. It initializes and coordinates AI agents, handles pre-analysis, processes components, determines update needs, applies feedback, and saves results.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindiagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`diagram_generator`</a>


### MetaAgent
An AI agent responsible for performing initial project metadata analysis, providing foundational context for subsequent analysis stages.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/meta_agent.py" target="_blank" rel="noopener noreferrer">`meta_agent`</a>


### AbstractionAgent
An AI agent that generates high-level architectural abstractions from the analyzed code, identifying major components and their relationships.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/abstraction_agent.py" target="_blank" rel="noopener noreferrer">`abstraction_agent`</a>


### DetailsAgent
An AI agent that provides detailed analysis of individual components, delving into their responsibilities, internal structure, and specific interactions.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/details_agent.py" target="_blank" rel="noopener noreferrer">`details_agent`</a>


### PlannerAgent
An AI agent that plans the next set of components to analyze, optimizing the analysis workflow based on dependencies and previous results.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/planner_agent.py" target="_blank" rel="noopener noreferrer">`planner_agent`</a>


### ValidatorAgent
An AI agent that validates the generated analysis and provides feedback, ensuring accuracy and consistency of the documentation.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/validator_agent.py" target="_blank" rel="noopener noreferrer">`validator_agent`</a>


### ProjectScanner
A component responsible for initiating and collecting static analysis data from the codebase, including specialized scanning for TypeScript configurations, serving as the primary input for the analysis pipeline.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/scanner.py" target="_blank" rel="noopener noreferrer">`scanner`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/typescript_config_scanner.py" target="_blank" rel="noopener noreferrer">`typescript_config_scanner`</a>


### StaticAnalysisResults
A data structure that holds the comprehensive results of static analysis, making this information accessible to the Orchestration Engine and AI agents.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/analysis_result.py" target="_blank" rel="noopener noreferrer">`analysis_result`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
