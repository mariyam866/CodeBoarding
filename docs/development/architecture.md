

```mermaid
graph LR
    Application_Orchestrator["Application Orchestrator"]
    QueryProcessor["QueryProcessor"]
    VectorStore["VectorStore"]
    DocumentRetriever["DocumentRetriever"]
    ResponseGenerator["ResponseGenerator"]
    PromptFactory["PromptFactory"]
    Unclassified["Unclassified"]
    Application_Orchestrator -- "initiates" --> QueryProcessor
    Application_Orchestrator -- "requests prompts from" --> PromptFactory
    QueryProcessor -- "embeds query for" --> VectorStore
    Application_Orchestrator -- "requests retrieval from" --> DocumentRetriever
    DocumentRetriever -- "queries" --> VectorStore
    DocumentRetriever -- "provides documents to" --> Application_Orchestrator
    Application_Orchestrator -- "sends context to" --> ResponseGenerator
    ResponseGenerator -- "utilizes prompts from" --> PromptFactory
    ResponseGenerator -- "returns response to" --> Application_Orchestrator
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The system operates around an `Application Orchestrator` that manages the overall flow from user query to response. User queries are initially processed by the `QueryProcessor`, which embeds them for efficient retrieval from the `VectorStore`. The `DocumentRetriever` then fetches relevant documents, which are passed back to the `Application Orchestrator`. A key architectural enhancement is the introduction of the `PromptFactory`, which centralizes and standardizes the generation of prompts for various agents and language models. The `Application Orchestrator` and `ResponseGenerator` both leverage the `PromptFactory` to obtain optimized prompts, enabling the `ResponseGenerator` to craft natural language responses based on the query and retrieved documents, including specialized prompts for models like Gemini Flash. This structured prompt management significantly refines how the system interacts with large language models, ensuring consistency and adaptability.

### Application Orchestrator
Manages the overall application flow, coordinating interactions between `QueryProcessor`, `DocumentRetriever`, `ResponseGenerator`, and now leveraging the `PromptFactory` for agent prompt generation. It receives user queries and delivers final responses, adapting its agent coordination mechanisms due to recent core agent logic refactoring and the new prompt management system.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/agent.py" target="_blank" rel="noopener noreferrer">`agents.agent`</a>


### QueryProcessor
Handles incoming user queries, embeds them, and prepares them for similarity search, potentially utilizing refined prompts from the `PromptFactory` for enhanced query understanding.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main." target="_blank" rel="noopener noreferrer">`langchain_core.embeddings.Embeddings:embed_query`</a>


### VectorStore
Stores and retrieves document embeddings based on similarity search.


**Related Classes/Methods**:

- `langchain_community.vectorstores.chroma.Chroma:similarity_search`


### DocumentRetriever
Retrieves relevant documents from the vector store.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main." target="_blank" rel="noopener noreferrer">`langchain_core.retrievers.BaseRetriever:get_relevant_documents`</a>


### ResponseGenerator
Generates a natural language response using a large language model based on the query and retrieved documents, now significantly enhanced by leveraging structured prompts from the `PromptFactory`, including specialized prompts for models like Gemini Flash.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main." target="_blank" rel="noopener noreferrer">`langchain_core.language_models.llms.BaseLLM:invoke`</a>


### PromptFactory
Centralizes the creation and management of prompts for various agents and language models. It provides a structured and standardized approach to prompt generation, including an expanded library of prompts, notably for Gemini Flash, ensuring consistent and optimized interactions with LLMs.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/prompts/prompt_factory.py#L27-L77" target="_blank" rel="noopener noreferrer">`prompt_factory.PromptFactory`:27-77</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    local_app_LocalApp["local_app.LocalApp"]
    diagram_analysis_diagram_generator["diagram_analysis.diagram_generator"]
    agents_prompts_PromptFactory["agents.prompts.PromptFactory"]
    duckdb_crud_DuckDBCRUD["duckdb_crud.DuckDBCRUD"]
    repo_utils_RepoUtils["repo_utils.RepoUtils"]
    vscode_runnable_VSCodeRunnable["vscode_runnable.VSCodeRunnable"]
    Unclassified["Unclassified"]
    vscode_runnable_VSCodeRunnable -- "initiates" --> local_app_LocalApp
    local_app_LocalApp -- "orchestrates" --> diagram_analysis_diagram_generator
    local_app_LocalApp -- "manages job data via" --> duckdb_crud_DuckDBCRUD
    local_app_LocalApp -- "utilizes" --> repo_utils_RepoUtils
    diagram_analysis_diagram_generator -- "utilizes agents which obtain prompts from" --> agents_prompts_PromptFactory
    agents_prompts_PromptFactory -- "provides prompts to" --> diagram_analysis_diagram_generator
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The CodeBoarding platform is orchestrated by `local_app.LocalApp`, which serves as the primary interface for users and the VS Code extension (`vscode_runnable.VSCodeRunnable`). `local_app.LocalApp` initiates and manages analysis jobs, leveraging `duckdb_crud.DuckDBCRUD` for persistent storage of job metadata and `repo_utils.RepoUtils` for repository operations. The core analysis and diagram generation workflow is handled by `diagram_analysis.diagram_generator`. A significant internal enhancement is the `agents.prompts.PromptFactory`, which centralizes and dynamically manages prompts for the various agents utilized by `diagram_analysis.diagram_generator` when interacting with LLMs, ensuring modularity and configurability in prompt management. This structured approach to prompt handling is crucial for the system's interaction with LLMs, which underpins the `diagram_analysis.diagram_generator`'s function.

### local_app.LocalApp
Serves as the primary local interface for CodeBoarding, enabling local users and the VS Code extension to initiate, manage, and retrieve the status of analysis jobs, and to trigger documentation generation. It acts as a local API endpoint, orchestrating interactions with core analysis and data management components.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app.LocalApp`</a>


