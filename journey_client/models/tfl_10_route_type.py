from enum import Enum


class Tfl10RouteType(str, Enum):
    ALL = "All"
    CENTRAL_LONDON_GRID = "Central London Grid"
    CYCLEWAYS = "Cycleways"
    CYCLE_SUPERHIGHWAYS = "Cycle Superhighways"
    MINI_HOLLANDS = "Mini-Hollands"
    QUIETWAYS = "Quietways"
    STREETSPACE_ROUTE = "Streetspace Route"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
