from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_24 import Tfl24


T = TypeVar("T", bound="Tfl25")


@_attrs_define
class Tfl25:
    """
    Attributes:
        atco_code (Union[Unset, str]):
        tap_details (Union[Unset, Tfl24]):
    """

    atco_code: Union[Unset, str] = UNSET
    tap_details: Union[Unset, "Tfl24"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        atco_code = self.atco_code

        tap_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tap_details, Unset):
            tap_details = self.tap_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if atco_code is not UNSET:
            field_dict["atcoCode"] = atco_code
        if tap_details is not UNSET:
            field_dict["tapDetails"] = tap_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_24 import Tfl24

        d = src_dict.copy()
        atco_code = d.pop("atcoCode", UNSET)

        _tap_details = d.pop("tapDetails", UNSET)
        tap_details: Union[Unset, Tfl24]
        if isinstance(_tap_details, Unset):
            tap_details = UNSET
        else:
            tap_details = Tfl24.from_dict(_tap_details)

        tfl_25 = cls(
            atco_code=atco_code,
            tap_details=tap_details,
        )

        tfl_25.additional_properties = d
        return tfl_25

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
