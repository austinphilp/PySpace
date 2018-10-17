from space.components import ReactionWheel
from space.components import Reactor
from space.components import Thruster
from space.constants import directions
from space.constants import math
from space.ship import Ship
from space.ship import ShipPanel


def _test_acceleration(
        direction, expected_position, orientation={},
        keep_mass=True, reactor_power=20):
    # Generate the components and build the ship
    thruster = Thruster(max_force=10.0)
    reactor = Reactor(max_output=reactor_power)
    panel = ShipPanel(
        side=directions.COUNTER_DIRECTIONS[direction],
        thrusters=[thruster]
    )
    ship = Ship(**{
        "reactors": [reactor],
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
        thruster.throttle = 1.0

    # Apply acceleration for one tick
    ship.apply_acceleration_vectors()

    # Error
    assert ship.position == expected_position, \
        F"{ship.position} != {expected_position}"
