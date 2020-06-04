from space.components import ReactionWheel
from space.components import Thruster
from space.constants import directions
from space.ship import Ship
from space.ship import ShipPanel


def test_ship_dimension_calculation():
    thruster = Thruster(max_force=10)
    ship = Ship(**{
        "reaction_wheels": [ReactionWheel(max_force=10, axis=directions.ROLL)],
        **{
            F"{side}_panel": ShipPanel(side=side, thrusters=[thruster])
            for side in directions.DIRECTIONS
        }
    })
    assert ship.width == 2.8
    assert ship.height == 2.8
    assert ship.depth == 2.8
