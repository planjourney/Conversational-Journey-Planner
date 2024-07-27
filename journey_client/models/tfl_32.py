import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl32")


@_attrs_define
class Tfl32:
    """Description of a Route used in Route search results.

    Attributes:
        route_code (Union[Unset, str]): The route code
        name (Union[Unset, str]): Name such as "72"
        direction (Union[Unset, str]): Inbound or Outbound
        origination_name (Union[Unset, str]): The name of the Origin StopPoint
        destination_name (Union[Unset, str]): The name of the Destination StopPoint
        originator (Union[Unset, str]): The Id (NaPTAN code) of the Origin StopPoint
        destination (Union[Unset, str]): The Id (NaPTAN code) or the Destination StopPoint
        service_type (Union[Unset, str]): Regular or Night
        valid_to (Union[Unset, datetime.datetime]): The DateTime that the Service containing this Route is valid until.
        valid_from (Union[Unset, datetime.datetime]): The DateTime that the Service containing this Route is valid from.
    """

    route_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    origination_name: Union[Unset, str] = UNSET
    destination_name: Union[Unset, str] = UNSET
    originator: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    service_type: Union[Unset, str] = UNSET
    valid_to: Union[Unset, datetime.datetime] = UNSET
    valid_from: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        route_code = self.route_code

        name = self.name

        direction = self.direction

        origination_name = self.origination_name

        destination_name = self.destination_name

        originator = self.originator

        destination = self.destination

        service_type = self.service_type

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if route_code is not UNSET:
            field_dict["routeCode"] = route_code
        if name is not UNSET:
            field_dict["name"] = name
        if direction is not UNSET:
            field_dict["direction"] = direction
        if origination_name is not UNSET:
            field_dict["originationName"] = origination_name
        if destination_name is not UNSET:
            field_dict["destinationName"] = destination_name
        if originator is not UNSET:
            field_dict["originator"] = originator
        if destination is not UNSET:
            field_dict["destination"] = destination
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        route_code = d.pop("routeCode", UNSET)

        name = d.pop("name", UNSET)

        direction = d.pop("direction", UNSET)

        origination_name = d.pop("originationName", UNSET)

        destination_name = d.pop("destinationName", UNSET)

        originator = d.pop("originator", UNSET)

        destination = d.pop("destination", UNSET)

        service_type = d.pop("serviceType", UNSET)

        _valid_to = d.pop("validTo", UNSET)
        valid_to: Union[Unset, datetime.datetime]
        if isinstance(_valid_to, Unset):
            valid_to = UNSET
        else:
            valid_to = isoparse(_valid_to)

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: Union[Unset, datetime.datetime]
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        tfl_32 = cls(
            route_code=route_code,
            name=name,
            direction=direction,
            origination_name=origination_name,
            destination_name=destination_name,
            originator=originator,
            destination=destination,
            service_type=service_type,
            valid_to=valid_to,
            valid_from=valid_from,
        )

        tfl_32.additional_properties = d
        return tfl_32

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
