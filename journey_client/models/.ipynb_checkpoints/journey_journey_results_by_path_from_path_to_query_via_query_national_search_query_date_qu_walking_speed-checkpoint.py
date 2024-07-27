from enum import Enum


class JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed(str, Enum):
    AVERAGE = "Average"
    FAST = "Fast"
    SLOW = "Slow"

    def __str__(self) -> str:
        return str(self.value)
