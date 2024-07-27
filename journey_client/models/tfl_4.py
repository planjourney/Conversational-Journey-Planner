from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_3 import Tfl3


T = TypeVar("T", bound="Tfl4")


@_attrs_define
class Tfl4:
    """
    Attributes:
        summary (Union[Unset, str]):
        detailed (Union[Unset, str]):
        steps (Union[Unset, List['Tfl3']]):
    """

    summary: Union[Unset, str] = UNSET
    detailed: Union[Unset, str] = UNSET
    steps: Union[Unset, List["Tfl3"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        summary = self.summary

        detailed = self.detailed

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if detailed is not UNSET:
            field_dict["detailed"] = detailed
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_3 import Tfl3

        d = src_dict.copy()
        summary = d.pop("summary", UNSET)

        detailed = d.pop("detailed", UNSET)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = Tfl3.from_dict(steps_item_data)

            steps.append(steps_item)

        tfl_4 = cls(
            summary=summary,
            detailed=detailed,
            steps=steps,
        )

        tfl_4.additional_properties = d
        return tfl_4

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
