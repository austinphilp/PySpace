from space.components import ReactionWheel
from space.components import Thruster
from space.constants import directions
from space.constants.ratios import KG_PER_RW_ACC
from space.constants.ratios import KG_PER_THRUSTER_ACC
from space.ship import Ship
from space.ship import ShipPanel


def test_thruster_mass_calculation():
    mass = Thruster(max_acceleration=10).mass
    assert mass == 10 * KG_PER_THRUSTER_ACC


def test_reaction_wheel_mass_calculation():
    mass = ReactionWheel(max_acceleration=10, axis=directions.ROLL).mass
    assert mass == 10 * KG_PER_RW_ACC


def test_ship_mass_calculation():
    thruster = Thruster(max_acceleration=10)
    ship = Ship(**{
        "reaction_wheels": [ReactionWheel(max_acceleration=10, axis=directions.ROLL)],
        **{
            F"{side}_panel": ShipPanel(side=side, thrusters=[thruster])
            for side in directions.DIRECTIONS
        }
    })
    assert ship.mass == 3500

