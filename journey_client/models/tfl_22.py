import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tfl22")


@_attrs_define
class Tfl22:
    """
    Attributes:
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        created_date_time (Union[Unset, datetime.datetime]):
        last_update_date_time (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    last_update_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        description = self.description

        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        last_update_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_date_time, Unset):
            last_update_date_time = self.last_update_date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if last_update_date_time is not UNSET:
            field_dict["lastUpdateDateTime"] = last_update_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _last_update_date_time = d.pop("lastUpdateDateTime", UNSET)
        last_update_date_time: Union[Unset, datetime.datetime]
        if isinstance(_last_update_date_time, Unset):
            last_update_date_time = UNSET
        else:
            last_update_date_time = isoparse(_last_update_date_time)

        tfl_22 = cls(
            id=id,
            description=description,
            created_date_time=created_date_time,
            last_update_date_time=last_update_date_time,
        )

        tfl_22.additional_properties = d
        return tfl_22

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
