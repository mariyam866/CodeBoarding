import os
import re
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=api_key,
)

response = llm.invoke("Explain how AI works in a few words")
print(response["content"])

ENTRYPOINT_PATTERNS = {
    "main_block": re.compile(r'if\s+__name__\s*==\s*[\'"]__main__[\'"]'),
    "main_function": re.compile(r'def\s+main\s*\('),
    "flask_app": re.compile(r'Flask\s*\('),
    "flask_run": re.compile(r'\.run\s*\('),
    "django_manage": re.compile(r'execute_from_command_line'),
    "click_decorator": re.compile(r'@click\.command'),
    "typer_app": re.compile(r'Typer\s*\('),
    "argparse": re.compile(r'argparse\.ArgumentParser'),
    "bash_python_call": re.compile(r'python[0-9.]*\s+[\w./_-]+\.py'),
    "shebang_python": re.compile(r'^#!.*python')
}

IGNORED_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'node_modules', '.mypy_cache'}

def is_text_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read(1024)
        return True
    except:
        return False

def scan_file(filepath):
    hits = []
    if not is_text_file(filepath):
        return hits

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        for key, pattern in ENTRYPOINT_PATTERNS.items():
            if pattern.search(line):
                hits.append((key, filepath, i + 1, line.strip()))
    return hits

def find_entrypoints(root='.'):
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if filename.endswith(('.py', '.sh', 'Dockerfile')) or filename.startswith('run') or filename.startswith('start'):
                hits = scan_file(filepath)
                results.extend(hits)
    return results

def main():
    print("🔍 Scanning for possible Python entrypoints...\n")
    entries = find_entrypoints()
    if not entries:
        print("No entrypoints found.")
        return

    for kind, file, line, code in entries:
        print(f"[{kind:<20}] {file}:{line} → {code}")

if __name__ == "__main__":
    main()
