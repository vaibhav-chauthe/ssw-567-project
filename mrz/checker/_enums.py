

from enum import IntEnum


class Kind(IntEnum):  # kind = 0:  fields, 1: warning, 2: error
    FIELDS = 0
    WARNING = 1
    ERROR = 2