### diagram_analysis.diagram_generator
Orchestrates the comprehensive code analysis and diagram generation workflow, initiated by the `local_app.LocalApp`. It's responsible for the core value proposition of the platform, leveraging various agents and LLMs for analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindiagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`diagram_analysis.diagram_generator`</a>


### agents.prompts.PromptFactory
Manages the dynamic selection and retrieval of prompts used by various agents for interacting with Large Language Models (LLMs). It centralizes prompt definitions, enhancing modularity, configurability, and maintainability of LLM interactions.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/prompts/prompt_factory.py#L27-L77" target="_blank" rel="noopener noreferrer">`agents.prompts.prompt_factory.PromptFactory`:27-77</a>


### duckdb_crud.DuckDBCRUD
Manages persistent storage and retrieval of analysis job metadata and status, crucial for `local_app.LocalApp` to track and report on job progress.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainduckdb_crud.py" target="_blank" rel="noopener noreferrer">`duckdb_crud.DuckDBCRUD`</a>


### repo_utils.RepoUtils
Provides repository-related operations such as cloning or fetching diffs, potentially utilized by `local_app.LocalApp` to prepare repositories for analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainrepo_utils/__init__.py" target="_blank" rel="noopener noreferrer">`repo_utils.RepoUtils`</a>


### vscode_runnable.VSCodeRunnable
An external client that consumes services provided by the `local_app.LocalApp` for VS Code extension functionalities, representing a key external integration point.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainvscode_runnable.py" target="_blank" rel="noopener noreferrer">`vscode_runnable.VSCodeRunnable`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    Orchestration_Engine["Orchestration Engine"]
    Job_Database["Job Database"]
    Repository_Manager["Repository Manager"]
    Analysis_Layer["Analysis Layer"]
    Output_Generation_Engine["Output Generation Engine"]
    External_Integrations["External Integrations"]
    Build_and_Deployment_Infrastructure["Build and Deployment Infrastructure"]
    Unclassified["Unclassified"]
    External_Integrations -- "triggers" --> Orchestration_Engine
    Orchestration_Engine -- "manages" --> Job_Database
    Orchestration_Engine -- "retrieves code via" --> Repository_Manager
    Orchestration_Engine -- "initiates" --> Analysis_Layer
    Analysis_Layer -- "provides results to" --> Orchestration_Engine
    Orchestration_Engine -- "directs output to" --> Output_Generation_Engine
    click Orchestration_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestration_Engine.md" "Details"
    click Repository_Manager href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Repository_Manager.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The system operates with an Orchestration Engine at its core, initiating and managing all documentation generation jobs. This engine interacts with a Job Database to maintain job status and details. Code repositories are handled by the Repository Manager, which provides the necessary code for analysis. The Analysis Layer performs comprehensive code analysis, including static analysis and AI-driven interpretation, now significantly enhanced by a dedicated prompt management system for AI agents. The results from the Analysis Layer are then passed back to the Orchestration Engine, which directs them to the Output Generation Engine for final documentation and diagram creation. External systems can trigger these workflows through the External Integrations component. The entire system is supported by the Build and Deployment Infrastructure, ensuring its operational readiness.

