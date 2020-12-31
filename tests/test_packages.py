"""Test dockerfile parsing."""
from action.dockerfile import Dockerfile
from action.helpers import get_packages


def test_get_packages(dockerfile: Dockerfile):
    x, y, z = dockerfile.get_structure()
    structure = {"from": x, "arg": y, "run": z}
    packages = get_packages(structure)
    assert "test-package" in [x.name for x in packages["pypi"]]
    assert "not-valid" not in [x.name for x in packages["pypi"]]

    assert packages["alpine"]
    assert packages["debian"]
    assert packages["pypi"]
