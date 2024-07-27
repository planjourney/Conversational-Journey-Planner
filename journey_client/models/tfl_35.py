from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl35")


@_attrs_define
class Tfl35:
    """
    Attributes:
        origin_number_of_bikes (Union[Unset, int]):
        destination_number_of_bikes (Union[Unset, int]):
        origin_number_of_empty_slots (Union[Unset, int]):
        destination_number_of_empty_slots (Union[Unset, int]):
        origin_id (Union[Unset, str]):
        destination_id (Union[Unset, str]):
    """

    origin_number_of_bikes: Union[Unset, int] = UNSET
    destination_number_of_bikes: Union[Unset, int] = UNSET
    origin_number_of_empty_slots: Union[Unset, int] = UNSET
    destination_number_of_empty_slots: Union[Unset, int] = UNSET
    origin_id: Union[Unset, str] = UNSET
    destination_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin_number_of_bikes = self.origin_number_of_bikes

        destination_number_of_bikes = self.destination_number_of_bikes

        origin_number_of_empty_slots = self.origin_number_of_empty_slots

        destination_number_of_empty_slots = self.destination_number_of_empty_slots

        origin_id = self.origin_id

        destination_id = self.destination_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if origin_number_of_bikes is not UNSET:
            field_dict["originNumberOfBikes"] = origin_number_of_bikes
        if destination_number_of_bikes is not UNSET:
            field_dict["destinationNumberOfBikes"] = destination_number_of_bikes
        if origin_number_of_empty_slots is not UNSET:
            field_dict["originNumberOfEmptySlots"] = origin_number_of_empty_slots
        if destination_number_of_empty_slots is not UNSET:
            field_dict["destinationNumberOfEmptySlots"] = destination_number_of_empty_slots
        if origin_id is not UNSET:
            field_dict["originId"] = origin_id
        if destination_id is not UNSET:
            field_dict["destinationId"] = destination_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        origin_number_of_bikes = d.pop("originNumberOfBikes", UNSET)

        destination_number_of_bikes = d.pop("destinationNumberOfBikes", UNSET)

        origin_number_of_empty_slots = d.pop("originNumberOfEmptySlots", UNSET)

        destination_number_of_empty_slots = d.pop("destinationNumberOfEmptySlots", UNSET)

        origin_id = d.pop("originId", UNSET)

        destination_id = d.pop("destinationId", UNSET)

        tfl_35 = cls(
            origin_number_of_bikes=origin_number_of_bikes,
            destination_number_of_bikes=destination_number_of_bikes,
            origin_number_of_empty_slots=origin_number_of_empty_slots,
            destination_number_of_empty_slots=destination_number_of_empty_slots,
            origin_id=origin_id,
            destination_id=destination_id,
        )

        tfl_35.additional_properties = d
        return tfl_35

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
