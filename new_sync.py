#!/usr/bin/env python
# coding: utf-8

# In[3]:


from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

from journey_client.api.journey.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu import (
    sync_detailed as original_sync_detailed,
)
from journey_client.client import AuthenticatedClient, Client
from journey_client.models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_accessibility_preference import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuAccessibilityPreference,
)
from journey_client.models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_bike_proficiency import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuBikeProficiency,
)
from journey_client.models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_cycle_preference import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuCyclePreference,
)
from journey_client.models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_journey_preference import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuJourneyPreference,
)
from journey_client.models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_time_is import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuTimeIs,
)
from journey_client.models.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu_walking_speed import (
    JourneyJourneyResultsByPathFromPathToQueryViaQueryNationalSearchQueryDateQuWalkingSpeed,
)
from journey_client.models.tfl_40 import Tfl40
from journey_client.types import UNSET, Response, Unset

from journey_client.api.journey.journey_journey_results_by_path_from_path_to_query_via_query_national_search_query_date_qu import sync_detailed 

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
    )


# In[ ]:




