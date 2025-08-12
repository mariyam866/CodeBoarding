```mermaid
graph LR
    API_Service["API Service"]
    Job_Database["Job Database"]
    Orchestration_Engine["Orchestration Engine"]
    Repository_Manager["Repository Manager"]
    Static_Analysis_Engine["Static Analysis Engine"]
    AI_Interpretation_Layer["AI Interpretation Layer"]
    Output_Generation_Engine["Output Generation Engine"]
    API_Service -- "Initiates Job" --> Job_Database
    API_Service -- "Triggers Analysis" --> Orchestration_Engine
    Orchestration_Engine -- "Manages Job State" --> Job_Database
    Orchestration_Engine -- "Requests Code" --> Repository_Manager
    Repository_Manager -- "Provides Code" --> Orchestration_Engine
    Orchestration_Engine -- "Requests Static Analysis" --> Static_Analysis_Engine
    Static_Analysis_Engine -- "Provides Analysis Results" --> Orchestration_Engine
    Orchestration_Engine -- "Feeds Data" --> AI_Interpretation_Layer
    AI_Interpretation_Layer -- "Returns Insights" --> Orchestration_Engine
    AI_Interpretation_Layer -- "Queries Diff" --> Repository_Manager
    Orchestration_Engine -- "Passes Final Insights" --> Output_Generation_Engine
    Output_Generation_Engine -- "Delivers Documentation" --> API_Service
    click API_Service href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/API_Service.md" "Details"
    click Job_Database href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Job_Database.md" "Details"
    click Repository_Manager href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Repository_Manager.md" "Details"
    click Static_Analysis_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Static_Analysis_Engine.md" "Details"
    click AI_Interpretation_Layer href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/AI_Interpretation_Layer.md" "Details"
    click Output_Generation_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Output_Generation_Engine.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The CodeBoarding system operates as a sophisticated pipeline for automated architectural documentation. It begins with the API Service receiving a request, which is then logged and managed by the Job Database. The Orchestration Engine serves as the central nervous system, coordinating the entire analysis process. It first directs the Repository Manager to fetch the target codebase. This code then undergoes structural examination by the Static Analysis Engine. The resulting raw data is intelligently processed by the AI Interpretation Layer, a suite of agents that abstract, detail, plan, validate, and analyze changes within the architecture. Finally, the refined architectural insights are passed to the Output Generation Engine to produce various documentation formats, completing the cycle by making the output accessible via the API Service. This design emphasizes a clear, sequential flow, distinct component responsibilities, and extensibility for future language and AI model integrations.

### API Service [[Expand]](./API_Service.md)
The external interface for CodeBoarding, handling user requests, job initiation, and status retrieval.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py" target="_blank" rel="noopener noreferrer">`local_app`</a>


### Job Database [[Expand]](./Job_Database.md)
Persistent storage for managing the lifecycle, status, and results of all documentation generation jobs.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/duckdb_crud.py" target="_blank" rel="noopener noreferrer">`duckdb_crud`</a>


### Orchestration Engine
The central control unit that manages the entire documentation generation pipeline, coordinating all analysis and generation stages.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`diagram_generator`</a>


### Repository Manager [[Expand]](./Repository_Manager.md)
Manages all interactions with source code repositories, including cloning, fetching, and extracting version differences.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/diff_analyzer.py#L21-L32" target="_blank" rel="noopener noreferrer">`__init__`:21-32</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/repo_utils/git_diff.py#L27-L76" target="_blank" rel="noopener noreferrer">`git_diff`:27-76</a>


### Static Analysis Engine [[Expand]](./Static_Analysis_Engine.md)
Performs deep, language-specific analysis of source code to extract structural information without semantic interpretation.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/scanner.py#L13-L66" target="_blank" rel="noopener noreferrer">`scanner`:13-66</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/lsp_client/typescript_client.py#L10-L214" target="_blank" rel="noopener noreferrer">`client`:10-214</a>


### AI Interpretation Layer [[Expand]](./AI_Interpretation_Layer.md)
A collection of specialized AI agents that interpret static analysis data to generate high-level architectural insights, including abstraction, detailing, planning, validation, and diff analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`meta_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`abstraction_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`details_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`planner_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`validator_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/diff_analyzer.py" target="_blank" rel="noopener noreferrer">`diff_analyzer`</a>


### Output Generation Engine [[Expand]](./Output_Generation_Engine.md)
Transforms the final, validated architectural insights into various human-readable and diagram-friendly documentation formats.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py#L36-L50" target="_blank" rel="noopener noreferrer">`html`:36-50</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py#L19-L33" target="_blank" rel="noopener noreferrer">`markdown`:19-33</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py#L53-L67" target="_blank" rel="noopener noreferrer">`mdx`:53-67</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/sphinx.py" target="_blank" rel="noopener noreferrer">`sphinx`</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
