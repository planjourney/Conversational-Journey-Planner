from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_7 import Tfl7
    from ..models.tfl_8 import Tfl8


T = TypeVar("T", bound="Tfl9")


@_attrs_define
class Tfl9:
    """
    Attributes:
        passenger_flows (Union[Unset, List['Tfl7']]): Busiest times at a station (static information)
        train_loadings (Union[Unset, List['Tfl8']]): Train Loading on a scale 1-6, 1 being "Very quiet" and 6 being
            "Exceptionally busy" (static information)
    """

    passenger_flows: Union[Unset, List["Tfl7"]] = UNSET
    train_loadings: Union[Unset, List["Tfl8"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        passenger_flows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.passenger_flows, Unset):
            passenger_flows = []
            for passenger_flows_item_data in self.passenger_flows:
                passenger_flows_item = passenger_flows_item_data.to_dict()
                passenger_flows.append(passenger_flows_item)

        train_loadings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.train_loadings, Unset):
            train_loadings = []
            for train_loadings_item_data in self.train_loadings:
                train_loadings_item = train_loadings_item_data.to_dict()
                train_loadings.append(train_loadings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if passenger_flows is not UNSET:
            field_dict["passengerFlows"] = passenger_flows
        if train_loadings is not UNSET:
            field_dict["trainLoadings"] = train_loadings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_7 import Tfl7
        from ..models.tfl_8 import Tfl8

        d = src_dict.copy()
        passenger_flows = []
        _passenger_flows = d.pop("passengerFlows", UNSET)
        for passenger_flows_item_data in _passenger_flows or []:
            passenger_flows_item = Tfl7.from_dict(passenger_flows_item_data)

            passenger_flows.append(passenger_flows_item)

        train_loadings = []
        _train_loadings = d.pop("trainLoadings", UNSET)
        for train_loadings_item_data in _train_loadings or []:
            train_loadings_item = Tfl8.from_dict(train_loadings_item_data)

            train_loadings.append(train_loadings_item)

        tfl_9 = cls(
            passenger_flows=passenger_flows,
            train_loadings=train_loadings,
        )

        tfl_9.additional_properties = d
        return tfl_9

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
