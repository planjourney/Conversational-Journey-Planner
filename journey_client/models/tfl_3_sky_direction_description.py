from enum import Enum


class Tfl3SkyDirectionDescription(str, Enum):
    EAST = "East"
    NORTH = "North"
    NORTHEAST = "NorthEast"
    NORTHWEST = "NorthWest"
    SOUTH = "South"
    SOUTHEAST = "SouthEast"
    SOUTHWEST = "SouthWest"
    WEST = "West"

    def __str__(self) -> str:
        return str(self.value)
