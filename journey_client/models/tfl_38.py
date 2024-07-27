import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tfl_38_date_time_type import Tfl38DateTimeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_37 import Tfl37


T = TypeVar("T", bound="Tfl38")


@_attrs_define
class Tfl38:
    """
    Attributes:
        date_time (Union[Unset, datetime.datetime]):
        date_time_type (Union[Unset, Tfl38DateTimeType]):
        time_adjustments (Union[Unset, Tfl37]):
    """

    date_time: Union[Unset, datetime.datetime] = UNSET
    date_time_type: Union[Unset, Tfl38DateTimeType] = UNSET
    time_adjustments: Union[Unset, "Tfl37"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_time: Union[Unset, str] = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat()

        date_time_type: Union[Unset, str] = UNSET
        if not isinstance(self.date_time_type, Unset):
            date_time_type = self.date_time_type.value

        time_adjustments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_adjustments, Unset):
            time_adjustments = self.time_adjustments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if date_time_type is not UNSET:
            field_dict["dateTimeType"] = date_time_type
        if time_adjustments is not UNSET:
            field_dict["timeAdjustments"] = time_adjustments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_37 import Tfl37

        d = src_dict.copy()
        _date_time = d.pop("dateTime", UNSET)
        date_time: Union[Unset, datetime.datetime]
        if isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)

        _date_time_type = d.pop("dateTimeType", UNSET)
        date_time_type: Union[Unset, Tfl38DateTimeType]
        if isinstance(_date_time_type, Unset):
            date_time_type = UNSET
        else:
            date_time_type = Tfl38DateTimeType(_date_time_type)

        _time_adjustments = d.pop("timeAdjustments", UNSET)
        time_adjustments: Union[Unset, Tfl37]
        if isinstance(_time_adjustments, Unset):
            time_adjustments = UNSET
        else:
            time_adjustments = Tfl37.from_dict(_time_adjustments)

        tfl_38 = cls(
            date_time=date_time,
            date_time_type=date_time_type,
            time_adjustments=time_adjustments,
        )

        tfl_38.additional_properties = d
        return tfl_38

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
