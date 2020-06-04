from vectors import Vector

from space.components import Thruster, Reactor
from space.constants.directions import PORT
from space.ship import Ship, ShipPanel


def test_mass_status_report():
    ship = Ship(
        port_panel=ShipPanel(side=PORT, thrusters=[Thruster(max_force=15)]),
        reactors=[Reactor(max_output=100)]
    )
    assert ship.status_report["mass"] == ship.mass, \
        "Thruster mass is innacurately reported"


def test_vector_status_report():
    ship = Ship(
        port_panel=ShipPanel(side=PORT, thrusters=[Thruster(max_force=15)]),
        reactors=[Reactor(max_output=100)]
    )
    report_vector = Vector.from_list(ship.status_report["vector"].values())
    assert report_vector == ship.current_vector, \
        "Thruster vector is innacurately reported"


def test_power_available_status_report():
    ship = Ship(
        port_panel=ShipPanel(side=PORT, thrusters=[Thruster(max_force=15)]),
        reactors=[Reactor(max_output=100)]
    )
    assert ship.status_report["power_available"] == ship.power_available, \
        "Thruster vector is innacurately reported"


def test_power_consumption_status_report():
    ship = Ship(
        port_panel=ShipPanel(side=PORT, thrusters=[Thruster(max_force=15)]),
        reactors=[Reactor(max_output=100)]
    )
    assert ship.status_report["power_consumption"] == ship.power_consumption, \
        "Thruster power_consumption is innacurately reported"
