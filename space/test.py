from decimal import Decimal

from space.components import Thruster
from space.constants import directions
from space.ship import Ship
from space.ship import ShipPanel

thruster = Thruster(max_acceleration=Decimal(10))
panel = ShipPanel(side=directions.DECK, thrusters=[thruster])
ship = Ship(reaction_wheels=[], deck_panel=panel)
for thruster in ship.thrusters:
    thruster.throttle = Decimal(1)

ship.apply_acceleration_vectors()
