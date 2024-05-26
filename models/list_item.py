from models.package_kind import PackageKind
import datetime

class ListItem:

    def __init__(self, name: str, amount: float, package_kind: PackageKind):
        self.name = name
        self.created_at = datetime.datetime.now()
        self.amount = amount
        self.package_kind = package_kind

    def __str__(self):
        return f"{self.name} ({self.amount}{self.package_kind})"