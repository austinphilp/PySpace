from space import command


def test_command_payload_parse_set_throttle():
    object_id = "12345"
    command_name = "set_throttle"
    args = "0.5"
    command_payload = (
        object_id.encode().ljust(8, b"\0")
        + command_name.encode().ljust(24, b"\0")
        + args.encode().ljust(224, b"\0")
    )
    cmd = command.Command.Parse(command_payload)
    assert isinstance(cmd, command.SetThrottle)
    assert cmd.object_id == object_id
    assert cmd.throttle == 0.5


def test_command_payload_parse_set_power():
    object_id = "12345"
    command_name = "set_power"
    args = "0"
    command_payload = (
        object_id.encode().ljust(8, b"\0")
        + command_name.encode().ljust(24, b"\0")
        + args.encode().ljust(224, b"\0")
    )
    cmd = command.Command.Parse(command_payload)
    assert isinstance(cmd, command.SetPower)
    assert cmd.object_id == object_id
    assert cmd.toggle is False


def test_command_payload_parse_set_rotation():
    object_id = "12345"
    command_name = "set_rotation"
    pitch = -89
    yaw = 54
    args = ','.join(str(x) for x in [pitch, yaw])
    command_payload = (
        object_id.encode().ljust(8, b"\0")
        + command_name.encode().ljust(24, b"\0")
        + args.encode().ljust(224, b"\0")
    )
    cmd = command.Command.Parse(command_payload)
    assert isinstance(cmd, command.SetRotation)
    assert cmd.object_id == object_id
    assert cmd.pitch == pitch
    assert cmd.yaw == yaw


def test_command_payload_parse_set_focus():
    object_id = "12345"
    command_name = "set_focus"
    args = "89"
    command_payload = (
        object_id.encode().ljust(8, b"\0")
        + command_name.encode().ljust(24, b"\0")
        + args.encode().ljust(224, b"\0")
    )
    cmd = command.Command.Parse(command_payload)
    assert isinstance(cmd, command.SetFocus)
    assert cmd.object_id == object_id
    assert cmd.focus == float(args)
