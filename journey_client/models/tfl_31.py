import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_21 import Tfl21
    from ..models.tfl_30 import Tfl30


T = TypeVar("T", bound="Tfl31")


@_attrs_define
class Tfl31:
    """
    Attributes:
        id (Union[Unset, int]):
        line_id (Union[Unset, str]):
        status_severity (Union[Unset, int]):
        status_severity_description (Union[Unset, str]):
        reason (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        modified (Union[Unset, datetime.datetime]):
        validity_periods (Union[Unset, List['Tfl30']]):
        disruption (Union[Unset, Tfl21]): Represents a disruption to a route within the transport network.
    """

    id: Union[Unset, int] = UNSET
    line_id: Union[Unset, str] = UNSET
    status_severity: Union[Unset, int] = UNSET
    status_severity_description: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    validity_periods: Union[Unset, List["Tfl30"]] = UNSET
    disruption: Union[Unset, "Tfl21"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        line_id = self.line_id

        status_severity = self.status_severity

        status_severity_description = self.status_severity_description

        reason = self.reason

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        validity_periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validity_periods, Unset):
            validity_periods = []
            for validity_periods_item_data in self.validity_periods:
                validity_periods_item = validity_periods_item_data.to_dict()
                validity_periods.append(validity_periods_item)

        disruption: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disruption, Unset):
            disruption = self.disruption.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if line_id is not UNSET:
            field_dict["lineId"] = line_id
        if status_severity is not UNSET:
            field_dict["statusSeverity"] = status_severity
        if status_severity_description is not UNSET:
            field_dict["statusSeverityDescription"] = status_severity_description
        if reason is not UNSET:
            field_dict["reason"] = reason
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if validity_periods is not UNSET:
            field_dict["validityPeriods"] = validity_periods
        if disruption is not UNSET:
            field_dict["disruption"] = disruption

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_21 import Tfl21
        from ..models.tfl_30 import Tfl30

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        line_id = d.pop("lineId", UNSET)

        status_severity = d.pop("statusSeverity", UNSET)

        status_severity_description = d.pop("statusSeverityDescription", UNSET)

        reason = d.pop("reason", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        validity_periods = []
        _validity_periods = d.pop("validityPeriods", UNSET)
        for validity_periods_item_data in _validity_periods or []:
            validity_periods_item = Tfl30.from_dict(validity_periods_item_data)

            validity_periods.append(validity_periods_item)

        _disruption = d.pop("disruption", UNSET)
        disruption: Union[Unset, Tfl21]
        if isinstance(_disruption, Unset):
            disruption = UNSET
        else:
            disruption = Tfl21.from_dict(_disruption)

        tfl_31 = cls(
            id=id,
            line_id=line_id,
            status_severity=status_severity,
            status_severity_description=status_severity_description,
            reason=reason,
            created=created,
            modified=modified,
            validity_periods=validity_periods,
            disruption=disruption,
        )

        tfl_31.additional_properties = d
        return tfl_31

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
