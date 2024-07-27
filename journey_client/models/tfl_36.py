from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl36")


@_attrs_define
class Tfl36:
    """
    Attributes:
        date (Union[Unset, str]):
        time (Union[Unset, str]):
        time_is (Union[Unset, str]):
        uri (Union[Unset, str]):
    """

    date: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    time_is: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date

        time = self.time

        time_is = self.time_is

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if time is not UNSET:
            field_dict["time"] = time
        if time_is is not UNSET:
            field_dict["timeIs"] = time_is
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        time = d.pop("time", UNSET)

        time_is = d.pop("timeIs", UNSET)

        uri = d.pop("uri", UNSET)

        tfl_36 = cls(
            date=date,
            time=time,
            time_is=time_is,
            uri=uri,
        )

        tfl_36.additional_properties = d
        return tfl_36

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
