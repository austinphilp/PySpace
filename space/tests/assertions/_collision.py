from space.components import Reactor
from space.components import Thruster
from space.constants.directions import (
    COUNTER_DIRECTIONS,
    PITCH,
    ROLL,
    STARBOARD,
    YAW,
)
from space.ship import Ship
from space.ship import ShipPanel


def _build_ship(direction, pos, orientation, throttle):
    # Generate the components and build the ship
    thruster = Thruster(max_force=10.0)
    reactor = Reactor(max_output=60)
    panel = ShipPanel(
        side=COUNTER_DIRECTIONS[direction],
        thrusters=[thruster]
    )
    ship = Ship(**{
        "reactors": [reactor],
        "width": 5,
        "height": 5,
        "depth": 5,
        F"{direction}_panel": panel,
        YAW: orientation.get(YAW, 0),
        ROLL: orientation.get(ROLL, 0),
        PITCH: orientation.get(PITCH, 0),
    })

    for thruster in ship.get_thrusters_by_orientation(direction):
        thruster.throttle = 1.0

    return ship


def _test_collision(
        direction_1=STARBOARD, pos_1={}, orientation_1={}, throttle_1=1.0,
        direction_2=STARBOARD, pos_2={}, orientation_2={}, throttle_2=1.0,
        max_ticks=100, expected_collision=True):
    ship_1 = _build_ship(direction_1, pos_1, orientation_1, throttle_1)
    ship_2 = _build_ship(direction_2, pos_2, orientation_2, throttle_2)

    # Apply acceleration for one tick
    collided = False
    for _ in range(max_ticks):
        ship_1.apply_acceleration_vectors()
        ship_2.apply_acceleration_vectors()
        if ship_1.is_colliding(ship_2):
            collided = True
            if expected_collision:
                break

    # Error
    assert collided or not expected_collision, \
        F"Collision result: {collided}, expected result: {expected_collision}"
