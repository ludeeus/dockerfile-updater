import os
import glob
from .config import Config
from .dockerfile import Dockerfile

current_branch_name = os.getenv("ACTION_CURRENT_BRANCH")
branch_name = os.getenv("ACTION_BRANCHNAME")
config = Config()

changed = False
skip = ["py", "txt", "sh", "yml", "yaml", "git"]

repofiles = [f for f in glob.glob(config.rootdir + "**/*", recursive=True)]
dockerfiles = [
    f for f in repofiles if config.dockerfile_name in f.split("/")[-1].lower()
]

if len(dockerfiles) == 0:
    exit(":error::No dockerfiles found")

if config.exclude_type:
    print(f"Skipping {config.exclude_type}")

if config.exclude_package:
    print(f"Skipping {config.exclude_package}")

for filepath in sorted(dockerfiles):
    if os.path.isdir(filepath):
        continue
    if filepath.split(".")[-1] in skip:
        continue
    if Dockerfile(config, filepath).update():
        changed = True
        with open(filepath) as target:
            print(target.read())

if not changed:
    exit(0)
