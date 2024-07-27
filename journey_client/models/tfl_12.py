from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_10 import Tfl10
    from ..models.tfl_11 import Tfl11


T = TypeVar("T", bound="Tfl12")


@_attrs_define
class Tfl12:
    """
    Attributes:
        line_string (Union[Unset, str]):
        stop_points (Union[Unset, List['Tfl10']]):
        elevation (Union[Unset, List['Tfl11']]):
    """

    line_string: Union[Unset, str] = UNSET
    stop_points: Union[Unset, List["Tfl10"]] = UNSET
    elevation: Union[Unset, List["Tfl11"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_string = self.line_string

        stop_points: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stop_points, Unset):
            stop_points = []
            for stop_points_item_data in self.stop_points:
                stop_points_item = stop_points_item_data.to_dict()
                stop_points.append(stop_points_item)

        elevation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elevation, Unset):
            elevation = []
            for elevation_item_data in self.elevation:
                elevation_item = elevation_item_data.to_dict()
                elevation.append(elevation_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_string is not UNSET:
            field_dict["lineString"] = line_string
        if stop_points is not UNSET:
            field_dict["stopPoints"] = stop_points
        if elevation is not UNSET:
            field_dict["elevation"] = elevation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_10 import Tfl10
        from ..models.tfl_11 import Tfl11

        d = src_dict.copy()
        line_string = d.pop("lineString", UNSET)

        stop_points = []
        _stop_points = d.pop("stopPoints", UNSET)
        for stop_points_item_data in _stop_points or []:
            stop_points_item = Tfl10.from_dict(stop_points_item_data)

            stop_points.append(stop_points_item)

        elevation = []
        _elevation = d.pop("elevation", UNSET)
        for elevation_item_data in _elevation or []:
            elevation_item = Tfl11.from_dict(elevation_item_data)

            elevation.append(elevation_item)

        tfl_12 = cls(
            line_string=line_string,
            stop_points=stop_points,
            elevation=elevation,
        )

        tfl_12.additional_properties = d
        return tfl_12

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
