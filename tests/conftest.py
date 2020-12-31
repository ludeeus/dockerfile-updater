from shutil import copyfile
from _pytest import config
import pytest
from action.dockerfile import Dockerfile
from action.config import Config


@pytest.fixture
def dockerfile(tmpdir):
    copyfile("./tests/Test.dockerfile", f"{tmpdir}/Test.dockerfile")
    yield Dockerfile(Config(tmpdir.strpath), f"{tmpdir}/Test.dockerfile")
