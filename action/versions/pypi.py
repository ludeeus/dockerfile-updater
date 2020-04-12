import requests

def version_pypi(pkg):
    print(f"[pypi] {pkg}")
    try:
        url = f"https://pypi.python.org/pypi/{pkg}/json"
        response = requests.get(url).json()
        return response["info"]["version"]
    except Exception as e:
        print(f"Could not get version for {pkg} - {e}")
        return None