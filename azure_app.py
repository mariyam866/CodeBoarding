import azure.functions as func
import logging
from utils import RepoDontExistError, RepoIsNone, CFGGenerationError, remove_temp_repo_folder

app = func.FunctionApp()
@app.function_name('FirstHTTPFunction')
@app.route(route="myroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    url = req.params.get('url')
    from main import generate_docs_remote

    response = None
    try:
        remove_temp_repo_folder()
        repo_name = generate_docs_remote(url, local_dev=False)
        logging.info('Python HTTP trigger function processed a request.')
        response = func.HttpResponse(
            f"https://github.com/CodeBoarding/GeneratedOnBoardings/blob/main/{repo_name}/on_boarding.md",
            status_code=200
        )

    except (RepoDontExistError, RepoIsNone):
        response = func.HttpResponse(
            f"Repository not found or failed to clone: {url}",
            status_code=404
        )

    except CFGGenerationError:
        response = func.HttpResponse(
            "Failed to generate diagram. We will look into it :)",
            status_code=404
        )

    except Exception as e:
        logging.exception("Unexpected error processing repo")
        response = func.HttpResponse(
            f"Internal server error: {e}",
            status_code=500
        )

    finally:
        remove_temp_repo_folder() # remove the unique id from the folder

    return response