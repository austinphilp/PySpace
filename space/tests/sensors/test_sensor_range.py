from vectors import Point
from space.constants.directions import STARBOARD
from space.tests.assertions import _assert_can_not_detect


def test_cant_sense_out_of_range():
    _assert_can_not_detect(
        target_pos=Point(0, 10000000, 0),
        scan_direction=STARBOARD,
    )
