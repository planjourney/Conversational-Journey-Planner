from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl")


@_attrs_define
class Tfl:
    """
    Attributes:
        is_tfl_service (Union[Unset, bool]):
        is_fare_paying (Union[Unset, bool]):
        is_scheduled_service (Union[Unset, bool]):
        mode_name (Union[Unset, str]):
    """

    is_tfl_service: Union[Unset, bool] = UNSET
    is_fare_paying: Union[Unset, bool] = UNSET
    is_scheduled_service: Union[Unset, bool] = UNSET
    mode_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_tfl_service = self.is_tfl_service

        is_fare_paying = self.is_fare_paying

        is_scheduled_service = self.is_scheduled_service

        mode_name = self.mode_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_tfl_service is not UNSET:
            field_dict["isTflService"] = is_tfl_service
        if is_fare_paying is not UNSET:
            field_dict["isFarePaying"] = is_fare_paying
        if is_scheduled_service is not UNSET:
            field_dict["isScheduledService"] = is_scheduled_service
        if mode_name is not UNSET:
            field_dict["modeName"] = mode_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_tfl_service = d.pop("isTflService", UNSET)

        is_fare_paying = d.pop("isFarePaying", UNSET)

        is_scheduled_service = d.pop("isScheduledService", UNSET)

        mode_name = d.pop("modeName", UNSET)

        tfl = cls(
            is_tfl_service=is_tfl_service,
            is_fare_paying=is_fare_paying,
            is_scheduled_service=is_scheduled_service,
            mode_name=mode_name,
        )

        tfl.additional_properties = d
        return tfl

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
