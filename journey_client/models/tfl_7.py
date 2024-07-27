from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl7")


@_attrs_define
class Tfl7:
    """
    Attributes:
        time_slice (Union[Unset, str]): Time in 24hr format with 15 minute intervals e.g. 0500-0515, 0515-0530 etc.
        value (Union[Unset, int]): Count of passenger flow towards a platform
    """

    time_slice: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        time_slice = self.time_slice

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_slice is not UNSET:
            field_dict["timeSlice"] = time_slice
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        time_slice = d.pop("timeSlice", UNSET)

        value = d.pop("value", UNSET)

        tfl_7 = cls(
            time_slice=time_slice,
            value=value,
        )

        tfl_7.additional_properties = d
        return tfl_7

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