### Orchestration Engine [[Expand]](./Orchestration_Engine.md)
The central control subsystem responsible for initiating, managing, and coordinating all analysis and documentation generation jobs, acting as the primary orchestrator for the end-to-end workflow.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app.py:start_generation_job`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app.py:start_docs_generation_job`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app.py:process_docs_generation_job`</a>


### Job Database
Manages the storage and retrieval of job details, including status updates, for the documentation generation pipeline.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainduckdb_crud.py" target="_blank" rel="noopener noreferrer">`duckdb_crud.py`</a>


### Repository Manager [[Expand]](./Repository_Manager.md)
Handles repository operations suchs as cloning code repositories and retrieving code differences for analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainrepo_utils/git_diff.py" target="_blank" rel="noopener noreferrer">`repo_utils.git_diff.py`</a>


### Analysis Layer
Performs comprehensive code analysis, encompassing static code analysis, AI-driven interpretation, and specialized data extraction for diagram generation. This layer now includes a dedicated and structured prompt management system for generating and managing prompts for AI agents, enhancing modularity and scalability.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/scanner.py" target="_blank" rel="noopener noreferrer">`static_analyzer.scanner.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/agent.py" target="_blank" rel="noopener noreferrer">`agents.agent.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindiagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`diagram_analysis/diagram_generator.py:generate_analysis`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/prompts/gemini_flash_prompts_bidirectional.py" target="_blank" rel="noopener noreferrer">`agents.prompts.gemini_flash_prompts_bidirectional.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/prompts/gemini_flash_prompts_unidirectional.py" target="_blank" rel="noopener noreferrer">`agents.prompts.gemini_flash_prompts_unidirectional.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/prompts/prompt_factory.py" target="_blank" rel="noopener noreferrer">`agents.prompts.prompt_factory.py`</a>


### Output Generation Engine
Responsible for the final formatting and generation of documentation and diagrams in various formats.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainoutput_generators/markdown.py" target="_blank" rel="noopener noreferrer">`output_generators.markdown.py`</a>


### External Integrations
Provides interfaces for external systems, such as VSCode and GitHub Actions, to trigger analysis workflows.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maingithub_action.py" target="_blank" rel="noopener noreferrer">`github_action.py`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainvscode_runnable.py" target="_blank" rel="noopener noreferrer">`vscode_runnable.py`</a>


### Build and Deployment Infrastructure
Encompasses the project's packaging, dependency management, and build processes, defining how the system is assembled, distributed, and integrated. This component underpins the operational readiness of all other components.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainsetup.py" target="_blank" rel="noopener noreferrer">`setup.py`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    Diff_Analyzer["Diff Analyzer"]
    Git_Operations_Utility["Git Operations Utility"]
    Unclassified["Unclassified"]
    Diff_Analyzer -- "depends on and invokes" --> Git_Operations_Utility
    Git_Operations_Utility -- "provides raw repository data and diff outputs to" --> Diff_Analyzer
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The system's core functionality revolves around analyzing code changes. The `Git Operations Utility` serves as the foundational layer, providing raw repository data and diffs to the `Diff Analyzer`. The `Diff Analyzer` then processes this raw information, transforming it into structured code artifacts and contextual data. These processed outputs are subsequently routed to two distinct downstream components: the `Static Analysis Engine` for identifying code quality and security issues, and the `AI Interpretation Layer` for advanced, AI-driven insights and recommendations based on the code changes. This architecture ensures a clear separation of concerns, with the `Diff Analyzer` acting as a central hub for preparing data for specialized analysis.

### Diff Analyzer
Orchestrates the process of identifying, analyzing, and preparing code differences from repositories. It leverages lower-level Git utilities to fetch raw data and then processes it into a usable format for subsequent analysis stages.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/diff_analyzer.py" target="_blank" rel="noopener noreferrer">`agents.diff_analyzer:__init__`</a>


