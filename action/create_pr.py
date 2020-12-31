import os
from .config import Config

current_branch_name = os.getenv("ACTION_CURRENT_BRANCH")
branch_name = os.getenv("ACTION_BRANCHNAME")
config = Config()
repo = config.github.get_repo(config.repo)

body = """
# Changes

{changes}

***

This pull request was created with the [Dockerfile updater](https://github.com/ludeeus/dockerfile-updater) action.
"""

with open(f"{config.rootdir}/changes", "r") as changes:
    changes = changes.read()

repo.create_pull(
    title=config.pr_title,
    body=body.format(changes=changes),
    head=branch_name,
    base=current_branch_name,
)
