from vectors import Point
from space.constants.directions import PITCH, ROLL, STARBOARD, YAW
from space.tests.assertions import _assert_can_detect


def test_can_sense_ship_at_angle():
    _assert_can_detect(
        target_pos=Point(0, 10, -10),
        scan_direction=STARBOARD,
        ship_orientation={
            PITCH: 0,
            YAW: 0,
            ROLL: -45
        },
        sensor_orientation={
            PITCH: 90,
            YAW: 90
        },
        sensor_focus=45,
    )
