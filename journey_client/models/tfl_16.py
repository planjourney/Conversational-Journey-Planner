import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl16")


@_attrs_define
class Tfl16:
    """
    Attributes:
        category (Union[Unset, str]):
        key (Union[Unset, str]):
        source_system_key (Union[Unset, str]):
        value (Union[Unset, str]):
        modified (Union[Unset, datetime.datetime]):
    """

    category: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    source_system_key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category

        key = self.key

        source_system_key = self.source_system_key

        value = self.value

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if key is not UNSET:
            field_dict["key"] = key
        if source_system_key is not UNSET:
            field_dict["sourceSystemKey"] = source_system_key
        if value is not UNSET:
            field_dict["value"] = value
        if modified is not UNSET:
            field_dict["modified"] = modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category", UNSET)

        key = d.pop("key", UNSET)

        source_system_key = d.pop("sourceSystemKey", UNSET)

        value = d.pop("value", UNSET)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        tfl_16 = cls(
            category=category,
            key=key,
            source_system_key=source_system_key,
            value=value,
            modified=modified,
        )

        tfl_16.additional_properties = d
        return tfl_16

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
