from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_accessibility_preference import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference,
)
from ...models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_bike_proficiency import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuBikeProficiency,
)
from ...models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_cycle_preference import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference,
)
from ...models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_journey_preference import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference,
)
from ...models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_time_is import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs,
)
from ...models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_walking_speed import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed,
)
from ...models.tfl_40 import Tfl40
from ...types import UNSET, Response, Unset


def _get_kwargs(
    from_: str,
    to: str,
    *,
    via: Union[Unset, str] = UNSET,
    national_search: Union[Unset, bool] = UNSET,
    date: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    time_is: Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs] = UNSET,
    journey_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference
    ] = UNSET,
    mode: Union[Unset, List[str]] = UNSET,
    accessibility_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference
    ] = UNSET,
    from_name: Union[Unset, str] = UNSET,
    to_name: Union[Unset, str] = UNSET,
    via_name: Union[Unset, str] = UNSET,
    max_transfer_minutes: Union[Unset, str] = UNSET,
    max_walking_minutes: Union[Unset, str] = UNSET,
    walking_speed: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed
    ] = UNSET,
    cycle_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference
    ] = UNSET,
    adjustment: Union[Unset, str] = UNSET,
    bike_proficiency: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuBikeProficiency
    ] = UNSET,
    alternative_cycle: Union[Unset, bool] = UNSET,
    alternative_walking: Union[Unset, bool] = UNSET,
    apply_html_markup: Union[Unset, bool] = UNSET,
    use_multi_modal_call: Union[Unset, bool] = UNSET,
    walking_optimization: Union[Unset, bool] = UNSET,
    taxi_only_trip: Union[Unset, bool] = UNSET,
    route_between_entrances: Union[Unset, bool] = UNSET,
    use_real_time_live_arrivals: Union[Unset, bool] = UNSET,
    calc_one_direction: Union[Unset, bool] = UNSET,
    include_alternative_routes: Union[Unset, bool] = UNSET,
    override_multi_modal_scenario: Union[Unset, int] = UNSET,
    combine_transfer_legs: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["via"] = via

    params["nationalSearch"] = national_search

    params["date"] = date

    params["time"] = time

    json_time_is: Union[Unset, str] = UNSET
    if not isinstance(time_is, Unset):
        json_time_is = time_is.value

    params["timeIs"] = json_time_is

    json_journey_preference: Union[Unset, str] = UNSET
    if not isinstance(journey_preference, Unset):
        json_journey_preference = journey_preference.value

    params["journeyPreference"] = json_journey_preference

    json_mode: Union[Unset, List[str]] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode

    params["mode"] = json_mode

    json_accessibility_preference: Union[Unset, str] = UNSET
    if not isinstance(accessibility_preference, Unset):
        json_accessibility_preference = accessibility_preference.value

    params["accessibilityPreference"] = json_accessibility_preference

    params["fromName"] = from_name

    params["toName"] = to_name

    params["viaName"] = via_name

    params["maxTransferMinutes"] = max_transfer_minutes

    params["maxWalkingMinutes"] = max_walking_minutes

    json_walking_speed: Union[Unset, str] = UNSET
    if not isinstance(walking_speed, Unset):
        json_walking_speed = walking_speed.value

    params["walkingSpeed"] = json_walking_speed

    json_cycle_preference: Union[Unset, str] = UNSET
    if not isinstance(cycle_preference, Unset):
        json_cycle_preference = cycle_preference.value

    params["cyclePreference"] = json_cycle_preference

    params["adjustment"] = adjustment

    json_bike_proficiency: Union[Unset, str] = UNSET
    if not isinstance(bike_proficiency, Unset):
        json_bike_proficiency = bike_proficiency.value

    params["bikeProficiency"] = json_bike_proficiency

    params["alternativeCycle"] = alternative_cycle

    params["alternativeWalking"] = alternative_walking

    params["applyHtmlMarkup"] = apply_html_markup

    params["useMultiModalCall"] = use_multi_modal_call

    params["walkingOptimization"] = walking_optimization

    params["taxiOnlyTrip"] = taxi_only_trip

    params["routeBetweenEntrances"] = route_between_entrances

    params["useRealTimeLiveArrivals"] = use_real_time_live_arrivals

    params["calcOneDirection"] = calc_one_direction

    params["includeAlternativeRoutes"] = include_alternative_routes

    params["overrideMultiModalScenario"] = override_multi_modal_scenario

    params["combineTransferLegs"] = combine_transfer_legs

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/JourneyResults/{from_}/to/{to}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Tfl40]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Tfl40.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Tfl40]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    from_: str,
    to: str,
    *,
    client: Union[AuthenticatedClient, Client],
    via: Union[Unset, str] = UNSET,
    national_search: Union[Unset, bool] = UNSET,
    date: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    time_is: Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs] = UNSET,
    journey_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference
    ] = UNSET,
    mode: Union[Unset, List[str]] = UNSET,
    accessibility_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference
    ] = UNSET,
    from_name: Union[Unset, str] = UNSET,
    to_name: Union[Unset, str] = UNSET,
    via_name: Union[Unset, str] = UNSET,
    max_transfer_minutes: Union[Unset, str] = UNSET,
    max_walking_minutes: Union[Unset, str] = UNSET,
    walking_speed: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed
    ] = UNSET,
    cycle_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference
    ] = UNSET,
    adjustment: Union[Unset, str] = UNSET,
    bike_proficiency: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuBikeProficiency
    ] = UNSET,
    alternative_cycle: Union[Unset, bool] = UNSET,
    alternative_walking: Union[Unset, bool] = UNSET,
    apply_html_markup: Union[Unset, bool] = UNSET,
    use_multi_modal_call: Union[Unset, bool] = UNSET,
    walking_optimization: Union[Unset, bool] = UNSET,
    taxi_only_trip: Union[Unset, bool] = UNSET,
    route_between_entrances: Union[Unset, bool] = UNSET,
    use_real_time_live_arrivals: Union[Unset, bool] = UNSET,
    calc_one_direction: Union[Unset, bool] = UNSET,
    include_alternative_routes: Union[Unset, bool] = UNSET,
    override_multi_modal_scenario: Union[Unset, int] = UNSET,
    combine_transfer_legs: Union[Unset, bool] = UNSET,
) -> Response[Tfl40]:
    """Perform a Journey Planner search from the parameters specified in simple types

     Perform a Journey Planner search from the parameters specified in simple types

    Args:
        from_ (str):
        to (str):
        via (Union[Unset, str]):
        national_search (Union[Unset, bool]):
        date (Union[Unset, str]):
        time (Union[Unset, str]):
        time_is (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs]):
            Example: Arriving.
        journey_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationa
            lSearchQueryDateQuJourneyPreference]):  Example: LeastInterchange.
        mode (Union[Unset, List[str]]):
        accessibility_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryN
            ationalSearchQueryDateQuAccessibilityPreference]):
        from_name (Union[Unset, str]):
        to_name (Union[Unset, str]):
        via_name (Union[Unset, str]):
        max_transfer_minutes (Union[Unset, str]):
        max_walking_minutes (Union[Unset, str]):
        walking_speed (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed]):
        cycle_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuCyclePreference]):
        adjustment (Union[Unset, str]):
        bike_proficiency (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuBikeProficiency]):
        alternative_cycle (Union[Unset, bool]):
        alternative_walking (Union[Unset, bool]):
        apply_html_markup (Union[Unset, bool]):
        use_multi_modal_call (Union[Unset, bool]):
        walking_optimization (Union[Unset, bool]):
        taxi_only_trip (Union[Unset, bool]):
        route_between_entrances (Union[Unset, bool]):
        use_real_time_live_arrivals (Union[Unset, bool]):
        calc_one_direction (Union[Unset, bool]):
        include_alternative_routes (Union[Unset, bool]):
        override_multi_modal_scenario (Union[Unset, int]):
        combine_transfer_legs (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tfl40]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        via=via,
        national_search=national_search,
        date=date,
        time=time,
        time_is=time_is,
        journey_preference=journey_preference,
        mode=mode,
        accessibility_preference=accessibility_preference,
        from_name=from_name,
        to_name=to_name,
        via_name=via_name,
        max_transfer_minutes=max_transfer_minutes,
        max_walking_minutes=max_walking_minutes,
        walking_speed=walking_speed,
        cycle_preference=cycle_preference,
        adjustment=adjustment,
        bike_proficiency=bike_proficiency,
        alternative_cycle=alternative_cycle,
        alternative_walking=alternative_walking,
        apply_html_markup=apply_html_markup,
        use_multi_modal_call=use_multi_modal_call,
        walking_optimization=walking_optimization,
        taxi_only_trip=taxi_only_trip,
        route_between_entrances=route_between_entrances,
        use_real_time_live_arrivals=use_real_time_live_arrivals,
        calc_one_direction=calc_one_direction,
        include_alternative_routes=include_alternative_routes,
        override_multi_modal_scenario=override_multi_modal_scenario,
        combine_transfer_legs=combine_transfer_legs,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    from_: str,
    to: str,
    *,
    client: Union[AuthenticatedClient, Client],
    via: Union[Unset, str] = UNSET,
    national_search: Union[Unset, bool] = UNSET,
    date: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    time_is: Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs] = UNSET,
    journey_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference
    ] = UNSET,
    mode: Union[Unset, List[str]] = UNSET,
    accessibility_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference
    ] = UNSET,
    from_name: Union[Unset, str] = UNSET,
    to_name: Union[Unset, str] = UNSET,
    via_name: Union[Unset, str] = UNSET,
    max_transfer_minutes: Union[Unset, str] = UNSET,
    max_walking_minutes: Union[Unset, str] = UNSET,
    walking_speed: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed
    ] = UNSET,
    cycle_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference
    ] = UNSET,
    adjustment: Union[Unset, str] = UNSET,
    bike_proficiency: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuBikeProficiency
    ] = UNSET,
    alternative_cycle: Union[Unset, bool] = UNSET,
    alternative_walking: Union[Unset, bool] = UNSET,
    apply_html_markup: Union[Unset, bool] = UNSET,
    use_multi_modal_call: Union[Unset, bool] = UNSET,
    walking_optimization: Union[Unset, bool] = UNSET,
    taxi_only_trip: Union[Unset, bool] = UNSET,
    route_between_entrances: Union[Unset, bool] = UNSET,
    use_real_time_live_arrivals: Union[Unset, bool] = UNSET,
    calc_one_direction: Union[Unset, bool] = UNSET,
    include_alternative_routes: Union[Unset, bool] = UNSET,
    override_multi_modal_scenario: Union[Unset, int] = UNSET,
    combine_transfer_legs: Union[Unset, bool] = UNSET,
) -> Optional[Tfl40]:
    """Perform a Journey Planner search from the parameters specified in simple types

     Perform a Journey Planner search from the parameters specified in simple types

    Args:
        from_ (str):
        to (str):
        via (Union[Unset, str]):
        national_search (Union[Unset, bool]):
        date (Union[Unset, str]):
        time (Union[Unset, str]):
        time_is (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs]):
            Example: Arriving.
        journey_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationa
            lSearchQueryDateQuJourneyPreference]):  Example: LeastInterchange.
        mode (Union[Unset, List[str]]):
        accessibility_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryN
            ationalSearchQueryDateQuAccessibilityPreference]):
        from_name (Union[Unset, str]):
        to_name (Union[Unset, str]):
        via_name (Union[Unset, str]):
        max_transfer_minutes (Union[Unset, str]):
        max_walking_minutes (Union[Unset, str]):
        walking_speed (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed]):
        cycle_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuCyclePreference]):
        adjustment (Union[Unset, str]):
        bike_proficiency (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuBikeProficiency]):
        alternative_cycle (Union[Unset, bool]):
        alternative_walking (Union[Unset, bool]):
        apply_html_markup (Union[Unset, bool]):
        use_multi_modal_call (Union[Unset, bool]):
        walking_optimization (Union[Unset, bool]):
        taxi_only_trip (Union[Unset, bool]):
        route_between_entrances (Union[Unset, bool]):
        use_real_time_live_arrivals (Union[Unset, bool]):
        calc_one_direction (Union[Unset, bool]):
        include_alternative_routes (Union[Unset, bool]):
        override_multi_modal_scenario (Union[Unset, int]):
        combine_transfer_legs (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tfl40
    """

    return sync_detailed(
        from_=from_,
        to=to,
        client=client,
        via=via,
        national_search=national_search,
        date=date,
        time=time,
        time_is=time_is,
        journey_preference=journey_preference,
        mode=mode,
        accessibility_preference=accessibility_preference,
        from_name=from_name,
        to_name=to_name,
        via_name=via_name,
        max_transfer_minutes=max_transfer_minutes,
        max_walking_minutes=max_walking_minutes,
        walking_speed=walking_speed,
        cycle_preference=cycle_preference,
        adjustment=adjustment,
        bike_proficiency=bike_proficiency,
        alternative_cycle=alternative_cycle,
        alternative_walking=alternative_walking,
        apply_html_markup=apply_html_markup,
        use_multi_modal_call=use_multi_modal_call,
        walking_optimization=walking_optimization,
        taxi_only_trip=taxi_only_trip,
        route_between_entrances=route_between_entrances,
        use_real_time_live_arrivals=use_real_time_live_arrivals,
        calc_one_direction=calc_one_direction,
        include_alternative_routes=include_alternative_routes,
        override_multi_modal_scenario=override_multi_modal_scenario,
        combine_transfer_legs=combine_transfer_legs,
    ).parsed


async def asyncio_detailed(
    from_: str,
    to: str,
    *,
    client: Union[AuthenticatedClient, Client],
    via: Union[Unset, str] = UNSET,
    national_search: Union[Unset, bool] = UNSET,
    date: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    time_is: Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs] = UNSET,
    journey_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference
    ] = UNSET,
    mode: Union[Unset, List[str]] = UNSET,
    accessibility_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference
    ] = UNSET,
    from_name: Union[Unset, str] = UNSET,
    to_name: Union[Unset, str] = UNSET,
    via_name: Union[Unset, str] = UNSET,
    max_transfer_minutes: Union[Unset, str] = UNSET,
    max_walking_minutes: Union[Unset, str] = UNSET,
    walking_speed: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed
    ] = UNSET,
    cycle_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference
    ] = UNSET,
    adjustment: Union[Unset, str] = UNSET,
    bike_proficiency: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuBikeProficiency
    ] = UNSET,
    alternative_cycle: Union[Unset, bool] = UNSET,
    alternative_walking: Union[Unset, bool] = UNSET,
    apply_html_markup: Union[Unset, bool] = UNSET,
    use_multi_modal_call: Union[Unset, bool] = UNSET,
    walking_optimization: Union[Unset, bool] = UNSET,
    taxi_only_trip: Union[Unset, bool] = UNSET,
    route_between_entrances: Union[Unset, bool] = UNSET,
    use_real_time_live_arrivals: Union[Unset, bool] = UNSET,
    calc_one_direction: Union[Unset, bool] = UNSET,
    include_alternative_routes: Union[Unset, bool] = UNSET,
    override_multi_modal_scenario: Union[Unset, int] = UNSET,
    combine_transfer_legs: Union[Unset, bool] = UNSET,
) -> Response[Tfl40]:
    """Perform a Journey Planner search from the parameters specified in simple types

     Perform a Journey Planner search from the parameters specified in simple types

    Args:
        from_ (str):
        to (str):
        via (Union[Unset, str]):
        national_search (Union[Unset, bool]):
        date (Union[Unset, str]):
        time (Union[Unset, str]):
        time_is (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs]):
            Example: Arriving.
        journey_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationa
            lSearchQueryDateQuJourneyPreference]):  Example: LeastInterchange.
        mode (Union[Unset, List[str]]):
        accessibility_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryN
            ationalSearchQueryDateQuAccessibilityPreference]):
        from_name (Union[Unset, str]):
        to_name (Union[Unset, str]):
        via_name (Union[Unset, str]):
        max_transfer_minutes (Union[Unset, str]):
        max_walking_minutes (Union[Unset, str]):
        walking_speed (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed]):
        cycle_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuCyclePreference]):
        adjustment (Union[Unset, str]):
        bike_proficiency (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuBikeProficiency]):
        alternative_cycle (Union[Unset, bool]):
        alternative_walking (Union[Unset, bool]):
        apply_html_markup (Union[Unset, bool]):
        use_multi_modal_call (Union[Unset, bool]):
        walking_optimization (Union[Unset, bool]):
        taxi_only_trip (Union[Unset, bool]):
        route_between_entrances (Union[Unset, bool]):
        use_real_time_live_arrivals (Union[Unset, bool]):
        calc_one_direction (Union[Unset, bool]):
        include_alternative_routes (Union[Unset, bool]):
        override_multi_modal_scenario (Union[Unset, int]):
        combine_transfer_legs (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Tfl40]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        via=via,
        national_search=national_search,
        date=date,
        time=time,
        time_is=time_is,
        journey_preference=journey_preference,
        mode=mode,
        accessibility_preference=accessibility_preference,
        from_name=from_name,
        to_name=to_name,
        via_name=via_name,
        max_transfer_minutes=max_transfer_minutes,
        max_walking_minutes=max_walking_minutes,
        walking_speed=walking_speed,
        cycle_preference=cycle_preference,
        adjustment=adjustment,
        bike_proficiency=bike_proficiency,
        alternative_cycle=alternative_cycle,
        alternative_walking=alternative_walking,
        apply_html_markup=apply_html_markup,
        use_multi_modal_call=use_multi_modal_call,
        walking_optimization=walking_optimization,
        taxi_only_trip=taxi_only_trip,
        route_between_entrances=route_between_entrances,
        use_real_time_live_arrivals=use_real_time_live_arrivals,
        calc_one_direction=calc_one_direction,
        include_alternative_routes=include_alternative_routes,
        override_multi_modal_scenario=override_multi_modal_scenario,
        combine_transfer_legs=combine_transfer_legs,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    from_: str,
    to: str,
    *,
    client: Union[AuthenticatedClient, Client],
    via: Union[Unset, str] = UNSET,
    national_search: Union[Unset, bool] = UNSET,
    date: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    time_is: Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs] = UNSET,
    journey_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference
    ] = UNSET,
    mode: Union[Unset, List[str]] = UNSET,
    accessibility_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference
    ] = UNSET,
    from_name: Union[Unset, str] = UNSET,
    to_name: Union[Unset, str] = UNSET,
    via_name: Union[Unset, str] = UNSET,
    max_transfer_minutes: Union[Unset, str] = UNSET,
    max_walking_minutes: Union[Unset, str] = UNSET,
    walking_speed: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed
    ] = UNSET,
    cycle_preference: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference
    ] = UNSET,
    adjustment: Union[Unset, str] = UNSET,
    bike_proficiency: Union[
        Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuBikeProficiency
    ] = UNSET,
    alternative_cycle: Union[Unset, bool] = UNSET,
    alternative_walking: Union[Unset, bool] = UNSET,
    apply_html_markup: Union[Unset, bool] = UNSET,
    use_multi_modal_call: Union[Unset, bool] = UNSET,
    walking_optimization: Union[Unset, bool] = UNSET,
    taxi_only_trip: Union[Unset, bool] = UNSET,
    route_between_entrances: Union[Unset, bool] = UNSET,
    use_real_time_live_arrivals: Union[Unset, bool] = UNSET,
    calc_one_direction: Union[Unset, bool] = UNSET,
    include_alternative_routes: Union[Unset, bool] = UNSET,
    override_multi_modal_scenario: Union[Unset, int] = UNSET,
    combine_transfer_legs: Union[Unset, bool] = UNSET,
) -> Optional[Tfl40]:
    """Perform a Journey Planner search from the parameters specified in simple types

     Perform a Journey Planner search from the parameters specified in simple types

    Args:
        from_ (str):
        to (str):
        via (Union[Unset, str]):
        national_search (Union[Unset, bool]):
        date (Union[Unset, str]):
        time (Union[Unset, str]):
        time_is (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs]):
            Example: Arriving.
        journey_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationa
            lSearchQueryDateQuJourneyPreference]):  Example: LeastInterchange.
        mode (Union[Unset, List[str]]):
        accessibility_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryN
            ationalSearchQueryDateQuAccessibilityPreference]):
        from_name (Union[Unset, str]):
        to_name (Union[Unset, str]):
        via_name (Union[Unset, str]):
        max_transfer_minutes (Union[Unset, str]):
        max_walking_minutes (Union[Unset, str]):
        walking_speed (Union[Unset,
            JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed]):
        cycle_preference (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuCyclePreference]):
        adjustment (Union[Unset, str]):
        bike_proficiency (Union[Unset, JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalS
            earchQueryDateQuBikeProficiency]):
        alternative_cycle (Union[Unset, bool]):
        alternative_walking (Union[Unset, bool]):
        apply_html_markup (Union[Unset, bool]):
        use_multi_modal_call (Union[Unset, bool]):
        walking_optimization (Union[Unset, bool]):
        taxi_only_trip (Union[Unset, bool]):
        route_between_entrances (Union[Unset, bool]):
        use_real_time_live_arrivals (Union[Unset, bool]):
        calc_one_direction (Union[Unset, bool]):
        include_alternative_routes (Union[Unset, bool]):
        override_multi_modal_scenario (Union[Unset, int]):
        combine_transfer_legs (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Tfl40
    """

    return (
        await asyncio_detailed(
            from_=from_,
            to=to,
            client=client,
            via=via,
            national_search=national_search,
            date=date,
            time=time,
            time_is=time_is,
            journey_preference=journey_preference,
            mode=mode,
            accessibility_preference=accessibility_preference,
            from_name=from_name,
            to_name=to_name,
            via_name=via_name,
            max_transfer_minutes=max_transfer_minutes,
            max_walking_minutes=max_walking_minutes,
            walking_speed=walking_speed,
            cycle_preference=cycle_preference,
            adjustment=adjustment,
            bike_proficiency=bike_proficiency,
            alternative_cycle=alternative_cycle,
            alternative_walking=alternative_walking,
            apply_html_markup=apply_html_markup,
            use_multi_modal_call=use_multi_modal_call,
            walking_optimization=walking_optimization,
            taxi_only_trip=taxi_only_trip,
            route_between_entrances=route_between_entrances,
            use_real_time_live_arrivals=use_real_time_live_arrivals,
            calc_one_direction=calc_one_direction,
            include_alternative_routes=include_alternative_routes,
            override_multi_modal_scenario=override_multi_modal_scenario,
            combine_transfer_legs=combine_transfer_legs,
        )
    ).parsed
