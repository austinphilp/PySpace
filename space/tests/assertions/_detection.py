from space.body import Body
from space.components import Reactor, Sensor
from space.constants.directions import DIRECTIONS, PITCH, ROLL, YAW
from space.ship import Panel, Ship


def _assert_can_detect(target_pos, ship_orientation, sensor_orientation={},
                       scan_direction=None, sensor_focus=89, has_power=True):
    reactor = Reactor(max_output=200)
    panels = {
        F"{direction}_panel": Panel(
            side=direction,
            sensors=[Sensor(
                base_range=2000,
                focus=sensor_focus,
                pitch=sensor_orientation.get(PITCH, 45),
                yaw=sensor_orientation.get(YAW, 45)
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
    if scan_direction is not None:
        sensors = [
            sensor for panel in ship.panels
            for sensor in panel.sensors
        ]
    else:
        sensors = [
            sensor for panel in ship.panels
            for sensor in panel.sensors
            if panel.side == scan_direction
        ]
    target = Body(position=target_pos)
    assert any(s.can_detect(target) for s in sensors)
