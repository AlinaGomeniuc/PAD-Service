import enum

LOW_PRIORITY_LIMIT = 20
HIGH_PRIORITY_LIMIT = 5
PROCESSING_TIME = 10
SESSION_TIME = 30


class Statuses(enum.Enum):
    Building = 1
    Processing = 2
    Processed = 3
    Done = 4
    Timed_out = 5
