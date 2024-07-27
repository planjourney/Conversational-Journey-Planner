from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_18 import Tfl18


T = TypeVar("T", bound="Tfl19")


@_attrs_define
class Tfl19:
    """
    Attributes:
        ordinal (Union[Unset, int]):
        stop_point (Union[Unset, Tfl18]):
    """

    ordinal: Union[Unset, int] = UNSET
    stop_point: Union[Unset, "Tfl18"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ordinal = self.ordinal

        stop_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if stop_point is not UNSET:
            field_dict["stopPoint"] = stop_point

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_18 import Tfl18

        d = src_dict.copy()
        ordinal = d.pop("ordinal", UNSET)

        _stop_point = d.pop("stopPoint", UNSET)
        stop_point: Union[Unset, Tfl18]
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = Tfl18.from_dict(_stop_point)

        tfl_19 = cls(
            ordinal=ordinal,
            stop_point=stop_point,
        )

        tfl_19.additional_properties = d
        return tfl_19

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
