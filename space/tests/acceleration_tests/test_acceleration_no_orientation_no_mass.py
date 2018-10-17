from vectors import Point

from space.constants import directions
from space.tests.assertions import _test_acceleration


def test_overhead_acceleration_default_orientation():
    _test_acceleration(
        direction=directions.OVERHEAD,
        expected_position=Point(0, 0, 5),
        keep_mass=False
    )


def test_deck_acceleration_default_orientation():
    _test_acceleration(
        direction=directions.DECK,
        expected_position=Point(0, 0, -5),
        keep_mass=False
    )


def test_port_acceleration_default_orientation():
    _test_acceleration(
        direction=directions.PORT,
        expected_position=Point(0, -5, 0),
        keep_mass=False
    )


def test_starboard_acceleration_default_orientation():
    _test_acceleration(
        direction=directions.STARBOARD,
        expected_position=Point(0, 5, 0),
        keep_mass=False
    )


def test_forward_acceleration_default_orientation():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(5, 0, 0),
        keep_mass=False
    )


def test_aft_acceleration_default_orientation():
    _test_acceleration(
        direction=directions.AFT,
        expected_position=Point(-5, 0, 0),
        keep_mass=False
    )
