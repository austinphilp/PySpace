from space.constants import directions
from space.tests.assertions import _test_rotation


def test_yaw_cw():
    _test_rotation(
        direction=directions.CLOCKWISE,
        axis=directions.YAW,
        expected_orientation={directions.YAW: 7.5},
        keep_mass=False
    )


def test_yaw_ccw():
    _test_rotation(
        direction=directions.COUNTER_CLOCKWISE,
        axis=directions.YAW,
        expected_orientation={directions.YAW: -7.5},
        keep_mass=False
    )


def test_roll_cw():
    _test_rotation(
        direction=directions.CLOCKWISE,
        axis=directions.ROLL,
        expected_orientation={directions.ROLL: 7.5},
        keep_mass=False
    )


def test_roll_ccw():
    _test_rotation(
        direction=directions.COUNTER_CLOCKWISE,
        axis=directions.ROLL,
        expected_orientation={directions.ROLL: -7.5},
        keep_mass=False
    )


def test_pitch_cw():
    _test_rotation(
        direction=directions.CLOCKWISE,
        axis=directions.PITCH,
        expected_orientation={directions.PITCH: 7.5},
        keep_mass=False
    )


def test_pitch_ccw():
    _test_rotation(
        direction=directions.COUNTER_CLOCKWISE,
        axis=directions.PITCH,
        expected_orientation={directions.PITCH: -7.5},
        keep_mass=False
    )
