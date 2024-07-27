from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_29 import Tfl29
    from ..models.tfl_34 import Tfl34
    from ..models.tfl_35 import Tfl35
    from ..models.tfl_38 import Tfl38
    from ..models.tfl_39 import Tfl39


T = TypeVar("T", bound="Tfl40")


@_attrs_define
class Tfl40:
    """A DTO representing a list of possible journeys.

    Attributes:
        journeys (Union[Unset, List['Tfl29']]):
        lines (Union[Unset, List['Tfl34']]):
        cycle_hire_docking_station_data (Union[Unset, Tfl35]):
        stop_messages (Union[Unset, List[str]]):
        recommended_max_age_minutes (Union[Unset, int]):
        search_criteria (Union[Unset, Tfl38]):
        journey_vector (Union[Unset, Tfl39]):
    """

    journeys: Union[Unset, List["Tfl29"]] = UNSET
    lines: Union[Unset, List["Tfl34"]] = UNSET
    cycle_hire_docking_station_data: Union[Unset, "Tfl35"] = UNSET
    stop_messages: Union[Unset, List[str]] = UNSET
    recommended_max_age_minutes: Union[Unset, int] = UNSET
    search_criteria: Union[Unset, "Tfl38"] = UNSET
    journey_vector: Union[Unset, "Tfl39"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        journeys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.journeys, Unset):
            journeys = []
            for journeys_item_data in self.journeys:
                journeys_item = journeys_item_data.to_dict()
                journeys.append(journeys_item)

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        cycle_hire_docking_station_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cycle_hire_docking_station_data, Unset):
            cycle_hire_docking_station_data = self.cycle_hire_docking_station_data.to_dict()

        stop_messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stop_messages, Unset):
            stop_messages = self.stop_messages

        recommended_max_age_minutes = self.recommended_max_age_minutes

        search_criteria: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.search_criteria, Unset):
            search_criteria = self.search_criteria.to_dict()

        journey_vector: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.journey_vector, Unset):
            journey_vector = self.journey_vector.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if journeys is not UNSET:
            field_dict["journeys"] = journeys
        if lines is not UNSET:
            field_dict["lines"] = lines
        if cycle_hire_docking_station_data is not UNSET:
            field_dict["cycleHireDockingStationData"] = cycle_hire_docking_station_data
        if stop_messages is not UNSET:
            field_dict["stopMessages"] = stop_messages
        if recommended_max_age_minutes is not UNSET:
            field_dict["recommendedMaxAgeMinutes"] = recommended_max_age_minutes
        if search_criteria is not UNSET:
            field_dict["searchCriteria"] = search_criteria
        if journey_vector is not UNSET:
            field_dict["journeyVector"] = journey_vector

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_29 import Tfl29
        from ..models.tfl_34 import Tfl34
        from ..models.tfl_35 import Tfl35
        from ..models.tfl_38 import Tfl38
        from ..models.tfl_39 import Tfl39

        d = src_dict.copy()
        journeys = []
        _journeys = d.pop("journeys", UNSET)
        for journeys_item_data in _journeys or []:
            journeys_item = Tfl29.from_dict(journeys_item_data)

            journeys.append(journeys_item)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = Tfl34.from_dict(lines_item_data)

            lines.append(lines_item)

        _cycle_hire_docking_station_data = d.pop("cycleHireDockingStationData", UNSET)
        cycle_hire_docking_station_data: Union[Unset, Tfl35]
        if isinstance(_cycle_hire_docking_station_data, Unset):
            cycle_hire_docking_station_data = UNSET
        else:
            cycle_hire_docking_station_data = Tfl35.from_dict(_cycle_hire_docking_station_data)

        stop_messages = cast(List[str], d.pop("stopMessages", UNSET))

        recommended_max_age_minutes = d.pop("recommendedMaxAgeMinutes", UNSET)

        _search_criteria = d.pop("searchCriteria", UNSET)
        search_criteria: Union[Unset, Tfl38]
        if isinstance(_search_criteria, Unset):
            search_criteria = UNSET
        else:
            search_criteria = Tfl38.from_dict(_search_criteria)

        _journey_vector = d.pop("journeyVector", UNSET)
        journey_vector: Union[Unset, Tfl39]
        if isinstance(_journey_vector, Unset):
            journey_vector = UNSET
        else:
            journey_vector = Tfl39.from_dict(_journey_vector)

        tfl_40 = cls(
            journeys=journeys,
            lines=lines,
            cycle_hire_docking_station_data=cycle_hire_docking_station_data,
            stop_messages=stop_messages,
            recommended_max_age_minutes=recommended_max_age_minutes,
            search_criteria=search_criteria,
            journey_vector=journey_vector,
        )

        tfl_40.additional_properties = d
        return tfl_40

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
