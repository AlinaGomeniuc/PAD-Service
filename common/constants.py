import enum


LIMIT = 3


class Statuses(enum.Enum):
    Building = 1
    Processing = 2
    Processed = 3
    Done = 4
