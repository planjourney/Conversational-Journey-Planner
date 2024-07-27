from enum import Enum


class Tfl3TrackType(str, Enum):
    BUSYROADS = "BusyRoads"
    CANALTOWPATH = "CanalTowpath"
    CYCLESUPERHIGHWAY = "CycleSuperHighway"
    NONE = "None"
    PROVISIONFORCYCLISTS = "ProvisionForCyclists"
    PUSHBIKE = "PushBike"
    QUIETROAD = "QuietRoad"
    QUIETWAY = "Quietway"

    def __str__(self) -> str:
        return str(self.value)
