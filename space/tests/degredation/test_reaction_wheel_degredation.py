from space.components import ReactionWheel
from space.constants import directions
from space.ship import Ship


def test_reaction_wheel_degredation():
    ship = Ship(
        reaction_wheels=[
            ReactionWheel(
                axis=directions.ROLL,
                rotation=directions.CLOCKWISE,
                max_force=15
            )
        ]
    )
    for reaction_wheel in ship.reaction_wheels:
        reaction_wheel.throttle = 1.2

    for _ in range(0, 100):
        ship.apply_acceleration_vectors()

    # Assert that reaction wheel integrity meets expected values
    assert ship.reaction_wheels[0].integrity == 0.996, \
        F"{ship.reaction_wheels[0].integrity} != {0.996}"
