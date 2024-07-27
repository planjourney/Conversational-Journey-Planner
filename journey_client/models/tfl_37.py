from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_36 import Tfl36


T = TypeVar("T", bound="Tfl37")


@_attrs_define
class Tfl37:
    """
    Attributes:
        earliest (Union[Unset, Tfl36]):
        earlier (Union[Unset, Tfl36]):
        later (Union[Unset, Tfl36]):
        latest (Union[Unset, Tfl36]):
    """

    earliest: Union[Unset, "Tfl36"] = UNSET
    earlier: Union[Unset, "Tfl36"] = UNSET
    later: Union[Unset, "Tfl36"] = UNSET
    latest: Union[Unset, "Tfl36"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        earliest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.earliest, Unset):
            earliest = self.earliest.to_dict()

        earlier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.earlier, Unset):
            earlier = self.earlier.to_dict()

        later: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.later, Unset):
            later = self.later.to_dict()

        latest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest, Unset):
            latest = self.latest.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if earliest is not UNSET:
            field_dict["earliest"] = earliest
        if earlier is not UNSET:
            field_dict["earlier"] = earlier
        if later is not UNSET:
            field_dict["later"] = later
        if latest is not UNSET:
            field_dict["latest"] = latest

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_36 import Tfl36

        d = src_dict.copy()
        _earliest = d.pop("earliest", UNSET)
        earliest: Union[Unset, Tfl36]
        if isinstance(_earliest, Unset):
            earliest = UNSET
        else:
            earliest = Tfl36.from_dict(_earliest)

        _earlier = d.pop("earlier", UNSET)
        earlier: Union[Unset, Tfl36]
        if isinstance(_earlier, Unset):
            earlier = UNSET
        else:
            earlier = Tfl36.from_dict(_earlier)

        _later = d.pop("later", UNSET)
        later: Union[Unset, Tfl36]
        if isinstance(_later, Unset):
            later = UNSET
        else:
            later = Tfl36.from_dict(_later)

        _latest = d.pop("latest", UNSET)
        latest: Union[Unset, Tfl36]
        if isinstance(_latest, Unset):
            latest = UNSET
        else:
            latest = Tfl36.from_dict(_latest)

        tfl_37 = cls(
            earliest=earliest,
            earlier=earlier,
            later=later,
            latest=latest,
        )

        tfl_37.additional_properties = d
        return tfl_37

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
