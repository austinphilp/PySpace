from vectors import Point
from space.constants import directions
from space.tests.assertions import _assert_can_detect


def test_can_sense_no_angle_sb():
    _assert_can_detect(
        target_pos=Point(0, 10, 0),
        scan_direction=directions.STARBOARD
    )


def test_can_sense_no_angle_port():
    _assert_can_detect(
        target_pos=Point(0, -10, 0),
        scan_direction=directions.PORT
    )


def test_can_sense_no_angle_oh():
    _assert_can_detect(
        target_pos=Point(0, 0, 10),
        scan_direction=directions.OVERHEAD
    )


def test_can_sense_no_angle_deck():
    _assert_can_detect(
        target_pos=Point(0, 0, -10),
        scan_direction=directions.DECK
    )


def test_can_sense_no_angle_for():
    _assert_can_detect(
        target_pos=Point(10, 0, 0),
        scan_direction=directions.FORWARD
    )


def test_can_sense_no_angle_aft():
    _assert_can_detect(
        target_pos=Point(-10, 0, 0),
        scan_direction=directions.AFT
    )
