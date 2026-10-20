from importlib.metadata import version

def dependency_versions():
    return {name: version(name) for name in ("requests","PyYAML","opsbase-utils")}
