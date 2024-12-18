"""
Partial Stubs - generated from pyright
"""

from enum import Enum

Point = tuple[float, float]

_AVG_EARTH_RADIUS_KM = ...

class Unit(str, Enum):
    """
    Enumeration of supported units.
    The full list can be checked by iterating over the class; e.g.
    the expression `tuple(Unit)`.
    """

    KILOMETERS = ...
    METERS = ...
    MILES = ...
    NAUTICAL_MILES = ...
    FEET = ...
    INCHES = ...
    RADIANS = ...
    DEGREES = ...

class Direction(float, Enum):
    """
    Enumeration of supported directions.
    The full list can be checked by iterating over the class; e.g.
    the expression `tuple(Direction)`.
    Angles expressed in radians.
    """

    NORTH = ...
    NORTHEAST = ...
    EAST = ...
    SOUTHEAST = ...
    SOUTH = ...
    SOUTHWEST = ...
    WEST = ...
    NORTHWEST = ...

_CONVERSIONS = ...

def get_avg_earth_radius(unit: Unit) -> float: ...

_haversine_kernel = ...
_inverse_haversine_kernel = ...
has_numpy = ...
_haversine_kernel_vector = ...
_inverse_haversine_kernel_vector = ...
if has_numpy:
    _haversine_kernel_vector = ...
    _inverse_haversine_kernel_vector = ...
_haversine_kernel = ...
_inverse_haversine_kernel = ...

def haversine(
    point1: tuple[float, float], point2: tuple[float, float], unit: Unit = ..., normalize: bool = ..., check: bool = ...
) -> float:
    """Calculate the great-circle distance between two points on the Earth surface.

    Takes two 2-tuples, containing the latitude and longitude of each point in decimal degrees,
    and, optionally, a unit of length.

    :param point1: first point; tuple of (latitude, longitude) in decimal degrees
    :param point2: second point; tuple of (latitude, longitude) in decimal degrees
    :param unit: a member of haversine.Unit, or, equivalently, a string containing the
                 initials of its corresponding unit of measurement (i.e. miles = mi)
                 default 'km' (kilometers).
    :param normalize: if True, normalize the points to [-90, 90] latitude and [-180, 180] longitude.
    :param check: if True, check that points are normalized.

    Example: ``haversine((45.7597, 4.8422), (48.8567, 2.3508), unit=Unit.METERS)``

    Precondition: ``unit`` is a supported unit (supported units are listed in the `Unit` enum)

    :return: the distance between the two points in the requested unit, as a float.

    The default returned unit is kilometers. The default unit can be changed by
    setting the unit parameter to a member of ``haversine.Unit``
    (e.g. ``haversine.Unit.INCHES``), or, equivalently, to a string containing the
    corresponding abbreviation (e.g. 'in'). All available units can be found in the ``Unit`` enum.
    """
    ...

def inverse_haversine(point: Point, distance: float, direction: Direction | float, unit: Unit = ...) -> Point: ...
