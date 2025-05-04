import azure.functions as func
import logging
from utils import RepoDontExistError, RepoIsNone, CFGGenerationError

app = func.FunctionApp()

@app.function_name('FirstHTTPFunction')
@app.route(route="myroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    url = req.params.get('url')
   
    from main import generate_docs_remote
    try:
        repo_name = generate_docs_remote(url, local_dev=False)
    except (RepoDontExistError, RepoIsNone):
        return func.HttpResponse(
            f"Repository not found or failed to clone: {url}",
            status_code=404
        )
    except CFGGenerationError:
        return func.HttpResponse(
            f"Failed to generate diagram. We will look into it :)",
            status_code=404
        )
    except Exception as e:
        logging.exception("Unexpected error processing repo")
        return func.HttpResponse(
            f"Internal server error {e};'",
            status_code=500
        )

    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        f"https://github.com/CodeBoarding/GeneratedOnBoardings/blob/main/{repo_name}/on_boarding.md",
        status_code=200
    )