from vectors import Point
from space.constants.directions import STARBOARD
from space.tests.assertions import _assert_can_detect


def test_can_sense_no_angle():
    _assert_can_detect(
        target_pos=Point(0, 10, 0),
        scan_direction=STARBOARD
    )
