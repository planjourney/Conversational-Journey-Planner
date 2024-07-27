from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl14")


@_attrs_define
class Tfl14:
    """
    Attributes:
        naptan_id_reference (Union[Unset, str]):
        station_atco_code (Union[Unset, str]):
        line_identifier (Union[Unset, List[str]]):
    """

    naptan_id_reference: Union[Unset, str] = UNSET
    station_atco_code: Union[Unset, str] = UNSET
    line_identifier: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        naptan_id_reference = self.naptan_id_reference

        station_atco_code = self.station_atco_code

        line_identifier: Union[Unset, List[str]] = UNSET
        if not isinstance(self.line_identifier, Unset):
            line_identifier = self.line_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if naptan_id_reference is not UNSET:
            field_dict["naptanIdReference"] = naptan_id_reference
        if station_atco_code is not UNSET:
            field_dict["stationAtcoCode"] = station_atco_code
        if line_identifier is not UNSET:
            field_dict["lineIdentifier"] = line_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        naptan_id_reference = d.pop("naptanIdReference", UNSET)

        station_atco_code = d.pop("stationAtcoCode", UNSET)

        line_identifier = cast(List[str], d.pop("lineIdentifier", UNSET))

        tfl_14 = cls(
            naptan_id_reference=naptan_id_reference,
            station_atco_code=station_atco_code,
            line_identifier=line_identifier,
        )

        tfl_14.additional_properties = d
        return tfl_14

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
