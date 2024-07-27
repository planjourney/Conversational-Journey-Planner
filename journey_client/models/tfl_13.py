from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_10 import Tfl10


T = TypeVar("T", bound="Tfl13")


@_attrs_define
class Tfl13:
    """
    Attributes:
        id (Union[Unset, str]): The Id of the route
        name (Union[Unset, str]): Name such as "72"
        directions (Union[Unset, List[str]]):
        line_identifier (Union[Unset, Tfl10]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    directions: Union[Unset, List[str]] = UNSET
    line_identifier: Union[Unset, "Tfl10"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        directions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.directions, Unset):
            directions = self.directions

        line_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.line_identifier, Unset):
            line_identifier = self.line_identifier.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if directions is not UNSET:
            field_dict["directions"] = directions
        if line_identifier is not UNSET:
            field_dict["lineIdentifier"] = line_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_10 import Tfl10

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        directions = cast(List[str], d.pop("directions", UNSET))

        _line_identifier = d.pop("lineIdentifier", UNSET)
        line_identifier: Union[Unset, Tfl10]
        if isinstance(_line_identifier, Unset):
            line_identifier = UNSET
        else:
            line_identifier = Tfl10.from_dict(_line_identifier)

        tfl_13 = cls(
            id=id,
            name=name,
            directions=directions,
            line_identifier=line_identifier,
        )

        tfl_13.additional_properties = d
        return tfl_13

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
