from vectors import Point

from space.constants import directions
from space.tests.assertions import _test_acceleration


# ==================== YAW Tests ====================
def test_overhead_acceleration_yaw_no_change():
    _test_acceleration(
        direction=directions.OVERHEAD,
        expected_position=Point(
            0.00,
            0.00,
            10.00,
        ),
        orientation={
            directions.YAW: 90,
            directions.ROLL: 0,
            directions.PITCH: 0
        },
        keep_mass=False
    )


def test_forward_acceleration_90_yaw():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            0.00,
            10.00,
            0.00,
        ),
        orientation={
            directions.YAW: 90,
            directions.ROLL: 0,
            directions.PITCH: 0
        },
        keep_mass=False
    )


def test_forward_acceleration_45_yaw():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            7.0711,
            7.0711,
            0.00,
        ),
        orientation={
            directions.YAW: 45,
            directions.ROLL: 0,
            directions.PITCH: 0
        },
        keep_mass=False
    )


# ==================== ROLL Tests ====================
def test_forward_acceleration_roll_no_change():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            10.00,
            0.00,
            0.00,
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 90,
            directions.PITCH: 0
        },
        keep_mass=False
    )


def test_port_acceleration_90_roll():
    _test_acceleration(
        direction=directions.PORT,
        expected_position=Point(
            0.00,
            0.00,
            -10.00,
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 90,
            directions.PITCH: 0
        },
        keep_mass=False
    )


def test_port_acceleration_45_roll():
    _test_acceleration(
        direction=directions.PORT,
        expected_position=Point(
            0.00,
            -7.0711,
            -7.0711,
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 45,
            directions.PITCH: 0
        },
        keep_mass=False
    )


# ==================== PITCH Tests ====================
def test_overhead_acceleration_pitch_no_change():
    _test_acceleration(
        direction=directions.STARBOARD,
        expected_position=Point(
            0.00,
            10.00,
            0.00,
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 0,
            directions.PITCH: 90
        },
        keep_mass=False
    )


def test_forward_acceleration_90_pitch():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            0.00,
            0.00,
            -10.00
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 0,
            directions.PITCH: 90
        },
        keep_mass=False
    )


def test_forward_acceleration_45_pitch():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            7.0711,
            0.00,
            -7.0711
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 0,
            directions.PITCH: 45
        },
        keep_mass=False
    )
