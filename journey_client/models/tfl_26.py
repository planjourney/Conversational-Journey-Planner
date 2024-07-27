from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_25 import Tfl25


T = TypeVar("T", bound="Tfl26")


@_attrs_define
class Tfl26:
    """
    Attributes:
        low_zone (Union[Unset, int]):
        high_zone (Union[Unset, int]):
        cost (Union[Unset, int]):
        charge_profile_name (Union[Unset, str]):
        is_hopper_fare (Union[Unset, bool]):
        charge_level (Union[Unset, str]):
        peak (Union[Unset, int]):
        off_peak (Union[Unset, int]):
        taps (Union[Unset, List['Tfl25']]):
    """

    low_zone: Union[Unset, int] = UNSET
    high_zone: Union[Unset, int] = UNSET
    cost: Union[Unset, int] = UNSET
    charge_profile_name: Union[Unset, str] = UNSET
    is_hopper_fare: Union[Unset, bool] = UNSET
    charge_level: Union[Unset, str] = UNSET
    peak: Union[Unset, int] = UNSET
    off_peak: Union[Unset, int] = UNSET
    taps: Union[Unset, List["Tfl25"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        low_zone = self.low_zone

        high_zone = self.high_zone

        cost = self.cost

        charge_profile_name = self.charge_profile_name

        is_hopper_fare = self.is_hopper_fare

        charge_level = self.charge_level

        peak = self.peak

        off_peak = self.off_peak

        taps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.taps, Unset):
            taps = []
            for taps_item_data in self.taps:
                taps_item = taps_item_data.to_dict()
                taps.append(taps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if low_zone is not UNSET:
            field_dict["lowZone"] = low_zone
        if high_zone is not UNSET:
            field_dict["highZone"] = high_zone
        if cost is not UNSET:
            field_dict["cost"] = cost
        if charge_profile_name is not UNSET:
            field_dict["chargeProfileName"] = charge_profile_name
        if is_hopper_fare is not UNSET:
            field_dict["isHopperFare"] = is_hopper_fare
        if charge_level is not UNSET:
            field_dict["chargeLevel"] = charge_level
        if peak is not UNSET:
            field_dict["peak"] = peak
        if off_peak is not UNSET:
            field_dict["offPeak"] = off_peak
        if taps is not UNSET:
            field_dict["taps"] = taps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_25 import Tfl25

        d = src_dict.copy()
        low_zone = d.pop("lowZone", UNSET)

        high_zone = d.pop("highZone", UNSET)

        cost = d.pop("cost", UNSET)

        charge_profile_name = d.pop("chargeProfileName", UNSET)

        is_hopper_fare = d.pop("isHopperFare", UNSET)

        charge_level = d.pop("chargeLevel", UNSET)

        peak = d.pop("peak", UNSET)

        off_peak = d.pop("offPeak", UNSET)

        taps = []
        _taps = d.pop("taps", UNSET)
        for taps_item_data in _taps or []:
            taps_item = Tfl25.from_dict(taps_item_data)

            taps.append(taps_item)

        tfl_26 = cls(
            low_zone=low_zone,
            high_zone=high_zone,
            cost=cost,
            charge_profile_name=charge_profile_name,
            is_hopper_fare=is_hopper_fare,
            charge_level=charge_level,
            peak=peak,
            off_peak=off_peak,
            taps=taps,
        )

        tfl_26.additional_properties = d
        return tfl_26

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
