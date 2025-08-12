```mermaid
graph LR
    ProjectScanner["ProjectScanner"]
    LSPClient["LSPClient"]
    TypeScriptClient["TypeScriptClient"]
    FileAnalysisResult["FileAnalysisResult"]
    ProjectScanner -- "provides input to" --> LSPClient
    ProjectScanner -- "provides input to" --> TypeScriptClient
    LSPClient -- "populates" --> FileAnalysisResult
    TypeScriptClient -- "extends" --> LSPClient
    TypeScriptClient -- "populates" --> FileAnalysisResult
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The `Static Analysis Engine` subsystem is primarily encapsulated within the `static_analyzer` package. Its core components include the `scanner` module for initial project scanning and the `lsp_client` subpackage, which handles Language Server Protocol (LSP) communication for detailed code analysis.

### ProjectScanner
Initiates the static analysis process by scanning the project repository. It identifies relevant source files, determines programming languages used, and extracts basic project metadata. This component acts as the initial data gatherer, preparing the input for more detailed LSP-based analysis.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/scanner.py#L13-L66" target="_blank" rel="noopener noreferrer">`ProjectScanner`:13-66</a>


### LSPClient
Serves as the generic Language Server Protocol client. It manages the communication lifecycle with an LSP server (initialization, sending requests, receiving responses, shutdown). It orchestrates the detailed static analysis for individual files and the entire workspace, extracting symbols, imports, call graphs, and class hierarchies.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/lsp_client/client.py#L37-L923" target="_blank" rel="noopener noreferrer">`LSPClient`:37-923</a>


### TypeScriptClient
A specialized implementation of `LSPClient` tailored for TypeScript projects. It handles TypeScript-specific initialization parameters, workspace configuration (e.g., processing `tsconfig.json`), and file discovery, ensuring the LSP server is correctly set up for TypeScript analysis. This component exemplifies the extensibility of the static analysis engine for different programming languages.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/lsp_client/typescript_client.py#L10-L214" target="_blank" rel="noopener noreferrer">`TypeScriptClient`:10-214</a>


### FileAnalysisResult
A data structure used to encapsulate the comprehensive static analysis results for a single source file. It stores extracted information such as imports, symbols (functions, classes), call relationships, class hierarchies, and external references. This acts as the structured output of the static analysis phase.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/static_analyzer/lsp_client/client.py#L22-L34" target="_blank" rel="noopener noreferrer">`FileAnalysisResult`:22-34</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
