from space.components import ReactionWheel
from space.components import Thruster
from space.constants import directions
from space.constants import math
from space.ship import Ship
from space.ship import ShipPanel


def _test_acceleration(direction, expected_position, orientation={}, keep_mass=True):
    # Generate the components and build the ship
    thruster = Thruster(max_force=10.0)
    panel = ShipPanel(
        side=directions.COUNTER_DIRECTIONS[direction],
        thrusters=[thruster]
    )
    ship = Ship(**{
        F"{direction}_panel": panel,
        directions.YAW: orientation.get(directions.YAW, 0),
        directions.ROLL: orientation.get(directions.ROLL, 0),
        directions.PITCH: orientation.get(directions.PITCH, 0),
    })

    # Set total mass to 1 in order to negate any mass affects on propulsion
    if not keep_mass:
        ship.mass = 1

    # Set thruster throttle to 50%
    for thruster in ship.get_thrusters_by_orientation(direction):
        thruster.throttle = 0.5

    # Apply acceleration for one tick
    ship.apply_acceleration_vectors()

    # Error
    assert ship.position == expected_position, \
        F"{ship.position} != {expected_position}"


def _test_rotation(direction, axis, expected_orientation={}, keep_mass=True):
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
