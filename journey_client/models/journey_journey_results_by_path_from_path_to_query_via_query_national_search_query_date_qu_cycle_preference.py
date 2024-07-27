from enum import Enum


class JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference(str, Enum):
    ALLTHEWAY = "AllTheWay"
    CYCLEHIRE = "CycleHire"
    LEAVEATSTATION = "LeaveAtStation"
    NONE = "None"
    TAKEONTRANSPORT = "TakeOnTransport"

    def __str__(self) -> str:
        return str(self.value)
