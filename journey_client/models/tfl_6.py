from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl6")


@_attrs_define
class Tfl6:
    """Represents a point located at a latitude and longitude using the WGS84 co-ordinate system.

    Attributes:
        lat (Union[Unset, float]): WGS84 latitude of the location.
        lon (Union[Unset, float]): WGS84 longitude of the location.
    """

    lat: Union[Unset, float] = UNSET
    lon: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lat = self.lat

        lon = self.lon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        tfl_6 = cls(
            lat=lat,
            lon=lon,
        )

        tfl_6.additional_properties = d
        return tfl_6

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
