# pyright: reportUnknownMemberType = false, reportPrivateUsage = false
from __future__ import annotations

import json

import aiohttp
import pytest
from aioresponses import aioresponses
from haversine.haversine import Unit, inverse_haversine

from evocarshare import EvoApi, EvoApiCallError, GpsCoord, Vehicle
from tests.test_utils import credentials_from_env

pytest_plugins = ("pytest_asyncio",)


def initialize_mock(m: aioresponses):
    with open("tests/canned_data/token.json", encoding="utf8") as file:
        d = json.load(file)
        m.post(EvoApi.URL_OAUTH, payload=d)

    with open("tests/canned_data/data-available-vehicles.json", encoding="utf8") as file:
        m.get(EvoApi.URL_VEHCILES, payload=json.load(file))


def initialize_mock_bad_token(m: aioresponses):
    with open("tests/canned_data/token-invalid.json", encoding="utf8") as file:
        d = json.load(file)
        m.post(EvoApi.URL_OAUTH, payload=d)


@pytest.mark.asyncio
async def test_fetch_good():
    """Integration test for processing Vehicle data"""

    with aioresponses() as m:
        initialize_mock(m)
        creds = credentials_from_env()

        async with aiohttp.ClientSession() as client_session:
            api = EvoApi(client_session, creds)

            data = await api.get_vehicles()

            m.assert_any_call(EvoApi.URL_OAUTH, method="POST")
            m.assert_any_call(EvoApi.URL_VEHCILES, method="GET")

            assert len(list(data)) > 0


@pytest.mark.asyncio
async def test_fetch_bad_token():
    """Integration test for processing Vehicle data"""

    with aioresponses() as m:
        initialize_mock_bad_token(m)
        creds = credentials_from_env()

        async with aiohttp.ClientSession() as client_session:
            api = EvoApi(client_session, creds)

            with pytest.raises(EvoApiCallError):
                await api.get_vehicles()


def test_range_filter():
    home = (49.279844999999995, -123.10200666666667)

    num_cases = 100
    spacing = 5

    gps = [GpsCoord(*inverse_haversine(home, i * spacing, 0, unit=Unit.METERS)) for i in range(num_cases)]  # pyright: ignore [reportUnknownArgumentType]

    for x in gps:
        print(x)

    vehicles = [Vehicle(f"ID:{i:3}", "Car", f"EVO{i:3}", g, 0, False) for i, g in enumerate(gps)]

    assert len(vehicles) == num_cases

    dist_0 = EvoApi._filter_vehicles_within(0, GpsCoord(*home), vehicles)

    assert len(list(dist_0)) == 1

    dist_10 = EvoApi._filter_vehicles_within(10, GpsCoord(*home), vehicles)
    assert len(list(dist_10)) == 3

    dist_500 = EvoApi._filter_vehicles_within(500, GpsCoord(*home), vehicles)
    assert len(list(dist_500)) == len(vehicles)
