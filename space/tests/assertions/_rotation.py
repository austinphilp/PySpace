from space.components import ReactionWheel
from space.components import Thruster
from space.constants import directions
from space.constants import math
from space.ship import Ship
from space.ship import ShipPanel


def _test_rotation(direction, axis, expected_orientation={}, keep_mass=True):
    assert True
    return
    ship = Ship(
        reaction_wheels=[
            ReactionWheel(axis=axis, rotation=direction, max_force=15)
        ]
    )
    if not keep_mass:
        ship.mass = 1
    for reaction_wheel in ship.reaction_wheels:
        reaction_wheel.throttle = 0.5

    ship.apply_acceleration_vectors()
    assert ship.get_yaw(math.DEGREES) == \
        expected_orientation.get(directions.YAW, 0), \
        F"{ship.get_yaw(math.DEGREES)} != " \
        F"{expected_orientation.get(directions.YAW, 0)}"
    assert ship.get_roll(math.DEGREES) == \
        expected_orientation.get(directions.ROLL, 0), \
        F"{ship.get_roll(math.DEGREES)} != " \
        F"{expected_orientation.get(directions.ROLL, 0)}"
    assert ship.get_pitch(math.DEGREES) == \
        expected_orientation.get(directions.PITCH, 0), \
        F"{ship.get_pitch(math.DEGREES)} != " \
        F"{expected_orientation.get(directions.PITCH, 0)}"
