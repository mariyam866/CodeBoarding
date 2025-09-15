```mermaid
graph LR
    Orchestration_Engine["Orchestration Engine"]
    Job_Database["Job Database"]
    Repository_Manager["Repository Manager"]
    Static_Analysis_Engine["Static Analysis Engine"]
    AI_Interpretation_Layer_Agents_["AI Interpretation Layer (Agents)"]
    Diagram_Analysis["Diagram Analysis"]
    Output_Generation_Engine["Output Generation Engine"]
    External_Integrations["External Integrations"]
    Unclassified["Unclassified"]
    Orchestration_Engine -- "interacts with" --> Job_Database
    Orchestration_Engine -- "requests code from" --> Repository_Manager
    Orchestration_Engine -- "triggers" --> Static_Analysis_Engine
    Orchestration_Engine -- "dispatches tasks to" --> AI_Interpretation_Layer_Agents_
    Orchestration_Engine -- "invokes" --> Diagram_Analysis
    Orchestration_Engine -- "triggers" --> Output_Generation_Engine
    External_Integrations -- "triggers" --> Orchestration_Engine
    click Orchestration_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestration_Engine.md" "Details"
    click Job_Database href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Job_Database.md" "Details"
    click Static_Analysis_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Static_Analysis_Engine.md" "Details"
    click Output_Generation_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Output_Generation_Engine.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The CodeBoarding system is orchestrated by the Orchestration Engine, which serves as the central control unit for initiating and managing documentation generation jobs. External systems, such as VSCode and GitHub Actions, interact with the system through the External Integrations component, triggering the Orchestration Engine to begin a new analysis workflow. The Orchestration Engine relies on the Job Database to store and retrieve job-related information and status updates throughout the process. To access the codebase, the Orchestration Engine communicates with the Repository Manager, which handles tasks like cloning repositories and retrieving code differences. Once the code is available, the Orchestration Engine triggers the Static Analysis Engine to perform initial code analysis. Subsequently, it dispatches tasks to the AI Interpretation Layer (Agents) for deeper, AI-driven code understanding. For visual representations, the Orchestration Engine invokes the Diagram Analysis component to generate structured data for diagrams. Finally, the Output Generation Engine is responsible for formatting and producing the final documentation and diagrams in various desired formats.

### Orchestration Engine [[Expand]](./Orchestration_Engine.md)
The central control subsystem responsible for initiating, managing, and coordinating all analysis and documentation generation jobs, acting as the primary orchestrator for the end-to-end workflow.


**Related Classes/Methods**:

- `local_app.py:process_docs_generation_job`:302-349
- `diagram_analysis/diagram_generator.py:generate_analysis`:100-169


### Job Database [[Expand]](./Job_Database.md)
Manages the storage and retrieval of job details, including status updates, for the documentation generation pipeline.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/duckdb_crud.py" target="_blank" rel="noopener noreferrer">`duckdb_crud.py`</a>


### Repository Manager
Handles repository operations such as cloning code repositories and retrieving code differences for analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/repo_utils/git_diff.py" target="_blank" rel="noopener noreferrer">`repo_utils.git_diff.py`</a>


### Static Analysis Engine [[Expand]](./Static_Analysis_Engine.md)
Performs static code analysis on the codebase.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/scanner.py" target="_blank" rel="noopener noreferrer">`static_analyzer.scanner.py`</a>


### AI Interpretation Layer (Agents)
Dispatches tasks to AI agents for advanced analysis and interpretation of code.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/agents/agent.py" target="_blank" rel="noopener noreferrer">`agents.agent.py`</a>


### Diagram Analysis
Generates structured analysis data specifically for creating diagrams.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/diagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`diagram_analysis.diagram_generator.py`</a>


### Output Generation Engine [[Expand]](./Output_Generation_Engine.md)
Responsible for the final formatting and generation of documentation and diagrams in various formats.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/output_generators/markdown.py" target="_blank" rel="noopener noreferrer">`output_generators.markdown.py`</a>


### External Integrations
Provides interfaces for external systems, such as VSCode and GitHub Actions, to trigger analysis workflows.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/github_action.py" target="_blank" rel="noopener noreferrer">`github_action.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/vscode_runnable.py" target="_blank" rel="noopener noreferrer">`vscode_runnable.py`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
