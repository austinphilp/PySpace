from space.command import Command
from space.components import ReactionWheel, Reactor, Sensor, Thruster
from space.constants import directions, math
from space.exceptions import InvalidObjectForCommand, InputValidationError
from space.ship import Ship, ShipPanel
from space.system import System


def _create_test_ship():
    return Ship(**{
        directions.YAW: 0,
        directions.ROLL: 0,
        directions.PITCH: 0,
        "reactors": [Reactor(max_output=20)],
        "reaction_wheels": [
            ReactionWheel(
                axis=axis,
                rotation=directions.FORWARD,
                max_force=15
            )
            for axis in [directions.YAW, directions.ROLL, directions.PITCH]
        ],
        **{
            F"{direction}_panel": ShipPanel(
                side=directions.COUNTER_DIRECTIONS[direction],
                thrusters=[Thruster(max_force=10.0)],
                sensors=[Sensor(base_range=2000)]
            ) for direction in directions.DIRECTIONS
        }
    })


def _create_test_system(num_of_ships=1):
    return System(ships=[_create_test_ship() for _ in range(num_of_ships)])


def _create_command(object_id, command_name, args):
    return Command.Parse(
        object_id.encode().ljust(8, b"\0")
        + command_name.encode().ljust(24, b"\0")
        + args.encode().ljust(224, b"\0")
    )


def test_object_id():
    system = _create_test_system()
    thruster = system.ships[0].thrusters[0]
    cmd = _create_command(
        object_id=thruster.object_id,
        command_name="set_throttle",
        args="0.5"
    )
    cmd.exec(system)
    assert cmd.object == thruster


def test_cannot_set_throttle_on_ship_bad_type():
    system = _create_test_system()
    try:
        cmd = _create_command(
            object_id=system.ships[0].object_id,
            command_name="set_throttle",
            args="0.5"
        )
        cmd.exec(system)
    except InvalidObjectForCommand:
        assert True
        return
    assert False, "Expected InvalidObjectForCommand to be thrown"


def test_can_set_throttle():
    system = _create_test_system()
    thruster = system.ships[0].thrusters[0]
    thruster.throttle = 1
    target_thrust = 0.5
    cmd = _create_command(
        object_id=thruster.object_id,
        command_name="set_throttle",
        args=str(target_thrust)
    )
    cmd.exec(system)
    assert thruster.throttle == target_thrust


def test_cannot_set_throttle_too_high():
    system = _create_test_system()
    thruster = system.ships[0].thrusters[0]
    target_thrust = 1.5
    try:
        cmd = _create_command(
            object_id=thruster.object_id,
            command_name="set_throttle",
            args=str(target_thrust)
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InvalidObjectForCommand to be thrown"


def test_can_set_power():
    system = _create_test_system()
    thruster = system.ships[0].thrusters[0]
    power_toggle = False
    cmd = _create_command(
        object_id=thruster.object_id,
        command_name="set_power",
        args="1" if power_toggle is True else "0"
    )
    cmd.exec(system)
    assert thruster.powered_on == power_toggle


def test_cannot_set_power_non_binary():
    system = _create_test_system()
    thruster = system.ships[0].thrusters[0]
    bad_toggle_arg = "X"
    try:
        cmd = _create_command(
            object_id=thruster.object_id,
            command_name="set_power",
            args=bad_toggle_arg
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"


def test_can_set_rotation_pitch_yaw():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    pitch, yaw = 10, -30
    cmd = _create_command(
        object_id=sensor.object_id,
        command_name="set_rotation",
        args=",".join([str(pitch), str(yaw)])
    )
    cmd.exec(system)
    assert sensor.get_pitch(math.DEGREES) == pitch
    assert sensor.get_yaw(math.DEGREES) == yaw


def test_cannot_set_pitch_high():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    pitch, yaw = 100, -30
    try:
        cmd = _create_command(
            object_id=sensor.object_id,
            command_name="set_rotation",
            args=",".join([str(pitch), str(yaw)])
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"


def test_cannot_set_pitch_low():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    pitch, yaw = -100, -30
    try:
        cmd = _create_command(
            object_id=sensor.object_id,
            command_name="set_rotation",
            args=",".join([str(pitch), str(yaw)])
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"


def test_cannot_set_yaw_high():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    pitch, yaw = 0, 100
    try:
        cmd = _create_command(
            object_id=sensor.object_id,
            command_name="set_rotation",
            args=",".join([str(pitch), str(yaw)])
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"


def test_cannot_set_yaw_low():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    pitch, yaw = 0, -100
    try:
        cmd = _create_command(
            object_id=sensor.object_id,
            command_name="set_rotation",
            args=",".join([str(pitch), str(yaw)])
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"


def test_can_set_focus():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    focus = 12
    cmd = _create_command(
        object_id=sensor.object_id,
        command_name="set_focus",
        args=str(focus)
    )
    cmd.exec(system)
    assert sensor.focus == focus


def test_cannot_set_focus_high():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    focus = 100
    try:
        cmd = _create_command(
            object_id=sensor.object_id,
            command_name="set_focus",
            args=str(focus)
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"


def test_cannot_set_focus_low():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    focus = 0
    try:
        cmd = _create_command(
            object_id=sensor.object_id,
            command_name="set_focus",
            args=str(focus)
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"


def test_cannot_set_focus_bad_val():
    system = _create_test_system()
    sensor = system.ships[0].sensors[0]
    focus = "x"
    try:
        cmd = _create_command(
            object_id=sensor.object_id,
            command_name="set_focus",
            args=str(focus)
        )
        cmd.exec(system)
    except InputValidationError:
        assert True
        return
    assert False, "Expected InputValidationError to be thrown"
