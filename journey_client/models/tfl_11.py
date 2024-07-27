from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl11")


@_attrs_define
class Tfl11:
    """
    Attributes:
        distance (Union[Unset, int]):
        start_lat (Union[Unset, float]):
        start_lon (Union[Unset, float]):
        end_lat (Union[Unset, float]):
        end_lon (Union[Unset, float]):
        height_from_previous_point (Union[Unset, int]):
        gradient (Union[Unset, float]):
    """

    distance: Union[Unset, int] = UNSET
    start_lat: Union[Unset, float] = UNSET
    start_lon: Union[Unset, float] = UNSET
    end_lat: Union[Unset, float] = UNSET
    end_lon: Union[Unset, float] = UNSET
    height_from_previous_point: Union[Unset, int] = UNSET
    gradient: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distance = self.distance

        start_lat = self.start_lat

        start_lon = self.start_lon

        end_lat = self.end_lat

        end_lon = self.end_lon

        height_from_previous_point = self.height_from_previous_point

        gradient = self.gradient

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distance is not UNSET:
            field_dict["distance"] = distance
        if start_lat is not UNSET:
            field_dict["startLat"] = start_lat
        if start_lon is not UNSET:
            field_dict["startLon"] = start_lon
        if end_lat is not UNSET:
            field_dict["endLat"] = end_lat
        if end_lon is not UNSET:
            field_dict["endLon"] = end_lon
        if height_from_previous_point is not UNSET:
            field_dict["heightFromPreviousPoint"] = height_from_previous_point
        if gradient is not UNSET:
            field_dict["gradient"] = gradient

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        distance = d.pop("distance", UNSET)

        start_lat = d.pop("startLat", UNSET)

        start_lon = d.pop("startLon", UNSET)

        end_lat = d.pop("endLat", UNSET)

        end_lon = d.pop("endLon", UNSET)

        height_from_previous_point = d.pop("heightFromPreviousPoint", UNSET)

        gradient = d.pop("gradient", UNSET)

        tfl_11 = cls(
            distance=distance,
            start_lat=start_lat,
            start_lon=start_lon,
            end_lat=end_lat,
            end_lon=end_lon,
            height_from_previous_point=height_from_previous_point,
            gradient=gradient,
        )

        tfl_11.additional_properties = d
        return tfl_11

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
