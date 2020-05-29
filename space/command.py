from space.components import (
    ReactionWheel,
    Thruster,
    Reactor,
    Sensor
)
from space.constants.math import DEGREES
from space.exceptions import InvalidObjectForCommand, InputValidationError
from space.mixins import IdentityMixin


class Response(object):
    def __init__(self, command, value):
        self.command = command
        self.value = value

    @property
    def command_id(self):
        return self.command.command_id

    @property
    def connection(self):
        return self.command.connection

    def __str__(self):
        return F"{self.command.command} - {self.value}"


class Command(IdentityMixin):
    def __init__(self, object_id, command, raw_arguments):
        self._object_id = object_id
        self.command = command
        self._raw_args = raw_arguments
        self._parse_args()
        self.command_id = self.object_id

    @classmethod
    def Parse(self, command_block):
        self.command_block = command_block
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
        if command == "sensor_ping":
            cls = PingSensor
        if command == "status_report":
            cls = StatusReport
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
        self.object = system.get_object_by_id(self._object_id)

    def exec(self, system):
        self._get_object(system)
        self._validate()


class SetThrottle(Command):
    ALLOWED_OBJECTS = [ReactionWheel, Thruster, Reactor]

    def _parse_args(self):
        try:
            self.throttle = float(self._raw_args)
        except ValueError:
            raise InputValidationError("Bad value for throttle")

    def _validate(self):
        super()._validate()
        if self.throttle < 0 or self.throttle > 1.2:
            raise InputValidationError("Bad Range")

    def exec(self, system):
        super().exec(system)
        if self.throttle > 0:
            print(F"Setting throttle from {self.object.throttle} to {self.throttle}")  # noqa
        self.object.throttle = self.throttle
        return Response(self, self.object.status_report)


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
        return Response(self, self.object.status_report)


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
        return Response(self, self.object.status_report)


class SetFocus(Command):
    ALLOWED_OBJECTS = [Sensor]

    def exec(self, system):
        super().exec(system)
        self.object.focus = self.focus
        return Response(self, self.object.status_report)

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
    def _parse_args(self):
        pass

    def _validate(self):
        pass

    def exec(self, system):
        super().exec(system)
        return Response(self, (self.object or system).status_report)


class PingSensor(Command):
    def _parse_args(self):
        pass

    def _validate(self):
        pass

    def exec(self, system):
        super().exec(system)
        bodies = {}
        # TODO Adapt to get sensors from ship, cache
        for sensor in self.object.ship.sensors:
            _bodies = {}
            if sensor.detected_bodies is None:
                _bodies = {
                    body.object_id: body
                    for body in system.bodies if sensor.can_detect(body)
                }
                sensor.detected_bodies = _bodies
            bodies.update(_bodies or sensor.detected_bodies)
        return Response(
            self,
            {
                "detectable_bodies": [
                    {
                        "object_id": body.object_id,
                        "vector": {
                            "x": body.current_vector.x,
                            "y": body.current_vector.y,
                            "z": body.current_vector.z,
                        },
                        "acceleration": {
                            "x": body.current_acceleration.x,
                            "y": body.current_acceleration.y,
                            "z": body.current_acceleration.z,
                        },
                        "dimmensions": {
                            "width": body.width,
                            "height": body.height,
                            "depth": body.depth,
                        },
                        "position": {
                            "x": body.position.x,
                            "y": body.position.y,
                            "z": body.position.z,
                        },
                        "orientation": {
                            "pitch_degrees": body.get_pitch(DEGREES),
                            "roll_degrees": body.get_roll(DEGREES),
                            "yaw_degrees": body.get_yaw(DEGREES),
                        },
                        "orientation_speed": {
                            "pitch_speed": body.pitch_speed,
                            "roll_speed": body.roll_speed,
                            "yaw_speed": body.yaw_speed,
                        }
                    } for body in bodies.values()
                ]
            }
        )
