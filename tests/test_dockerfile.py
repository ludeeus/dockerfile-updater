"""Test dockerfile parsing."""
import os
from shutil import copyfile
from action.dockerfile import Dockerfile
from action.config import Config


def test_structure(tmpdir):
    dockerfile = copyDockerfile(tmpdir)
    x, y, z = dockerfile.get_structure()
    structure = {"from": x, "arg": y, "run": z}
    assert ["alpine:0.0.0", "debian:0.0",
            "debian:0.0-slim"] == structure["from"]
    assert "apk add" in structure["run"][0] 
    assert "python" in structure["run"][1]
    apt = "apt install"
    assert any(apt in cmd for cmd in structure["run"][3])
    assert ['S6_VERSION="0.0.0"', "ARG1=VALUE1", "ARG2=VALUE2", "ARG3"] in structure["arg"]


def test_args_replacement(tmpdir):
    arg1 = "ARG1=\"VALUE1\""
    arg2 = "ARG2=\"VALUE2\""
    arg3 = "ARG3"
    args = arg1 + "," + arg2 + "," + arg3
    dockerfile = copyDockerfile(tmpdir)
    x, y, z = dockerfile.get_structure()
    structure = {"from": x, "arg": y, "run": z}
    os.environ["INPUT_ARGS"] = args
    dockerfile.update_args(structure)
    assert [arg1, arg2, arg3] in structure["arg"]


def copyDockerfile(tmpdir):
    copyfile("tests/Test.dockerfile", f"{tmpdir}/Test.dockerfile")
    config = Config()
    return Dockerfile(config, f"{tmpdir}/Test.dockerfile")