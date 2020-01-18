from space.constants.directions import YAW
from space.components import ReactionWheel


def test_axis_status_report():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    assert wheel.status_report["axis"] == wheel.axis, \
        "Wheel axis is innacurately reported"


def test_rotation_status_report():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    assert wheel.status_report["rotation"] == wheel.rotation, \
        "Wheel rotation is innacurately reported"


def test_mass_status_report():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    assert wheel.status_report["mass"] == wheel.mass, \
        "Wheel mass is innacurately reported"


def test_integrity_status_report():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    assert wheel.status_report["integrity"] == wheel.integrity, \
        "Wheel integrity is innacurately reported"


def test_low_integrity_status_report():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    wheel.degrade(0.5)
    assert wheel.status_report["integrity"] == wheel.integrity, \
        "Wheel integrity is innacurately reported"


def test_is_active_status_report():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    assert wheel.status_report["is_active"] == wheel.is_active, \
        "Wheel is_active is innacurately reported"


def test_is_active_status_report_no_integrity():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    wheel.degrade(1)
    assert wheel.status_report["is_active"] == wheel.is_active, \
        "Wheel is_active is innacurately reported"


def test_is_active_status_report_no_power():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    wheel.powered_on = False
    assert wheel.status_report["is_active"] == wheel.is_active, \
        "Wheel is_active is innacurately reported"


def test_powered_on_status_report():
    wheel = ReactionWheel(axis=YAW, max_force=15)
    wheel.powered_on = False
    assert wheel.status_report["powered_on"] == wheel.powered_on, \
        "Wheel powered_on is innacurately reported"


def test_power_consumption_low_throttle_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    w.throttle = 0.1
    assert w.status_report["power_consumption"] == w.power_consumption, \
        "Wheel power_consumption is innacurately reported"


def test_power_consumption_high_throttle_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    assert w.status_report["power_consumption"] == w.power_consumption, \
        "Wheel power_consumption is innacurately reported"


def test_low_throttle_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    w.throttle = 0.1
    assert w.status_report["throttle"] == w.throttle, \
        "Wheel throttle is innacurately reported"


def test_throttle_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    assert w.status_report["throttle"] == w.throttle, \
        "Wheel throttle is innacurately reported"


def test_current_force_status_report_no_throttle():
    w = ReactionWheel(axis=YAW, max_force=15)
    w.throttle = 0.1
    assert w.status_report["current_force"] == w.current_force, \
        "Wheel current_force is innacurately reported"


def test_current_force_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    assert w.status_report["current_force"] == w.current_force, \
        "Wheel current_force is innacurately reported"


def test_degredation_rate_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    assert w.status_report["degredation_rate"] == w.degredation_rate, \
        "Wheel degredation_rate is innacurately reported"


def test_degredation_rate_status_report_high_throttle():
    w = ReactionWheel(axis=YAW, max_force=15)
    w.throttle = 1.2
    assert w.status_report["degredation_rate"] == w.degredation_rate, \
        "Wheel degredation_rate is innacurately reported"


def test_max_force_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    assert w.status_report["max_force"] == w.max_force, \
        "Wheel max_force is innacurately reported"


def test_max_force_status_report_low_integrity():
    w = ReactionWheel(axis=YAW, max_force=15)
    w.degrade(0.2)
    assert w.status_report["max_force"] == w.max_force, \
        "Wheel max_force is innacurately reported"


def test_current_acceleration_status_report():
    w = ReactionWheel(axis=YAW, max_force=15)
    assert w.status_report["current_acceleration"] == w.current_acceleration, \
        "Wheel current_acceleration is innacurately reported"


def test_current_acceleration_status_report_low_throttle():
    w = ReactionWheel(axis=YAW, max_force=15)
    w.throttle = 0.2
    assert w.status_report["current_acceleration"] == w.current_acceleration, \
        "Wheel current_acceleration is innacurately reported"


def test_current_acceleration_status_report_low_max_force():
    w = ReactionWheel(axis=YAW, max_force=5)
    assert w.status_report["current_acceleration"] == w.current_acceleration, \
        "Wheel current_acceleration is innacurately reported"


def test_current_acceleration_status_report_high_max_force():
    w = ReactionWheel(axis=YAW, max_force=150)
    assert w.status_report["current_acceleration"] == w.current_acceleration, \
        "Wheel current_acceleration is innacurately reported"
