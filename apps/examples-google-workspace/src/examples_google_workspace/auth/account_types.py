from enum import Enum


class AccountTypes(Enum):
    default = 0
    user = 2
    service = 3

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_string(s: str) -> "AccountTypes":
        try:
            return AccountTypes[s]
        except KeyError:
            raise ValueError()
