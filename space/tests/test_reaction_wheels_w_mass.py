from space.constants import directions
from space.tests.assertions import _test_rotation


def test_yaw_cw():
    _test_rotation(
        direction=directions.CLOCKWISE,
        axis=directions.YAW,
        expected_orientation={directions.YAW: 0.01}
    )


def test_yaw_ccw():
    _test_rotation(
        direction=directions.COUNTER_CLOCKWISE,
        axis=directions.YAW,
        expected_orientation={directions.YAW: -0.01}
    )


def test_roll_cw():
    _test_rotation(
        direction=directions.CLOCKWISE,
        axis=directions.ROLL,
        expected_orientation={directions.ROLL: 0.01}
    )


def test_roll_ccw():
    _test_rotation(
        direction=directions.COUNTER_CLOCKWISE,
        axis=directions.ROLL,
        expected_orientation={directions.ROLL: -0.01}
    )


def test_pitch_cw():
    _test_rotation(
        direction=directions.CLOCKWISE,
        axis=directions.PITCH,
        expected_orientation={directions.PITCH: 0.01}
    )


def test_pitch_ccw():
    _test_rotation(
        direction=directions.COUNTER_CLOCKWISE,
        axis=directions.PITCH,
        expected_orientation={directions.PITCH: -0.01}
    )
