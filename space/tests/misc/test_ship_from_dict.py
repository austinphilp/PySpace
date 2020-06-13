from space.components import Reactor, ReactionWheel
from space.constants.directions import PITCH, CLOCKWISE, STARBOARD
from space.ship import Ship


def test_ship_from_dict_has_reactor():
    ship = Ship.from_dict({"reactors": [{"max_output": 100}]})
    assert len(ship.reactors) == 1
    assert isinstance(ship.reactors[0], Reactor)


def test_ship_from_dict_reactor_max_output():
    expected_max_output = 100
    ship = Ship.from_dict({"reactors": [{"max_output": expected_max_output}]})
    assert ship.reactors[0].initial_max_output == expected_max_output


def test_ship_from_dict_has_reaction_wheel():
    expected_max_force = 100
    expected_pitch = PITCH
    expected_rotation = CLOCKWISE
    ship = Ship.from_dict({"reaction_wheels": [{
        "axis": expected_pitch,
        "rotation": expected_rotation,
        "max_force": expected_max_force
    }]})
    assert len(ship.reaction_wheels) == 1
    assert isinstance(ship.reaction_wheels[0], ReactionWheel)


def test_ship_from_dict_has_reaction_wheel_rotation():
    expected_max_force = 100
    expected_axis = PITCH
    expected_rotation = CLOCKWISE
    ship = Ship.from_dict({"reaction_wheels": [{
        "axis": expected_axis,
        "rotation": expected_rotation,
        "max_force": expected_max_force
    }]})
    assert ship.reaction_wheels[0].rotation == expected_rotation


def test_ship_from_dict_has_reaction_wheel_axis():
    expected_max_force = 100
    expected_axis = PITCH
    expected_rotation = CLOCKWISE
    ship = Ship.from_dict({"reaction_wheels": [{
        "axis": expected_axis,
        "rotation": expected_rotation,
        "max_force": expected_max_force
    }]})
    assert ship.reaction_wheels[0].axis == expected_axis


def test_ship_from_dict_has_reaction_wheel_max_force():
    expected_max_force = 100
    expected_pitch = PITCH
    expected_rotation = CLOCKWISE
    ship = Ship.from_dict({"reaction_wheels": [{
        "axis": expected_pitch,
        "rotation": expected_rotation,
        "max_force": expected_max_force
    }]})
    assert ship.reaction_wheels[0].max_force == expected_max_force

# TODO(Austin) - tests for panels and all their components


def test_ship_from_dict_panel_has_thruster():
    expected_side = STARBOARD
    ship = Ship.from_dict({"panels": {
        expected_side: {"thrusters": [{"max_force": 0}]}
    }})
    assert len(ship.thrusters) == 1


def test_ship_from_dict_panel_thruster_max_force():
    expected_max_force = 100
    expected_side = STARBOARD
    ship = Ship.from_dict({"panels": {
        expected_side: {"thrusters": [{"max_force": expected_max_force}]}
    }})
    assert ship.thrusters[0].initial_max_force == expected_max_force


def test_ship_from_dict_panel_has_sensor():
    expected_side = STARBOARD
    ship = Ship.from_dict({"panels": {
        expected_side: {"sensors": [{"base_range": 0, "focus": 90}]}
    }})
    assert len(ship.sensors) == 1


def test_ship_from_dict_panel_has_sensor_base_range():
    expected_side = STARBOARD
    expected_base_range = 5000
    expected_focus = 10
    ship = Ship.from_dict({"panels": {
        expected_side: {"sensors": [{
            "base_range": expected_base_range,
            "focus": expected_focus
        }]}
    }})
    assert ship.sensors[0].base_range == expected_base_range


def test_ship_from_dict_panel_has_sensor_focus():
    expected_base_range = 5000
    expected_focus = 10
    expected_side = STARBOARD
    ship = Ship.from_dict({"panels": {
        expected_side: {"sensors": [{
            "base_range": expected_base_range,
            "focus": expected_focus
        }]}
    }})
    assert ship.sensors[0].focus == expected_focus


def test_ship_from_dict_panel_has_mining_laser():
    expected_side = STARBOARD
    expected_base_range = 100
    expected_mine_rate = 1
    ship = Ship.from_dict({"panels": {
        expected_side: {"lasers": [{
            "base_range": expected_base_range,
            "mine_rate": expected_mine_rate
        }]}
    }})
    assert len(ship.mining_lasers) > 0


def test_ship_from_dict_panel_has_mining_laser_base_range():
    expected_side = STARBOARD
    expected_base_range = 100
    expected_mine_rate = 1
    ship = Ship.from_dict({"panels": {
        expected_side: {"lasers": [{
            "base_range": expected_base_range,
            "mine_rate": expected_mine_rate
        }]}
    }})
    assert ship.mining_lasers[0].base_range == expected_base_range


def test_ship_from_dict_panel_has_mining_laser_mine_rate():
    expected_side = STARBOARD
    expected_base_range = 100
    expected_mine_rate = 1
    ship = Ship.from_dict({"panels": {
        expected_side: {"lasers": [{
            "base_range": expected_base_range,
            "mine_rate": expected_mine_rate
        }]}
    }})
    assert ship.mining_lasers[0].mine_rate == expected_mine_rate
