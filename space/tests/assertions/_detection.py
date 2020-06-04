from space.body import Body
from space.components import Reactor, Sensor
from space.constants.directions import DIRECTIONS, PITCH, ROLL, YAW
from space.ship import ShipPanel, Ship


def _get_sensors_for_assertion(ship_orientation={},
                               sensor_orientation={}, scan_direction=None,
                               sensor_focus=89, has_power=True):
    reactor = Reactor(max_output=200)
    panels = {
        F"{direction}_panel": ShipPanel(
            side=direction,
            sensors=[Sensor(
                base_range=2000,
                focus=sensor_focus,
                pitch=sensor_orientation.get(PITCH, 90),
                yaw=sensor_orientation.get(YAW, 90)
            )]
        )
        for direction in DIRECTIONS
    }

    ship = Ship(**{
        **panels,
        "reactors": [reactor] if has_power else [],
        PITCH: ship_orientation.get(PITCH, 0),
        ROLL: ship_orientation.get(ROLL, 0),
        YAW: ship_orientation.get(YAW, 0),
    })
    if scan_direction is None:
        sensors = [
            sensor for panel in ship.panels.values()
            for sensor in panel.sensors
        ]
    else:
        sensors = [
            sensor for sensor in ship.panels[scan_direction].sensors
        ]
    return sensors


def _assert_can_detect(target_pos, *args, **kwargs):
    if kwargs.pop('test', False):
        import pdb
        pdb.set_trace()
    target = Body(position=target_pos)
    sensors = _get_sensors_for_assertion(*args, **kwargs)
    assert any(s.can_detect(target) for s in sensors)


def _assert_can_not_detect(target_pos, *args, **kwargs):
    if kwargs.pop('test', False):
        import pdb
        pdb.set_trace()
    target = Body(position=target_pos)
    sensors = _get_sensors_for_assertion(*args, **kwargs)
    assert all(not s.can_detect(target) for s in sensors)
