import enum


LIMIT = 20


class Statuses(enum.Enum):
    Building = 1
    Processing = 2
    Processed = 3
    Done = 4
    Timed_out = 5
