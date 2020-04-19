from alpinepkgs.packages import get_package

def version_alpine(pkg):
    try:
        return get_package(pkg)["x86_64"]["version"]
    except Exception as e:
        print(f"Could not get version for {pkg} - {e}")
        return None