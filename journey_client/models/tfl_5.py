from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl5")


@_attrs_define
class Tfl5:
    """
    Attributes:
        type (Union[Unset, str]):
        incline (Union[Unset, str]):
        stop_id (Union[Unset, int]):
        position (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    incline: Union[Unset, str] = UNSET
    stop_id: Union[Unset, int] = UNSET
    position: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        incline = self.incline

        stop_id = self.stop_id

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if incline is not UNSET:
            field_dict["incline"] = incline
        if stop_id is not UNSET:
            field_dict["stopId"] = stop_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        incline = d.pop("incline", UNSET)

        stop_id = d.pop("stopId", UNSET)

        position = d.pop("position", UNSET)

        tfl_5 = cls(
            type=type,
            incline=incline,
            stop_id=stop_id,
            position=position,
        )

        tfl_5.additional_properties = d
        return tfl_5

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
