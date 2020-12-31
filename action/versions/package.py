class Package:
    def __init__(self, package, seperator="="):
        self.old = package
        self.seperator = seperator
        self.name = package.split(seperator)[0]
        self.installed = package.split(seperator)[-1]
        self.available = None

    @property
    def new(self):
        return f"{self.name}{self.seperator}{self.available}"

    @property
    def updated(self):
        if self.installed is None or self.available is None:
            return False
        return self.installed != self.available
