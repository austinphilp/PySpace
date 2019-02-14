from vectors import Point
from space.constants.directions import PITCH, STARBOARD, YAW
from space.tests.assertions import _assert_can_detect


def test_can_sense_at_angle_pitch():
    _assert_can_detect(
        target_pos=Point(0, 10, 10),
        scan_direction=STARBOARD,
        sensor_orientation={
            PITCH: 15,
            YAW: 45
        }
    )


def test_can_sense_at_angle_yaw():
    _assert_can_detect(
        target_pos=Point(10, 10, 0),
        scan_direction=STARBOARD,
        sensor_orientation={
            PITCH: 45,
            YAW: 67.5
        },
    )
