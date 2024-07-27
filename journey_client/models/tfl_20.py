import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_19 import Tfl19


T = TypeVar("T", bound="Tfl20")


@_attrs_define
class Tfl20:
    """
    Attributes:
        id (Union[Unset, str]): The Id of the route
        line_id (Union[Unset, str]): The Id of the Line
        route_code (Union[Unset, str]): The route code
        name (Union[Unset, str]): Name such as "72"
        line_string (Union[Unset, str]): The co-ordinates of the route's path as a geoJSON lineString
        direction (Union[Unset, str]): Inbound or Outbound
        origination_name (Union[Unset, str]): The name of the Origin StopPoint
        destination_name (Union[Unset, str]): The name of the Destination StopPoint
        valid_to (Union[Unset, datetime.datetime]): The DateTime that the Service containing this Route is valid until.
        valid_from (Union[Unset, datetime.datetime]): The DateTime that the Service containing this Route is valid from.
        route_section_naptan_entry_sequence (Union[Unset, List['Tfl19']]):
    """

    id: Union[Unset, str] = UNSET
    line_id: Union[Unset, str] = UNSET
    route_code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    line_string: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    origination_name: Union[Unset, str] = UNSET
    destination_name: Union[Unset, str] = UNSET
    valid_to: Union[Unset, datetime.datetime] = UNSET
    valid_from: Union[Unset, datetime.datetime] = UNSET
    route_section_naptan_entry_sequence: Union[Unset, List["Tfl19"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        line_id = self.line_id

        route_code = self.route_code

        name = self.name

        line_string = self.line_string

        direction = self.direction

        origination_name = self.origination_name

        destination_name = self.destination_name

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        route_section_naptan_entry_sequence: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.route_section_naptan_entry_sequence, Unset):
            route_section_naptan_entry_sequence = []
            for route_section_naptan_entry_sequence_item_data in self.route_section_naptan_entry_sequence:
                route_section_naptan_entry_sequence_item = route_section_naptan_entry_sequence_item_data.to_dict()
                route_section_naptan_entry_sequence.append(route_section_naptan_entry_sequence_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if line_id is not UNSET:
            field_dict["lineId"] = line_id
        if route_code is not UNSET:
            field_dict["routeCode"] = route_code
        if name is not UNSET:
            field_dict["name"] = name
        if line_string is not UNSET:
            field_dict["lineString"] = line_string
        if direction is not UNSET:
            field_dict["direction"] = direction
        if origination_name is not UNSET:
            field_dict["originationName"] = origination_name
        if destination_name is not UNSET:
            field_dict["destinationName"] = destination_name
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if route_section_naptan_entry_sequence is not UNSET:
            field_dict["routeSectionNaptanEntrySequence"] = route_section_naptan_entry_sequence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_19 import Tfl19

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        line_id = d.pop("lineId", UNSET)

        route_code = d.pop("routeCode", UNSET)

        name = d.pop("name", UNSET)

        line_string = d.pop("lineString", UNSET)

        direction = d.pop("direction", UNSET)

        origination_name = d.pop("originationName", UNSET)

        destination_name = d.pop("destinationName", UNSET)

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

        route_section_naptan_entry_sequence = []
        _route_section_naptan_entry_sequence = d.pop("routeSectionNaptanEntrySequence", UNSET)
        for route_section_naptan_entry_sequence_item_data in _route_section_naptan_entry_sequence or []:
            route_section_naptan_entry_sequence_item = Tfl19.from_dict(route_section_naptan_entry_sequence_item_data)

            route_section_naptan_entry_sequence.append(route_section_naptan_entry_sequence_item)

        tfl_20 = cls(
            id=id,
            line_id=line_id,
            route_code=route_code,
            name=name,
            line_string=line_string,
            direction=direction,
            origination_name=origination_name,
            destination_name=destination_name,
            valid_to=valid_to,
            valid_from=valid_from,
            route_section_naptan_entry_sequence=route_section_naptan_entry_sequence,
        )

        tfl_20.additional_properties = d
        return tfl_20

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
