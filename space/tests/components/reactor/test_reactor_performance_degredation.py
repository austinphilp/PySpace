from vectors import Point

from space.constants import directions
from space.tests.assertions import _test_acceleration


def test_overloaded_reactor_performance_degredation():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(0.33333, 0, 0),
        reactor_power=5
    )


def test_overloaded_reactor_performance_undegraded():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(0.5, 0, 0),
        reactor_power=10
    )
