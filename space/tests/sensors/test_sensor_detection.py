from vectors import Point
from space.constants.directions import PITCH, ROLL, STARBOARD, YAW
from space.tests.assertions import _assert_can_detect


def test_can_sense_no_angle():
    _assert_can_detect(
        target_position=Point(0, 10, 0),
        scan_direction=STARBOARD
    )


def test_can_sense_at_angle_pitch():
    _assert_can_detect(
        target_position=Point(0, 10, 10),
        scan_direction=STARBOARD,
        sensor_orientation={
            PITCH: 10,
            YAW: 45
        }
    )


def test_can_sense_at_angle_yaw():
    _assert_can_detect(
        target_position=Point(10, 10, 0),
        scan_direction=STARBOARD,
        sensor_orientation={
            PITCH: 45,
            YAW: 10
        }
    )


def test_can_sense_ship_at_angle():
    _assert_can_detect(
        target_position=Point(0, 0, -10),
        scan_direction=STARBOARD,
        ship_orientation={
            PITCH: 0,
            YAW: 0,
            ROLL: 45
        },
        sensor_orientation={
            PITCH: 45,
            YAW: 10
        },
        sensor_focus=45
    )


def test_can_sense_narrow_focus():
    _assert_can_detect(
        target_position=Point(0, 10, 0),
        scan_direction=STARBOARD,
        sensor_focus=5
    )


def test_can_sense_wide_focus():
    _assert_can_detect(
        target_position=Point(0, 1, 10),
        scan_direction=STARBOARD,
        sensor_focus=89
    )


def test_cant_sense_out_of_range():
    _assert_can_detect(
        target_position=Point(0, 0, 10000000),
        scan_direction=STARBOARD,
    )


def test_cant_sense_out_of_focus():
    _assert_can_detect(
        target_position=Point(0, 10, 10),
        scan_direction=STARBOARD,
        sensor_focus=5
    )


def test_cant_sense_out_of_power():
    _assert_can_detect(
        target_position=Point(0, 10, 0),
        scan_direction=STARBOARD,
        has_power=False
    )


def test_cant_sense_other_side():
    _assert_can_detect(
        target_position=Point(0, -10, 0),
        scan_direction=STARBOARD,
        has_power=False
    )
