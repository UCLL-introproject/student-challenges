
import pathlib
import urllib.request
import urllib.parse
from functools import cache
import json


url = "http://challenges.leone.ucll.be"

@cache
def find_test_path():
    return pathlib.Path(__file__).parent.resolve()

@cache
def find_root():
    current_path = find_test_path()
    while not (current_path / "pyproject.toml").exists():
        current_path = current_path.parent
    return current_path

def load_solution():
    path = find_test_path() / "solution.txt"
    assert path.exists(), f"file {path} not found"
    with path.open("r") as f:
        return f.read()

def derive_url():
    root = find_root()
    path = "/".join(urllib.parse.quote(part) for part in find_test_path().relative_to(root).parts)
    return f"{url}/{path}"

def create_request_payload():
    solution = load_solution()
    data = { "student_solution": solution }
    return json.dumps(data).encode("utf-8")

def query_server():
    url = derive_url()
    payload = create_request_payload()
    request = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(request) as f:
        response = f.read().decode("utf-8")
    return json.loads(response)

def failure_message(response):
    if response['message']:
        return f'Failed: {response["message"]}'
    else:
        return 'Wrong answer'

def verify():
    response = query_server()
    assert response["grade"] == 1, failure_message(response)
