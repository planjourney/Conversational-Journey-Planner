from enum import Enum


class Tfl21Category(str, Enum):
    CROWDING = "Crowding"
    EVENT = "Event"
    INFORMATION = "Information"
    PLANNEDWORK = "PlannedWork"
    REALTIME = "RealTime"
    STATUSALERT = "StatusAlert"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
