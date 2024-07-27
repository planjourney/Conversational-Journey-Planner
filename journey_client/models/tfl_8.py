from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl8")


@_attrs_define
class Tfl8:
    """
    Attributes:
        line (Union[Unset, str]): The Line Name e.g. "Victoria"
        line_direction (Union[Unset, str]): Direction of the Line e.g. NB, SB, WB etc.
        platform_direction (Union[Unset, str]): Direction displayed on the platform e.g. NB, SB, WB etc.
        direction (Union[Unset, str]): Direction in regards to Journey Planner i.e. inbound or outbound
        naptan_to (Union[Unset, str]): Naptan of the adjacent station
        time_slice (Union[Unset, str]): Time in 24hr format with 15 minute intervals e.g. 0500-0515, 0515-0530 etc.
        value (Union[Unset, int]): Scale between 1-6,
                         1 = Very quiet, 2 = Quiet, 3 = Fairly busy, 4 = Busy, 5 = Very busy, 6 = Exceptionally busy
    """

    line: Union[Unset, str] = UNSET
    line_direction: Union[Unset, str] = UNSET
    platform_direction: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    naptan_to: Union[Unset, str] = UNSET
    time_slice: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line = self.line

        line_direction = self.line_direction

        platform_direction = self.platform_direction

        direction = self.direction

        naptan_to = self.naptan_to

        time_slice = self.time_slice

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line is not UNSET:
            field_dict["line"] = line
        if line_direction is not UNSET:
            field_dict["lineDirection"] = line_direction
        if platform_direction is not UNSET:
            field_dict["platformDirection"] = platform_direction
        if direction is not UNSET:
            field_dict["direction"] = direction
        if naptan_to is not UNSET:
            field_dict["naptanTo"] = naptan_to
        if time_slice is not UNSET:
            field_dict["timeSlice"] = time_slice
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line = d.pop("line", UNSET)

        line_direction = d.pop("lineDirection", UNSET)

        platform_direction = d.pop("platformDirection", UNSET)

        direction = d.pop("direction", UNSET)

        naptan_to = d.pop("naptanTo", UNSET)

        time_slice = d.pop("timeSlice", UNSET)

        value = d.pop("value", UNSET)

        tfl_8 = cls(
            line=line,
            line_direction=line_direction,
            platform_direction=platform_direction,
            direction=direction,
            naptan_to=naptan_to,
            time_slice=time_slice,
            value=value,
        )

        tfl_8.additional_properties = d
        return tfl_8

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
