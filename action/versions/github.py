import requests

def version_github(github, repo):
    print(f"[github] {repo}")
    repo = github.get_repo(repo)
    releases = repo.get_releases()
    return releases[0].tag_name