import requests

def version_github(github, repo):
    print(f"[github] {repo}")
    try:
        repo = github.get_repo(repo)
        releases = repo.get_releases()
        return releases[0].tag_name
    except Exception as e:
        print(f"Could not get version for {pkg} - {e}")
        return None