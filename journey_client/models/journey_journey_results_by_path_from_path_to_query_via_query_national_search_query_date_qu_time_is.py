from enum import Enum


class JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs(str, Enum):
    ARRIVING = "Arriving"
    DEPARTING = "Departing"

    def __str__(self) -> str:
        return str(self.value)
