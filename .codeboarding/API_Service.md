```mermaid
graph LR
    API_Gateway_Main_Application_Instance_["API Gateway (Main Application Instance)"]
    Job_Initiation_Endpoint_Code_Analysis_["Job Initiation Endpoint (Code Analysis)"]
    Job_Initiation_Endpoint_Documentation_Only_["Job Initiation Endpoint (Documentation Only)"]
    Job_Status_Retrieval_Endpoint_Single_Job_["Job Status Retrieval Endpoint (Single Job)"]
    Job_Status_Retrieval_Endpoint_List_All_Jobs_["Job Status Retrieval Endpoint (List All Jobs)"]
    API_Gateway_Main_Application_Instance_ -- "contains" --> Job_Initiation_Endpoint_Code_Analysis_
    API_Gateway_Main_Application_Instance_ -- "contains" --> Job_Initiation_Endpoint_Documentation_Only_
    API_Gateway_Main_Application_Instance_ -- "contains" --> Job_Status_Retrieval_Endpoint_Single_Job_
    API_Gateway_Main_Application_Instance_ -- "contains" --> Job_Status_Retrieval_Endpoint_List_All_Jobs_
```

[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Details

The API Service (referred to as API Gateway in the analysis summary) forms the external interface of CodeBoarding. Its boundaries are defined by the local_app.py file, specifically the FastAPI application instance (local_app.app) and its exposed RESTful endpoints. This subsystem is responsible for handling all incoming user requests, initiating analysis jobs, and providing job status updates.

### API Gateway (Main Application Instance)
The core FastAPI application instance that defines and serves all external API endpoints for CodeBoarding. It acts as the central dispatcher for incoming HTTP requests, routing them to the appropriate handlers.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py" target="_blank" rel="noopener noreferrer">`local_app.app`</a>


### Job Initiation Endpoint (Code Analysis)
Handles requests to initiate a comprehensive code analysis and documentation generation job. It validates input parameters and triggers the subsequent orchestration process.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py#L133-L150" target="_blank" rel="noopener noreferrer">`local_app.start_generation_job`:133-150</a>


### Job Initiation Endpoint (Documentation Only)
Manages requests specifically for generating documentation, potentially for pre-analyzed code or a subset of the full analysis, providing a more focused entry point.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py#L181-L231" target="_blank" rel="noopener noreferrer">`local_app.start_docs_generation_job`:181-231</a>


### Job Status Retrieval Endpoint (Single Job)
Provides an interface for clients to query the real-time status and detailed results of a specific, identified job using its unique ID.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py#L161-L170" target="_blank" rel="noopener noreferrer">`local_app.get_job`:161-170</a>


### Job Status Retrieval Endpoint (List All Jobs)
Allows clients to retrieve a list of all ongoing or completed jobs, offering an overview of system activity and job history.


**Related Classes/Methods**:

- <a href="https://github.com/CodeBoarding/CodeBoarding/blob/main/local_app.py#L282-L311" target="_blank" rel="noopener noreferrer">`local_app.list_jobs`:282-311</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)
