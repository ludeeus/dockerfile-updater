"""Test dockerfile parsing."""
import os
from unittest.mock import MagicMock
from shutil import copyfile
from action.dockerfile import Dockerfile
from action.config import Config


def test_structure(tmpdir):
    dockerfile = copyDockerfile(tmpdir)
    x, y, z = dockerfile.get_structure()
    structure = {"from": x, "arg": y, "run": z}
    assert ["alpine:0.0.0", "debian:0.0",
            "debian:0.0-slim"] == structure["from"]
    runList = structure["run"]
    match = "apk add"
    assert any(match in cmd for cmd in runList)
    match = "python"
    assert any(match in cmd for cmd in runList)
    match = "apt install"
    assert any(match in cmd for cmd in runList)
    assert ['S6_VERSION="0.0.0"', "ARG1=\"VALUE1\"", "ARG2=\"VALUE2\"", "ARG3"] == structure["arg"]


def test_args_replacement(tmpdir):
        arg1 = "ARG1=\"VALUE1\""
        arg2 = "ARG2=\"VALUE2\""
        arg3 = "ARG3"
        args = arg1 + "," + arg2 + "," + arg3
        dockerfile = copyDockerfile(tmpdir)
        x, y, z = dockerfile.get_structure()
        structure = {"from": x, "arg": y, "run": z}
        os.environ["INPUT_ARGS"] = args
        dockerfile.commit = MagicMock()
        assert [arg1, arg2, arg3] == structure["arg"]


def copyDockerfile(tmpdir):
    copyfile("tests/Test.dockerfile", f"{tmpdir}/Test.dockerfile")
    config = Config()
    return Dockerfile(config, f"{tmpdir}/Test.dockerfile")