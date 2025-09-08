```mermaid
graph LR
    Static_Analysis_Engine["Static Analysis Engine"]
    Output_Generation_Engine["Output Generation Engine"]
    HTMLGenerator["HTMLGenerator"]
    MarkdownGenerator["MarkdownGenerator"]
    MDXGenerator["MDXGenerator"]
    SphinxGenerator["SphinxGenerator"]
    GitHubActionOutputFormatter["GitHubActionOutputFormatter"]
    HTML_Template_Populator["HTML Template Populator"]
    Unclassified["Unclassified"]
    Static_Analysis_Engine -- "provides insights to" --> Output_Generation_Engine
    Output_Generation_Engine -- "orchestrates" --> HTMLGenerator
    Output_Generation_Engine -- "orchestrates" --> MarkdownGenerator
    Output_Generation_Engine -- "orchestrates" --> MDXGenerator
    Output_Generation_Engine -- "orchestrates" --> SphinxGenerator
    Output_Generation_Engine -- "uses" --> GitHubActionOutputFormatter
    HTMLGenerator -- "provides data to" --> HTML_Template_Populator
    GitHubActionOutputFormatter -- "uses" --> HTMLGenerator
    GitHubActionOutputFormatter -- "uses" --> MarkdownGenerator
    GitHubActionOutputFormatter -- "uses" --> MDXGenerator
    click Static_Analysis_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Static_Analysis_Engine.md" "Details"
    click Output_Generation_Engine href "https://github.com/CodeBoarding/CodeBoarding/blob/main/.codeboarding/Output_Generation_Engine.md" "Details"
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/CodeBoarding)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/diagrams)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The system's architecture is centered around the generation of comprehensive architectural documentation from source code. The process begins with the Static Analysis Engine, which meticulously scans the codebase to extract raw architectural insights. These insights are then fed into the Output Generation Engine, the central orchestrator that manages the overall documentation workflow. The Output Generation Engine dispatches the insights to various specialized generators: HTMLGenerator, MarkdownGenerator, MDXGenerator, and SphinxGenerator, each responsible for producing documentation in its respective format. The HTML Template Populator further refines the HTML output by integrating generated data into predefined templates. Additionally, the GitHubActionOutputFormatter ensures that the generated documentation is appropriately formatted for seamless integration into GitHub Actions workflows, leveraging the capabilities of the other generators. This structured approach ensures accurate, consistent, and versatile architectural documentation.

### Static Analysis Engine [[Expand]](./Static_Analysis_Engine.md)
This foundational component is responsible for scanning the source code, performing static analysis, and generating the initial architectural insights. It extracts critical data, identifies relationships, and prepares the raw information that downstream components will consume to generate documentation.


**Related Classes/Methods**: _None_

### Output Generation Engine [[Expand]](./Output_Generation_Engine.md)
The primary component responsible for orchestrating the overall process of generating documentation in various formats. It consumes architectural insights from the `Static Analysis Engine`, handles repository cloning, initiates the analysis generation, and dispatches the actual documentation generation to specific format generators based on the desired output.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/demo.py#L57-L80" target="_blank" rel="noopener noreferrer">`demo.py`:57-80</a>
- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/demo.py#L82-L101" target="_blank" rel="noopener noreferrer">`demo.py`:82-101</a>


### HTMLGenerator
This component is dedicated to converting the processed architectural insights into a structured HTML format. It handles the rendering of diagrams, text, and other elements into web-friendly documentation. It prepares data (e.g., Cytoscape.js compatible JSON) for interactive architectural diagrams.


**Related Classes/Methods**: _None_

### MarkdownGenerator
Responsible for generating documentation in standard Markdown format. This component ensures that architectural insights are presented in a widely compatible and easily readable text-based format, suitable for various platforms and tools. It includes embedded Mermaid diagrams and basic component details.


**Related Classes/Methods**: _None_

### MDXGenerator
This component extends Markdown generation by incorporating JSX capabilities, allowing for more dynamic and interactive documentation. It transforms insights into MDX, enabling the embedding of React components within the documentation, including Mermaid diagrams and frontmatter.


**Related Classes/Methods**: _None_

### SphinxGenerator
Focuses on generating documentation in reStructuredText (RST) format, specifically tailored for use with the Sphinx documentation generator. This component ensures compatibility with Sphinx's powerful features for technical documentation, including embedded Mermaid diagrams and structured component information.


**Related Classes/Methods**: _None_

### GitHubActionOutputFormatter
This component acts as an integration layer, specifically formatting and preparing the generated documentation for consumption within GitHub Actions workflows. It leverages the capabilities of the other generators (HTML, Markdown, MDX) to produce output suitable for GitHub's environment.


**Related Classes/Methods**: _None_

### HTML Template Populator
Integrates generated architectural data (like Cytoscape JSON and component-specific HTML snippets) into a predefined HTML template to produce the final, complete, and styled HTML output.


**Related Classes/Methods**: _None_

### Unclassified
Component for all unclassified files and utility functions (Utility functions/External Libraries/Dependencies)


**Related Classes/Methods**: _None_



### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
