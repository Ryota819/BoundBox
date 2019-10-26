from enum import Enum


class Choosable(Enum):
    @classmethod
    def choices(cls):
        return [(m.name, m.value) for m in cls]

    @classmethod
    def contains(cls, val):
        return val in [m.name for m in cls]


class Kind(Choosable):
    LIKE = 1
    CUTE = 2
    COOL = 3


class Tag(Choosable):
    YUZU = 1
    KITA = 2
    IWA = 3
    Other = 4
