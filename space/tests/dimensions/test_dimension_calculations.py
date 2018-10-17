from space.components import ReactionWheel
from space.components import Thruster
from space.constants import directions
from space.constants.ratios import KG_PER_RW_ACC
from space.constants.ratios import KG_PER_THRUSTER_ACC
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
    assert ship.width == 3.5
    assert ship.height == 3.5
    assert ship.depth == 3.5

