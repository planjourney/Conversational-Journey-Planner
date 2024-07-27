from enum import Enum


class JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference(str, Enum):
    NOELEVATORS = "NoElevators"
    NOESCALATORS = "NoEscalators"
    NOREQUIREMENTS = "NoRequirements"
    NOSOLIDSTAIRS = "NoSolidStairs"
    STEPFREETOPLATFORM = "StepFreeToPlatform"
    STEPFREETOVEHICLE = "StepFreeToVehicle"

    def __str__(self) -> str:
        return str(self.value)
