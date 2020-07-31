"""Helpers."""
import re
from .versions.package import Package


def get_packages(structure):
    alpine, debian, pypi = [], [], []
    tmp = [x for x in structure.get("run") if "=" in x]
    for pkg in tmp:
        if re.search(r"apk add", pkg):
            alpine.extend([Package(x) for x in pkg.split(" ") if "=" in x])
        elif re.search(r"apt(|-get)\ install", pkg):
            debian.extend([Package(x) for x in pkg.split(" ") if "=" in x])
        elif re.search(r"pip(|3)\ install", pkg):
            pypi.extend([Package(x, "==") for x in pkg.split(" ") if "=" in x])
    return {"alpine": alpine, "debian": debian, "pypi": pypi}
