from space.constants.math import DEGREES_TO_RADIANS, RADIANS


class DimensionsMixin(object):
    def __init__(self, *args, **kwargs):
        self.width = kwargs.pop('width', 0)
        self.height = kwargs.pop('height', 0)
        self.depth = kwargs.pop('depth', 0)


class OrientationMixin(DimensionsMixin):
    def __init__(self, *args, **kwargs):
        self.yaw_degrees = kwargs.pop('yaw', 0)
        self.roll_degrees = kwargs.pop('roll', 0)
        self.pitch_degrees = kwargs.pop('pitch', 0)
        super(OrientationMixin, self).__init__(self)

    def get_yaw(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self.yaw_degrees * DEGREES_TO_RADIANS
        else:
            return self.yaw_degrees

    def get_pitch(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self.pitch_degrees * DEGREES_TO_RADIANS
        else:
            return self.pitch_degrees

    def get_roll(self, unit_type=RADIANS):
        if unit_type == RADIANS:
            return self.roll_degrees * DEGREES_TO_RADIANS
        else:
            return self.roll_degrees
