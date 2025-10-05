```mermaid
graph LR
    API_Service["API Service"]
    Job_Database["Job Database"]
    Orchestration_Engine["Orchestration Engine"]
    Repository_Manager["Repository Manager"]
    Analysis_Pipeline["Analysis Pipeline"]
    Output_Generation_Engine["Output Generation Engine"]
    Configuration_Utilities["Configuration & Utilities"]
    Unclassified["Unclassified"]
    API_Service -- "initiates jobs in" --> Orchestration_Engine
    API_Service -- "queries job status from" --> Job_Database
    Orchestration_Engine -- "updates job information in" --> Job_Database
    Orchestration_Engine -- "manages repository via" --> Repository_Manager
    Orchestration_Engine -- "executes analysis with" --> Analysis_Pipeline
    Orchestration_Engine -- "processes results from" --> Output_Generation_Engine
    Repository_Manager -- "provides source code to" --> Analysis_Pipeline
    Analysis_Pipeline -- "generates raw analysis data for" --> Output_Generation_Engine
    Output_Generation_Engine -- "provides final results to" --> API_Service
    Configuration_Utilities -- "provides settings to" --> API_Service
    Configuration_Utilities -- "provides settings to" --> Job_Database
    Configuration_Utilities -- "provides settings to" --> Orchestration_Engine
    Configuration_Utilities -- "provides settings to" --> Repository_Manager
    Configuration_Utilities -- "provides settings to" --> Analysis_Pipeline
    Configuration_Utilities -- "provides settings to" --> Output_Generation_Engine
    Configuration_Utilities -- "offers utility functions to" --> API_Service
    Configuration_Utilities -- "offers utility functions to" --> Job_Database
    Configuration_Utilities -- "offers utility functions to" --> Orchestration_Engine
    Configuration_Utilities -- "offers utility functions to" --> Repository_Manager
    Configuration_Utilities -- "offers utility functions to" --> Analysis_Pipeline
    Configuration_Utilities -- "offers utility functions to" --> Output_Generation_Engine
    click API_Service href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/API_Service.md" "Details"
    click Orchestration_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestration_Engine.md" "Details"
    click Repository_Manager href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Repository_Manager.md" "Details"
    click Output_Generation_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Output_Generation_Engine.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The CodeBoarding system operates on a pipeline/event-driven and producer-consumer architectural pattern, centered around an `API Service` that handles user interactions and initiates analysis jobs. The `Orchestration Engine` coordinates these jobs, managing the workflow from repository access via the `Repository Manager` to the core `Analysis Pipeline`. The `Analysis Pipeline` performs static analysis, now including the scanning and analysis of TypeScript configuration files, and AI-driven interpretation of code. Results are then processed by the `Output Generation Engine` to produce user-consumable documentation and visualizations. All job states and metadata are persistently managed by the `Job Database`, while the `Configuration & Utilities` component provides essential shared services across the system.

### API Service [[Expand]](./API_Service.md)
The API Service acts as the primary external interface for CodeBoarding, responsible for receiving and processing user requests related to code analysis and visualization. It handles the initiation of new analysis jobs, provides mechanisms for users to retrieve the status of ongoing jobs, and serves the final analysis results, including generated documentation and visualizations. Furthermore, it integrates with external systems like GitHub Actions to trigger automated documentation generation workflows. This component is crucial for orchestrating the interaction between users and the backend analysis pipeline, aligning with the project's pipeline/event-driven and producer-consumer architectural patterns.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app.app`</a>


### Job Database
Manages the state and metadata of all analysis jobs, including their status, progress, and associated results. It acts as a central ledger for asynchronous operations, ensuring persistence and traceability of analysis tasks.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainduckdb_crud.py" target="_blank" rel="noopener noreferrer">`duckdb_crud`</a>


### Orchestration Engine [[Expand]](./Orchestration_Engine.md)
Coordinates the execution of analysis tasks, managing the flow of data and control between different engines. It's responsible for task scheduling, dependency management, and overall workflow execution, embodying the pipeline/event-driven architecture.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app.generate_onboarding`</a>


### Repository Manager [[Expand]](./Repository_Manager.md)
Handles interactions with code repositories (e.g., GitHub), including cloning, fetching, and managing local copies of the source code to be analyzed. It ensures the analysis engines have access to the correct code versions.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainrepo_utils" target="_blank" rel="noopener noreferrer">`repo_utils`</a>


### Analysis Pipeline
This component encapsulates the core logic for static analysis and AI-driven interpretation of the codebase. It takes the raw source code, extracts structural information, and then uses AI models to generate insights, summaries, and initial documentation drafts. Its capabilities have been enhanced to include scanning and analyzing TypeScript configuration files, further enriching the depth of static analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindemo.py" target="_blank" rel="noopener noreferrer">`demo.generate_docs_remote`</a>


### Output Generation Engine [[Expand]](./Output_Generation_Engine.md)
Responsible for formatting and generating the final outputs, such as documentation (e.g., Markdown, HTML), visualizations (e.g., Mermaid.js diagrams), and structured data. It transforms processed information into user-consumable formats.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app.generate_onboarding`</a>


### Configuration & Utilities
Provides common utilities, configuration management, and helper functions used across various components. This component ensures consistency and reusability of common functionalities.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainutils.py" target="_blank" rel="noopener noreferrer">`utils`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
