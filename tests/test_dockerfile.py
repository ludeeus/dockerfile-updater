"""Test dockerfile parsing."""
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
    assert "apt install" in structure["run"][3]
    assert ['S6_VERSION="0.0.0"', "DEBIAN=0.0"] in structure["arg"]
    assert 'DEBIAN="0.0"' in structure["arg"]


def test_args_replacement(tmpdir):
    arg1 = "ARG1=\"VALUE1\""
    arg2 = "ARG2=\"VALUE2\""
    args = arg1 + "," + arg2
    dockerfile = copyDockerfile(tmpdir)
    x, y, z = dockerfile.get_structure()
    structure = {"from": x, "arg": y, "run": z}
    assert ['S6_VERSION="0.0.0"', "DEBIAN=0.0"] in structure["arg"]
    dockerfile.update_args(args)
    assert [arg1, arg2] in structure["arg"]


def copyDockerfile(tmpdir):
    copyfile("tests/Test.dockerfile", f"{tmpdir}/Test.dockerfile")
    config = Config()
    return Dockerfile(config, f"{tmpdir}/Test.dockerfile")
