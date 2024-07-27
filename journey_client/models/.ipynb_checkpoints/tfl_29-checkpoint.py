import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_23 import Tfl23
    from ..models.tfl_28 import Tfl28


T = TypeVar("T", bound="Tfl29")


@_attrs_define
class Tfl29:
    """Object that represents an end to end journey (see schematic).

    Attributes:
        start_date_time (Union[Unset, datetime.datetime]):
        duration (Union[Unset, int]):
        arrival_date_time (Union[Unset, datetime.datetime]):
        legs (Union[Unset, List['Tfl23']]):
        fare (Union[Unset, Tfl28]):
    """

    start_date_time: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, int] = UNSET
    arrival_date_time: Union[Unset, datetime.datetime] = UNSET
    legs: Union[Unset, List["Tfl23"]] = UNSET
    fare: Union[Unset, "Tfl28"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        duration = self.duration

        arrival_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_date_time, Unset):
            arrival_date_time = self.arrival_date_time.isoformat()

        legs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.legs, Unset):
            legs = []
            for legs_item_data in self.legs:
                legs_item = legs_item_data.to_dict()
                legs.append(legs_item)

        fare: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fare, Unset):
            fare = self.fare.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if arrival_date_time is not UNSET:
            field_dict["arrivalDateTime"] = arrival_date_time
        if legs is not UNSET:
            field_dict["legs"] = legs
        if fare is not UNSET:
            field_dict["fare"] = fare

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_23 import Tfl23
        from ..models.tfl_28 import Tfl28

        d = src_dict.copy()
        _start_date_time = d.pop("startDateTime", UNSET)
        start_date_time: Union[Unset, datetime.datetime]
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = isoparse(_start_date_time)

        duration = d.pop("duration", UNSET)

        _arrival_date_time = d.pop("arrivalDateTime", UNSET)
        arrival_date_time: Union[Unset, datetime.datetime]
        if isinstance(_arrival_date_time, Unset):
            arrival_date_time = UNSET
        else:
            arrival_date_time = isoparse(_arrival_date_time)

        legs = []
        _legs = d.pop("legs", UNSET)
        for legs_item_data in _legs or []:
            legs_item = Tfl23.from_dict(legs_item_data)

            legs.append(legs_item)

        _fare = d.pop("fare", UNSET)
        fare: Union[Unset, Tfl28]
        if isinstance(_fare, Unset):
            fare = UNSET
        else:
            fare = Tfl28.from_dict(_fare)

        tfl_29 = cls(
            start_date_time=start_date_time,
            duration=duration,
            arrival_date_time=arrival_date_time,
            legs=legs,
            fare=fare,
        )

        tfl_29.additional_properties = d
        return tfl_29

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
