from enum import Enum

class PackageKind(Enum):
    KG = 'kg'
    PACK = 'op'

    def __str__(self) -> str:
        return self.value