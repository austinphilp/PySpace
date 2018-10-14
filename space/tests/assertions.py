from decimal import Decimal

from space.components import Thruster
from space.constants import directions
from space.ship import Ship
from space.ship import ShipPanel


def _test_acceleration(direction, expected_position, orientation={}):
    thruster = Thruster(max_acceleration=Decimal(10))
    panel = ShipPanel(
        side=directions.COUNTER_DIRECTIONS[direction],
        thrusters=[thruster]
    )
    ship = Ship(**{
        "{}_panel".format(direction): panel,
        directions.YAW: orientation.get(directions.YAW, 0),
        directions.ROLL: orientation.get(directions.ROLL, 0),
        directions.PITCH: orientation.get(directions.PITCH, 0),
    })
    directional_thrusters = [
        t for t in ship.thrusters if t.direction == direction
    ]
    for thruster in directional_thrusters:
        thruster.throttle = Decimal('0.5')

    ship.apply_acceleration_vectors()
    print(ship.position)
    print(expected_position)
    assert ship.position == expected_position
