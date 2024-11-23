# pyright: reportUnknownMemberType = false
from decimal import Decimal

import pytest

from evocarshare import GpsCoord, RangedVehicle, Vehicle

EPSILON = Decimal(0.005)  # Allow 1/2 percent variance when comparing gps distances


class TestCoord:
    NULL_ISLE = GpsCoord(0, 0)
    NULL_ISLE_1k = GpsCoord(0.00849158482, 0.00309066567)
    VAN = GpsCoord(49.279844999999995, -123.10200666666667)
    VAN_10m = GpsCoord(49.27979984695, -123.10205241248)


def get_test_vehicle(gps: GpsCoord = TestCoord.NULL_ISLE) -> Vehicle:
    return Vehicle("001", "white tesla", "zooom", gps, 99, False)


def test_gps_ident():
    assert TestCoord.VAN.distanceTo(TestCoord.VAN) == 0
    assert TestCoord.NULL_ISLE.distanceTo(TestCoord.NULL_ISLE_1k) == pytest.approx(Decimal(1), rel=EPSILON)
    assert TestCoord.VAN_10m.distanceTo(TestCoord.VAN) == pytest.approx(Decimal(0.010), abs=EPSILON)


def test_ranged_vehicle_attr():
    v = get_test_vehicle(TestCoord.NULL_ISLE)
    r = RangedVehicle(v, TestCoord.NULL_ISLE_1k)

    assert r.distance == pytest.approx(1, rel=EPSILON)
    assert r.model == v.model

    with pytest.raises(AttributeError):
        r.doesnt_exist  # noqa: B018
