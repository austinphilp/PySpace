from vectors import Point


from space.constants import directions
from space.tests.assertions import _test_collision


def test_rear_collision():
    _test_collision(
        direction_1=directions.FORWARD,
        pos_1=Point(0, 0, 0),
        throttle_1=1.0,
        direction_2=directions.FORWARD,
        pos_2=Point(100, 0, 0),
        throttle_2=0.5,
    )


def test_head_on_collision():
    _test_collision(
        direction_1=directions.FORWARD,
        pos_1=Point(-100, 0, 0),
        throttle_1=1.0,
        direction_2=directions.AFT,
        pos_2=Point(100, 0, 0),
        throttle_2=1.0,
    )


def test_angular_collision():
    _test_collision(
        direction_1=directions.FORWARD,
        pos_1=Point(-100, 0, 0),
        throttle_1=1.0,
        direction_2=directions.AFT,
        pos_2=Point(100, 0, 0),
        throttle_2=1.0,
    )


def test_level_tbone_collision():
    _test_collision(
        direction_1=directions.FORWARD,
        pos_1=Point(0, 0, 0),
        throttle_1=0.0,
        direction_2=directions.STARBOARD,
        pos_2=Point(0, -100, 0),
        throttle_2=1.0,
    )


def test_top_down_tbone_collision():
    _test_collision(
        direction_1=directions.FORWARD,
        pos_1=Point(0, 0, 0),
        throttle_1=0.0,
        direction_2=directions.DECK,
        pos_2=Point(0, 0, 100),
        throttle_2=1.0,
    )