### Git Operations Utility
Provides low-level, atomic functionalities for interacting directly with Git repositories. This includes operations such as cloning repositories, fetching updates, and generating detailed version differences (diffs). It abstracts the complexities of Git commands.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainrepo_utils/git_diff.py" target="_blank" rel="noopener noreferrer">`repo_utils.git_diff:git_diff`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    Code_Scanner_Parser["Code Scanner/Parser"]
    LSP_Client_Manager["LSP Client Manager"]
    Reference_Resolution_Module["Reference Resolution Module"]
    Unclassified["Unclassified"]
    Code_Scanner_Parser -- "sends requests to" --> LSP_Client_Manager
    Code_Scanner_Parser -- "provides parsed structures to" --> Reference_Resolution_Module
    LSP_Client_Manager -- "delivers analysis to" --> Reference_Resolution_Module
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The static analysis subsystem is composed of three central components: the `Code Scanner/Parser`, the `LSP Client Manager`, and the `Reference Resolution Module`. The `Code Scanner/Parser` initiates the analysis by ingesting and structuring source code, performing language-agnostic parsing. It then interacts with the `LSP Client Manager` to leverage language-specific analysis capabilities provided by external Language Server Protocol (LSP) servers. Both the parsed structures from the `Code Scanner/Parser` and the detailed analysis from the `LSP Client Manager` feed into the `Reference Resolution Module`. This module is responsible for identifying and resolving code references, thereby establishing a comprehensive understanding of the codebase's structural interactions. This architecture ensures a modular and extensible approach to static code analysis, separating initial parsing from language-specific and reference resolution concerns.

### Code Scanner/Parser
Responsible for the initial ingestion and parsing of source code, breaking it down into a structured format suitable for further analysis. It handles language-agnostic lexical and syntactic analysis, potentially delegating language-specific parsing to specialized clients.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/scanner.py" target="_blank" rel="noopener noreferrer">`static_analyzer/scanner.py`</a>


### LSP Client Manager
Manages communication with Language Server Protocol (LSP) servers for various programming languages. It acts as an intermediary, sending code analysis requests to external language servers and receiving detailed, language-specific structural information (e.g., ASTs, symbol tables, type information). The `LSPClient` serves as the foundational abstract class for all language-specific LSP client implementations, defining the core communication protocol and lifecycle management.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/lsp_client/typescript_client.py" target="_blank" rel="noopener noreferrer">`static_analyzer.lsp_client.client.LSPClient`</a>


### Reference Resolution Module
Focuses on identifying and resolving code references within the parsed source code. It links declarations to their usages, providing a comprehensive understanding of how different parts of the codebase interact at a structural level. The `ReferenceResolverMixin` provides the core logic and orchestration for various reference resolution strategies, including exact, loose, file path, and LLM-based matching.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/reference_resolve_mixin.py" target="_blank" rel="noopener noreferrer">`static_analyzer.reference_resolve_mixin.ReferenceResolverMixin`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)


