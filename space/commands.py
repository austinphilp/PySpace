from components import (
    ReactionWheel,
    Thruster,
    Reactor,
    Sensor
)


class Command(object):
    def __init__(self, command_block):
        self.object_id = command_block[0:8].rstrip('\0').decode('utf-8')
        self.command = command_block[8:32].rstrip('\0').decode('utf-8')
        self._raw_args = command_block[32:256].rstrip('\0').decode('utf-8')

    def _validate(self):
        if self.object.__class__ not in self.ALLOWED_OBJECTS:
            raise Exception("Cannot perform this action on {}".format(
                self.object.__class__.__name__
            ))

    def _parse_args(self):
        # TODO(Austin) - throw correct exception
        raise Exception("Not Implemented")

    def _get_object(self, system):
        self.object = system.get_object_by_id(self.object_id)

    def exec(self, system):
        self._parse_args()
        self._get_object(system)
        self._validate()


class SetThrottle(Command):
    ALLOWED_OBJECTS = [ReactionWheel, Thruster, Reactor]

    def _parse_args(self):
        self.throttle = float(self._raw_args)

    def _validate(self):
        super()._validate()
        if self.throttle < 0 or self.throttle > 90:
            raise Exception("Bad Range")

    def exec(self, system):
        super().exec(system)
        self.object.throttle = self.throttle


class SetPower(Command):
    ALLOWED_OBJECTS = [ReactionWheel, Thruster, Reactor, Sensor]

    def _parse_args(self):
        self.toggle = bool(int(self._raw_args))

    def exec(self, system):
        super().exec(system)
        self.object.powered_on = self.toggle


class SetRotation(Command):
    ALLOWED_OBJECTS = [Sensor]

    def _parse_args(self):
        self.pitch, self.yaw = self._raw_args.split(',')

    def _validate(self):
        super()._validate()
        if self.pitch < -90 or self.pitch > 90:
            raise Exception("Bad Range for Pitch")
        if self.yaw < -90 or self.yaw > 90:
            raise Exception("Bad Range for Yaw")

    def exec(self, system):
        super().exec(system)
        self.object.pitch_degrees = self.pitch
        self.object.yaw_degrees = self.yaw


class SetFocus(Command):
    def exec(self, system):
        super().exec(system)
        self.object.focus = self.focus

    def _parse_args(self):
        self.focus = float(self._raw_args)

    def _validate(self):
        super()._validate()
        if self.focus <= 0 or self.focus >= 90:
            raise Exception("Bad Range for Focus")
