from decimal import Decimal
from vectors import Point

from constants import directions
from tests.assertions import _test_acceleration


# ==================== YAW Tests ====================
def test_overhead_acceleration_yaw_no_change():
    _test_acceleration(
        direction=directions.OVERHEAD,
        expected_position=Point(
            Decimal('0.00'),
            Decimal('0.00'),
            Decimal('5.00'),
        ),
        orientation={
            directions.YAW: 90,
            directions.ROLL: 0,
            directions.PITCH: 0
        }
    )


def test_forward_acceleration_90_yaw():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            Decimal('0.00'),
            Decimal('5.00'),
            Decimal('0.00'),
        ),
        orientation={
            directions.YAW: 90,
            directions.ROLL: 0,
            directions.PITCH: 0
        }
    )


def test_forward_acceleration_45_yaw():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            Decimal('3.55'),
            Decimal('3.55'),
            Decimal('0.00'),
        ),
        orientation={
            directions.YAW: 45,
            directions.ROLL: 0,
            directions.PITCH: 0
        }
    )


# ==================== ROLL Tests ====================
def test_forward_acceleration_roll_no_change():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            Decimal('5.00'),
            Decimal('0.00'),
            Decimal('0.00'),
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 90,
            directions.PITCH: 0
        }
    )


def test_port_acceleration_90_roll():
    _test_acceleration(
        direction=directions.PORT,
        expected_position=Point(
            Decimal('0.00'),
            Decimal('0.00'),
            Decimal('-5.00'),
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 90,
            directions.PITCH: 0
        }
    )


def test_port_acceleration_45_roll():
    _test_acceleration(
        direction=directions.PORT,
        expected_position=Point(
            Decimal('0.00'),
            Decimal('-3.55'),
            Decimal('-3.55'),
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 45,
            directions.PITCH: 0
        }
    )


# ==================== PITCH Tests ====================
def test_overhead_acceleration_pitch_no_change():
    _test_acceleration(
        direction=directions.STARBOARD,
        expected_position=Point(
            Decimal('0.00'),
            Decimal('5.00'),
            Decimal('0.00'),
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 0,
            directions.PITCH: 90
        }
    )


def test_forward_acceleration_90_pitch():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            Decimal('0.00'),
            Decimal('0.00'),
            Decimal('-5.00')
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 0,
            directions.PITCH: 90
        }
    )


def test_forward_acceleration_45_pitch():
    _test_acceleration(
        direction=directions.FORWARD,
        expected_position=Point(
            Decimal('3.55'),
            Decimal('0.00'),
            Decimal('-3.55')
        ),
        orientation={
            directions.YAW: 0,
            directions.ROLL: 0,
            directions.PITCH: 45
        }
    )