```mermaid
graph LR
    API_Service["API Service"]
    Job_Database["Job Database"]
    Orchestration_Engine["Orchestration Engine"]
    Repository_Manager["Repository Manager"]
    Static_Analysis_Engine["Static Analysis Engine"]
    AI_Interpretation_Layer["AI Interpretation Layer"]
    Output_Generation_Engine["Output Generation Engine"]
    Unclassified["Unclassified"]
    API_Service -- "initiates jobs and triggers analysis within" --> Orchestration_Engine
    API_Service -- "requests GitHub Action jobs from" --> Orchestration_Engine
    Orchestration_Engine -- "manages job state in" --> Job_Database
    Orchestration_Engine -- "requests code from" --> Repository_Manager
    Repository_Manager -- "provides code to" --> Orchestration_Engine
    Orchestration_Engine -- "requests static analysis from" --> Static_Analysis_Engine
    Static_Analysis_Engine -- "provides richer analysis results (including reference resolution) to" --> Orchestration_Engine
    Orchestration_Engine -- "feeds rich analysis data to" --> AI_Interpretation_Layer
    AI_Interpretation_Layer -- "returns enhanced architectural insights to" --> Orchestration_Engine
    AI_Interpretation_Layer -- "queries diff information from" --> Repository_Manager
    Orchestration_Engine -- "passes enhanced insights for generation to" --> Output_Generation_Engine
    Output_Generation_Engine -- "delivers documentation to" --> API_Service
    Output_Generation_Engine -- "provides GitHub Action output to" --> API_Service
    click API_Service href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/API_Service.md" "Details"
    click Orchestration_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Orchestration_Engine.md" "Details"
    click Repository_Manager href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Repository_Manager.md" "Details"
    click Static_Analysis_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Static_Analysis_Engine.md" "Details"
    click AI_Interpretation_Layer href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/AI_Interpretation_Layer.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The CodeBoarding project is structured around a robust pipeline for automated software documentation and diagram generation. At its core, the system processes source code through static analysis, interprets the results using specialized AI agents, and then generates various output formats. The recent architectural enhancements significantly bolster the `AI Interpretation Layer`, particularly in how it manages and applies prompts for interacting with diverse AI models. The main flow begins with the `API Service` receiving user requests, which are then managed by the `Orchestration Engine`. This engine coordinates the entire process, from fetching code via the `Repository Manager` to performing `Static Analysis`. The results of this analysis, now enriched with reference resolution, are fed into the `AI Interpretation Layer`. This layer, comprising multiple AI agents, interprets the data to produce high-level architectural insights. A key update here is the introduction of a sophisticated `Prompt Management System` within this layer, centralizing prompt creation and enabling support for various language models and prompting strategies. Finally, these insights are passed to the `Output Generation Engine` to produce documentation in desired formats, which can then be delivered back via the `API Service` or integrated with external systems like GitHub Actions.

### API Service [[Expand]](./API_Service.md)
The external interface for CodeBoarding, handling user requests, job initiation, status retrieval, and integrating with GitHub Actions for automated documentation generation.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainlocal_app.py" target="_blank" rel="noopener noreferrer">`local_app`</a>


### Job Database
Persistent storage for managing the lifecycle, status, and results of all documentation generation jobs.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainduckdb_crud.py" target="_blank" rel="noopener noreferrer">`duckdb_crud`</a>


### Orchestration Engine [[Expand]](./Orchestration_Engine.md)
The central control unit that manages the entire documentation generation pipeline, coordinating all analysis and generation stages.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindiagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`diagram_generator`</a>


### Repository Manager [[Expand]](./Repository_Manager.md)
Manages all interactions with source code repositories, including cloning, fetching, and extracting version differences.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/diff_analyzer.py#L21-L32" target="_blank" rel="noopener noreferrer">`__init__`:21-32</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainrepo_utils/git_diff.py#L27-L76" target="_blank" rel="noopener noreferrer">`git_diff`:27-76</a>


### Static Analysis Engine [[Expand]](./Static_Analysis_Engine.md)
Performs deep, language-specific analysis of source code, now explicitly including **reference resolution capabilities**, to extract richer, more detailed, and comprehensive structural information without semantic interpretation.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/scanner.py#L13-L82" target="_blank" rel="noopener noreferrer">`scanner`:13-82</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/lsp_client/typescript_client.py#L10-L214" target="_blank" rel="noopener noreferrer">`client`:10-214</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/abstraction_agent.py" target="_blank" rel="noopener noreferrer">`analysis_result`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainstatic_analyzer/reference_resolve_mixin.py" target="_blank" rel="noopener noreferrer">`reference_resolve_mixin`</a>


### AI Interpretation Layer [[Expand]](./AI_Interpretation_Layer.md)
A collection of specialized AI agents that perform sophisticated interpretation of static analysis data, generating enhanced high-level architectural insights, including detailed abstractions, refined planning, robust validation, and comprehensive diff analysis. This layer now features a **significantly enhanced prompt management system**, utilizing a `prompt_factory` for structured prompt definition, selection, and application, supporting various language models (e.g., Gemini Flash) and prompting strategies.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindiagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`meta_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/abstraction_agent.py" target="_blank" rel="noopener noreferrer">`abstraction_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/details_agent.py" target="_blank" rel="noopener noreferrer">`details_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindiagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`planner_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maindiagram_analysis/diagram_generator.py" target="_blank" rel="noopener noreferrer">`validator_agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/diff_analyzer.py" target="_blank" rel="noopener noreferrer">`diff_analyzer`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/agent.py" target="_blank" rel="noopener noreferrer">`agent`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/agent_responses.py" target="_blank" rel="noopener noreferrer">`agent_responses`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainagents/details_agent.py" target="_blank" rel="noopener noreferrer">`prompts`</a>


### Output Generation Engine
Transforms the final, validated architectural insights into various human-readable and diagram-friendly documentation formats, with enhanced capabilities for specific output formats and external integrations like GitHub Actions.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maingithub_action.py#L37-L51" target="_blank" rel="noopener noreferrer">`html`:37-51</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maingithub_action.py#L20-L34" target="_blank" rel="noopener noreferrer">`markdown`:20-34</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maingithub_action.py#L54-L68" target="_blank" rel="noopener noreferrer">`mdx`:54-68</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/mainoutput_generators/sphinx.py" target="_blank" rel="noopener noreferrer">`sphinx`</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/maingithub_action.py" target="_blank" rel="noopener noreferrer">`github_action`</a>


### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)

