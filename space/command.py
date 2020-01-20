from space.components import (
    ReactionWheel,
    Thruster,
    Reactor,
    Sensor
)
from space.exceptions import InvalidObjectForCommand, InputValidationError


class Command(object):
    def __init__(self, object_id, command, raw_arguments):
        self.object_id = object_id
        self.command = command
        self._raw_args = raw_arguments
        self._parse_args()

    @classmethod
    def Parse(self, command_block):
        object_id = command_block[0:8].rstrip(b"\0").decode('utf-8')
        command = command_block[8:32].rstrip(b"\0").decode('utf-8')
        _raw_args = command_block[32:256].rstrip(b"\0").decode('utf-8')
        if command == "set_throttle":
            cls = SetThrottle
        if command == "set_power":
            cls = SetPower
        if command == "set_rotation":
            cls = SetRotation
        if command == "set_focus":
            cls = SetFocus
        return cls(object_id, command, _raw_args)

    def _validate(self):
        if self.object.__class__ not in self.ALLOWED_OBJECTS:
            raise InvalidObjectForCommand(
                "Cannot perform this action on {}".format(
                    self.object.__class__.__name__
                )
            )

    def _parse_args(self):
        raise NotImplementedError("Not Implemented")

    def _get_object(self, system):
        self.object = system.get_object_by_id(self.object_id)

    def exec(self, system):
        self._get_object(system)
        self._validate()


class SetThrottle(Command):
    ALLOWED_OBJECTS = [ReactionWheel, Thruster, Reactor]

    def _parse_args(self):
        self.throttle = float(self._raw_args)

    def _validate(self):
        super()._validate()
        if self.throttle < 0 or self.throttle > 1.2:
            raise InputValidationError("Bad Range")

    def exec(self, system):
        super().exec(system)
        self.object.throttle = self.throttle


class SetPower(Command):
    ALLOWED_OBJECTS = [ReactionWheel, Thruster, Reactor, Sensor]

    def _parse_args(self):
        try:
            self.toggle = bool(int(self._raw_args))
        except ValueError:
            raise InputValidationError("Bad value for power toggle")

    def exec(self, system):
        super().exec(system)
        self.object.powered_on = self.toggle


class SetRotation(Command):
    ALLOWED_OBJECTS = [Sensor]

    def _parse_args(self):
        try:
            self.pitch, self.yaw = [
                float(x) for x in self._raw_args.split(',')
            ]
        except ValueError:
            raise InputValidationError("Bad values given for pitch or yaw")

    def _validate(self):
        super()._validate()
        if self.pitch < -90 or self.pitch > 90:
            raise InputValidationError("Bad Range for Pitch")
        if self.yaw < -90 or self.yaw > 90:
            raise InputValidationError("Bad Range for Yaw")

    def exec(self, system):
        super().exec(system)
        self.object.pitch_degrees = self.pitch
        self.object.yaw_degrees = self.yaw


class SetFocus(Command):
    ALLOWED_OBJECTS = [Sensor]

    def exec(self, system):
        super().exec(system)
        self.object.focus = self.focus

    def _parse_args(self):
        try:
            self.focus = float(self._raw_args)
        except ValueError:
            raise InputValidationError("Bad value for focus")

    def _validate(self):
        super()._validate()
        if self.focus <= 0 or self.focus >= 90:
            raise InputValidationError("Bad Range for Focus")


class StatusReport(Command):
    def exec(self, system):
        super().exec(system)
        return self.object.status_report
