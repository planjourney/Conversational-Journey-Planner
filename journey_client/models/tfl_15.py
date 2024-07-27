from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl15")


@_attrs_define
class Tfl15:
    """
    Attributes:
        mode_name (Union[Unset, str]):
        line_identifier (Union[Unset, List[str]]):
    """

    mode_name: Union[Unset, str] = UNSET
    line_identifier: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode_name = self.mode_name

        line_identifier: Union[Unset, List[str]] = UNSET
        if not isinstance(self.line_identifier, Unset):
            line_identifier = self.line_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode_name is not UNSET:
            field_dict["modeName"] = mode_name
        if line_identifier is not UNSET:
            field_dict["lineIdentifier"] = line_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode_name = d.pop("modeName", UNSET)

        line_identifier = cast(List[str], d.pop("lineIdentifier", UNSET))

        tfl_15 = cls(
            mode_name=mode_name,
            line_identifier=line_identifier,
        )

        tfl_15.additional_properties = d
        return tfl_15

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
