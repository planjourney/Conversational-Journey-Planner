from enum import Enum


class JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference(str, Enum):
    LEASTINTERCHANGE = "LeastInterchange"
    LEASTTIME = "LeastTime"
    LEASTWALKING = "LeastWalking"

    def __str__(self) -> str:
        return str(self.value)
