from space.components import Thruster
from space.constants.directions import PORT
from space.ship import Ship, ShipPanel


def test_mass_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    assert thruster.status_report["mass"] == thruster.mass, \
        "Thruster mass is innacurately reported"


def test_direction_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    assert thruster.status_report["direction"] == thruster.direction, \
        "Thruster direction is innacurately reported"


def test_integrity_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    assert thruster.status_report["integrity"] == thruster.integrity, \
        "Thruster integrity is innacurately reported"


def test_low_integrity_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    thruster.degrade(0.5)
    assert thruster.status_report["integrity"] == thruster.integrity, \
        "Thruster integrity is innacurately reported"


def test_is_active_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    assert thruster.status_report["is_active"] == thruster.is_active, \
        "Thruster is_active is innacurately reported"


def test_is_active_status_report_no_integrity():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    thruster.degrade(1)
    assert thruster.status_report["is_active"] == thruster.is_active, \
        "Thruster is_active is innacurately reported"


def test_is_active_status_report_no_power():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    thruster.powered_on = False
    assert thruster.status_report["is_active"] == thruster.is_active, \
        "Thruster is_active is innacurately reported"


def test_powered_on_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    thruster.powered_on = False
    assert thruster.status_report["powered_on"] == thruster.powered_on, \
        "Thruster powered_on is innacurately reported"


def test_power_consumption_low_throttle_status_report():
    t = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    t.throttle = 0.1
    assert t.status_report["power_consumption"] == t.power_consumption, \
        "Thruster power_consumption is innacurately reported"


def test_power_consumption_high_throttle_status_report():
    t = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    assert t.status_report["power_consumption"] == t.power_consumption, \
        "Thruster power_consumption is innacurately reported"


def test_low_throttle_status_report():
    thruster = Thruster(max_force=15)
    thruster.throttle = 0.1
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    assert thruster.status_report["throttle"] == thruster.throttle, \
        "Thruster throttle is innacurately reported"


def test_throttle_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    assert thruster.status_report["throttle"] == thruster.throttle, \
        "Thruster throttle is innacurately reported"


def test_current_force_status_report_no_throttle():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    thruster.throttle = 0.1
    reported_force = thruster.status_report["current_force"]
    actual_force = thruster.power_adjusted_current_force
    assert reported_force == actual_force, \
        "Thruster.power_adjusted_current_force is innacurately reported"


def test_current_force_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    reported_force = thruster.status_report["current_force"]
    actual_force = thruster.power_adjusted_current_force
    assert reported_force == actual_force, \
        "Thruster current_force is innacurately reported"


def test_degredation_rate_status_report():
    t = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    assert t.status_report["degredation_rate"] == t.degredation_rate, \
        "Thruster degredation_rate is innacurately reported"


def test_degredation_rate_status_report_high_throttle():
    t = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    t.throttle = 1.2
    assert t.status_report["degredation_rate"] == t.degredation_rate, \
        "Thruster degredation_rate is innacurately reported"


def test_max_force_status_report():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    assert thruster.status_report["max_force"] == thruster.max_force, \
        "Thruster max_force is innacurately reported"


def test_max_force_status_report_lothruster_integrity():
    thruster = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[thruster]))
    thruster.degrade(0.2)
    assert thruster.status_report["max_force"] == thruster.max_force, \
        "Thruster max_force is innacurately reported"


def test_current_acceleration_status_report():
    t = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    assert t.status_report["current_acceleration"] == t.current_acceleration, \
        "Thruster current_acceleration is innacurately reported"


def test_current_acceleration_status_report_lothruster_throttle():
    t = Thruster(max_force=15)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    t.throttle = 0.2
    assert t.status_report["current_acceleration"] == t.current_acceleration, \
        "Thruster current_acceleration is innacurately reported"


def test_current_acceleration_status_report_lothruster_max_force():
    t = Thruster(max_force=5)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    assert t.status_report["current_acceleration"] == t.current_acceleration, \
        "Thruster current_acceleration is innacurately reported"


def test_current_acceleration_status_report_high_max_force():
    t = Thruster(max_force=150)
    Ship(port_panel=ShipPanel(side=PORT, thrusters=[t]))
    assert t.status_report["current_acceleration"] == t.current_acceleration, \
        "Thruster current_acceleration is innacurately reported"
