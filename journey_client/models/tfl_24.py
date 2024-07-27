import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl24")


@_attrs_define
class Tfl24:
    """
    Attributes:
        mode_type (Union[Unset, str]):
        validation_type (Union[Unset, str]):
        host_device_type (Union[Unset, str]):
        bus_route_id (Union[Unset, str]):
        national_location_code (Union[Unset, int]):
        tap_timestamp (Union[Unset, datetime.datetime]):
    """

    mode_type: Union[Unset, str] = UNSET
    validation_type: Union[Unset, str] = UNSET
    host_device_type: Union[Unset, str] = UNSET
    bus_route_id: Union[Unset, str] = UNSET
    national_location_code: Union[Unset, int] = UNSET
    tap_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode_type = self.mode_type

        validation_type = self.validation_type

        host_device_type = self.host_device_type

        bus_route_id = self.bus_route_id

        national_location_code = self.national_location_code

        tap_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.tap_timestamp, Unset):
            tap_timestamp = self.tap_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode_type is not UNSET:
            field_dict["modeType"] = mode_type
        if validation_type is not UNSET:
            field_dict["validationType"] = validation_type
        if host_device_type is not UNSET:
            field_dict["hostDeviceType"] = host_device_type
        if bus_route_id is not UNSET:
            field_dict["busRouteId"] = bus_route_id
        if national_location_code is not UNSET:
            field_dict["nationalLocationCode"] = national_location_code
        if tap_timestamp is not UNSET:
            field_dict["tapTimestamp"] = tap_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mode_type = d.pop("modeType", UNSET)

        validation_type = d.pop("validationType", UNSET)

        host_device_type = d.pop("hostDeviceType", UNSET)

        bus_route_id = d.pop("busRouteId", UNSET)

        national_location_code = d.pop("nationalLocationCode", UNSET)

        _tap_timestamp = d.pop("tapTimestamp", UNSET)
        tap_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_tap_timestamp, Unset):
            tap_timestamp = UNSET
        else:
            tap_timestamp = isoparse(_tap_timestamp)

        tfl_24 = cls(
            mode_type=mode_type,
            validation_type=validation_type,
            host_device_type=host_device_type,
            bus_route_id=bus_route_id,
            national_location_code=national_location_code,
            tap_timestamp=tap_timestamp,
        )

        tfl_24.additional_properties = d
        return tfl_24

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
