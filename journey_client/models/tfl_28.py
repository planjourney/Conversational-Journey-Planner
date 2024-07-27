from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_26 import Tfl26
    from ..models.tfl_27 import Tfl27


T = TypeVar("T", bound="Tfl28")


@_attrs_define
class Tfl28:
    """
    Attributes:
        total_cost (Union[Unset, int]):
        fares (Union[Unset, List['Tfl26']]):
        caveats (Union[Unset, List['Tfl27']]):
    """

    total_cost: Union[Unset, int] = UNSET
    fares: Union[Unset, List["Tfl26"]] = UNSET
    caveats: Union[Unset, List["Tfl27"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_cost = self.total_cost

        fares: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fares, Unset):
            fares = []
            for fares_item_data in self.fares:
                fares_item = fares_item_data.to_dict()
                fares.append(fares_item)

        caveats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.caveats, Unset):
            caveats = []
            for caveats_item_data in self.caveats:
                caveats_item = caveats_item_data.to_dict()
                caveats.append(caveats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if fares is not UNSET:
            field_dict["fares"] = fares
        if caveats is not UNSET:
            field_dict["caveats"] = caveats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_26 import Tfl26
        from ..models.tfl_27 import Tfl27

        d = src_dict.copy()
        total_cost = d.pop("totalCost", UNSET)

        fares = []
        _fares = d.pop("fares", UNSET)
        for fares_item_data in _fares or []:
            fares_item = Tfl26.from_dict(fares_item_data)

            fares.append(fares_item)

        caveats = []
        _caveats = d.pop("caveats", UNSET)
        for caveats_item_data in _caveats or []:
            caveats_item = Tfl27.from_dict(caveats_item_data)

            caveats.append(caveats_item)

        tfl_28 = cls(
            total_cost=total_cost,
            fares=fares,
            caveats=caveats,
        )

        tfl_28.additional_properties = d
        return tfl_28

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
