import os
from github import Github


class Config:
    github = Github(os.getenv("INPUT_TOKEN"))

    def __init__(self, rootdir: str = "/github/workspace/"):
        self._rootdir = rootdir

    @property
    def dockerfile_name(self):
        if os.getenv("INPUT_DOCKERFILE_NAME"):
            return os.getenv("INPUT_DOCKERFILE_NAME").replace('"', "").lower()
        return "dockerfile".lower()

    @property
    def pr_title(self):
        if os.getenv("INPUT_PR_TITLE"):
            return os.getenv("INPUT_PR_TITLE")
        return "Dockerfile updates 🎉"

    @property
    def rootdir(self):
        return self._rootdir

    @property
    def repo(self):
        return os.getenv("GITHUB_REPOSITORY")

    @property
    def exclude_type(self):
        if os.getenv("INPUT_EXCLUDE_TYPE"):
            return (
                os.getenv("INPUT_EXCLUDE_TYPE")
                .replace('"', "")
                .replace(" ", "")
                .split(",")
            )
        return []

    @property
    def exclude_package(self):
        if os.getenv("INPUT_EXCLUDE_PACKAGE"):
            return (
                os.getenv("INPUT_EXCLUDE_PACKAGE")
                .replace('"', "")
                .replace(" ", "")
                .split(",")
            )
        return []

    @property
    def commit_msg(self):
        if os.getenv("INPUT_COMMIT_MSG"):
            return os.getenv("INPUT_COMMIT_MSG")
        return "Update [package] from [from_version] to [to_version]"

    @property
    def args(self):
        print("INPUT_ARGS: " + os.getenv("INPUT_ARGS", ""))
        return self.extractValuesToList(os.getenv("INPUT_ARGS", ""))

    def extractValuesToList(self, values):
        args = {}
        if values:
            argList = values.split(",")
            for argPair in argList:
                keyValue = argPair.split("=")
                args[keyValue[0]] = argPair
        return args
