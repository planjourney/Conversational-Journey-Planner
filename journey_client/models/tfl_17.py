from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_16 import Tfl16


T = TypeVar("T", bound="Tfl17")


@_attrs_define
class Tfl17:
    """
    Attributes:
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
        from ..models.tfl_16 import Tfl16

        d = src_dict.copy()
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

        tfl_17 = cls(
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

        tfl_17.additional_properties = d
        return tfl_17

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
