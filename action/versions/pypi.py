import requests

def version_pypi(pkg):
    url = f"https://pypi.python.org/pypi/{pkg}/json"
    response = requests.get(url).json()
    return response["info"]["version"]