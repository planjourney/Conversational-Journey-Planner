import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_9 import Tfl9
    from ..models.tfl_21 import Tfl21
    from ..models.tfl_31 import Tfl31
    from ..models.tfl_32 import Tfl32
    from ..models.tfl_33 import Tfl33


T = TypeVar("T", bound="Tfl34")


@_attrs_define
class Tfl34:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        mode_name (Union[Unset, str]):
        disruptions (Union[Unset, List['Tfl21']]):
        created (Union[Unset, datetime.datetime]):
        modified (Union[Unset, datetime.datetime]):
        line_statuses (Union[Unset, List['Tfl31']]):
        route_sections (Union[Unset, List['Tfl32']]):
        service_types (Union[Unset, List['Tfl33']]):
        crowding (Union[Unset, Tfl9]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mode_name: Union[Unset, str] = UNSET
    disruptions: Union[Unset, List["Tfl21"]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    line_statuses: Union[Unset, List["Tfl31"]] = UNSET
    route_sections: Union[Unset, List["Tfl32"]] = UNSET
    service_types: Union[Unset, List["Tfl33"]] = UNSET
    crowding: Union[Unset, "Tfl9"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        mode_name = self.mode_name

        disruptions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.disruptions, Unset):
            disruptions = []
            for disruptions_item_data in self.disruptions:
                disruptions_item = disruptions_item_data.to_dict()
                disruptions.append(disruptions_item)

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        line_statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_statuses, Unset):
            line_statuses = []
            for line_statuses_item_data in self.line_statuses:
                line_statuses_item = line_statuses_item_data.to_dict()
                line_statuses.append(line_statuses_item)

        route_sections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.route_sections, Unset):
            route_sections = []
            for route_sections_item_data in self.route_sections:
                route_sections_item = route_sections_item_data.to_dict()
                route_sections.append(route_sections_item)

        service_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_types, Unset):
            service_types = []
            for service_types_item_data in self.service_types:
                service_types_item = service_types_item_data.to_dict()
                service_types.append(service_types_item)

        crowding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crowding, Unset):
            crowding = self.crowding.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if mode_name is not UNSET:
            field_dict["modeName"] = mode_name
        if disruptions is not UNSET:
            field_dict["disruptions"] = disruptions
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if line_statuses is not UNSET:
            field_dict["lineStatuses"] = line_statuses
        if route_sections is not UNSET:
            field_dict["routeSections"] = route_sections
        if service_types is not UNSET:
            field_dict["serviceTypes"] = service_types
        if crowding is not UNSET:
            field_dict["crowding"] = crowding

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_9 import Tfl9
        from ..models.tfl_21 import Tfl21
        from ..models.tfl_31 import Tfl31
        from ..models.tfl_32 import Tfl32
        from ..models.tfl_33 import Tfl33

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        mode_name = d.pop("modeName", UNSET)

        disruptions = []
        _disruptions = d.pop("disruptions", UNSET)
        for disruptions_item_data in _disruptions or []:
            disruptions_item = Tfl21.from_dict(disruptions_item_data)

            disruptions.append(disruptions_item)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        line_statuses = []
        _line_statuses = d.pop("lineStatuses", UNSET)
        for line_statuses_item_data in _line_statuses or []:
            line_statuses_item = Tfl31.from_dict(line_statuses_item_data)

            line_statuses.append(line_statuses_item)

        route_sections = []
        _route_sections = d.pop("routeSections", UNSET)
        for route_sections_item_data in _route_sections or []:
            route_sections_item = Tfl32.from_dict(route_sections_item_data)

            route_sections.append(route_sections_item)

        service_types = []
        _service_types = d.pop("serviceTypes", UNSET)
        for service_types_item_data in _service_types or []:
            service_types_item = Tfl33.from_dict(service_types_item_data)

            service_types.append(service_types_item)

        _crowding = d.pop("crowding", UNSET)
        crowding: Union[Unset, Tfl9]
        if isinstance(_crowding, Unset):
            crowding = UNSET
        else:
            crowding = Tfl9.from_dict(_crowding)

        tfl_34 = cls(
            id=id,
            name=name,
            mode_name=mode_name,
            disruptions=disruptions,
            created=created,
            modified=modified,
            line_statuses=line_statuses,
            route_sections=route_sections,
            service_types=service_types,
            crowding=crowding,
        )

        tfl_34.additional_properties = d
        return tfl_34

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
