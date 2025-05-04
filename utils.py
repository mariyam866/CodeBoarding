import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from git import Git, GitCommandError
from typing import Optional

class NoGithubTokenFoundError(Exception):
    pass

class CFGGenerationError(Exception):
    pass

class RepoDontExistError(Exception):
    pass

class RepoIsNone(Exception):
    pass

def init_llm():
    api_key = os.getenv("API_KEY")

    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-001",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        google_api_key=api_key,
    )

def caching_enabled():
    return os.getenv('CACHING_DOCUMENTATION', 'false').lower() in ('1', 'true', 'yes')

def remote_repo_exists(repo_url: str) -> bool:
    if repo_url is None:
        return False
    try:
        Git().ls_remote(repo_url)
        return True
    except GitCommandError as e:
        stderr = (e.stderr or "").lower()
        if "not found" in stderr or "repository not found" in stderr:
            return False
        # something else went wrong (auth, network); re-raise so caller can decide
        raise

def sanitize_repo_url(repo_url: str) -> str:
    if not repo_url or not isinstance(repo_url, str):
        raise RepoIsNone("No repo URL provided")
    clean = repo_url.strip().strip('"').strip("'")
    if not clean:
        raise ValueError("Repo URL is empty after sanitization")
    return clean