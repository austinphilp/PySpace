from vectors import Point
from space.constants.directions import STARBOARD
from space.tests.assertions import _assert_can_detect, _assert_can_not_detect


def test_can_sense_narrow_focus():
    _assert_can_detect(
        target_pos=Point(0, 10, 0),
        scan_direction=STARBOARD,
        sensor_focus=5,
    )


def test_can_sense_wide_focus():
    _assert_can_detect(
        target_pos=Point(0, 1, 10),
        scan_direction=STARBOARD,
        sensor_focus=89
    )


def test_cant_sense_out_of_focus():
    _assert_can_not_detect(
        target_pos=Point(0, 10, 10),
        scan_direction=STARBOARD,
        sensor_focus=1,
        test=True
    )
