from vectors import Point
from space.constants.directions import PITCH, ROLL, STARBOARD, YAW
from space.tests.assertions import _assert_can_detect, _assert_can_not_detect


def test_cant_sense_out_of_power():
    _assert_can_not_detect(
        target_pos=Point(0, 10, 0),
        scan_direction=STARBOARD,
        has_power=False
    )
