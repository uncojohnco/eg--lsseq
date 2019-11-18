
from typing import Tuple
from dataclasses import dataclass


@dataclass
class SubstrPos:
    start: int
    end: int


@dataclass
class SubstrMatch:
    pos: SubstrPos
    groups: Tuple[str, str]


@dataclass
class Fileobj:

    dirname: str
    ext: str
