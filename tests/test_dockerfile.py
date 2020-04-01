"""Test dockerfile parsing."""
from shutil import copyfile
from action.dockerfile import Dockerfile
from action.config import Config


def test_structure(tmpdir):
    copyfile("tests/Test.dockerfile", f"{tmpdir}/Test.dockerfile")
    config = Config()
    dockerfile = Dockerfile(config, f"{tmpdir}/Test.dockerfile")
    x, y, z = dockerfile.get_structure()
    structure = {"from": x, "arg": y, "run": z}
    assert ["alpine:0.0.0", "debian:0.0", "debian:0.0-slim"] == structure["from"]
    assert "apk add" in structure["run"][0]
    assert "python" in structure["run"][1]
    assert "apt install" in structure["run"][3]
    assert 'S6_VERSION="0.0.0"' in structure["arg"]
