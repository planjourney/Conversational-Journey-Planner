from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_10 import Tfl10
    from ..models.tfl_14 import Tfl14
    from ..models.tfl_15 import Tfl15
    from ..models.tfl_16 import Tfl16
    from ..models.tfl_17 import Tfl17


T = TypeVar("T", bound="Tfl18")


@_attrs_define
class Tfl18:
    """
    Attributes:
        naptan_id (Union[Unset, str]):
        platform_name (Union[Unset, str]):
        indicator (Union[Unset, str]): The indicator of the stop point e.g. "Stop K"
        stop_letter (Union[Unset, str]): The stop letter, if it could be cleansed from the Indicator e.g. "K"
        modes (Union[Unset, List[str]]):
        ics_code (Union[Unset, str]):
        sms_code (Union[Unset, str]):
        stop_type (Union[Unset, str]):
        station_naptan (Union[Unset, str]):
        accessibility_summary (Union[Unset, str]):
        hub_naptan_code (Union[Unset, str]):
        lines (Union[Unset, List['Tfl10']]):
        line_group (Union[Unset, List['Tfl14']]):
        line_mode_groups (Union[Unset, List['Tfl15']]):
        full_name (Union[Unset, str]):
        naptan_mode (Union[Unset, str]):
        status (Union[Unset, bool]):
        id (Union[Unset, str]): A unique identifier.
        url (Union[Unset, str]): The unique location of this resource.
        common_name (Union[Unset, str]): A human readable name.
        distance (Union[Unset, float]): The distance of the place from its search point, if this is the result
                        of a geographical search, otherwise zero.
        place_type (Union[Unset, str]): The type of Place. See /Place/Meta/placeTypes for possible values.
        additional_properties (Union[Unset, List['Tfl16']]): A bag of additional key/value pairs with extra information
            about this place.
        children (Union[Unset, List['Tfl17']]):
        children_urls (Union[Unset, List[str]]):
        lat (Union[Unset, float]): WGS84 latitude of the location.
        lon (Union[Unset, float]): WGS84 longitude of the location.
    """

    naptan_id: Union[Unset, str] = UNSET
    platform_name: Union[Unset, str] = UNSET
    indicator: Union[Unset, str] = UNSET
    stop_letter: Union[Unset, str] = UNSET
    modes: Union[Unset, List[str]] = UNSET
    ics_code: Union[Unset, str] = UNSET
    sms_code: Union[Unset, str] = UNSET
    stop_type: Union[Unset, str] = UNSET
    station_naptan: Union[Unset, str] = UNSET
    accessibility_summary: Union[Unset, str] = UNSET
    hub_naptan_code: Union[Unset, str] = UNSET
    lines: Union[Unset, List["Tfl10"]] = UNSET
    line_group: Union[Unset, List["Tfl14"]] = UNSET
    line_mode_groups: Union[Unset, List["Tfl15"]] = UNSET
    full_name: Union[Unset, str] = UNSET
    naptan_mode: Union[Unset, str] = UNSET
    status: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    common_name: Union[Unset, str] = UNSET
    distance: Union[Unset, float] = UNSET
    place_type: Union[Unset, str] = UNSET
    additional_properties: Union[Unset, List["Tfl16"]] = UNSET
    children: Union[Unset, List["Tfl17"]] = UNSET
    children_urls: Union[Unset, List[str]] = UNSET
    lat: Union[Unset, float] = UNSET
    lon: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        naptan_id = self.naptan_id

        platform_name = self.platform_name

        indicator = self.indicator

        stop_letter = self.stop_letter

        modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.modes, Unset):
            modes = self.modes

        ics_code = self.ics_code

        sms_code = self.sms_code

        stop_type = self.stop_type

        station_naptan = self.station_naptan

        accessibility_summary = self.accessibility_summary

        hub_naptan_code = self.hub_naptan_code

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        line_group: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_group, Unset):
            line_group = []
            for line_group_item_data in self.line_group:
                line_group_item = line_group_item_data.to_dict()
                line_group.append(line_group_item)

        line_mode_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_mode_groups, Unset):
            line_mode_groups = []
            for line_mode_groups_item_data in self.line_mode_groups:
                line_mode_groups_item = line_mode_groups_item_data.to_dict()
                line_mode_groups.append(line_mode_groups_item)

        full_name = self.full_name

        naptan_mode = self.naptan_mode

        status = self.status

        id = self.id

        url = self.url

        common_name = self.common_name

        distance = self.distance

        place_type = self.place_type

        additional_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.additional_properties, Unset):
            additional_properties = []
            for additional_properties_item_data in self.additional_properties:
                additional_properties_item = additional_properties_item_data.to_dict()
                additional_properties.append(additional_properties_item)

        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        children_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.children_urls, Unset):
            children_urls = self.children_urls

        lat = self.lat

        lon = self.lon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if naptan_id is not UNSET:
            field_dict["naptanId"] = naptan_id
        if platform_name is not UNSET:
            field_dict["platformName"] = platform_name
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if stop_letter is not UNSET:
            field_dict["stopLetter"] = stop_letter
        if modes is not UNSET:
            field_dict["modes"] = modes
        if ics_code is not UNSET:
            field_dict["icsCode"] = ics_code
        if sms_code is not UNSET:
            field_dict["smsCode"] = sms_code
        if stop_type is not UNSET:
            field_dict["stopType"] = stop_type
        if station_naptan is not UNSET:
            field_dict["stationNaptan"] = station_naptan
        if accessibility_summary is not UNSET:
            field_dict["accessibilitySummary"] = accessibility_summary
        if hub_naptan_code is not UNSET:
            field_dict["hubNaptanCode"] = hub_naptan_code
        if lines is not UNSET:
            field_dict["lines"] = lines
        if line_group is not UNSET:
            field_dict["lineGroup"] = line_group
        if line_mode_groups is not UNSET:
            field_dict["lineModeGroups"] = line_mode_groups
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if naptan_mode is not UNSET:
            field_dict["naptanMode"] = naptan_mode
        if status is not UNSET:
            field_dict["status"] = status
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if distance is not UNSET:
            field_dict["distance"] = distance
        if place_type is not UNSET:
            field_dict["placeType"] = place_type
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties
        if children is not UNSET:
            field_dict["children"] = children
        if children_urls is not UNSET:
            field_dict["childrenUrls"] = children_urls
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_10 import Tfl10
        from ..models.tfl_14 import Tfl14
        from ..models.tfl_15 import Tfl15
        from ..models.tfl_16 import Tfl16
        from ..models.tfl_17 import Tfl17

        d = src_dict.copy()
        naptan_id = d.pop("naptanId", UNSET)

        platform_name = d.pop("platformName", UNSET)

        indicator = d.pop("indicator", UNSET)

        stop_letter = d.pop("stopLetter", UNSET)

        modes = cast(List[str], d.pop("modes", UNSET))

        ics_code = d.pop("icsCode", UNSET)

        sms_code = d.pop("smsCode", UNSET)

        stop_type = d.pop("stopType", UNSET)

        station_naptan = d.pop("stationNaptan", UNSET)

        accessibility_summary = d.pop("accessibilitySummary", UNSET)

        hub_naptan_code = d.pop("hubNaptanCode", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = Tfl10.from_dict(lines_item_data)

            lines.append(lines_item)

        line_group = []
        _line_group = d.pop("lineGroup", UNSET)
        for line_group_item_data in _line_group or []:
            line_group_item = Tfl14.from_dict(line_group_item_data)

            line_group.append(line_group_item)

        line_mode_groups = []
        _line_mode_groups = d.pop("lineModeGroups", UNSET)
        for line_mode_groups_item_data in _line_mode_groups or []:
            line_mode_groups_item = Tfl15.from_dict(line_mode_groups_item_data)

            line_mode_groups.append(line_mode_groups_item)

        full_name = d.pop("fullName", UNSET)

        naptan_mode = d.pop("naptanMode", UNSET)

        status = d.pop("status", UNSET)

        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        common_name = d.pop("commonName", UNSET)

        distance = d.pop("distance", UNSET)

        place_type = d.pop("placeType", UNSET)

        additional_properties = []
        _additional_properties = d.pop("additionalProperties", UNSET)
        for additional_properties_item_data in _additional_properties or []:
            additional_properties_item = Tfl16.from_dict(additional_properties_item_data)

            additional_properties.append(additional_properties_item)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = Tfl17.from_dict(children_item_data)

            children.append(children_item)

        children_urls = cast(List[str], d.pop("childrenUrls", UNSET))

        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        tfl_18 = cls(
            naptan_id=naptan_id,
            platform_name=platform_name,
            indicator=indicator,
            stop_letter=stop_letter,
            modes=modes,
            ics_code=ics_code,
            sms_code=sms_code,
            stop_type=stop_type,
            station_naptan=station_naptan,
            accessibility_summary=accessibility_summary,
            hub_naptan_code=hub_naptan_code,
            lines=lines,
            line_group=line_group,
            line_mode_groups=line_mode_groups,
            full_name=full_name,
            naptan_mode=naptan_mode,
            status=status,
            id=id,
            url=url,
            common_name=common_name,
            distance=distance,
            place_type=place_type,
            additional_properties=additional_properties,
            children=children,
            children_urls=children_urls,
            lat=lat,
            lon=lon,
        )

        tfl_18.additional_properties = d
        return tfl_18

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
