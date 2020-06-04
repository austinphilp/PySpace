from space.components import Thruster
from space.constants import directions
from space.ship import Ship
from space.ship import ShipPanel


def test_thruster_degredation():
    # Generate the components and build the ship
    thruster = Thruster(max_force=10.0)
    panel = ShipPanel(
        side=directions.FORWARD,
        thrusters=[thruster]
    )
    ship = Ship(**{F"{directions.FORWARD}_panel": panel})

    # Set thruster throttle to 120%
    for thruster in ship.thrusters:
        thruster.throttle = 1.2

    # Apply acceleration for one hundred ticks
    for _ in range(0, 100):
        ship.apply_acceleration_vectors()

    # Error
    assert ship.thrusters[0].integrity == 0.996, \
        F"{ship.thrusters[0].integrity} != {0.996}"
