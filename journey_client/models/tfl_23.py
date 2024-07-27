import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tfl_4 import Tfl4
    from ..models.tfl_5 import Tfl5
    from ..models.tfl_6 import Tfl6
    from ..models.tfl_10 import Tfl10
    from ..models.tfl_12 import Tfl12
    from ..models.tfl_13 import Tfl13
    from ..models.tfl_21 import Tfl21
    from ..models.tfl_22 import Tfl22


T = TypeVar("T", bound="Tfl23")


@_attrs_define
class Tfl23:
    """
    Attributes:
        duration (Union[Unset, int]):
        speed (Union[Unset, str]):
        instruction (Union[Unset, Tfl4]):
        obstacles (Union[Unset, List['Tfl5']]):
        departure_time (Union[Unset, datetime.datetime]):
        arrival_time (Union[Unset, datetime.datetime]):
        departure_point (Union[Unset, Tfl6]): Represents a point located at a latitude and longitude using the WGS84 co-
            ordinate system.
        arrival_point (Union[Unset, Tfl6]): Represents a point located at a latitude and longitude using the WGS84 co-
            ordinate system.
        path (Union[Unset, Tfl12]):
        route_options (Union[Unset, List['Tfl13']]):
        mode (Union[Unset, Tfl10]):
        disruptions (Union[Unset, List['Tfl21']]):
        planned_works (Union[Unset, List['Tfl22']]):
        distance (Union[Unset, float]):
        is_disrupted (Union[Unset, bool]):
        has_fixed_locations (Union[Unset, bool]):
    """

    duration: Union[Unset, int] = UNSET
    speed: Union[Unset, str] = UNSET
    instruction: Union[Unset, "Tfl4"] = UNSET
    obstacles: Union[Unset, List["Tfl5"]] = UNSET
    departure_time: Union[Unset, datetime.datetime] = UNSET
    arrival_time: Union[Unset, datetime.datetime] = UNSET
    departure_point: Union[Unset, "Tfl6"] = UNSET
    arrival_point: Union[Unset, "Tfl6"] = UNSET
    path: Union[Unset, "Tfl12"] = UNSET
    route_options: Union[Unset, List["Tfl13"]] = UNSET
    mode: Union[Unset, "Tfl10"] = UNSET
    disruptions: Union[Unset, List["Tfl21"]] = UNSET
    planned_works: Union[Unset, List["Tfl22"]] = UNSET
    distance: Union[Unset, float] = UNSET
    is_disrupted: Union[Unset, bool] = UNSET
    has_fixed_locations: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration = self.duration

        speed = self.speed

        instruction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instruction, Unset):
            instruction = self.instruction.to_dict()

        obstacles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.obstacles, Unset):
            obstacles = []
            for obstacles_item_data in self.obstacles:
                obstacles_item = obstacles_item_data.to_dict()
                obstacles.append(obstacles_item)

        departure_time: Union[Unset, str] = UNSET
        if not isinstance(self.departure_time, Unset):
            departure_time = self.departure_time.isoformat()

        arrival_time: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_time, Unset):
            arrival_time = self.arrival_time.isoformat()

        departure_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.departure_point, Unset):
            departure_point = self.departure_point.to_dict()

        arrival_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arrival_point, Unset):
            arrival_point = self.arrival_point.to_dict()

        path: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        route_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.route_options, Unset):
            route_options = []
            for route_options_item_data in self.route_options:
                route_options_item = route_options_item_data.to_dict()
                route_options.append(route_options_item)

        mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.to_dict()

        disruptions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.disruptions, Unset):
            disruptions = []
            for disruptions_item_data in self.disruptions:
                disruptions_item = disruptions_item_data.to_dict()
                disruptions.append(disruptions_item)

        planned_works: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.planned_works, Unset):
            planned_works = []
            for planned_works_item_data in self.planned_works:
                planned_works_item = planned_works_item_data.to_dict()
                planned_works.append(planned_works_item)

        distance = self.distance

        is_disrupted = self.is_disrupted

        has_fixed_locations = self.has_fixed_locations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if speed is not UNSET:
            field_dict["speed"] = speed
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if obstacles is not UNSET:
            field_dict["obstacles"] = obstacles
        if departure_time is not UNSET:
            field_dict["departureTime"] = departure_time
        if arrival_time is not UNSET:
            field_dict["arrivalTime"] = arrival_time
        if departure_point is not UNSET:
            field_dict["departurePoint"] = departure_point
        if arrival_point is not UNSET:
            field_dict["arrivalPoint"] = arrival_point
        if path is not UNSET:
            field_dict["path"] = path
        if route_options is not UNSET:
            field_dict["routeOptions"] = route_options
        if mode is not UNSET:
            field_dict["mode"] = mode
        if disruptions is not UNSET:
            field_dict["disruptions"] = disruptions
        if planned_works is not UNSET:
            field_dict["plannedWorks"] = planned_works
        if distance is not UNSET:
            field_dict["distance"] = distance
        if is_disrupted is not UNSET:
            field_dict["isDisrupted"] = is_disrupted
        if has_fixed_locations is not UNSET:
            field_dict["hasFixedLocations"] = has_fixed_locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tfl_4 import Tfl4
        from ..models.tfl_5 import Tfl5
        from ..models.tfl_6 import Tfl6
        from ..models.tfl_10 import Tfl10
        from ..models.tfl_12 import Tfl12
        from ..models.tfl_13 import Tfl13
        from ..models.tfl_21 import Tfl21
        from ..models.tfl_22 import Tfl22

        d = src_dict.copy()
        duration = d.pop("duration", UNSET)

        speed = d.pop("speed", UNSET)

        _instruction = d.pop("instruction", UNSET)
        instruction: Union[Unset, Tfl4]
        if isinstance(_instruction, Unset):
            instruction = UNSET
        else:
            instruction = Tfl4.from_dict(_instruction)

        obstacles = []
        _obstacles = d.pop("obstacles", UNSET)
        for obstacles_item_data in _obstacles or []:
            obstacles_item = Tfl5.from_dict(obstacles_item_data)

            obstacles.append(obstacles_item)

        _departure_time = d.pop("departureTime", UNSET)
        departure_time: Union[Unset, datetime.datetime]
        if isinstance(_departure_time, Unset):
            departure_time = UNSET
        else:
            departure_time = isoparse(_departure_time)

        _arrival_time = d.pop("arrivalTime", UNSET)
        arrival_time: Union[Unset, datetime.datetime]
        if isinstance(_arrival_time, Unset):
            arrival_time = UNSET
        else:
            arrival_time = isoparse(_arrival_time)

        _departure_point = d.pop("departurePoint", UNSET)
        departure_point: Union[Unset, Tfl6]
        if isinstance(_departure_point, Unset):
            departure_point = UNSET
        else:
            departure_point = Tfl6.from_dict(_departure_point)

        _arrival_point = d.pop("arrivalPoint", UNSET)
        arrival_point: Union[Unset, Tfl6]
        if isinstance(_arrival_point, Unset):
            arrival_point = UNSET
        else:
            arrival_point = Tfl6.from_dict(_arrival_point)

        _path = d.pop("path", UNSET)
        path: Union[Unset, Tfl12]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = Tfl12.from_dict(_path)

        route_options = []
        _route_options = d.pop("routeOptions", UNSET)
        for route_options_item_data in _route_options or []:
            route_options_item = Tfl13.from_dict(route_options_item_data)

            route_options.append(route_options_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, Tfl10]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = Tfl10.from_dict(_mode)

        disruptions = []
        _disruptions = d.pop("disruptions", UNSET)
        for disruptions_item_data in _disruptions or []:
            disruptions_item = Tfl21.from_dict(disruptions_item_data)

            disruptions.append(disruptions_item)

        planned_works = []
        _planned_works = d.pop("plannedWorks", UNSET)
        for planned_works_item_data in _planned_works or []:
            planned_works_item = Tfl22.from_dict(planned_works_item_data)

            planned_works.append(planned_works_item)

        distance = d.pop("distance", UNSET)

        is_disrupted = d.pop("isDisrupted", UNSET)

        has_fixed_locations = d.pop("hasFixedLocations", UNSET)

        tfl_23 = cls(
            duration=duration,
            speed=speed,
            instruction=instruction,
            obstacles=obstacles,
            departure_time=departure_time,
            arrival_time=arrival_time,
            departure_point=departure_point,
            arrival_point=arrival_point,
            path=path,
            route_options=route_options,
            mode=mode,
            disruptions=disruptions,
            planned_works=planned_works,
            distance=distance,
            is_disrupted=is_disrupted,
            has_fixed_locations=has_fixed_locations,
        )

        tfl_23.additional_properties = d
        return tfl_23

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
