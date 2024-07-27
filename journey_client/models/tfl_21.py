import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tfl_21_category import Tfl21Category
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_18 import Tfl18
    from ..models.tfl_20 import Tfl20


T = TypeVar("T", bound="Tfl21")


@_attrs_define
class Tfl21:
    """Represents a disruption to a route within the transport network.

    Attributes:
        category (Union[Unset, Tfl21Category]): Gets or sets the category of this dispruption.
        type (Union[Unset, str]): Gets or sets the disruption type of this dispruption.
        category_description (Union[Unset, str]): Gets or sets the description of the category.
        description (Union[Unset, str]): Gets or sets the description of this disruption.
        summary (Union[Unset, str]): Gets or sets the summary of this disruption.
        additional_info (Union[Unset, str]): Gets or sets the additionaInfo of this disruption.
        created (Union[Unset, datetime.datetime]): Gets or sets the date/time when this disruption was created.
        last_update (Union[Unset, datetime.datetime]): Gets or sets the date/time when this disruption was last updated.
        affected_routes (Union[Unset, List['Tfl20']]): Gets or sets the routes affected by this disruption
        affected_stops (Union[Unset, List['Tfl18']]): Gets or sets the stops affected by this disruption
        closure_text (Union[Unset, str]): Text describing the closure type
    """

    category: Union[Unset, Tfl21Category] = UNSET
    type: Union[Unset, str] = UNSET
    category_description: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_info: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    last_update: Union[Unset, datetime.datetime] = UNSET
    affected_routes: Union[Unset, List["Tfl20"]] = UNSET
    affected_stops: Union[Unset, List["Tfl18"]] = UNSET
    closure_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        type = self.type

        category_description = self.category_description

        description = self.description

        summary = self.summary

        additional_info = self.additional_info

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        last_update: Union[Unset, str] = UNSET
        if not isinstance(self.last_update, Unset):
            last_update = self.last_update.isoformat()

        affected_routes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affected_routes, Unset):
            affected_routes = []
            for affected_routes_item_data in self.affected_routes:
                affected_routes_item = affected_routes_item_data.to_dict()
                affected_routes.append(affected_routes_item)

        affected_stops: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affected_stops, Unset):
            affected_stops = []
            for affected_stops_item_data in self.affected_stops:
                affected_stops_item = affected_stops_item_data.to_dict()
                affected_stops.append(affected_stops_item)

        closure_text = self.closure_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if type is not UNSET:
            field_dict["type"] = type
        if category_description is not UNSET:
            field_dict["categoryDescription"] = category_description
        if description is not UNSET:
            field_dict["description"] = description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if additional_info is not UNSET:
            field_dict["additionalInfo"] = additional_info
        if created is not UNSET:
            field_dict["created"] = created
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update
        if affected_routes is not UNSET:
            field_dict["affectedRoutes"] = affected_routes
        if affected_stops is not UNSET:
            field_dict["affectedStops"] = affected_stops
        if closure_text is not UNSET:
            field_dict["closureText"] = closure_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_18 import Tfl18
        from ..models.tfl_20 import Tfl20

        d = src_dict.copy()
        _category = d.pop("category", UNSET)
        category: Union[Unset, Tfl21Category]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Tfl21Category(_category)

        type = d.pop("type", UNSET)

        category_description = d.pop("categoryDescription", UNSET)

        description = d.pop("description", UNSET)

        summary = d.pop("summary", UNSET)

        additional_info = d.pop("additionalInfo", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _last_update = d.pop("lastUpdate", UNSET)
        last_update: Union[Unset, datetime.datetime]
        if isinstance(_last_update, Unset):
            last_update = UNSET
        else:
            last_update = isoparse(_last_update)

        affected_routes = []
        _affected_routes = d.pop("affectedRoutes", UNSET)
        for affected_routes_item_data in _affected_routes or []:
            affected_routes_item = Tfl20.from_dict(affected_routes_item_data)

            affected_routes.append(affected_routes_item)

        affected_stops = []
        _affected_stops = d.pop("affectedStops", UNSET)
        for affected_stops_item_data in _affected_stops or []:
            affected_stops_item = Tfl18.from_dict(affected_stops_item_data)

            affected_stops.append(affected_stops_item)

        closure_text = d.pop("closureText", UNSET)

        tfl_21 = cls(
            category=category,
            type=type,
            category_description=category_description,
            description=description,
            summary=summary,
            additional_info=additional_info,
            created=created,
            last_update=last_update,
            affected_routes=affected_routes,
            affected_stops=affected_stops,
            closure_text=closure_text,
        )

        tfl_21.additional_properties = d
        return tfl_21

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
