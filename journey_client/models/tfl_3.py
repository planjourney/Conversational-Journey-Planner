from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tfl_3_sky_direction_description import Tfl3SkyDirectionDescription
from ..models.tfl_3_track_type import Tfl3TrackType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_2 import Tfl2


T = TypeVar("T", bound="Tfl3")


@_attrs_define
class Tfl3:
    """
    Attributes:
        description (Union[Unset, str]):
        turn_direction (Union[Unset, str]):
        street_name (Union[Unset, str]):
        distance (Union[Unset, int]):
        cumulative_distance (Union[Unset, int]):
        sky_direction (Union[Unset, int]):
        sky_direction_description (Union[Unset, Tfl3SkyDirectionDescription]):
        cumulative_travel_time (Union[Unset, int]):
        latitude (Union[Unset, float]):
        longitude (Union[Unset, float]):
        path_attribute (Union[Unset, Tfl2]):
        description_heading (Union[Unset, str]):
        track_type (Union[Unset, Tfl3TrackType]):
    """

    description: Union[Unset, str] = UNSET
    turn_direction: Union[Unset, str] = UNSET
    street_name: Union[Unset, str] = UNSET
    distance: Union[Unset, int] = UNSET
    cumulative_distance: Union[Unset, int] = UNSET
    sky_direction: Union[Unset, int] = UNSET
    sky_direction_description: Union[Unset, Tfl3SkyDirectionDescription] = UNSET
    cumulative_travel_time: Union[Unset, int] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    path_attribute: Union[Unset, "Tfl2"] = UNSET
    description_heading: Union[Unset, str] = UNSET
    track_type: Union[Unset, Tfl3TrackType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        turn_direction = self.turn_direction

        street_name = self.street_name

        distance = self.distance

        cumulative_distance = self.cumulative_distance

        sky_direction = self.sky_direction

        sky_direction_description: Union[Unset, str] = UNSET
        if not isinstance(self.sky_direction_description, Unset):
            sky_direction_description = self.sky_direction_description.value

        cumulative_travel_time = self.cumulative_travel_time

        latitude = self.latitude

        longitude = self.longitude

        path_attribute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.path_attribute, Unset):
            path_attribute = self.path_attribute.to_dict()

        description_heading = self.description_heading

        track_type: Union[Unset, str] = UNSET
        if not isinstance(self.track_type, Unset):
            track_type = self.track_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if turn_direction is not UNSET:
            field_dict["turnDirection"] = turn_direction
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if distance is not UNSET:
            field_dict["distance"] = distance
        if cumulative_distance is not UNSET:
            field_dict["cumulativeDistance"] = cumulative_distance
        if sky_direction is not UNSET:
            field_dict["skyDirection"] = sky_direction
        if sky_direction_description is not UNSET:
            field_dict["skyDirectionDescription"] = sky_direction_description
        if cumulative_travel_time is not UNSET:
            field_dict["cumulativeTravelTime"] = cumulative_travel_time
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if path_attribute is not UNSET:
            field_dict["pathAttribute"] = path_attribute
        if description_heading is not UNSET:
            field_dict["descriptionHeading"] = description_heading
        if track_type is not UNSET:
            field_dict["trackType"] = track_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_2 import Tfl2

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        turn_direction = d.pop("turnDirection", UNSET)

        street_name = d.pop("streetName", UNSET)

        distance = d.pop("distance", UNSET)

        cumulative_distance = d.pop("cumulativeDistance", UNSET)

        sky_direction = d.pop("skyDirection", UNSET)

        _sky_direction_description = d.pop("skyDirectionDescription", UNSET)
        sky_direction_description: Union[Unset, Tfl3SkyDirectionDescription]
        if isinstance(_sky_direction_description, Unset):
            sky_direction_description = UNSET
        else:
            sky_direction_description = Tfl3SkyDirectionDescription(_sky_direction_description)

        cumulative_travel_time = d.pop("cumulativeTravelTime", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        _path_attribute = d.pop("pathAttribute", UNSET)
        path_attribute: Union[Unset, Tfl2]
        if isinstance(_path_attribute, Unset):
            path_attribute = UNSET
        else:
            path_attribute = Tfl2.from_dict(_path_attribute)

        description_heading = d.pop("descriptionHeading", UNSET)

        _track_type = d.pop("trackType", UNSET)
        track_type: Union[Unset, Tfl3TrackType]
        if isinstance(_track_type, Unset):
            track_type = UNSET
        else:
            track_type = Tfl3TrackType(_track_type)

        tfl_3 = cls(
            description=description,
            turn_direction=turn_direction,
            street_name=street_name,
            distance=distance,
            cumulative_distance=cumulative_distance,
            sky_direction=sky_direction,
            sky_direction_description=sky_direction_description,
            cumulative_travel_time=cumulative_travel_time,
            latitude=latitude,
            longitude=longitude,
            path_attribute=path_attribute,
            description_heading=description_heading,
            track_type=track_type,
        )

        tfl_3.additional_properties = d
        return tfl_3

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
