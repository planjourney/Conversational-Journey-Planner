from enum import Enum


class Tfl10Status(str, Enum):
    ALL = "All"
    IN_PROGRESS = "In Progress"
    NOT_OPEN = "Not Open"
    OPEN = "Open"
    PLANNED = "Planned"
    PLANNED_SUBJECT_TO_FEASIBILITY_AND_CONSULTATION = "Planned - Subject to feasibility and consultation."
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
