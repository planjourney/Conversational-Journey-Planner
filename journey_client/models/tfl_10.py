from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tfl_10_route_type import Tfl10RouteType
from ..models.tfl_10_status import Tfl10Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_9 import Tfl9


T = TypeVar("T", bound="Tfl10")


@_attrs_define
class Tfl10:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        uri (Union[Unset, str]):
        full_name (Union[Unset, str]):
        type (Union[Unset, str]):
        crowding (Union[Unset, Tfl9]):
        route_type (Union[Unset, Tfl10RouteType]):
        status (Union[Unset, Tfl10Status]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    crowding: Union[Unset, "Tfl9"] = UNSET
    route_type: Union[Unset, Tfl10RouteType] = UNSET
    status: Union[Unset, Tfl10Status] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        uri = self.uri

        full_name = self.full_name

        type = self.type

        crowding: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crowding, Unset):
            crowding = self.crowding.to_dict()

        route_type: Union[Unset, str] = UNSET
        if not isinstance(self.route_type, Unset):
            route_type = self.route_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if uri is not UNSET:
            field_dict["uri"] = uri
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if type is not UNSET:
            field_dict["type"] = type
        if crowding is not UNSET:
            field_dict["crowding"] = crowding
        if route_type is not UNSET:
            field_dict["routeType"] = route_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_9 import Tfl9

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        uri = d.pop("uri", UNSET)

        full_name = d.pop("fullName", UNSET)

        type = d.pop("type", UNSET)

        _crowding = d.pop("crowding", UNSET)
        crowding: Union[Unset, Tfl9]
        if isinstance(_crowding, Unset):
            crowding = UNSET
        else:
            crowding = Tfl9.from_dict(_crowding)

        _route_type = d.pop("routeType", UNSET)
        route_type: Union[Unset, Tfl10RouteType]
        if isinstance(_route_type, Unset):
            route_type = UNSET
        else:
            route_type = Tfl10RouteType(_route_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Tfl10Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Tfl10Status(_status)

        tfl_10 = cls(
            id=id,
            name=name,
            uri=uri,
            full_name=full_name,
            type=type,
            crowding=crowding,
            route_type=route_type,
            status=status,
        )

        tfl_10.additional_properties = d
        return tfl_10

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
