from space.components import ReactionWheel
from space.components import Thruster
from space.constants import directions
from space.constants import math
from space.ship import Ship
from space.ship import ShipPanel


def _test_acceleration(direction, expected_position, orientation={}):
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
    directional_thrusters = [
        t for t in ship.thrusters if t.direction == direction
    ]
    for thruster in directional_thrusters:
        thruster.throttle = 0.5

    ship.apply_acceleration_vectors()
    print(ship.position)
    print(expected_position)
    assert ship.position == expected_position


def _test_rotation(direction, axis, expected_orientation={}):
    ship = Ship(
        reaction_wheels=[
            ReactionWheel(axis=axis, rotation=direction, max_force=15)
        ]
    )
    for reaction_wheel in ship.reaction_wheels:
        reaction_wheel.throttle = 0.5

    ship.apply_acceleration_vectors()
    print(F"""yaw: {ship.get_yaw(math.DEGREES)}
        pitch: {ship.get_pitch(math.DEGREES)}
        roll: {ship.get_roll(math.DEGREES)}""")
    assert (
        ship.get_yaw(math.DEGREES) ==
        expected_orientation.get(directions.YAW, 0)
    )
    assert (
        ship.get_pitch(math.DEGREES) ==
        expected_orientation.get(directions.PITCH, 0)
    )
    assert (
        ship.get_roll(math.DEGREES) ==
        expected_orientation.get(directions.ROLL, 0)
    )
